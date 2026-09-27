// Independent computation of h(p) (least Ionascu-Wilson class) for all primes p <= N.
// For p = 1 mod 4: h(p) = (R+1)/4 for the least R = 3 mod 4 whose shell a=(p+R)/4 is occupied:
// some u | a^2 with R | 4u+1 or R | u+a.  For p = 3 mod 4 and p = 2: h = 1.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static uint32_t *spf; static uint8_t *comp; // bitset
static int occupied(uint64_t p, uint32_t R) {
    uint64_t a = (p + R) / 4;
    static uint8_t cur[4096], nxt[4096];
    memset(cur, 0, R); cur[1 % R] = 1;
    uint64_t n = a;
    while (n > 1) {
        uint32_t q = spf[n]; int e = 0;
        while (n % q == 0) { n /= q; e++; }
        memset(nxt, 0, R);
        uint32_t qr = q % R;
        for (uint32_t x = 0; x < R; x++) if (cur[x]) {
            uint64_t y = x;
            for (int k = 0; k <= 2*e; k++) { nxt[y] = 1; y = (y * qr) % R; }
        }
        memcpy(cur, nxt, R);
    }
    // targets: -4^{-1} mod R and -a mod R
    uint32_t inv4 = 0; for (uint32_t t = 1; t < R; t++) if ((4ULL*t) % R == 1) { inv4 = t; break; }
    if (R == 1) return 1;
    uint32_t t1 = (R - inv4) % R, t2 = (uint32_t)((R - a % R) % R);
    return cur[t1] || cur[t2];
}
int main(int argc, char **argv) {
    uint64_t N = strtoull(argv[1], 0, 10);
    uint64_t M = N / 4 + 2000;
    spf = calloc(M + 1, sizeof(uint32_t));
    for (uint64_t i = 2; i <= M; i++) if (!spf[i]) for (uint64_t j = i; j <= M; j += i) if (!spf[j]) spf[j] = (uint32_t)i;
    comp = calloc(N / 8 + 2, 1);
    for (uint64_t i = 2; i * i <= N; i++) if (!(comp[i>>3]&(1<<(i&7)))) for (uint64_t j = i * i; j <= N; j += i) comp[j>>3] |= (uint8_t)(1<<(j&7));
    int best = 0; uint64_t nprimes = 0; long hist[200] = {0};
    for (uint64_t p = 2; p <= N; p++) {
        if (comp[p>>3]&(1<<(p&7))) continue;
        nprimes++;
        int h;
        if (p == 2 || p % 4 == 3) h = 1;
        else { h = 1; while (!occupied(p, 4*h - 1)) h++; }
        if (h < 200) hist[h]++;
        if (h >= 19) printf("  big h(%llu)=%d\n", (unsigned long long)p, h);
        if (h > best) { best = h; printf("strict record p=%llu h=%d R=%d\n", (unsigned long long)p, h, 4*h-1); fflush(stdout); }
        if (p == 118801 || p == 806521 || p == 12289 || p == 67369 || p == 7840561 || p == 2521 || p == 87481)
            printf("  h(%llu)=%d\n", (unsigned long long)p, h);
    }
    printf("primes <= %llu: %llu\n", (unsigned long long)N, (unsigned long long)nprimes);
    for (int h = 1; h < 200; h++) if (hist[h]) printf("  #h=%d: %ld\n", h, hist[h]);
    return 0;
}
