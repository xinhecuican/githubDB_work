/*
 * treecode.h
 * Author Jiahui Chen
 */

struct cube {               /* cube */
  int level;                /* 0 => root */
  int nPnts;                /* number of panels in cube */
  int beg,end;              /* begin and end points index */
  int nKids;                /* Number of kids */
  struct cube *kids[8];     /* Array of kids ptrs. */
  int existMom;            /* moments exist 1 or no 0 */
  double *mom;              /* moments */
  double *lec;              /* local expansion coefficients */
  double max[3], min[3];    /* max center min */
  double ctr[3];
  double eRad;              /* half-diameter of enclosing box */
};
typedef struct cube cube;



struct ssystem {
  int maxparCube;           /* max particles per cube */
  int nPnts;                /* nr of panels */
  int nCubes;               /* nr of finest cube level */
  int layer;                /* single layer=0; double layer=1; adjoint=2 */
  int *nMom;                /* number of moments (as a function of order) */
  int maxSngs;              /* max number of panels in a finest level cube */
  int max1Nbrs;             /* max number of frist neighbors that a cube can have */
  int *orderarr;            /* where the point is originally from */
  int order;                /* order */
  double kappa;             /* kappa */
  double theta;             /* MAC */
  double *positions;        /* positions */
  double *charges;          /* charges */
  cube *topCube;            /* the first cube (biggest tree) */
};
typedef struct ssystem ssystem;
