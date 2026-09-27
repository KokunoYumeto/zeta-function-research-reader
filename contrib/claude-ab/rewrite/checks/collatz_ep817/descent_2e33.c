/* Every odd n with 3 <= n < 2^33 falls below itself under T(x) = (3x+1)/2 (x odd), x/2 (x even).
   (claude-ab, Opus 5.5, 26 September 2026; check for the remark after Theorem 2.8 of the workbench reader.)
   n = 1 mod 4 falls below itself after two steps, (3n+1)/4 < n, so only n = 3 mod 4 is iterated.
   Arithmetic in unsigned 128-bit integers; the largest value met is reported.
   Consequence: by strong induction every n < 2^33 reaches 1, so the least element of a nontrivial cycle is > 2^33.
   Compile: gcc -O2 -fopenmp descent_2e33.c -o descent_2e33 */
#include <stdio.h>
#include <stdint.h>
typedef unsigned __int128 u128;
int main(void) {
    const uint64_t LIM = (uint64_t)1 << 33;
    uint64_t maxhi = 0, maxlo = 0, bad = 0, count = 0;
    u128 gmax = 0;
    #pragma omp parallel
    {
        u128 lmax = 0; uint64_t lbad = 0, lcount = 0;
        #pragma omp for schedule(static, 1<<20)
        for (uint64_t n = 3; n < LIM; n += 4) {
            u128 x = n; long steps = 0;
            while (x >= n) {
                if (x & 1) x = (3 * x + 1) >> 1; else x >>= 1;
                if (x > lmax) lmax = x;
                if (++steps > 100000) { lbad++; break; }
            }
            lcount++;
        }
        #pragma omp critical
        { if (lmax > gmax) gmax = lmax; bad += lbad; count += lcount; }
    }
    maxhi = (uint64_t)(gmax >> 64); maxlo = (uint64_t)gmax;
    printf("odd n = 3 mod 4 in [3, 2^33): %llu starts iterated\n", (unsigned long long)count);
    printf("starts not falling below themselves within 100000 steps: %llu\n", (unsigned long long)bad);
    printf("largest value met: hi=%llu lo=%llu (as a double: %.6e)\n", (unsigned long long)maxhi, (unsigned long long)maxlo, (double)gmax);
    printf(bad == 0 ? "RESULT: every odd n with 3 <= n < 2^33 falls below itself\n" : "RESULT: FAILURE\n");
    return bad != 0;
}
