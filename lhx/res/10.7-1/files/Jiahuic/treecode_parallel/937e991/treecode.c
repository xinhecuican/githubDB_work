/* Jiahui Chen
 * Advisor Dr. Geng
 * 3/3/2015
 * derive from fortran
 * */

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdint.h>

#include "treecode.h"
double minval(double* x, int numpars){
  int i;
  double MinVal;
  MinVal = x[0];
  for(i=1;i<numpars;i++){
    if(MinVal>x[i])
      MinVal = x[i];
  }
  return MinVal;
}

double maxval(double* x, int numpars){
  int i;
  double MaxVal;
  MaxVal = x[0];
  for(i=1;i<numpars;i++){
    if(MaxVal<x[i])
      MaxVal = x[i];
  }
  return MaxVal;
}

int setup(double* x,double* y,double* z,double* q,int numpars,\
           int order, double xyzminmax[6]){
//
// SETUP allocates and initializes arrays needed for the Taylor expansion.
// Also, global variables are set and the Cartesian coordinates of
// the smallest box containing the particles is determined. The particle
// postions and charges are copied so that they can be restored upon exit.
//

  int err,i,j,k;
  double t1;

/* global integers and reals:  TORDER, TORDERLIM and THETASQ */
  torder = order;
  orderoffset = 0;
  torderlim = torder+orderoffset;

/* allocate global Taylor expansion variables */
  cf = (double*)calloc(torder+1, sizeof(double));
  if (cf == NULL){
    fprintf(stderr, "setup error: cf empty data array\n");
    return 1;
  }
  cf1 = (double*)calloc(torderlim, sizeof(double));
  if (cf1 == NULL){
    fprintf(stderr, "setup error: cf1 empty data array\n");
    return 1;
  }
  cf2 = (double*)calloc(torderlim, sizeof(double));
  if (cf2 == NULL){
    fprintf(stderr, "setup error: cf2 empty data array\n");
    return 1;
  }
  cf3 = (double*)calloc(torderlim, sizeof(double));
  if (cf3 == NULL){
    fprintf(stderr, "setup error: cf3 empty data array\n");
    return 1;
  }

  a = (double***)calloc(torderlim+3, sizeof(double**));
  b = (double***)calloc(torderlim+3, sizeof(double**));
  for (i=0;i<torderlim+3;i++) 
    a[i] = (double**)calloc(torderlim+3, sizeof(double*));
  for (i=0;i<torderlim+3;i++) 
    b[i] = (double**)calloc(torderlim+3, sizeof(double*));
  for (i=0;i<torderlim+3;i++){
    for (j=0;j<torderlim+3;j++)
      a[i][j]=(double*)calloc(torderlim+3, sizeof(double));
  }
  for (i=0;i<torderlim+3;i++){
    for (j=0;j<torderlim+3;j++)
      b[i][j]=(double*)calloc(torderlim+3, sizeof(double));
  }
  if (a == NULL){
    fprintf(stderr, "setup error: a empty data array\n");
    return 1;
  }
  if (b == NULL){
    fprintf(stderr, "setup error: b empty data array\n");
    return 1;
  }
  
  for (i=0;i<torderlim+3;i++){
    for (j=0;j<torderlim+3;j++){
      for (k=0;k<torderlim+3;k++){
        a[i][j][k]=0.0;
        b[i][j][k]=0.0;
      }
    }
  }

  for (i=0;i<torder+1;i++)
    cf[i] = i+1.0;

  for (i=0;i<torderlim;i++){
    t1=1.0/(i+1.0);
    cf1[i]=t1;
    cf2[i]=1.0-0.5*t1;
    cf3[i]=1.0-t1;
  }

/* find bounds of Cartesion box enclosing the particles */

  xyzminmax[0]=minval(x,numpars);
  xyzminmax[1]=maxval(x,numpars);
  xyzminmax[2]=minval(y,numpars);
  xyzminmax[3]=maxval(y,numpars);
  xyzminmax[4]=minval(z,numpars);
  xyzminmax[5]=maxval(z,numpars);

  printf("%f,%f,%f,%f,%f,%f\n",xyzminmax[0],xyzminmax[1],xyzminmax[2],
         xyzminmax[3],xyzminmax[4],xyzminmax[5]);




  for (i=0;i<numpars;i++)
    orderarr[i]=i+1;

  return(0);
}

