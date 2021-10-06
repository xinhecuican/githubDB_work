/* Jiahui Chen
   Advisor  Dr. Weihua Geng
   2/11/2015
   Derive from modules.f90 */
/* 6/16/2016
   merge the three head files */

 int natm, nspt, nface, nchr, nt;
 int *natmaff, *nsftype, *mface; // natmsf, nsfatm, npture, nsptno
 int **nvert, **nvert_copy;/* in readin */
 int **extr_v; //[3][nspt]
 int **extr_f; //[2][nface]

 double eps, rds, eps0, eps1, para;
 double *atmrad, *atmchr;
 double **atmpos, **sptpos, **sptnrm, **chrpos, **chrpos_sph;
 double ***chgmnx;

// runtime parameters

int numpars, order, maxparnode, iflag, forcedim;
int itheta, iorder;
double kappa, theta;
double center[3], r0[3], v0[3]; // fortran center(3)

// arrays for coordinates, charge, potential & force

double *x,*y,*z,*q;
double *x_copy, *y_copy, *z_copy, *q_copy;
double *tpoten, *dpoten;
double **tforce, **dforce;
int *orderind, *n_clst;

// timing variables

double timebeg, timeend;

/* head of treecode3d_yukawa */

/* global variables for taylor expansions */
int torder, torderlim;
double *cf;
double *cf1;
double *cf2;
double *cf3;
double ***a;
double ***b;

/* global variables to track tree levels */
int minlevel,maxlevel;

/* global variables used when computing potential/force */
int orderoffset;
double tarpos[3];

/* global variables for position and charge storage */
/* arrays are not copied in this version!! orderarr is till valid*/
int *orderarr;
double *xcopy,*ycopy,*zcopy,*qcopy;

/* node pointer and nod type declarations*/
//#ifndef NODE_POINTER_DEFINED
//#define NODE_POINTER_DEFINED

typedef struct tnode_pointer tnode_pointer;
typedef struct tnode tnode;

//struct tnode_pointer{
//  tnode* p_to_tnode;
//};

struct tnode{
  int node_idx;
  int numpar,ibeg,iend;
  double x_min,y_min,z_min;
  double x_max,y_max,z_max;
  double x_mid,y_mid,z_mid;
  double radius,aspect;
  int level,num_children,exist_ms;
  double ***ms;
  tnode** child;
//  tnode_pointer child[8];
};
