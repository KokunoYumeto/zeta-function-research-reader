/* Independent exact computation of g_4(n): the least N such that some n-element
   set A of distinct positive integers in [1,N] has subset-sum set H(A) (empty sum
   included) free of nonconstant 4-term arithmetic progressions.
   Method: depth-first search over increasing sequences a_1<...<a_n, pruning any
   prefix whose H already contains a nonconstant 4-AP (4-AP-freeness of H is
   hereditary under taking subsets of A), branch-and-bound on the maximum, and
   the valid pruning a_j >= g_4(j) (the j smallest elements form a j-set).
   All optimal sets are counted (search uses max <= best, not < best).
   Usage: ./g4 NMAX            Written for this audit; not workbench code. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXS 60000
#define MAXH 4096
static unsigned char M[MAXS];
static int Hv[16][MAXH];
static int Hn[16];
static int A[16];
static int n_target, best, nsol;
static long long nodes;
static int g[16];
static int firstsol[16];

static int free_after(int k){ /* H = Hv[k], membership in M: any nonconstant 4-AP? */
  int *v=Hv[k], m=Hn[k];
  for(int i=0;i<m;i++){ int x=v[i];
    for(int j=i+1;j<m;j++){ int diff=v[j]-x; if(diff%3) continue; int d=diff/3;
      if(M[x+d] && M[x+2*d]) return 0; } }
  return 1;
}

static void dfs(int k, int last){ /* k elements chosen, H=Hv[k] marked in M */
  int rem = n_target-k;              /* elements still to choose, rem>=1 */
  for(int a=last+1; a<=best-(rem-1); a++){
    if(a < g[k+1]) continue;           /* a_{k+1} >= g_4(k+1) */
    nodes++;
    /* merge Hv[k] and Hv[k]+a */
    int *v=Hv[k], m=Hn[k], *w=Hv[k+1]; int i=0,j=0,t=0;
    int newbuf_start=0; (void)newbuf_start;
    while(i<m || j<m){
      int x = (i<m)? v[i] : 1<<30; int y = (j<m)? v[j]+a : 1<<30;
      if(x<y){ w[t++]=x; i++; } else if(y<x){ w[t++]=y; j++; } else { w[t++]=x; i++; j++; }
    }
    Hn[k+1]=t;
    /* mark new elements */
    static int newv[16][MAXH]; int nn=0;
    for(int s=0;s<m;s++){ int y=v[s]+a; if(!M[y]){ M[y]=1; newv[k][nn++]=y; } }
    int ok = free_after(k+1);
    if(ok){
      A[k]=a;
      if(k+1==n_target){
        if(a<best){ best=a; nsol=0; printf("improved: max=%d set=",a); for(int s=0;s<n_target;s++) printf("%d ",A[s]); printf("\n"); fflush(stdout);} 
        if(nsol==0){ for(int s=0;s<n_target;s++) firstsol[s]=A[s]; }
        nsol++;
      } else dfs(k+1,a);
    }
    for(int s=0;s<nn;s++) M[newv[k][s]]=0;
  }
}

int main(int argc,char**argv){
  int NMAX = 7; int init = argc>1? atoi(argv[1]) : 400;
  g[0]=0; g[1]=1; g[2]=3; g[3]=5; g[4]=14; g[5]=40; g[6]=79;
  for(n_target=7;n_target<=NMAX;n_target++){
    best = init; nsol=0; nodes=0;
    memset(M,0,sizeof(M)); Hv[0][0]=0; Hn[0]=1; M[0]=1;
    dfs(0,0);
    g[n_target]=best;
    printf("n=%d g4=%d  #optimal_sets=%d  nodes=%lld  example=", n_target,best,nsol,nodes);
    for(int s=0;s<n_target;s++) printf("%d%s",firstsol[s], s+1<n_target?",":"\n");
    fflush(stdout);
  }
  return 0;
}