void create_tree(tnode* p,int ibeg,int iend,double* x,double* y,
                 double* z,double*q,int maxparnode,double xyzmm[6],
                 int level,int numpars){

  /* local variables */
  double x_mid,y_mid,z_mid,xl,yl,zl,lmax,t1,t2,t3;
  int **ind;
  double xyzmms[6][8];
  int i,j,limin,limax,err,loclev,numposchild;
  double lxyzmm[6];
  tnode *childnode;

  int partition_8(double *x,double *y,double *z,double *q,
                   double xyzmms[6][8],
                   double xl,double yl,double zl,double lmax,
                   int numposchild, double x_mid,double y_mid,
                   double z_mid,int **ind,int numpars);

  ind = (int**)calloc(8,sizeof(int*));
  for (i=0;i<8;i++){
    ind[i]=(int*)calloc(2,sizeof(int));
  }
  
/* set node fields: number of particles, exist_ms and xyz bounds */

  p->numpar=iend-ibeg+1;
  p->exist_ms=0;

  p->x_min=xyzmm[0];
  p->x_max=xyzmm[1];
  p->y_min=xyzmm[2];
  p->y_max=xyzmm[3];
  p->z_min=xyzmm[4];
  p->z_max=xyzmm[5];
/* compute aspect ratio */
  xl=p->x_max-p->x_min;
  yl=p->y_max-p->y_min;
  zl=p->z_max-p->z_min;

  lmax = xl;
  if (lmax<yl) lmax = yl;
  if (lmax<zl) lmax = zl;

  t1 = lmax;
  t2 = xl;
  if (t2>yl) t2 = yl;
  if (t2>zl) t2 = zl;

  if (t2!=0.0) p->aspect=t1/t2;
  else p->aspect=0.0;
/* midpoint coordinates, RADIUS and SQRADIUS */
  p->x_mid = (p->x_max+p->x_min)/2.0;
  p->y_mid = (p->y_max+p->y_min)/2.0;
  p->z_mid = (p->z_max+p->z_min)/2.0;
  t1=p->x_max-p->x_mid;
  t2=p->y_max-p->y_mid;
  t3=p->z_max-p->z_mid;
  p->radius=sqrt(t1*t1+t2*t2+t3*t3);


/* set particle limits, tree level of node, and nullify children pointers */
  p->ibeg=ibeg;
  p->iend=iend;
  p->level=level;
//  if (ibeg==14158 || iend==14158 )
//  if (level==2)
//  if (ibeg>=13322 && iend <=15055)
//    printf("Tree is %d and %d, of level %d\n",ibeg,iend,level);
 
  if (maxlevel < level) maxlevel=level;
  p->num_children = 0;
  p->child=(tnode**)malloc(8*sizeof(tnode*));
  for (i=0;i<8;i++) p->child[i]=(tnode*)malloc(1*sizeof(tnode));
  p->child[0]->x_min = 1.0;

  if (p->numpar > maxparnode){

    xyzmms[0][0]=p->x_min;
    xyzmms[1][0]=p->x_max;
    xyzmms[2][0]=p->y_min;
    xyzmms[3][0]=p->y_max;
    xyzmms[4][0]=p->z_min;
    xyzmms[5][0]=p->z_max;
    for (i=0;i<8;i++){
      ind[i][0]=0;
      ind[i][1]=0;
    }    
    ind[0][0]=ibeg;
    ind[0][1]=iend;
    x_mid=p->x_mid;
    y_mid=p->y_mid;
    z_mid=p->z_mid;

    numposchild = partition_8(x,y,z,q,xyzmms,xl,yl,zl,lmax,numposchild,
                              x_mid,y_mid,z_mid,ind,numpars);

//printf("ind %d,%d\n",ind[1][0],ind[1][1]);
//    if (ibeg>=13322 && iend <=15055)
//    
//      printf("from %d to %d, the number of children is %d\n",ibeg,iend, numposchild);

    loclev = level+1;
 
    for (i=0;i<numposchild;i++){
//    if (ind[i][0]>=2088 & ind[i][1]<=2100)
//      printf("%d %d, %d\n",i,ind[i][0],ind[i][1]);

      if (ind[i][0] <= ind[i][1]){
//        printf("%d ind(1) ind(2) is %d %d\n",i,ind[i][0],ind[i][1]);
        p->num_children = p->num_children+1;
        for (j=0;j<6;j++) {
          lxyzmm[j]=xyzmms[j][i];
        }        
        create_tree(p->child[p->num_children-1],
                    ind[i][0],ind[i][1],x,y,z,q,maxparnode,
                    lxyzmm,loclev,numpars);
      }
    }
  }
  else {
    if(level < minlevel) minlevel = level;
  }
}

