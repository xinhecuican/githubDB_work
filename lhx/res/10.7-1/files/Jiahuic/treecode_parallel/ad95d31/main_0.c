/* Jiahui Chen
   Advisor Dr. Weihua Geng
   2/5/2015 */

/* Inclusions */
#include <stdlib.h> /* malloc(), free() */
#include <stdio.h>  /* printf() */
#include <time.h>   /* time */
#include <math.h>   /* pow() */
#include <stdint.h> /* INT#@_MAX */

/* Writen Inclusions */
#include "treecode.h" /* writen in molecule */


int main(int argc, char *argv[]) {

  /* local variables */
  int i,j,k,err,idx[3],ileverl,istep;
  int ii,jj,kk;
  double t1,abserr,relerr,absinf_err,relinf_err;
  double ***f_inferr, ***f_relinferr,t;
  double tnorm;
  int maxint;
  time_t sttime,ettime,sdtime,edtime;
  double tttime,tdtime;

  char fname[16],density[16];

  /* functions */
  int readin(char fname[16],char density[16]);
  int compute_direct(double* x,double* y,double* z,double* q,
                     double kappa,int numpars,double* dpoten);
  int compute_direct2(double* x,double* y,double* z,double* q,
                      double kappa,int numpars,double* dpoten);
  int compute_direct3(double* x,double* y,double* z,double* q,
                      double kappa,int numpars,double* dpoten);
  int treecode3d_yukawa(double* x,double* y,double* z,double* q,
                        double kappa,int order,double theta,
                        int maxparnode,int numpars,
                        int* orderind,double* tpoten);

  /* set constant */
  kappa=0.0;             // screening coefficient
  maxparnode=500;

  /* by readin to get the surface of molecule */
  sprintf(fname,"1ajj");
  sprintf(density,"3");
  readin(fname,density);
  numpars=nface;         // number of partucakes = number of faces

  x = (double*)calloc(numpars, sizeof(double));
  y = (double*)calloc(numpars, sizeof(double));
  z = (double*)calloc(numpars, sizeof(double));
  q = (double*)calloc(numpars, sizeof(double));
  orderind = (int*)calloc(numpars, sizeof(int));
  if (x==NULL){
    fprintf(stderr, "setup error in main.c: x empty data array");
    return 1;
  }
  if (y==NULL){
    fprintf(stderr, "setup error in main.c: y empty data array");
    return 1;
  }
  if (z==NULL){
    fprintf(stderr, "setup error in main.c: z empty data array");
    return 1;
  }
  if (q==NULL){
    fprintf(stderr, "setup error in main.c: q empty data array");
    return 1;
  }
  if (orderind==NULL){
    fprintf(stderr, "setup error in main.c: orderind empty data array");
    return 1;
  }

  for (i=0;i<numpars;i++){
    for (j=0;j<3;j++){
      idx[j] = nvert[j][i];
      r0[j] = 0.0;
      v0[j] = 0.0;
    }
    for (j=0;j<3;j++){
      for (k=0;k<3;k++){
        r0[k] += 1.0/3.0*sptpos[k][idx[j]-1];
        v0[k] += 1.0/3.0*sptnrm[k][idx[j]-1];
      }
    }

    /* normlaize */
    double dot_product = 0.0;
    for (j=0;j<3;j++)
      dot_product += v0[j]*v0[j];
    dot_product = sqrt(dot_product);
    for (j=0;j<3;j++)
      v0[j] = v0[j]/dot_product;

    x[i] = r0[0];
    y[i] = r0[1];
    z[i] = r0[2];
  }

  /* two tepy charge */
  for (i=0;i<numpars;i++)
    q[i]=1.0;
//    q[i] = random()/(pow(2.0,31.0)-1.0)-0.5;
//  printf("%f\n",q[i]);

  tpoten = (double*)calloc(numpars, sizeof(double));
  dpoten = (double*)calloc(numpars, sizeof(double));
  if (tpoten==NULL){
    fprintf(stderr, "setup error in main.c: tpoten empty data array");
    return 1;
  }
  if (dpoten==NULL){
    fprintf(stderr, "setup error in main.c: dpoten empty data array");
    return 1;
  }

  order = 3;
  theta = 0.5;

  printf("  \n");
  printf("Run parameteres:  ");
  printf("                   numpars    = %d\n ",numpars);
  printf("                   kappa      = %f\n ",kappa);
  printf("                   theta      = %f\n ",theta);
  printf("                   order      = %d\n ",order);
  printf("                   maxparnode = %d\n",maxparnode);

  /* compute potential by treecode */
  for (i=0;i<numpars;i++) tpoten[i]=0.0;

  sttime = time(NULL);
  treecode3d_yukawa(x,y,z,q,kappa,order,theta,maxparnode,numpars,
                    orderind,tpoten);
  ettime = time(NULL);
  tttime = ((double)ettime-sttime);
  printf("  \n");
  printf("Runtime for treecode is %f\n",tttime);

  /* compute potential directly */
  printf("  \n");
  printf("Computing potential - directly\n");

  sdtime = time(NULL);
  compute_direct(x,y,z,q,kappa,numpars,dpoten);
  edtime = time(NULL);
  tdtime = ((double)edtime-sdtime);
  printf("  \n");
  printf("Runtime for treecode is %f\n",tdtime);

  printf("  \n");
  printf("Computing potential error\n");
  printf("  \n");

  abserr=0.0;
  relerr=0.0;
  relinf_err=0.0;
  absinf_err=0.0;
  for (i=0;i<numpars;i++){
    tnorm = fabs(tpoten[i]-dpoten[i]);
    relerr += tnorm*tnorm;
    abserr+=dpoten[i]*dpoten[i];
    if (tnorm>relinf_err){
      relinf_err = tnorm;
    }
    tnorm = fabs(dpoten[i]);
    if (tnorm>absinf_err){
      absinf_err = tnorm;
      maxint = i;
    }
  }

  relerr = sqrt(relerr/abserr);
  relinf_err = relinf_err/absinf_err;
  printf("get max %f @ %d\n",absinf_err,maxint);
  printf("Relative L2 and Inf error: %e,%e\n",relerr,relinf_err);
  printf("  \n");

  for (i=0;i<3;i++){
    free(extr_v[i]);
    free(sptpos[i]);
    free(sptnrm[i]);
    free(atmpos[i]);
  }
  for (i=0;i<2;i++){
    free(extr_f[i]);
  }
  free(extr_v);
  free(sptpos);
  free(sptnrm);
  free(extr_f);
  free(atmpos);
  free(atmrad);

  free(x);

  free(y);

  free(z);

  free(q);

//  free(orderind);

//  free(tpoten);

//  free(dpoten);

  return 0;
} // end main


