/* Jiahui Chen
   Program: testing for using xxxx_all_mute.pqr triangulization and xxxx.pqr
   triangulization to get solvation energy
*/

/* Inclusions */
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdint.h>

int main(int argc, char *argv[]) {
  FILE *fp;
  char *proteinfile,titrating[256],**titratinglist,fname[256];
  int ntitrate;

  /* local coefficients */
  int i;

  /* set protein file */
  if ( argv[1] == NULL ) {
    printf("No target protein\n");
    exit(1);
  }
  proteinfile = argv[1];
  sprintf(fname,"%s.txt",proteinfile);
  ntitrate = 0;
  fp = fopen(fname,"r");
    while(fscanf(fp,"%s",titrating) != EOF){
      ntitrate++;
    }
  fclose(fp);

  titratinglist = (char**)calloc(ntitrate, sizeof(char*));
  for (i=0; i<ntitrate; i++)
    titratinglist[i] = (char*)calloc(256, sizeof(char));

  fp = fopen(fname,"r");
    for (i=0; i<ntitrate; i++) {
      fscanf(fp,"%s",titratinglist[i]);
    }
  fclose(fp);

  for (i=1; i<3; i++) {
//  for (i=0; i<ntitrate; i++) {
  /* write uesr data input */
    fp = fopen("usrdata.in","w");
      fprintf(fp,"fname %s\n",titratinglist[0]);
      fprintf(fp,"fname %s\n",titratinglist[i]);
      fprintf(fp,"den 1\n");
      fprintf(fp,"epsp 1\n");
      fprintf(fp,"epsw 80\n");
      fprintf(fp,"bulk_strength 0.15\n");
      fprintf(fp,"order 3\n");
      fprintf(fp,"maxparnode 500\n");
      fprintf(fp,"mac 0.8\n");
    fclose(fp);

    sprintf(fname,"./tabipb.exe");
    system(fname);
  }

  for (i=0; i<ntitrate; i++)
    free(titratinglist[i]);
  free(titratinglist);

}