int partition_8(double *x,double *y,double *z,double *q,
                 double xyzmms[6][8],
                 double xl,double yl,double zl,double lmax,
                 int numposchild, double x_mid,double y_mid,
                 double z_mid,int **ind,int numpars){
/* PARTITION_8 determines the particle indices of the eight sub boxes
 * containing the particles after the box defined by particles I_BEG
 * to I_END is divided by its midpoints in each coordinate direction.
 * The determination of the indices is accomplished by the subroutine
 * PARTITION. A box is divided in a coordinate direction as long as the
 * resulting aspect ratio is not too large. This avoids the creation of
 * "narrow" boxes in which Talyor expansions may become inefficient.
 * On exit the INTEGER array IND (dimension 8 x 2) contains
 * the indice limits of each new box (node) and NUMPOSCHILD the number 
 * of possible children.  If IND(J,1) > IND(J,2) for a given J this indicates
 * that box J is empty.*/

  int temp_ind,i,j;
  double critlen;

  extern int partition();

  numposchild = 1;
  critlen = lmax/sqrt(2.0);
//if(ind[0][0]==0) printf("x[0]=%f\n",x[0]);
  if (xl >= critlen) {    
    temp_ind = partition(x,y,z,q,orderarr,ind[0][0],ind[0][1],x_mid,
                         temp_ind,numpars);

    ind[1][0]=temp_ind+1;
    ind[1][1]=ind[0][1];
    ind[0][1]=temp_ind;

//    printf("%d    %d    %d    %d\n",ind[0][0],ind[0][1],ind[1][0],ind[1][1]);
    for (i=0;i<6;i++) xyzmms[i][1]=xyzmms[i][0];
    xyzmms[1][0]=x_mid;
    xyzmms[0][1]=x_mid;
    numposchild=2*numposchild;
  }
//if(ind[0][0]==0) printf("x[0]=%f\n",x[0]);
  if (yl >= critlen) {
    for (i=0;i<numposchild;i++){
      temp_ind = partition(y,x,z,q,orderarr,ind[i][0],ind[i][1],y_mid,
                           temp_ind,numpars);
      ind[numposchild+i][0]=temp_ind+1;
      ind[numposchild+i][1]=ind[i][1];
      ind[i][1]=temp_ind;
// printf("%d    %d    %d    %d\n",ind[i][0],ind[i][1],
//        ind[numposchild+i][0],ind[numposchild+i][1]);
      for (j=0;j<6;j++) xyzmms[j][numposchild+i]=xyzmms[j][i];
      xyzmms[3][i]=y_mid;
      xyzmms[2][numposchild+i]=y_mid;
    }
    numposchild = 2*numposchild;
  }

  if (zl >= critlen) {
//    printf("zl=%f\n",z_mid);
    for (i=0;i<numposchild;i++){
      temp_ind = partition(z,x,y,q,orderarr,ind[i][0],ind[i][1],z_mid,
                           temp_ind,numpars);
      ind[numposchild+i][0]=temp_ind+1;
      ind[numposchild+i][1]=ind[i][1];
      ind[i][1]=temp_ind;
//printf("temp=%d %d    %d    %d    %d\n",temp_ind,ind[i][0],ind[i][1],
//        ind[numposchild+i][0],ind[numposchild+i][1]);
 
      for (j=0;j<6;j++) xyzmms[j][numposchild+i]=xyzmms[j][i];
      xyzmms[5][i]=z_mid;
      xyzmms[4][numposchild+i]=z_mid;
    }
    numposchild=2*numposchild;
  }
//printf("%d,%d,%d,%d,%d,%d,%d,%d\n",ind[0][0],ind[0][1],ind[1][0],
//ind[1][1],ind[2][0],ind[2][1],ind[3][0],ind[3][1],ind[4][0],ind[4][1]);

  return (numposchild);
}

