/*
 *  treecode.c
 *    transfored from: Peijun Li's fortran code
 *
 *  Author: Jiahui Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "treeGlobal.h"
#include "treecode.h"
#include <time.h>

/* global variables */
double *cf, *cf1, *cf2, *cf3;
double ***a, ***b;
double *positions, *charges, *potential;
double kappa, theta;
int order, nPnts, nMom, *orderarr, maxparCube, minlevel=50000;
int ***idx3;

/* locate coefficients and setup the topCube */
void setupCOEF(ssystem *sys) {
  int i, j, k, i1, i2, i3, n;
  double t1, t[3];
  cube *cb = sys->topCube;

  positions = sys->positions;
  charges = sys->charges;
  order=sys->order;
  nMom = ((order+1)*(order+2)*(order+3))/6;
  kappa = sys->kappa;
  theta = sys->theta;
  nPnts=sys->nPnts;

  CALLOC(a, order+1, double**, ON, AMISC);
  CALLOC(b, order+1, double**, ON, AMISC);

  for ( i=0; i<=order; i++ ){
    CALLOC(a[i], order+1, double*, ON, AMISC);
    CALLOC(b[i], order+1, double*, ON, AMISC);

    for ( j=0; j<=order; j++ ){
      CALLOC(a[i][j], order+1, double, ON, AMISC);
      CALLOC(b[i][j], order+1, double, ON, AMISC);
    }
  }

  for ( i=0; i<=order; i++ ){
    for ( j=0; j<=order; j++ ){
      for ( k=0; k<=order; k++ ){
        a[i][j][k] = 0.0;
        b[i][j][k] = 0.0;
      }
    }
  }

  CALLOC(cf1, order, double, ON, AMISC);
  CALLOC(cf2, order, double, ON, AMISC);
  CALLOC(cf3, order, double, ON, AMISC);

  for ( i=0; i<order; i++ ){
    t1 = 1.0/(i+1.0);
    cf1[i] = t1;
    cf2[i] = 1.0-0.5*t1;
    cf3[i] = 1.0-t1;
  }

  cb->min[0] = cb->max[0] = positions[0];
  cb->min[1] = cb->max[1] = positions[1];
  cb->min[2] = cb->max[2] = positions[2];
  for ( i=0; i<nPnts; i++ ){
    for ( k=0; k<3; k++ ){
      if ( positions[3*i+k] > cb->max[k] )
        cb->max[k] = positions[3*i+k];
      if ( positions[3*i+k] < cb->min[k] )
        cb->min[k] = positions[3*i+k];
    }
  }

  cb->eRad = 0.0;
  for ( k=0; k<3; k++ ) {
    cb->ctr[k] = (cb->max[k]+cb->min[k])/2.0;
    cb->eRad += SQR(cb->max[k]-cb->ctr[k]);
  }
  cb->eRad = sqrt(cb->eRad);

  cb->beg = 0; cb->end = nPnts - 1;
  cb->nPnts = cb->end - cb->beg + 1;
  cb->level = 0;
  cb->nKids = 0;
  cb->existMom = 0;
  for ( i=0; i<8; i++ )
    CALLOC(cb->kids[i], 1, cube, ON, ACUBES);

  CALLOC(orderarr, nPnts, int, ON, AMISC);

  for (i=0;i<nPnts;i++)
    orderarr[i]=i+1;
  sys->orderarr = orderarr;

  /* setup global variables */
  maxparCube = sys->maxparCube;

  CALLOC(idx3, order+1, int**, ON, AMISC);
  for ( i1=0; i1<=order; i1++ ) {
    CALLOC(idx3[i1], order+1, int*, ON, AMISC);
    for ( i2=0; i2<=order; i2++ ) {
      CALLOC(idx3[i1][i2], order+1, int, ON, AMISC);
    }
  }

  for ( i=n=0; n<=order; n++ ) {
    for ( i1=0; i1<=n; i1++ ) {
      for ( i2=0; i2<=n-i1; i2++, i++ ) {
        i3=n-i1-i2;
        idx3[i1][i2][i3] = i;
      }
    }
  }
} /* setupCOEF */

