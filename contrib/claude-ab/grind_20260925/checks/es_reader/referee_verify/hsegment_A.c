/* Independent (claude-ab) segmented computation of the least Ionascu-Wilson class h(p) for all primes p <= N.
   h(2)=1, h(p)=1 for p = 3 mod 4; for p = 1 mod 4, h(p) = (R+1)/4 for the least R = 4h-1 whose shell
   a = (p+R)/4 is occupied, i.e. some divisor u of a^2 has u = -4^{-1} or u = -a (mod R) (reader, Thm 3.1(b), Lemma 4.1).
   Factorisations of a are obtained by a segmented sieve (not by a smallest-prime-factor table). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define HMAX 60
#define MAXF 12
int main(int argc,char**argv){
  uint64_t N=strtoull(argv[1],0,10);
  uint64_t S=(uint64_t)1<<24;
  /* base primes up to sqrt(N)+1 */
  uint32_t B=1; while((uint64_t)B*B<=N+4*HMAX) B++;
  uint8_t *isc=calloc(B+1,1); uint32_t *bp=malloc(sizeof(uint32_t)*(B+1)); int nb=0;
  for(uint32_t i=2;i<=B;i++){ if(!isc[i]){bp[nb++]=i; for(uint64_t j=(uint64_t)i*i;j<=B;j+=i) isc[j]=1;} }
  uint8_t *comp=malloc(S);
  uint64_t AS=S/4+HMAX+4;
  uint32_t *rem=malloc(sizeof(uint32_t)*AS); uint32_t *fq=malloc(sizeof(uint32_t)*AS*MAXF);
  uint8_t *fe=malloc(AS*MAXF), *fn=malloc(AS);
  long hist[HMAX+2]; memset(hist,0,sizeof hist);
  int best=0; uint64_t nprimes=0; uint64_t nonhard3=0;
  uint8_t cur[4*HMAX+4], nxt[4*HMAX+4];
  for(uint64_t P0=0;P0<=N;P0+=S){
    uint64_t P1=P0+S; if(P1>N+1) P1=N+1;
    memset(comp,0,S);
    for(int k=0;k<nb;k++){ uint64_t q=bp[k]; if(q*q>=P1) break;
      uint64_t st=((P0+q-1)/q)*q; if(st<q*q) st=q*q;
      for(uint64_t j=st;j<P1;j+=q) comp[j-P0]=1; }
    /* a-range */
    uint64_t A0=P0/4, A1=(P1+4*HMAX)/4+1; uint64_t L=A1-A0+1;
    for(uint64_t i=0;i<L;i++){ rem[i]=(uint32_t)(A0+i); fn[i]=0; }
    for(int k=0;k<nb;k++){ uint64_t q=bp[k]; if(q*q>A1) break;
      uint64_t st=((A0+q-1)/q)*q; if(st==0) st=q;
      for(uint64_t j=st;j<=A1;j+=q){ uint64_t i=j-A0; int e=0; while(rem[i]%q==0){rem[i]/=q;e++;}
        int c=fn[i]; fq[i*MAXF+c]=(uint32_t)q; fe[i*MAXF+c]=(uint8_t)e; fn[i]=c+1; } }
    for(uint64_t i=0;i<L;i++) if(rem[i]>1){ int c=fn[i]; fq[i*MAXF+c]=rem[i]; fe[i*MAXF+c]=1; fn[i]=c+1; rem[i]=1; }
    for(uint64_t p=(P0<2?2:P0);p<P1;p++){
      if(comp[p-P0]) continue;
      nprimes++;
      int h;
      if(p==2||p%4==3) h=1;
      else {
        h=0;
        for(int hh=1;hh<=HMAX;hh++){
          uint32_t R=4*hh-1; uint64_t a=(p+R)/4; uint64_t i=a-A0;
          memset(cur,0,R); cur[1%R]=1;
          for(int c=0;c<fn[i];c++){ uint32_t q=fq[i*MAXF+c]%R; int e=fe[i*MAXF+c];
            memset(nxt,0,R);
            for(uint32_t x=0;x<R;x++) if(cur[x]){ uint64_t y=x; for(int k=0;k<=2*e;k++){ nxt[y]=1; y=(y*q)%R; } }
            memcpy(cur,nxt,R); }
          uint32_t inv4=0; for(uint32_t t=1;t<R;t++) if((4u*t)%R==1){inv4=t;break;}
          uint32_t t1=(R-inv4)%R, t2=(uint32_t)((R-a%R)%R);
          if(cur[t1]||cur[t2]){ h=hh; break; }
        }
        if(h==0){ printf("h exceeds %d at p=%llu\n",HMAX,(unsigned long long)p); h=HMAX+1; }
      }
      hist[h]++;
      { uint64_t r=p%840; int hard=(r==1||r==121||r==169||r==289||r==361||r==529); if(h>=3 && !hard){ nonhard3++; if(nonhard3<=5) printf("  NON-HARD with h>=3: p=%llu h=%d\n",(unsigned long long)p,h);} }
      if(h>best){ best=h; printf("strict record p=%llu h=%d\n",(unsigned long long)p,h); fflush(stdout); }
      else if(h>=19) { printf("  h(%llu)=%d\n",(unsigned long long)p,h); fflush(stdout); }
    }
  }
  printf("primes <= %llu: %llu\n",(unsigned long long)N,(unsigned long long)nprimes);
  printf("primes with h>=3 outside the six hard classes mod 840: %llu\n",(unsigned long long)nonhard3);
  for(int h=1;h<=HMAX+1;h++) if(hist[h]) printf("  #h=%d: %ld\n",h,hist[h]);
  return 0;
}