int partition(double *a,double *b,double *c,double *q,int *indarr,int ibeg,
               int iend,double val,int midind,int numpars){

  double ta,tb,tc,tq;
  int lower,upper,tind;
//printf("%d,%d\n",ibeg,iend);

  if (ibeg<iend){
//    printf("ibeg<iend\n");
    ta=a[ibeg];
    tb=b[ibeg];
    tc=c[ibeg];
    tq=q[ibeg];
    tind=indarr[ibeg];
    a[ibeg]=val;
    upper=ibeg;
    lower=iend;
    while(upper!=lower){
      while(upper < lower && val < a[lower])
        lower=lower-1;
      if(upper != lower){
        a[upper] = a[lower];
        b[upper] = b[lower];
        c[upper] = c[lower];
        q[upper] = q[lower];
        indarr[upper]=indarr[lower];
      }
      while(upper < lower && val >= a[upper])
        upper=upper+1;
      if (upper != lower){
        a[lower]=a[upper];
        b[lower]=b[upper];
        c[lower]=c[upper];
        q[lower]=q[upper];
        indarr[lower]=indarr[upper];
      }
    }
    midind = upper;//    printf("adfs%d\n",upper);
    if (ta > val)
      midind = upper - 1;
    a[upper]=ta;
    b[upper]=tb;
    c[upper]=tc;
    q[upper]=tq;
    indarr[upper]=tind;    
  }
  else if (ibeg == iend){
//    printf("ibeg=iend\n");
    if (a[ibeg] <= val){
      midind = ibeg;
    }
    else{
      midind = ibeg - 1;
    }
  }
  else if (ibeg > iend){ 
//    printf("it is %d\n",ibeg);
    midind = ibeg - 1;
  }
  return (midind);
}

void tree_compp(tnode *p,double *x,double *y,double *z,double *q,
                double kappa,double theta,double *tpoten,int numpars){

/* TREE_COMPF is the driver routine which calls COMPF_TREE for each
   particle, setting the global variable TARPOS before the call. 
   The current target particle's x coordinate and charge are changed
   so that it does not interact with itself. P is the root node of the tree.*/
 
  int i,j;
  double peng,tempx,tempq,pi4;

  extern double compp_tree();
  extern void comp_ms_all();

//  pi4=3.141592653589793238462643*4.0;
  for (i=0;i<numpars;i++) tpoten[i]=0.0;

  comp_ms_all(p,1);
/* by compare with fortran comp_ms_all works good */
  for (i=0;i<numpars;i++){
//  for (i=0;i<100;i++){
    peng=0.0;
    tarpos[0]=x[i];
    tarpos[1]=y[i];
    tarpos[2]=z[i];
   
    tempx=x[i];
    tempq=q[i];
    x[i]=x[i]+100.123456789;
    q[i]=0.0;

    peng = compp_tree(p,peng,x,y,z,q,kappa,theta,numpars);
  

    x[i]=tempx;
    q[i]=tempq;
//    USE order of points imposed by tree creation!
//    tpoten[orderarr[i]]=tempq*peng;
    tpoten[i]=tempq*peng;
//    printf("%f\n",tpoten[i]);
  }
}

