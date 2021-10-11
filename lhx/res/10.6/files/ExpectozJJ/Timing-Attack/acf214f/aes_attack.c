#include <stdio.h>
#include <stdlib.h>
#include "aes.h"

unsigned char key[16];//={0x2b, 0xa8, 0x62, 0xa3, 0x4d, 0x42, 0xe2, 0x44, 0x27, 0x89, 0xa4, 0x4a, 0xc6, 0x7e, 0xcd, 0xeb};
unsigned char out[16];
unsigned char plaintext[16];
double timing[16][256];
double timing2[256][256];
double timing3[256];
long long tnum[16][256];
long long tnum2[256][256];
long long tnum3[256];

unsigned int start, end;
AES_KEY enc_key;
unsigned int time1, time2;

unsigned int timestamp(void)
{
    unsigned int bottom;
    unsigned int top;
    asm volatile(".byte 15;.byte 49" : "=a"(bottom),"=d"(top));
    return bottom;
}

unsigned int Encrypt(unsigned char x[])
{
    start = timestamp();
    AES_encrypt(x,out,&enc_key);
    end = timestamp();
    time1 = end-start;
    return time1;
}

unsigned long long data[4096*128];

int main()
{
    int i,j,k, m;


    unsigned char b;
    unsigned int iterations;

    FILE *fp2;
    /* Setup Files for timing data */
    fp2=fopen("timing3.txt","w+");

    /* GENERATE UNKNOWN KEY */
    b=0x00;
    for (i=0; i<16; i++)
    {
        key[i]=b++;
        printf("%02x ",key[i]);
        fflush(stdout);
    }
    AES_set_encrypt_key(key,128,&enc_key);

    /*printf("\n\n");
    for (i=0;i<10;i++){
        printf("%08x %08x %08x %08x\n",enc_key.rd_key[4*i],enc_key.rd_key[4*i+1],enc_key.rd_key[4*i+2], enc_key.rd_key[4*i+3]);
        fflush(stdout);
    }*/

    /* Initialise timing matrix as zeros */
    for (i=0; i<16; i++)
    {
        for (j=0; j<256; j++)
        {
            timing3[j]=0;
            timing[i][j]=0;
            for(k=0; k<256; k++)
            {
                timing2[j][k]=0;
                tnum2[j][k]=0;
            }
            tnum[i][j]=0;
            tnum3[j]=0;
        }
    }


    // Instruction for Encryption
    for (i=0;i<256*256;i++) Encrypt(plaintext);

    /* Convert the timing data to the second timing table data for k_i xor k_j*/
    for (i=0;i<256;i++){
        for (j=0;j<256;j++){
            for (iterations=0; iterations<65536/32/8; iterations++)
            {
                for (k=0; k<16; k++)
                {
                    plaintext[k]=out[k]; //Randomise with ciphertext
                }
                plaintext[13]=i;
                plaintext[9]=j;

                for (m = 0; m < 4096*128/8; m++) data[m] = 3; //Flush L1 L2 Cache

                time2 = Encrypt(plaintext);

                if (time2 < 600)
                {
                    timing3[i^j] += (double)time2;
                    tnum3[i^j]+=1;
                }
            }
        }
    }

    for (m = 0; m < 4096*128/8; m++) data[0] += data[m];

    printf("\n %d \n", data[0]);

    for (i=0;i<256;i++){
        timing3[i]/=tnum3[i];
    }

    for (i=0;i<256;i++){
        fprintf(fp2,"%f ",timing3[i]);
    }

    return 0;
}



