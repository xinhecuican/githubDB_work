#include <math.h>
#include <time.h>
#include "treeGlobal.h"
double solveTimeNoPC, solveTimePC;
int calculM2MTime, calculM2LTime, calculL2LTime, calculLDSTime;

/* memory counters */
long memcount=0;    /* total memory */
long memXYZQ=0;      /* x, y, z, charges */
long memCUBES=0;    /* cube tree */
long memACCUBE=0;      /* treecode coeffecients */
long memMISC=0;     /* all other stuff */

/* matrix entry counters */
long numKernRealEval=0, numKernCplxEval=0;

/* misc constants */
double fourPi = 4*M_PI, fourPiI = 1.0/(4*M_PI);
double twoPi = 2*M_PI, twoPiI = 1.0/(2*M_PI);
double kappa = 0.0, theta = 0.0;
double zero=0.0, one=1.0;

char hChr='T';             /* transpose */
char nChr='N';             /* normal */