void comp_ms_all(tnode *p,int ifirst){
/* REMOVE_NODE recursively removes each node from the tree and deallocates
 *    its memory for MS array if it exits. */

  int i,j,k,err;
  int k1,k2,k3;
  double dx,dy,dz,tx,ty,tz;

  extern void comp_ms();

  if (p->exist_ms == 0 && ifirst == 0){
    p->ms = (double***)calloc(torder+1, sizeof(double**));
    for (i=0;i<torder+1;i++) 
      p->ms[i] = (double**)calloc(torder+1, sizeof(double*));
    for (i=0;i<torder+1;i++){
      for (j=0;j<torder+1;j++)
        p->ms[i][j]=(double*)calloc(torder+1, sizeof(double));
    }
    // if null
    comp_ms(p,x,y,z,q,numpars);
    p->exist_ms=1;

  }

  if(p->num_children > 0){

    for (i=0;i<p->num_children;i++)
      comp_ms_all(p->child[i],0);
  }
}

void comp_ms(tnode *p,double *x,double *y,double *z,double* q,int numpars){
/* COMP_MS computes the moments for node P needed in the Taylor 
 *  * approximation */

  int i,k1,k2,k3,n,m,k;
  double dx,dy,dz,tx,ty,tz;
   
  for (i=p->ibeg;i<p->iend+1;i++){
    dx=x[i]-p->x_mid;
    dy=y[i]-p->y_mid;
    dz=z[i]-p->z_mid;
    tz=1.0;
    for (k3=0;k3<torder+1;k3++){
      ty=1.0;
      for (k2=0;k2<torder+1-k3;k2++){
        tx=1.0;
        for (k1=0;k1<torder+1-k3-k2;k1++){
          p->ms[k1][k2][k3]=p->ms[k1][k2][k3]+q[i]*tx*ty*tz;
          tx=tx*dx;
        }
        ty=ty*dy;
      }
      tz=tz*dz;
    }
  }
}

double compp_tree(tnode *p,double peng,double *x,double *y,double *z,
                double *q,double kappa,double theta,int numpars){

  double tx,ty,tz,dist,dist2,penglocal,pi;
  int i,j,k,err;

  extern double compp_direct();
  extern void comp_tcoeff();

/* determine DISTSQ for MAC test */
  pi = 3.141592653589793238462643;
  tx = p->x_mid - tarpos[0];
  ty = p->y_mid - tarpos[1];
  tz = p->z_mid - tarpos[2];
  dist = sqrt(tx*tx+ty*ty+tz*tz);

/* intialize potential energy */
  peng = 0.0;

/* If MAC is accepted and there is more than 1 particale in the */
/* box use the expansion for the approximation. */
  if (p->radius < dist*theta && p->numpar > 1) {
    comp_tcoeff(p,kappa);
    for (k=0;k<torder+1;k++){
      for (j=0;j<torder+1-k;j++){
        for(i=0;i<torder+1-k-j;i++){
          peng = peng +a[i+2][j+2][k+2]*p->ms[i][j][k];
        }
      }
    }
    peng = peng/4/pi;
  }
  else {
    if (p->num_children == 0){
      peng = compp_direct(penglocal,p->ibeg,p->iend,x,y,z,q,kappa,numpars);
    }
    else {
    //If MAC fails check to see if there are children. If not, perform direct
    //calculation.  If there are children, call routine recursively for each.
      for (i=0;i<p->num_children;i++){
        penglocal = compp_tree(p->child[i],penglocal,x,y,z,q,kappa,
                   theta,numpars);
        peng += penglocal;
      }
    }
  }
  return peng;
}