int compute_direct(double* x,double* y,double* z,double* q, \
                    double kappa,int numpars,double* dpoten){
  int i,j,k;
  double tx,ty,tz,fx,fy,fz,teng,dist,t1;
  double dpeng,temp,peng,pi;

//
  pi = 3.141592653589793238462643;/* 24 digits of point */

  for (i=0;i<numpars;i++) dpoten[i]=0.0;


  for (i=0;i<numpars-1;i++){
    peng = 0.0;
    for (j=i+1;j<numpars;j++){
      tx = x[j]-x[i];
      ty = y[j]-y[i];
      tz = z[j]-z[i];
      dist = sqrt(tx*tx+ty*ty+tz*tz);
      temp = exp(-kappa*dist)/dist/4/pi;
      peng += q[j]*temp;
      dpoten[j] += q[i]*temp;
    }
    dpoten[i] = q[i]*(dpoten[i]+peng);

  }
  dpoten[numpars] = q[numpars]*dpoten[numpars];

}

int compute_direct2(double* x,double* y,double* z,double* q,
                     double kappa,int numpars,double* dpoten){
  int i,j,k;
  double tx,ty,tz,fx,fy,fz,teng,dist,t1;
  double dpeng,temp,peng,pi;

  pi = 3.141592653589793238462643;/* 24 digits of point */

  for (i=0;i<numpars;i++) dpoten[i]=0.0;

  for (i=0;i<numpars;i++){
    peng = 0.0;
    for (j=0;j<numpars;j++){
      if (j!=i){
        tx = x[j]-x[i];
        ty = y[j]-y[i];
        tz = z[j]-z[i];
        dist = sqrt(tx*tx+ty*ty+tz*tz);
        temp = exp(-kappa*dist)/dist/4/pi;
        peng += q[j]*temp;
      }else{
        peng = peng;
      }
    }
    dpoten[i]=q[i]*peng;
  }
}

int compute_direct3(double* x,double* y,double* z,double* q,
                     double kappa,int numpars,double* dpoten){
  int i,j,k;
  double tx,ty,tz,fx,fy,fz,teng,dist,t1;
  double dpeng,temp,peng,pi,tempx,tempq;

  pi = 3.141592653589793238462643;/* 24 digits of point */

  for (i=0;i<numpars;i++) dpoten[i]=0.0;

  for (i=0;i<numpars;i++){
    peng = 0.0;
    tempx=x[i];
    tempq=q[i];
    q[i]=0.0;
    x[i]=100.0;

    for (j=0;j<numpars;j++){


      tx = x[j]-tempx;
      ty = y[j]-y[i];
      tz = z[j]-z[i];
      dist = sqrt(tx*tx+ty*ty+tz*tz);
      temp = exp(-kappa*dist)/dist/4/pi;
      peng += q[j]*temp;

    }
    dpoten[i]=tempq*peng;
    q[i]=tempq;
    x[i]=tempx;
  }
}
