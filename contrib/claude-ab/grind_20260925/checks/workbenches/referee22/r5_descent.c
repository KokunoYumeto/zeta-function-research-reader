// Verify that every odd n in [3, LIMIT) falls below itself under T (so, by induction, every n < LIMIT reaches 1).
// 128-bit arithmetic; aborts on overflow risk. Usage: ./r5_descent log2limit
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef unsigned __int128 u128;
int main(int argc,char**argv){
  int e=atoi(argv[1]); uint64_t LIMIT=((uint64_t)1)<<e;
  uint64_t maxsteps=0, worst=0; u128 maxval=0;
  for(uint64_t n=3;n<LIMIT;n+=2){
    u128 x=n; uint64_t steps=0;
    while(x>=n){
      x=3*x+1; while(!(x&1)) x>>=1; steps++;
      if(x>maxval) maxval=x;
      if(x>(((u128)1)<<120)){printf("overflow risk at n=%llu\n",(unsigned long long)n);return 1;}
    }
    if(steps>maxsteps){maxsteps=steps;worst=n;}
  }
  unsigned long long hi=(unsigned long long)(maxval>>64), lo=(unsigned long long)maxval;
  printf("all odd n in [3,2^%d) fall below themselves under T; max odd steps %llu at n=%llu; max value hi=%llu lo=%llu\n",e,(unsigned long long)maxsteps,(unsigned long long)worst,hi,lo);
  return 0;
}