void comp_tcoeff(tnode *p, double kappa){
// COMP_TCOEFF computes the Taylor coefficients of the potential
// using a recurrence formula.  The center of the expansion is the
// midpoint of the node P.  TARPOS and TORDERLIM are globally defined.
  
  double dx,dy,dz,ddx,ddy,ddz,dist,fac;
  double kappax,kappay,kappaz;
  int i,j,k;

  /* setup variables */
  dx=tarpos[0]-p->x_mid;
  dy=tarpos[1]-p->y_mid;
  dz=tarpos[2]-p->z_mid;

  ddx=2.0*dx;
  ddy=2.0*dy;
  ddz=2.0*dz;

  kappax=kappa*dx;
  kappay=kappa*dy;
  kappaz=kappa*dz;

  dist=dx*dx+dy*dy+dz*dz;
  fac=1.0/dist;
  dist=sqrt(dist);
//  printf("%f\n",dist);

  /* 0th coeff or function val */
  b[2][2][2]=exp(-kappa*dist);
  a[2][2][2]=b[2][2][2]/dist;

  /* 2 indices are 0 */
  b[3][2][2]=kappax*a[2][2][2];
  b[2][3][2]=kappay*a[2][2][2];
  b[2][2][3]=kappaz*a[2][2][2];

  a[3][2][2]=fac*dx*(a[2][2][2]+kappa*b[2][2][2]);
  a[2][3][2]=fac*dy*(a[2][2][2]+kappa*b[2][2][2]);
  a[2][2][3]=fac*dz*(a[2][2][2]+kappa*b[2][2][2]);

  for (i=2;i<torderlim+1;i++){
    b[i+2][2][2]=cf1[i-1]*kappa*(dx*a[i+1][2][2]-a[i][2][2]);
    b[2][i+2][2]=cf1[i-1]*kappa*(dy*a[2][i+1][2]-a[2][i][2]);
    b[2][2][i+2]=cf1[i-1]*kappa*(dz*a[2][2][i+1]-a[2][2][i]);

    a[i+2][2][2]=fac*(ddx*cf2[i-1]*a[i+1][2][2]-cf3[i-1]*a[i][2][2]+
                 cf1[i-1]*kappa*(dx*b[i+1][2][2]-b[i][2][2]));
    a[2][i+2][2]=fac*(ddy*cf2[i-1]*a[2][i+1][2]-cf3[i-1]*a[2][i][2]+
                 cf1[i-1]*kappa*(dy*b[2][i+1][2]-b[2][i][2]));
    a[2][2][i+2]=fac*(ddz*cf2[i-1]*a[2][2][i+1]-cf3[i-1]*a[2][2][i]+
                 cf1[i-1]*kappa*(dz*b[2][2][i+1]-b[2][2][i]));
  }

  /* 1 index 0, 1 index 1, other >=1 */
  b[3][3][2]=kappax*a[2][3][2];
  b[3][2][3]=kappax*a[2][2][3];
  b[2][3][3]=kappay*a[2][2][3];

  a[3][3][2]=fac*(dx*a[2][3][2]+ddy*a[3][2][2]+kappax*b[2][3][2]);
  a[3][2][3]=fac*(dx*a[2][2][3]+ddz*a[3][2][2]+kappax*b[2][2][3]);
  a[2][3][3]=fac*(dy*a[2][2][3]+ddz*a[2][3][2]+kappay*b[2][2][3]);

  for (i=2;i<torderlim;i++){
    b[3][2][i+2]=kappax*a[2][2][i+2];
    b[2][3][i+2]=kappay*a[2][2][i+2];
    b[2][i+2][3]=kappaz*a[2][i+2][2];
    b[3][i+2][2]=kappax*a[2][i+2][2];
    b[i+2][3][2]=kappay*a[i+2][2][2];
    b[i+2][2][3]=kappaz*a[i+2][2][2]; 
    
    a[3][2][i+2]=fac*(dx*a[2][2][i+2]+ddz*a[3][2][i+1]-a[3][2][i]+
                 kappax*b[2][2][i+2]);
    a[2][3][i+2]=fac*(dy*a[2][2][i+2]+ddz*a[2][3][i+1]-a[2][3][i]+
                 kappay*b[2][2][i+2]);
    a[2][i+2][3]=fac*(dz*a[2][i+2][2]+ddy*a[2][i+1][3]-a[2][i][3]+
                 kappaz*b[2][i+2][2]);
    a[3][i+2][2]=fac*(dx*a[2][i+2][2]+ddy*a[3][i+1][2]-a[3][i][2]+
                 kappax*b[2][i+2][2]);
    a[i+2][3][2]=fac*(dy*a[i+2][2][2]+ddx*a[i+1][3][2]-a[i][3][2]+
                 kappay*b[i+2][2][2]);
    a[i+2][2][3]=fac*(dz*a[i+2][2][2]+ddx*a[i+1][2][3]-a[i][2][3]+
                 kappaz*b[i+2][2][2]);
  }

  /* 1 index 0, others >=2 */
  for (i=2;i<torderlim-1;i++){
   for (j=2;j<torderlim-i+1;j++){
      b[i+2][j+2][2]=cf1[i-1]*kappa*(dx*a[i+1][j+2][2]-a[i][j+2][2]);
      b[i+2][2][j+2]=cf1[i-1]*kappa*(dx*a[i+1][2][j+2]-a[i][2][j+2]);
      b[2][i+2][j+2]=cf1[i-1]*kappa*(dy*a[2][i+1][j+2]-a[2][i][j+2]);

      a[i+2][j+2][2]=fac*(ddx*cf2[i-1]*a[i+1][j+2][2]+ddy*a[i+2][j+1][2]
                     -cf3[i-1]*a[i][j+2][2]-a[i+2][j][2]+
                     cf1[i-1]*kappa*(dx*b[i+1][j+2][2]-b[i][j+2][2]));
      a[i+2][2][j+2]=fac*(ddx*cf2[i-1]*a[i+1][2][j+2]+ddz*a[i+2][2][j+1]
                     -cf3[i-1]*a[i][2][j+2]-a[i+2][2][j]+
                     cf1[i-1]*kappa*(dx*b[i+1][2][j+2]-b[i][2][j+2]));
      a[2][i+2][j+2]=fac*(ddy*cf2[i-1]*a[2][i+1][j+2]+ddz*a[2][i+2][j+1]
                     -cf3[i-1]*a[2][i][j+2]-a[2][i+2][j]+
                     cf1[i-1]*kappa*(dy*b[2][i+1][j+2]-b[2][i][j+2]));      
    }
  }

  /* 2 indices 1,other >= 1 */
  b[3][3][3]=kappax*a[2][3][3];
  a[3][3][3]=fac*(dx*a[2][3][3]+ddy*a[3][2][3]+ddz*a[3][3][2]+
             kappax*b[2][3][3]);

  for (i=2;i<torderlim-1;i++){
    b[3][3][i+2]=kappax*a[2][3][i+2];
    b[3][i+2][3]=kappax*a[2][i+2][3];
    b[i+2][3][3]=kappay*a[i+2][2][3];

    a[3][3][i+2]=fac*(dx*a[2][3][i+2]+ddy*a[3][2][i+2]+ddz*a[3][3][i+1]
                 -a[3][3][i]+kappax*b[2][3][i+2]);
    a[3][i+2][3]=fac*(dx*a[2][i+2][3]+ddy*a[3][i+1][3]+ddz*a[3][i+2][2]
                 -a[3][i][3]+kappax*b[2][i+2][3]);
    a[i+2][3][3]=fac*(dy*a[i+2][2][3]+ddx*a[i+1][3][3]+ddz*a[i+2][3][2]
                 -a[i][3][3]+kappay*b[i+2][2][3]);
  }

  /* 1 index 1, others >=2 */
  for (i=2;i<torderlim-2;i++){
    for (j=2;j<torderlim-i+1;j++){
      b[3][i+2][j+2]=kappax*a[2][i+2][j+2];
      b[i+2][3][j+2]=kappay*a[i+2][2][j+2];
      b[i+2][j+2][3]=kappaz*a[i+2][j+2][2];

      a[3][i+2][j+2]=fac*(dx*a[2][i+2][j+2]+ddy*a[3][i+1][j+2]
                     +ddz*a[3][i+2][j+1]-a[3][i][j+2]
                     -a[3][i+2][j]+kappax*b[2][i+2][j+2]);
      a[i+2][3][j+2]=fac*(dy*a[i+2][2][j+2]+ddx*a[i+1][3][j+2]
                     +ddz*a[i+2][3][j+1]-a[i][3][j+2]
                     -a[i+2][3][j]+kappay*b[i+2][2][j+2]);
      a[i+2][j+2][3]=fac*(dz*a[i+2][j+2][2]+ddx*a[i+1][j+2][3]
                     +ddy*a[i+2][j+1][3]-a[i][j+2][3]
                     -a[i+2][j][3]+kappaz*b[i+2][j+2][2]);
    }
  }

  /* all indices >=2 */
  for (k=2;k<torderlim-3;k++){
    for (j=2;j<torderlim-1-k;j++){
      for (i=2;i<torderlim+1-k-j;i++){
        b[i+2][j+2][k+2]=cf1[i-1]*kappa*(dx*a[i+1][j+2][k+2]-a[i][j+2][k+2]);
        a[i+2][j+2][k+2]=fac*(ddx*cf2[i-1]*a[i+1][j+2][k+2]
                         +ddy*a[i+2][j+1][k+2]+ddz*a[i+2][j+2][k+1]
                         -cf3[i-1]*a[i][j+2][k+2]-a[i+2][j][k+2]-a[i+2][j+2][k]
                         +cf1[i-1]*kappa*(dx*b[i+1][j+2][k+2]-b[i][j+2][k+2]));
      }
    }
  }
}