/* xyzswitch: 0 for x, 1 for y, 2 for z */
int partition(int xyzswitch, int beg, int end, double val) {
  int tind, lower, upper, midind;
  double ta, tb, tc, tq;

  if ( beg < end ) {
    ta = positions[3*beg+xyzswitch];
    tb = positions[3*beg+(xyzswitch+1)%3];
    tc = positions[3*beg+(xyzswitch+2)%3];
    tq = charges[beg];
    tind = orderarr[beg];
    upper = beg;
    lower = end;
    while ( upper != lower ) {
      while ( upper < lower && val < positions[3*lower+xyzswitch] ) {
        lower -= 1;
      }
      if ( upper != lower ) {
        positions[3*upper] = positions[3*lower];
        positions[3*upper+1] = positions[3*lower+1];
        positions[3*upper+2] = positions[3*lower+2];
        charges[upper] = charges[lower];
        orderarr[upper] = orderarr[lower];
      }
      while ( upper < lower && val >= positions[3*upper+xyzswitch] ) {
        upper += 1;
      }
      if ( upper != lower ) {
        positions[3*lower] = positions[3*upper];
        positions[3*lower+1] = positions[3*upper+1];
        positions[3*lower+2] = positions[3*upper+2];
        charges[lower] = charges[upper];
        orderarr[lower] = orderarr[upper];
      }
    }
    midind = upper;
    if ( ta > val ) midind = upper - 1;
    positions[3*upper+xyzswitch] = ta;
    positions[3*upper+(xyzswitch+1)%3] = tb;
    positions[3*upper+(xyzswitch+2)%3] = tc;
    charges[upper] = tq;
    orderarr[upper] = tind;
  }
  else if ( beg == end ) {
    midind = ( positions[3*upper+xyzswitch] <= val ) ? beg : beg-1;
  }
  else {
    midind = beg - 1;
  }

  return midind;
} /* partition */

/* partition_8 in treecode */
int partEight(double (*xyzmms)[6], cube *cb, int (*ind)[2]) {
  int i, j, temp_ind, nchild;
  double xl, yl, zl, lmax, critlen;
  double x_mid=cb->ctr[0], y_mid=cb->ctr[1], z_mid=cb->ctr[2];

  lmax = xl = cb->max[0] - cb->min[0];
  yl = cb->max[1] - cb->min[1];
  if ( lmax < yl ) lmax = yl;
  zl = cb->max[2] - cb->min[2];
  if ( lmax < zl ) lmax = zl;

  nchild = 1;
  critlen = lmax/sqrt(2.0);

  if ( xl >= critlen ) {
    temp_ind = partition(0, ind[0][0], ind[0][1], x_mid);

    ind[1][0] = temp_ind+1;
    ind[1][1] = ind[0][1];
    ind[0][1] = temp_ind;

    for ( i=0; i<6; i++ ) xyzmms[1][i] = xyzmms[0][i];
    xyzmms[0][1] = xyzmms[1][0] = x_mid;
    nchild *= 2;
  }

  if ( yl >= critlen ) {
    for ( i=0; i<nchild; i++ ) {
      temp_ind = partition(1, ind[i][0], ind[i][1], y_mid);

      ind[nchild+i][0] = temp_ind+1;
      ind[nchild+i][1] = ind[i][1];
      ind[i][1] = temp_ind;
      for ( j=0; j<6; j++ ) xyzmms[nchild+i][j] = xyzmms[i][j];
      xyzmms[i][3] = xyzmms[nchild+i][2] = y_mid;
    }
    nchild *= 2;
  }

  if ( zl >= critlen ) {
    for ( i=0; i<nchild; i++ ) {
      temp_ind = partition(2, ind[i][0], ind[i][1], z_mid);

      ind[nchild+i][0] = temp_ind+1;
      ind[nchild+i][1] = ind[i][1];
      ind[i][1] = temp_ind;
      for ( j=0; j<6; j++ ) xyzmms[nchild+i][j] = xyzmms[i][j];
      xyzmms[i][5] = xyzmms[nchild+i][4] = z_mid;
    }
    nchild *= 2;
  }

  return nchild;
} /* partEight */

