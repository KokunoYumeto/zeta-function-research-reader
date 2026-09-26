/* Independent exact computation of g_4(n), second implementation (decreasing order).
   For N = g_4(n-1)+1, ...: does some n-set with maximum exactly N have 4-AP-free H(A)?
   The first such N is g_4(n) (g_4 is strictly increasing: delete the maximum).
   Elements are chosen N=b_1>b_2>...>b_n>=1.
   Pruning (all are necessary conditions for an admissible final set A):
    (P1) heredity: every chosen prefix must itself have 4-AP-free H;
    (P2) the elements still to choose after b lie in [1,b-1] and form an admissible
         set, so b-1 >= g_4(#remaining) (exact values from earlier rounds);
    (P3) M_n <= |T(A)| <= 2*sum(A)+1   (paper eq. ternary-count + EP-03 Sec. 5);
    (P4) 19(M_n^2-1) <= 192*sum(a^2)   (EP-03 theorem),
   where M_n = 19^q 3^r, n=3q+r; unknown elements are bounded by b-1, b-2, ....
   P3/P4 rely on the lemmas under audit; pass second argument 0 to disable them
   (P1,P2 only) as a cross-check that does not depend on those lemmas.
   Usage: ./g4d NMAX [use_P3P4=1]      Written for this audit; not workbench code. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAXS 80000
#define MAXH 8192
static unsigned char M[MAXS];
static int Hv[16][MAXH], Hn[16], newv[16][MAXH];
static int B[16], n_target, found, usepr = 1;
static long long nodes, nsol;
static long long g[16];
static double Mn;
static int firstsol[16];

static int is_free(int k) {
  int *v = Hv[k], m = Hn[k];
  for (int i = 0; i < m; i++) {
    int x = v[i];
    for (int j = i + 1; j < m; j++) {
      int df = v[j] - x;
      if (df % 3) continue;
      int d = df / 3;
      if (M[x + d] && M[x + 2 * d]) return 0;
    }
  }
  return 1;
}

static void dfs(int k, long long S, double Q) { /* k elements chosen: B[0..k-1]; H = Hv[k-1] */
  int r = n_target - k;
  int last = B[k - 1];
  if (r == 0) {
    if (!found) for (int s = 0; s < n_target; s++) firstsol[s] = B[s];
    found = 1; nsol++;
    return;
  }
  for (int b = last - 1; b >= 1; b--) {
    if (b - 1 < g[r - 1]) break; /* P2 */
    if (usepr) {
      long long Smax = S + b; double Qmax = Q + (double)b * b;
      for (int i = 1; i < r; i++) { Smax += b - i; Qmax += (double)(b - i) * (b - i); }
      if ((double)2 * Smax + 1 < Mn) break;              /* P3, monotone in b */
      if (192.0 * Qmax < 19.0 * (Mn * Mn - 1)) break;     /* P4, monotone in b */
    }
    nodes++;
    int *v = Hv[k - 1], m = Hn[k - 1], *w = Hv[k];
    int i = 0, j = 0, t = 0;
    while (i < m || j < m) {
      int x = (i < m) ? v[i] : 1 << 30, y = (j < m) ? v[j] + b : 1 << 30;
      if (x < y) { w[t++] = x; i++; } else if (y < x) { w[t++] = y; j++; } else { w[t++] = x; i++; j++; }
    }
    Hn[k] = t;
    int nn = 0;
    for (int s = 0; s < m; s++) { int y = v[s] + b; if (!M[y]) { M[y] = 1; newv[k][nn++] = y; } }
    if (is_free(k)) { B[k] = b; dfs(k + 1, S + b, Q + (double)b * b); }
    for (int s = 0; s < nn; s++) M[newv[k][s]] = 0;
  }
}

int main(int argc, char **argv) {
  int NMAX = argc > 1 ? atoi(argv[1]) : 7;
  if (argc > 2) usepr = atoi(argv[2]);
  g[0] = 0;
  for (n_target = 1; n_target <= NMAX; n_target++) {
    int q = n_target / 3, rr = n_target % 3;
    Mn = 1; for (int s = 0; s < q; s++) Mn *= 19; for (int s = 0; s < rr; s++) Mn *= 3;
    nodes = 0;
    int N0 = (int)g[n_target - 1] + 1; if (n_target >= 7 && getenv("START")) { int s0 = atoi(getenv("START")); if (s0 > N0) N0 = s0; }
    for (int N = N0;; N++) {
      found = 0; nsol = 0;
      memset(M, 0, sizeof(M));
      Hv[0][0] = 0; Hv[0][1] = N; Hn[0] = 2; M[0] = 1; M[N] = 1; B[0] = N;
      if (n_target == 1) { found = 1; nsol = 1; firstsol[0] = N; }
      else dfs(1, N, (double)N * N);
      if (n_target >= 7) { fprintf(stderr, "n=%d N=%d done, found=%d, nodes so far=%lld\n", n_target, N, found, nodes); fflush(stderr); }
      if (found) {
        g[n_target] = N;
        printf("n=%d g4=%d  #optimal_sets=%lld  nodes=%lld  example(desc)=", n_target, N, nsol, nodes);
        for (int s = 0; s < n_target; s++) printf("%d%s", firstsol[s], s + 1 < n_target ? "," : "\n");
        fflush(stdout);
        break;
      }
    }
  }
  return 0;
}
