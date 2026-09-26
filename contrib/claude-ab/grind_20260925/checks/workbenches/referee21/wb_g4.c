/* Referee 21 (wbreader): independent small-g4 search.  For each n<=6 find the least N such that some
   n-subset of [1..N] with maximum exactly N has 4-AP-free subset sums (heredity pruning on prefixes),
   and count the optimal sets.  Subset sums kept as a sorted-free char array; 4-AP test by pairs. */
#include <stdio.h>
#include <string.h>
#define MAXS 600
static int n, N; static long cnt; static int A[8];
static int ap4(const char *h, int top){ /* exists x,d>0 with x,x+d,x+2d,x+3d all in h */
  for(int x=0;x<=top;x++) if(h[x]) for(int d=1;x+3*d<=top;d++) if(h[x+d]&&h[x+2*d]&&h[x+3*d]) return 1;
  return 0; }
static void dfs(int k, int last, const char *h, int top){
  if(k==n-1){ /* last element must be exactly N */
    if(N<=last) return; char g[MAXS]; memcpy(g,h,MAXS); for(int x=top;x>=0;x--) if(h[x]) g[x+N]=1;
    if(!ap4(g, top+N)){ A[k]=N; cnt++; if(cnt<=8){ printf("   set:"); for(int i=0;i<n;i++) printf(" %d",A[i]); printf("\n"); } }
    return; }
  for(int a=last+1; a<N; a++){
    char g[MAXS]; memcpy(g,h,MAXS); for(int x=top;x>=0;x--) if(h[x]) g[x+a]=1;
    if(ap4(g, top+a)) continue; A[k]=a; dfs(k+1,a,g,top+a); }
}
int main(void){
  for(n=1;n<=6;n++){ for(N=1;;N++){ char h[MAXS]; memset(h,0,MAXS); h[0]=1; cnt=0; dfs(0,0,h,0);
      if(cnt){ printf("n=%d g4=%d optimal sets=%ld\n", n, N, cnt); fflush(stdout); break; } } }
  return 0; }