/* create tree, criteria by max particles per cube */
void createTree(cube *cb) {
  int i, j, k, ind[8][2], nKids, nRealKids=0;
  double xyzmms[8][6], *lxyzmms;
  cube *kid;

  if ( cb->nPnts > maxparCube ) {
    for ( k=0; k<3; k++ ){
      xyzmms[0][2*k] = cb->min[k];
      xyzmms[0][2*k+1] = cb->max[k];
    }
    for ( k=0; k<8; k++ ) {
      ind[i][0] = 0;
      ind[i][1] = 0;
    }
    ind[0][0] = cb->beg;
    ind[0][1] = cb->end;

    nKids = partEight(xyzmms, cb, ind);

    for ( i=0; i<nKids; i++ ) {
      if ( ind[i][0] <= ind[i][1] ) {

        CALLOC(cb->kids[nRealKids], 1, cube, ON, ACUBES);
        kid = cb->kids[nRealKids];
        nRealKids++;

        lxyzmms = xyzmms[i];
        for ( k=0; k<3; k++ ) {
          kid->min[k] = lxyzmms[2*k];
          kid->max[k] = lxyzmms[2*k+1];
        }

        kid->eRad = 0.0;
        for ( k=0; k<3; k++ ) {
          kid->ctr[k] = (kid->max[k]+kid->min[k])/2.0;
          kid->eRad += SQR((kid->max[k]-kid->min[k])/2.0);
        }
        kid->eRad = sqrt(kid->eRad);

        kid->beg = ind[i][0]; kid->end = ind[i][1];
        kid->nPnts = kid->end - kid->beg;
        kid->level = cb->level + 1;
        kid->nKids = 0;
        kid->existMom = 0;

        createTree(kid);
      }
    }
    cb->nKids = nRealKids;
  }
  else {
    if ( cb->level < minlevel ) minlevel = cb->level;
  }

} /* createTree */

void compMom( cube *cb ) {
  int i, i1, i2, i3, j, n;
  double dx, dy, dz, tx, ty, tz;

  for ( j=cb->beg; j<cb->end+1; j++ ) {
    dx = positions[3*j] - cb->ctr[0];
    dy = positions[3*j+1] - cb->ctr[1];
    dz = positions[3*j+2] - cb->ctr[2];
/*
    for ( i=n=0; n<=order; n++ ){
      for ( i1=0; i1<=n; i1++ ){
        for ( i2=0; i2<=n-i1; i2++, i++ ){
          i3 = n-i1-i2;
          cb->mom[i] += charges[j]*pow(dx,i1)*pow(dy,i2)*pow(dz,i3);
        }
      }
    }
*/
    tx = 1.0;
    for ( i1=0; i1<order+1; i1++ ) {
      ty = 1.0;
      for ( i2=0; i2<order+1-i1; i2++ ) {
        tz = 1.0;
        for ( i3=0; i3<order+1-i1-i2; i3++ ) {
          cb->mom[idx3[i1][i2][i3]] += charges[j]*tx*ty*tz;
          tz *= dz;
        }
        ty *= dy;
      }
      tx *= dx;
    }
  }
} /* compMom */

/* REMOVE_NODE recursively removes each node from the tree and deallocates
 *    its memory for MS array if it exits. */
void compMomAll( cube *cb, int ifirst ) {
  int i,j,k,err;
  int k1,k2,k3;
  double dx,dy,dz,tx,ty,tz;

  if ( cb->existMom == 0 && ifirst == 0 ){
    CALLOC(cb->mom, nMom, double, ON, ACUBES);
    for ( k=0; k<nMom; k++ ) cb->mom[k] = 0.0;

    compMom(cb);
    cb->existMom = 1;
  }

  if( cb->nKids > 0 ){
    for ( i=0; i<cb->nKids; i++ ) compMomAll(cb->kids[i],0);
  }

} /* compMSall */

