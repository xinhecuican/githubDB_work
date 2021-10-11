/*
 * input.c
 *   various input/output routines for gk package
 *
 *   Author: Jiahui Chen
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "treeGlobal.h"
#include "treecode.h"

/*
 * calculate area and normal
 */
double triangle_area(double v[3][3]){
  int i;
  double a[3], b[3], c[3], aa, bb, cc, ss, t_area;
  for (i=0;i<3;i++){
    a[i] = v[0][i]-v[1][i];
    b[i] = v[0][i]-v[2][i];
    c[i] = v[1][i]-v[2][i];
  }
  aa = sqrt(SQR(a[0])+SQR(a[1])+SQR(a[2]));
  bb = sqrt(SQR(b[0])+SQR(b[1])+SQR(b[2]));
  cc = sqrt(SQR(c[0])+SQR(c[1])+SQR(c[2]));
  ss = 0.5*(aa+bb+cc);
  t_area = sqrt(ss*(ss-aa)*(ss-bb)*(ss-cc));
  return(t_area);
}

/*
 * loadpanel returns a list of panel structs derived from passed data:
 * shape, vertices, and type.
 */
double *loadPanel(char *panelfile, char *density, int *numSing) {
  int i, j, k, ii, shape, type;
  char fpath[256], fname[256];
  FILE *fp, *wfp;

  char c,c1[10],c2[10],c3[10],c4[10],c5[10];
  double a1,a2,a3,b1,b2,b3;//a_norm,r0_norm,v0_norm;
  int i1,i2,i3,j1,j2,j3,ierr,ialert,*iface,*jface;
  double den,prob_rds,xx[3],yy[3],vv[3],normrr,face[3][3],tface[3][3],s_area;
  double **sptpos, **sptnrm, *positions;
  int **extr_v, **extr_f, *nvert;
  double dist_local, area_local, cpuf;
  int nspt, natm, nface;

  /* read in vertices */
  sprintf(fpath,"test_proteins/");
  sprintf(fname,"%s%s.pqr",fpath,panelfile);
  fp=fopen(fname,"r");
  sprintf(fname,"%s%s.xyzr",fpath,panelfile);
  wfp=fopen(fname,"w");
  while(fscanf(fp,"%s %s %s %s %s %lf %lf %lf %lf %lf",c1,c2,c3,
               c4,c5,&a1,&a2,&a3,&b1,&b2) != EOF){
    fprintf(wfp,"%f %f %f %f\n",a1,a2,a3,b2);
  }
  fclose(fp);
  fclose(wfp);

  /* run msms */
  sprintf(fname,"msms -if %s%s.xyzr -prob 1.4 -de %s -of %s%s ", fpath, panelfile, density, fpath, panelfile);
  printf("%s\n",fname);
  ierr=system(fname);

  /*======================================================================*/

  /* read in vert */
  sprintf(fname, "%s%s.vert",fpath,panelfile);
  printf("%s\n",fname);

  /* open the file and read through the first two rows */
  fp=fopen(fname,"r");
  for (i=1;i<=2;i++){
    while (c=getc(fp)!='\n'){
   }
  }

  ierr=fscanf(fp,"%d %d %lf %lf ",&nspt,&natm,&den,&prob_rds);
  //printf("nspt=%d, natm=%d, den=%lf, prob=%lf\n", nspt,natm,den,prob_rds);

  /*allocate variables for vertices file*/
  CALLOC(sptpos, 3, double*, ON, AXYZQ);
  for (i=0;i<3;i++) CALLOC(sptpos[i], nspt, double, ON, AXYZQ);

  for (i=0;i<=nspt-1;i++){
    ierr=fscanf(fp,"%lf %lf %lf %lf %lf %lf %d %d %d",&a1,&a2,&a3,&b1,&b2,&b3,&i1,&i2,&i3);

    sptpos[0][i]=a1;
    sptpos[1][i]=a2;
    sptpos[2][i]=a3;

  }
  fclose(fp);
  printf("finish reading vertices file\n");

  /* read in faces */
  ierr=sprintf(fname, "%s%s.face",fpath,panelfile);
  fp=fopen(fname,"r");
  for (i=1;i<=2;i++){ while (c=getc(fp)!='\n'){} }

  ierr=fscanf(fp,"%d %d %lf %lf ",&nface,&natm,&den,&prob_rds);
  //printf("nface=%d, natm=%d, den=%lf, prob=%lf\n", nface,natm,den,prob_rds);

  /* allocate variables for vertices file */
  CALLOC(nvert, 3*nface, int, ON, AXYZQ);

  for (i=0;i<nface;i++){
    ierr=fscanf(fp,"%d %d %d %d %d",&j1,&j2,&j3,&i1,&i2);
    nvert[3*i]=j1;
    nvert[3*i+1]=j2;
    nvert[3*i+2]=j3;
  }
  fclose(fp);
  printf("finish reading face file\n");

  /* we delete ill performence triangles */
  s_area = 0.0;
  printf("Number of surfaces = %d\n",nface);
  printf("Number of surface points = %d\n",nspt);
  time_t cpu1 = time(NULL);

  CALLOC(positions, 3*nface, double, ON, AXYZQ);

  *numSing = 0;
  for (i=0;i<nface;i++){

    iface = &nvert[3*i];
    for (j=0; j<3; j++){
  xx[j]=0.0;
  for (k=0; k<3; k++){
    face[k][j]=sptpos[j][iface[k]-1];
	  xx[j] += 1.0/3.0*(face[k][j]);
  }
    }
    /* compute the area of each triangule */
    area_local=triangle_area(face);
    /* if the point is too close with 10 points infront, delete it */
    ialert=0;
    for (j=i-10;(j>=0&&j<i);j++){ /* like k=max(1,i-10), i-1 in fortran */
  jface = &nvert[3*j];
  for (k=0; k<3; k++){
    yy[k]=0.0;
    for (ii=0;ii<3;ii++){
      tface[ii][k] = sptpos[k][jface[ii]-1];
      yy[k] += 1.0/3.0*(tface[ii][k]);
    }
  }
  dist_local = 0.0;
  for(k=0;k<3;k++) dist_local +=(xx[k]-yy[k])*(xx[k]-yy[k]);/* dot_product */
  dist_local=sqrt(dist_local);
  if (dist_local<1.0e-6) {
    ialert=1;
    //printf("particles %d and %d are too close: %e\n", i,j,dist_local);
  }
    }

    /* allocate the panel */
    if(area_local>=1.0e-5 && ialert == 0){
  (*numSing)++;

  positions[3*(*numSing-1)] = xx[0];
  positions[3*(*numSing-1)+1] = xx[1];
  positions[3*(*numSing-1)+2] = xx[2];

  s_area += area_local;
    }
  }

  printf("total area = %f\n",s_area);

  time_t cpu2 = time(NULL);
  cpuf = ((double)(cpu2-cpu1));
  printf("total MSMS post-processing time = %f\n",cpuf);

  sprintf(fname,"rm %s%s.xyzr",fpath,panelfile);
  ierr=system(fname);
  sprintf(fname,"rm %s%s.vert",fpath,panelfile);
  ierr=system(fname);
  sprintf(fname,"rm %s%s.face",fpath,panelfile);
  ierr=system(fname);

  for (i=0;i<3;i++){
    free(sptpos[i]);
  }
  free(sptpos);
  free(nvert);

  return (positions);
} /* loadPanel */

double uniform_distribution(double rangelow, double rangehigh){

  double randnum;
  randnum = rand()/(RAND_MAX+1.0)*(rangehigh-rangelow)+rangelow;
  //randnum = rand()/(RAND_MAX/(rangehigh-rangelow))+rangelow;
  return randnum;

}

double *UniformCube(int numSing){
  double *positions;
  int i;

  CALLOC(positions, 3*numSing, double, ON, AXYZQ);

  for ( i=0; i<numSing; i++ ) {
    positions[3*i]   = uniform_distribution(0.0,10.0);
    positions[3*i+1] = uniform_distribution(0.0,10.0);
    positions[3*i+2] = uniform_distribution(0.0,10.0);
  }

  return (positions);
}
