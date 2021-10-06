/*
 *  treeGlobal.h
 *
 *  Copyright by Jiahui Chen
 *  some stuff was inspired by Johannes Tausch
 *
 */


/*
 * begin configuration parameters
 */
#define ON 1
#define OFF 0
#define NUMKERNEL OFF        /* count number of kernel evaluations */

/*
 * end configuration parameters
 */
#include <time.h>

#define ONESIXTH 0.16666666666666666666666667
#define ONETHIRD 0.33333333333333333333333333
#define TWOTHIRD 0.66666666666666666666666667
#define ONENINTH 0.11111111111111111111111111
#define ONETWLF 0.08333333333333333333333333
#define ONESQTWO 0.70710678118654752440084436



#ifndef MAX
#define MAX(A,B)  ( (A) > (B) ? (A) : (B) )
#endif

#ifndef MIN
#define MIN(A,B)  ( (A) > (B) ? (B) : (A) )
#endif

#define ABS(A) ( ( (A) > 0 ) ? (A) : (-(A)) )
#define SQR(x) ( (x)*(x) )
#define DIST2(V,W) (SQR((V)[0]-(W)[0]) + SQR((V)[1]-(W)[1]) + SQR((V)[2]-(W)[2]))
#define INNR(V,W) ((V)[0]*(W)[0] + (V)[1]*(W)[1] + (V)[2]*(W)[2]);
#define SWITCH(x,y,tmp) tmp = y; y = x; x = tmp;

#if COMPLEX
#define FABS(A)  sqrt( __real__(A)*__real__(A) + __imag__(A)*__imag__(A) )
#define FABS2(A)  __real__(A)*__real__(A) + __imag__(A)*__imag__(A)
#else
#define FABS(A)  fabs( (A) )
#define FABS2(A) (A)*(A)
#endif

/* memory types */
#define AXYZQ 1      /* x, y, z, charges */
#define ACUBES 2    /* cube tree */
#define AMISC 4     /* misc. memory such as workspaces */


#define NOT !
#define  ABORT()						      \
{   (void)fflush(stdout);					      \
    (void)fprintf(stdout, "panic in file `%s' at line %d.\n",\
	    __FILE__, __LINE__);				      \
    (void)fflush(stdout);					      \
    abort();							      \
}

#define ASSERT(condition) if(NOT(condition)) ABORT()



#define CALLOC(PNTR, NUM, TYPE, FLAG, MTYP)                                 \
{                                                                           \
     if((NUM)*sizeof(TYPE)==0)                                              \
       (void)fprintf(stdout,                                                \
		     "zero element request in file `%s' at line %d\n",      \
		     __FILE__, __LINE__);	                            \
     else if(((PNTR)=(TYPE*)calloc(NUM, sizeof(TYPE)))==NULL) {             \
       (void)fprintf(stdout,                                                \
	 "\ngk: out of memory in file `%s' at line %d\n",                   \
	       __FILE__, __LINE__);                                         \
       (void)fflush(stdout);                                                \
       (void)fflush(stdout);                                                \
       if(FLAG == ON) exit(0);                                              \
     }                                                                      \
     else {                                                                 \
       memcount += ((NUM)*sizeof(TYPE));                                    \
       if(MTYP == AXYZQ) memXYZQ += ((NUM)*sizeof(TYPE));                     \
       else if(MTYP == ACUBES) memCUBES += ((NUM)*sizeof(TYPE));            \
       else if(MTYP == AMISC) memMISC += ((NUM)*sizeof(TYPE));              \
       else {                                                               \
         (void)fprintf(stdout, "CALLOC: unknown memory type %d\n", MTYP);   \
         exit(0);                                                           \
       }                                                                    \
     }                                                                      \
}


#define TRUE 1
#define FALSE 0
#define QUADRILAT 4
#define TRIANGLE 3
#define PCWCONST 0
#define PCWLINEAR 1
#define SINGLE 0
#define DOUBLE 1
#define ADJOINT 2
#define HYPERSING 3
#define COMBINED 4

/* timers */
extern double solveTimeNoPC, solveTimePC;
extern int calculM2MTime, calculM2LTime, calculL2LTime, calculLDSTime;
/* counts of memory usage */
extern long memcount;
extern long memXYZQ, memCUBES, memMISC;
/* counts of kernel evaluations */
extern long numKernRealEval, numKernCplxEval;
/* misc constants */
extern double twoPi, twoPiI, fourPi, fourPiI;
extern double zero, one;
extern char hChr, nChr;