/* compute treecode coefficients */
void compCoef( cube *cb, double *point ){
  double dx,dy,dz,ddx,ddy,ddz,dist,fac;
  double kappax,kappay,kappaz;
  int i,j,k;

  /* setup variables */
  dx=point[0]-cb->ctr[0];
  dy=point[1]-cb->ctr[1];
  dz=point[2]-cb->ctr[2];

  ddx=2.0*dx;
  ddy=2.0*dy;
  ddz=2.0*dz;

  kappax=kappa*dx;
  kappay=kappa*dy;
  kappaz=kappa*dz;

  dist=dx*dx+dy*dy+dz*dz;
  fac=1.0/dist;
  dist=sqrt(dist);

  /* 0th coeff or function val */
  b[0][0][0]=exp(-kappa*dist);
  a[0][0][0]=b[0][0][0]/dist;

  /* 2 indices are 0 */
  b[1][0][0]=kappax*a[0][0][0];
  b[0][1][0]=kappay*a[0][0][0];
  b[0][0][1]=kappaz*a[0][0][0];

  a[1][0][0]=fac*dx*(a[0][0][0]+kappa*b[0][0][0]);
  a[0][1][0]=fac*dy*(a[0][0][0]+kappa*b[0][0][0]);
  a[0][0][1]=fac*dz*(a[0][0][0]+kappa*b[0][0][0]);

  for (i=2;i<order+1;i++){
    b[i][0][0]=cf1[i-1]*kappa*(dx*a[i-1][0][0]-a[i-2][0][0]);
    b[0][i][0]=cf1[i-1]*kappa*(dy*a[0][i-1][0]-a[0][i-2][0]);
    b[0][0][i]=cf1[i-1]*kappa*(dz*a[0][0][i-1]-a[0][0][i-2]);

    a[i][0][0]=fac*(ddx*cf2[i-1]*a[i-1][0][0]-cf3[i-1]*a[i-2][0][0]+
                 cf1[i-1]*kappa*(dx*b[i-1][0][0]-b[i-2][0][0]));
    a[0][i][0]=fac*(ddy*cf2[i-1]*a[0][i-1][0]-cf3[i-1]*a[0][i-2][0]+
                 cf1[i-1]*kappa*(dy*b[0][i-1][0]-b[0][i-2][0]));
    a[0][0][i]=fac*(ddz*cf2[i-1]*a[0][0][i-1]-cf3[i-1]*a[0][0][i-2]+
                 cf1[i-1]*kappa*(dz*b[0][0][i-1]-b[0][0][i-2]));
  }

  /* 1 index 0, 1 index 1, other >=1 */
  b[1][1][0]=kappax*a[0][1][0];
  b[1][0][1]=kappax*a[0][0][1];
  b[0][1][1]=kappay*a[0][0][1];

  a[1][1][0]=fac*(dx*a[0][1][0]+ddy*a[1][0][0]+kappax*b[0][1][0]);
  a[1][0][1]=fac*(dx*a[0][0][1]+ddz*a[1][0][0]+kappax*b[0][0][1]);
  a[0][1][1]=fac*(dy*a[0][0][1]+ddz*a[0][1][0]+kappay*b[0][0][1]);

  for (i=2;i<order;i++){
    b[1][0][i]=kappax*a[0][0][i];
    b[0][1][i]=kappay*a[0][0][i];
    b[0][i][1]=kappaz*a[0][i][0];
    b[1][i][0]=kappax*a[0][i][0];
    b[i][1][0]=kappay*a[i][0][0];
    b[i][0][1]=kappaz*a[i][0][0];

    a[1][0][i]=fac*(dx*a[0][0][i]+ddz*a[1][0][i-1]-a[1][0][i-2]+
                 kappax*b[0][0][i]);
    a[0][1][i]=fac*(dy*a[0][0][i]+ddz*a[0][1][i-1]-a[0][1][i-2]+
                 kappay*b[0][0][i]);
    a[0][i][1]=fac*(dz*a[0][i][0]+ddy*a[0][i-1][1]-a[0][i-2][1]+
                 kappaz*b[0][i][0]);
    a[1][i][0]=fac*(dx*a[0][i][0]+ddy*a[1][i-1][0]-a[1][i-2][0]+
                 kappax*b[0][i][0]);
    a[i][1][0]=fac*(dy*a[i][0][0]+ddx*a[i-1][1][0]-a[i-2][1][0]+
                 kappay*b[i][0][0]);
    a[i][0][1]=fac*(dz*a[i][0][0]+ddx*a[i-1][0][1]-a[i-2][0][1]+
                 kappaz*b[i][0][0]);
  }

  /* 1 index 0, others >=2 */
  for (i=2;i<order-1;i++){
   for (j=2;j<order-i+1;j++){
      b[i][j][0]=cf1[i-1]*kappa*(dx*a[i-1][j][0]-a[i-2][j][0]);
      b[i][0][j]=cf1[i-1]*kappa*(dx*a[i-1][0][j]-a[i-2][0][j]);
      b[0][i][j]=cf1[i-1]*kappa*(dy*a[0][i-1][j]-a[0][i-2][j]);

      a[i][j][0]=fac*(ddx*cf2[i-1]*a[i-1][j][0]+ddy*a[i][j-1][0]
                     -cf3[i-1]*a[i-2][j][0]-a[i][j-2][0]+
                     cf1[i-1]*kappa*(dx*b[i-1][j][0]-b[i-2][j][0]));
      a[i][0][j]=fac*(ddx*cf2[i-1]*a[i-1][0][j]+ddz*a[i][0][j-1]
                     -cf3[i-1]*a[i-2][0][j]-a[i][0][j-2]+
                     cf1[i-1]*kappa*(dx*b[i-1][0][j]-b[i-2][0][j]));
      a[0][i][j]=fac*(ddy*cf2[i-1]*a[0][i-1][j]+ddz*a[0][i][j-1]
                     -cf3[i-1]*a[0][i-2][j]-a[0][i][j-2]+
                     cf1[i-1]*kappa*(dy*b[0][i-1][j]-b[0][i-2][j]));
    }
  }

  /* 2 indices 1,other >= 1 */
  b[1][1][1]=kappax*a[0][1][1];
  a[1][1][1]=fac*(dx*a[0][1][1]+ddy*a[1][0][1]+ddz*a[1][1][0]+
             kappax*b[0][1][1]);

  for (i=2;i<order-1;i++){
    b[1][1][i]=kappax*a[0][1][i];
    b[1][i][1]=kappax*a[0][i][1];
    b[i][1][1]=kappay*a[i][0][1];

    a[1][1][i]=fac*(dx*a[0][1][i]+ddy*a[1][0][i]+ddz*a[1][1][i-1]
                 -a[1][1][i-2]+kappax*b[0][1][i]);
    a[1][i][1]=fac*(dx*a[0][i][1]+ddy*a[1][i-1][1]+ddz*a[1][i][0]
                 -a[1][i-2][1]+kappax*b[0][i][1]);
    a[i][1][1]=fac*(dy*a[i][0][1]+ddx*a[i-1][1][1]+ddz*a[i][1][0]
                 -a[i-2][1][1]+kappay*b[i][0][1]);
  }

  /* 1 index 1, others >=2 */
  for (i=2;i<order-2;i++){
    for (j=2;j<order-i+1;j++){
      b[1][i][j]=kappax*a[0][i][j];
      b[i][1][j]=kappay*a[i][0][j];
      b[i][j][1]=kappaz*a[i][j][0];

      a[1][i][j]=fac*(dx*a[0][i][j]+ddy*a[1][i-1][j]+ddz*a[1][i][j-1]-a[1][i-2][j]
                     -a[1][i][j-2]+kappax*b[0][i][j]);
      a[i][1][j]=fac*(dy*a[i][0][j]+ddx*a[i-1][1][j]+ddz*a[i][1][j-1]-a[i-2][1][j]
                     -a[i][1][j-2]+kappay*b[i][0][j]);
      a[i][j][1]=fac*(dz*a[i][j][0]+ddx*a[i-1][j][1]+ddy*a[i][j-1][1]-a[i-2][j][1]
                     -a[i][j-2][1]+kappaz*b[i][j][0]);
    }
  }

  /* all indices >=2 */
  for (k=2;k<order-3;k++){
    for (j=2;j<order-1-k;j++){
      for (i=2;i<order+1-k-j;i++){
        b[i][j][k]=cf1[i-1]*kappa*(dx*a[i-1][j][k]-a[i-2][j][k]);
        a[i][j][k]=fac*(ddx*cf2[i-1]*a[i-1][j][k]+ddy*a[i][j-1][k]+ddz*a[i][j][k-1]
                       -cf3[i-1]*a[i-2][j][k]-a[i][j-2][k]-a[i][j][k-2]
                       +cf1[i-1]*kappa*(dx*b[i-1][j][k]-b[i-2][j][k]));
      }
    }
  }

} /* compCoef */

