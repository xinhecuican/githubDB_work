#include <iostream>
#include <fstream>
#include <NTL/ZZ.h>
#define SIZE 256

using namespace std;
using namespace NTL;

unsigned int time1, time2;

unsigned int timestamp(void)
{
    unsigned int bottom;
    unsigned int top;
    asm volatile(".byte 15;.byte 49" : "=a"(bottom),"=d"(top));
    return bottom;
}

ZZ Encrypt(ZZ& a, ZZ& e, ZZ& n)
{
    if (e == 0) {return (ZZ) 1;}

    long k = NumBits(e);
    long i; int m;

    ZZ z;

    z=1;
    for (i = k-1; i >= 0; i--)
    {
        z = (z*z) % n;
        if (bit(e, i) == 1) {z = (z*a) % n;}
        //cout<<data[m][i]<<" "<<endl;
    }

    if (e < 0){
        return InvMod(z, n);
    }
    else{
        return z;
    }
}

ZZ Decrypt(ZZ& a, ZZ& e, ZZ& n)
{
    ofstream fout;
    fout.open("Timing.txt");
    if (e == 0) {return (ZZ) 1;}

    long k = NumBits(e);
    long i; int m;

    unsigned int data[SIZE][k];
    ZZ z;

    for (m=0;m<SIZE;m++){
        z=1;
        for (i = k-1; i >= 0; i--)
        {
            time1=timestamp();
            z = (z*z) % n;
            if (bit(e, i) == 1) {z = (z*a) % n;}
            data[m][i]=timestamp()-time1;
            //cout<<data[m][i]<<" "<<endl;
        }
    }

    unsigned int avg[k];
    for (i=0;i<k;i++){
        avg[i]=0;
        for (m=0;m<SIZE;m++){
            avg[i]+=data[m][i];
        }
        avg[i]/=SIZE;
        fout<<avg[i]<<" "<<endl;
    }

    fout.close();

    if (e < 0){
        return InvMod(z, n);
    }
    else{
        return z;
    }
}

ZZ Decrypt_Blinding(ZZ& a, ZZ& e, ZZ& n, ZZ& b)
{
    ZZ r1=conv<ZZ> ("4303324236324956492569821469382146291456284659246924846594259612564612349");
    ZZ t=Encrypt(r1,b,n);
    ZZ c1=t*a;
    ZZ r_inv=InvMod(r1,n);

    ofstream fout;
    fout.open("Timing_B.txt");
    if (e == 0) {return (ZZ) 1;}

    long k = NumBits(e);
    long i; int m;

    unsigned int data[SIZE][k];
    ZZ z;

    for (m=0;m<SIZE;m++){
        z=1;
        for (i = k-1; i >= 0; i--)
        {
            time1=timestamp();
            z = (z*z) % n;
            if (bit(e, i) == 1) {z = (z*c1) % n;}

            data[m][i]=timestamp()-time1;
            //cout<<data[m][i]<<" "<<endl;
        }
        z=(z*r_inv) % n;
    }


    unsigned int avg[k];
    for (i=0;i<k;i++){
        avg[i]=0;
        for (m=0;m<SIZE;m++){
            avg[i]+=data[m][i];
        }
        avg[i]/=SIZE;
        fout<<avg[i]<<" "<<endl;
    }

    fout.close();

    if (e < 0){
        return InvMod(z, n);
    }
    else{
        return z;
    }
}

int main()
{
    ZZ i=conv<ZZ> ("0");
    ZZ phi_n;
    ZZ p = conv<ZZ> ("12773923387768812656290133259050686398356959994052376880237790534825411026749212679438870099230034772650772642885345677000533307274569067457328328135584763");
    ZZ q = conv<ZZ> ("11387857670961732277078854716422860841400463353288126771202173876424383730365709933890951400155266553509633891848456750972584811360627599890282310671555741");
    phi_n = (p-1)*(q-1);
    ZZ n=p*q;
    ZZ e=(ZZ) 65537;

    //cout<<hex<<n<<endl;
    /*
    for (; i<conv<ZZ> ("20000000000000000000000000000000000000000000000000000000000000000000000"); i++)
    {
        if (n%(SqrRoot(n)-i)==0)
        {
            q = n/(SqrRoot(n)-i);
            cout<<SqrRoot(n)-i<<" "<<q<<endl;
            cout<<"Prime Factors p and q found"<<endl;
            p = n/q;
            phi_n = (p-1)*(q-1);
        }
        fflush(stdout);
    }*/

    ZZ d=InvMod(e,phi_n);

    cout<<"d: "<<d<<endl;

    cout<<"n: "<<n<<endl;
    cout<<"e: "<<e<<endl;
    cout<<"p: "<<p<<endl;
    cout<<"q: "<<q<<endl;
    cout<<"phi_n: "<<phi_n<<endl;

    ZZ m=conv<ZZ> ("3942686243261485164296291698270439703214701283965921846327149865921649832749437964926432964932649821475041297589246973254693824");
    cout<<"Plaintext m: "<<hex<<m<<endl;

    ZZ c=Encrypt(m,e,n);
    cout<<"Ciphertext c: "<<c<<endl;

    ZZ m_1=Decrypt(c,d,n);
    cout<<"Decrypted m: "<<m_1<<endl;

    /** RSA Blinding **/
    m_1=Decrypt_Blinding(c,d,n,e);
    cout<<"Decrypted Blinding m: "<<m_1<<endl;

    //cout<<sqrt(n)<<endl;

    return 0;
}
