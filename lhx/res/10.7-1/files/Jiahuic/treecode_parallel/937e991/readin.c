/* Jiahui Chen
   Advisor Dr. Weihua Geng
   2/5/2015 */

/* Inclusions */
#include <stdlib.h> /* malloc(), free() */
#include <stdio.h>  /* printf() */
#include <time.h>   /* time */
#include <math.h>   /* pow() */
#include <string.h>
/* Writen Inclusions */
#include "treecode.h" /* writen in molecule */

/* the part different from readin.f90 same like readin.c  */


/* function read in molecule */
int readin(char fname[16],char density[16]){
  FILE *fp;
  char c;
  char fpath[256],fname_tp[256]; //fname,density
  /* fpath=pathname,fname_tp,fname,density*/

  /* variables in c */
  int i,j,k,i1,i2,i3,j1,j2,j3,ii,jj,kk; //nfacenew,ichanged;
  double a1,a2,a3,b1,b2,b3;//a_norm,r0_norm,v0_norm;

  /* in fortran with double presision */
  double den,prob_rds,pos[3],vector[3];
  int nind[5];

  /* variables in deleted part */
  int iface[3],jface[3],nfacenew,ialert;
  double face[3][3],s_area,face_old[3][3],xx[3],yy[3],cpuf,dist_local,ichanged;
  double area_local;

  double triangle_area(double v[3][3]);

  /* read in vertices */
  sprintf(fpath,"");
  sprintf(fname_tp,"msms -if %s.xyzr -prob 1.4 -de %s -of %s ", fname, density, fname);
  printf("%s\n",fname_tp);
  system(fname_tp);

  /*======================================================================*/

  /* read in vert */
  sprintf(fname_tp, "%s%s.vert",fpath,fname);
  printf("%s\n",fname_tp);

  /* open the file and read through the first two rows */
  fp=fopen(fname_tp,"r");
  for (i=1;i<=2;i++){
    while (c=getc(fp)!='\n'){
   }
  }

  fscanf(fp,"%d %d %lf %lf ",&nspt,&natm,&den,&prob_rds);
  printf("nspt=%d, natm=%d, den=%lf, prob=%lf\n", nspt,natm,den,prob_rds);

  /*allocate variables for vertices file*/
  extr_v=(int**)calloc(3,sizeof(int*));
  for (i=0;i<3;i++){
    extr_v[i]=(int*)calloc(nspt,sizeof(int));
  }
  sptpos=(double**)calloc(3,sizeof(double*));
  for (i=0;i<3;i++){
    sptpos[i]=(double*)calloc(nspt,sizeof(double));
  }
  sptnrm=(double**)calloc(3,sizeof(double*));
  for (i=0;i<3;i++){
    sptnrm[i]=(double*)calloc(nspt,sizeof(double));
  } 


  for (i=0;i<=nspt-1;i++){
    fscanf(fp,"%lf %lf %lf %lf %lf %lf %d %d %d",&a1,&a2,&a3,&b1,&b2,&b3,&i1,&i2,&i3);

    sptpos[0][i]=a1;
    sptpos[1][i]=a2;
    sptpos[2][i]=a3;
    sptnrm[0][i]=b1;
    sptnrm[1][i]=b2;
    sptnrm[2][i]=b3;
    extr_v[0][i]=i1;
    extr_v[1][i]=i2;
    extr_v[2][i]=i3;
  }
  fclose(fp);
  printf("finish reading vertices file\n");

  /* read in faces */
  sprintf(fname_tp, "%s%s.face",fpath,fname);
  fp=fopen(fname_tp,"r");
  for (i=1;i<=2;i++){
    while (c=getc(fp)!='\n'){
   }
  }

  fscanf(fp,"%d %d %lf %lf ",&nface,&natm,&den,&prob_rds);
  printf("nface=%d, natm=%d, den=%lf, prob=%lf\n", nface,natm,den,prob_rds);

  /* allocate variables for vertices file */
  extr_f=(int**)calloc(2,sizeof(int*));
  for (i=0;i<2;i++){
    extr_f[i]=(int*)calloc(nface,sizeof(int));
  }
  nvert=(int**)calloc(3,sizeof(int*));
  for (i=0;i<3;i++){
    nvert[i]=(int*)calloc(nface,sizeof(int));
  }
  
  for (i=0;i<=nface-1;i++){
    fscanf(fp,"%d %d %d %d %d",&j1,&j2,&j3,&i1,&i2);
    nvert[0][i]=j1;
    nvert[1][i]=j2;
    nvert[2][i]=j3;
    extr_f[0][i]=i1;
    extr_f[1][i]=i2;
    }
  fclose(fp);
  printf("finish reading face file\n");

  /* read in atom coodinates and raduis */

  sprintf(fname_tp, "%s%s.xyzr",fpath,fname);
  fp=fopen(fname_tp,"r");

  if ((atmrad=(double *) calloc(natm,sizeof(double)))==NULL) {
    printf("error in allcating atmrad");
  }
  atmpos=(double**)calloc(3,sizeof(double*));
  for (i=0;i<3;i++){
    atmpos[i]=(double*)calloc(natm,sizeof(double));
  }
  for (i=0;i<=natm-1;i++){
    fscanf(fp,"%lf %lf %lf %lf ",&a1,&a2,&a3,&b1);
    atmpos[0][i]=a1;
    atmpos[1][i]=a2;
    atmpos[2][i]=a3;
    atmrad[i]=b1;
  } 
  fclose(fp);
  printf("finish reading position file\n");

  /* we delete ill performence triangles */
  s_area = 0.0;
  printf("Number of surfaces = %d\n",nface);
  printf("Number of surface points = %d\n",nspt);
  time_t cpu1 = time(NULL);

  nfacenew = nface;

  nvert_copy=(int**)calloc(3,sizeof(int*));
  for (i=0;i<3;i++){
    nvert_copy[i]=(int*)calloc(nface,sizeof(int));
  }
  for (i=0;i<3;i++) memcpy(nvert_copy[i],nvert[i],nface*sizeof(int));

  for (i=0;i<nface;i++){

    for (j=0;j<3;j++){
      iface[j]=nvert[j][i];
      xx[j]=0.0;
    }
    for (j=0; j<3; j++){
      for (ii=0; ii<3; ii++){
        face[ii][j]=sptpos[ii][iface[j]-1];
	xx[ii] += 1.0/3.0*(face[ii][j]);
      }
    }
    /* compute the area of each triangule */
    area_local=triangle_area(face);
    /* if the point is too close with 10 points infront, delete it */
    ialert=0;
    for (j=i-10; (j>=0&&j<i);j++){ /* like ii=max(1,i-10), i-1 in fortran */
      for (ii=0; ii<3; ii++) {
        jface[ii] = nvert[ii][j];
        yy[ii]=0.0;
      }
      for (ii=0;ii<3;ii++){
        for (jj=0;jj<3;jj++){
          face[jj][ii] = sptpos[jj][jface[ii]-1];  
          yy[jj] += 1.0/3.0*(face[jj][ii]);
        }
      }
      dist_local = 0.0;
      for(ii=0;ii<3;ii++) dist_local +=(xx[ii]-yy[ii])*(xx[ii]-yy[ii]);/* dot_product */
      dist_local=sqrt(dist_local);
      if (dist_local<1.0e-6) {
        ialert=1;
printf("particles %d and %d are too close: %e\n", i,j,dist_local);
      }
    }

    /* delete the points */
    if(area_local<1.0e-5 || ialert == 1){
      ichanged = nface-nfacenew;
      for (j=i-ichanged;j<nface;j++){
        for (ii=0;ii<3;ii++)
            nvert_copy[ii][j]=nvert_copy[ii][j+1];
      }
      nfacenew=nfacenew-1;
    }

    /* get the summation of surface area */
    if(area_local>1.0e-5 && ialert == 0)
      s_area += area_local;
  }
  printf("%d face are deleted\n",nface-nfacenew);
  nface=nfacenew;

  for(i=0; i<3; i++) free(nvert[i]);
  free(nvert);

//  nvert = Make2DIntArray(3,nface,"face msms");
  nvert=(int**)calloc(3,sizeof(int*));
  for (i=0;i<3;i++){
    nvert[i]=(int*)calloc(nface,sizeof(int));
  }
  for (i=0;i<nface;i++){
    for(j=0;j<3;j++) nvert[j][i]=nvert_copy[j][i];
  }
  for(i=0;i<3;i++) free(nvert_copy[i]);
  free(nvert_copy);

 

  printf("total area = %f\n",s_area);
  time_t cpu2 = time(NULL);
  cpuf = ((double)(cpu2-cpu1));
  printf("total MSMS post-processing time = %f\n",cpuf);

}

double triangle_area(double v[3][3]){
  int i;
  double a[3], b[3], c[3], aa, bb, cc, ss, t_area;
  for (i=0;i<3;i++){
    a[i] = v[i][0]-v[i][1];
    b[i] = v[i][0]-v[i][2];
    c[i] = v[i][1]-v[i][2];
  }
  aa = sqrt(a[0]*a[0]+a[1]*a[1]+a[2]*a[2]);
  bb = sqrt(b[0]*b[0]+b[1]*b[1]+b[2]*b[2]);
  cc = sqrt(c[0]*c[0]+c[1]*c[1]+c[2]*c[2]);
  ss = 0.5*(aa+bb+cc);
  t_area = sqrt(ss*(ss-aa)*(ss-bb)*(ss-cc));
  return(t_area);
}