double directTree( int beg, int end, double *point ) {
  int i;
  double dist, dx, dy, dz, energy=0.0;

  for ( i=beg; i<end; i++ ) {
    dx = positions[3*i] - point[0];
    dy = positions[3*i+1] - point[1];
    dz = positions[3*i+2] - point[2];
    dist = sqrt(SQR(dx)+SQR(dy)+SQR(dz));

    //energy += charges[i]*exp(-kappa*dist)/dist*fourPiI;
    energy += charges[i]*exp(-kappa*dist)/dist;
  }

  return energy;
} /* directTree */

double compEnergy( cube *cb, double *point ) {
  int i, i1, i2, i3, n;
  double energy=0.0, dx, dy, dz, dist;

  dx = cb->ctr[0] - point[0];
  dy = cb->ctr[1] - point[1];
  dz = cb->ctr[2] - point[2];
  dist = sqrt(SQR(dx)+SQR(dy)+SQR(dz));

  if ( cb->eRad<dist*theta && cb->nPnts>1 ) {
    compCoef(cb, point);
    for ( i=n=0; n<=order; n++ ){
      for ( i1=0; i1<=n; i1++ ){
        for ( i2=0; i2<=n-i1; i2++, i++ ){
          i3 = n-i1-i2;
          energy += a[i1][i2][i3]*cb->mom[i];
        }
      }
    }
    //energy *= fourPiI;
  }
  else {
    if ( cb->nKids == 0 ) energy = directTree(cb->beg, cb->end+1, point);
    else {
      for ( i=0; i<cb->nKids; i++ ) energy += compEnergy(cb->kids[i], point);
    }
  }

  return energy;
} /* compEnergy */

