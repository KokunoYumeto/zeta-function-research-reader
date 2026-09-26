/* Third, independent check of small g_4 values (written by the main author, not the audit agent).
   Question for each (n, N): does some n-subset of {1..N} have 4-AP-free subset-sum set H(A)?
   Method: increasing DFS a_1<...<a_n<=N, heredity pruning only (every prefix must be admissible),
   subset sums as a bitset, 4-AP test "exists d>=1 with H & H>>d & H>>2d & H>>3d != 0" by word shifts.
   No lemma of the paper is used. */
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#define W 16             /* 1024 bits: sums up to 1023 */
typedef struct { uint64_t w[W]; } bs;
static void shl(const bs *a, int s, bs *r){ int q=s/64, b=s%64; for(int i=W-1;i>=0;i--){ uint64_t v=0; int j=i-q; if(j>=0){ v=a->w[j]<<b; if(b && j-1>=0) v|=a->w[j-1]>>(64-b);} r->w[i]=v; } }
static void shr(const bs *a, int s, bs *r){ int q=s/64, b=s%64; for(int i=0;i<W;i++){ uint64_t v=0; int j=i+q; if(j<W){ v=a->w[j]>>b; if(b && j+1<W) v|=a->w[j+1]<<(64-b);} r->w[i]=v; } }
static int has4ap(const bs *h, int maxsum){
  bs s1,s2,s3; for(int d=1; 3*d<=maxsum; d++){ shr(h,d,&s1); shr(h,2*d,&s2); shr(h,3*d,&s3);
    for(int i=0;i<W;i++) if(h->w[i]&s1.w[i]&s2.w[i]&s3.w[i]) return 1; }
  return 0; }
static int n, N; static long long nodes, sols; static int A[16], firstA[16];
static void dfs(int k, int last, const bs *h, int sum){
  if(k==n){ if(!sols) memcpy(firstA,A,sizeof(A)); sols++; return; }
  for(int a=last+1; a<=N-(n-1-k); a++){
    bs t, h2; shl(h,a,&t); for(int i=0;i<W;i++) h2.w[i]=h->w[i]|t.w[i];
    nodes++;
    if(has4ap(&h2, sum+a)) continue;
    A[k]=a; dfs(k+1,a,&h2,sum+a);
  }
}
int main(int argc,char**argv){
  n=atoi(argv[1]); int N0=atoi(argv[2]), N1=atoi(argv[3]);
  for(N=N0; N<=N1; N++){ bs h; memset(&h,0,sizeof h); h.w[0]=1; nodes=0; sols=0; dfs(0,0,&h,0);
    printf("n=%d N=%d admissible_n_subsets_of_[1,N]=%lld nodes=%lld", n, N, sols, nodes);
    if(sols){ printf(" first="); for(int i=0;i<n;i++) printf("%d%s",firstA[i],i+1<n?",":""); }
    printf("\n"); fflush(stdout); }
  return 0; }