double compp_direct(double peng,int ibeg,int iend,double *x,double *y,
                  double *z,double *q,double kappa,int numpars){
  int j;
  double dist2,dist,tx,ty,tz,pi;

  pi = 3.141592653589793238462643;
  peng = 0.0;
  for (j=ibeg;j<iend+1;j++){
    tx=x[j]-tarpos[0];
    ty=y[j]-tarpos[1];
    tz=z[j]-tarpos[2];
    dist2=tx*tx+ty*ty+tz*tz;
    dist=sqrt(dist2);
//  removal the singularities
//    if (dist>1.0e-6){
      peng = peng +q[j]*exp(-kappa*dist)/dist/4/pi;
//    }
  }

  return peng;
}

void cleanup(p){
  int i,j,err;

  /* delete 1D array */
  free(cf);
  free(cf1);
  free(cf2);
  free(cf3);

  /* delete 3D array */
  for (i=0;i<torderlim+3;i++){
    for (j=0;j<torderlim+3;j++){
      free(a[i][j]);
      free(b[i][j]);
    }
    free(a[i]);
    free(b[i]);
  }
  free(a);
  free(b);

  /* delete 1D array */
//  free(xcopy);
//  free(ycopy);
//  free(zcopy);
//  free(qcopy);
  free(orderarr);

  remove_node(p);
}