/* compute tree */
void compTree(cube *cb, double *pot) {
  int i,j,k;
  double energy, tx, tq, point[3];
  potential = pot;

  //for ( i=0; i<100; i++ ) {
  for ( i=0; i<nPnts; i++ ) {
    energy = 0.0;
    for ( k=0; k<3; k++ ) point[k] = positions[3*i+k];

    tx = positions[3*i];
    tq = charges[i];
    positions[3*i] += 100.0;
    charges[i] = 0.0;

    energy = compEnergy(cb, point);

    positions[3*i] = tx;
    charges[i] = tq;

    pot[i] = tq*energy;
  }

} /* compTree */

void freeMomCube(cube *cb) {
  int i;
  if ( cb->existMom == 1 ) free(cb->mom);
  for ( i=0; i<cb->nKids; i++ ) {
    freeMomCube(cb->kids[i]);
    free(cb->kids[i]);
  }

} /* freeMomCube */

/* free memory of coefficients */
void freeCOEF(ssystem *sys, double *pot, double *dpot) {
  int i, j, i1, i2;

  for ( i1=0; i1<=order; i1++ ) {
    for ( i2=0; i2<=order; i2++ ) {
      free(idx3[i1][i2]);
    }
    free(idx3[i1]);
  }
  free(idx3);

  free(cf1);
  free(cf2);
  free(cf3);

  for ( i=0; i<=order; i++ ) {
    for ( j=0; j<=order; j++) {
      free(a[i][j]);
      free(b[i][j]);
    }
    free(a[i]);
    free(b[i]);
  }
  free(a);
  free(b);

  free(orderarr);
  free(sys->positions);
  free(sys->charges);
  free(pot);
  free(dpot);

  freeMomCube(sys->topCube);
  free(sys->topCube);
  free(sys);

} /* freeCOEF */