void remove_node(p){
  int i,j;

//  if (p->exist_ms == 1){
//    for (i=0;i<torder+1;i++){    
//      for (j=0;j<torder+1;j++){
//        free(p->ms[i][j]);
//      }
//      free(p->ms[i]);
//    }
//    free(p->node_idx);
//    free(numpar);
//  }
}


int treecode3d_yukawa(double *x,double *y,double *z,double *q,double kappa,
                       int order,double theta,int maxparnode,int numpars,
                       int *orderind,double *tpoten){
  tnode *troot;
  int i,level,err;
  double xyzminmax[6];
  time_t create_stime,create_etime,tree_stime,tree_etime;
  double create_ttime,tree_ttime;
//printf("numpar is %d\n",numpars);
  err=setup(x,y,z,q,numpars,order,xyzminmax);

  level = 0;
  minlevel = 50000;
  maxlevel = 0;
  troot = (tnode*)malloc(1*sizeof(tnode));

/**************** add timer and create tree ****************/
  create_stime=time(NULL);

  create_tree(troot,0,numpars-1,x,y,z,q,maxparnode,xyzminmax,level,numpars);

  create_etime=time(NULL);
  create_ttime=((double)(create_etime-create_stime));
  printf("runtime for create tree is    %f\n",create_ttime);
/***********************************************************/

/**************** add timer and compute cf *****************/
  tree_stime=time(NULL);

  tree_compp(troot,x,y,z,q,kappa,theta,tpoten,numpars);

  tree_etime=time(NULL);
  tree_ttime=((double)(tree_etime-tree_stime));
  printf("runtime for compute tree is   %f\n",tree_ttime);
/***********************************************************/

  for (i=0;i<numpars;i++) orderind[orderarr[i]]=i;

//  cleanup(troot);

  return 0;
}



