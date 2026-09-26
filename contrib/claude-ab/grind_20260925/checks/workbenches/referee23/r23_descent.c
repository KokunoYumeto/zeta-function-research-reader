/* Referee 23: independent re-check that every odd n with 3 <= n < 2^33 falls below itself.
   Different implementation from the author's: odd-to-odd map T(x) = (3x+1)/2^v2(3x+1) with a count-trailing-zeros shift,
   and it records the largest value of 3x+1 met (the peak in the plain 3x+1 map), for comparison with the published
   path record n = 8,528,817,511, peak 18,144,594,937,356,598,024 (OEIS A006884/A006885).
   n = 1 mod 4 needs no iteration: T(n) <= (3n+1)/4 < n.
   Compile: gcc -O2 -fopenmp r23_descent.c -o r23_descent */
#include <stdio.h>
#include <stdint.h>
typedef unsigned __int128 u128;
static int ctz128(u128 x) { uint64_t lo = (uint64_t)x; if (lo) return __builtin_ctzll(lo); return 64 + __builtin_ctzll((uint64_t)(x >> 64)); }
int main(void) {
    const uint64_t LIM = (uint64_t)1 << 33;
    u128 gpeak = 0; uint64_t gpeakn = 0, gbad = 0, gcount = 0, gmaxsteps = 0, gmaxstepsn = 0;
    #pragma omp parallel
    {
        u128 peak = 0; uint64_t peakn = 0, bad = 0, count = 0, maxsteps = 0, maxstepsn = 0;
        #pragma omp for schedule(dynamic, 1<<16)
        for (uint64_t n = 3; n < LIM; n += 4) {           /* n = 3 mod 4 */
            u128 x = n; uint64_t steps = 0;
            do {
                u128 y = 3 * x + 1;
                if (y > peak) { peak = y; peakn = n; }
                x = y >> ctz128(y);
                if (++steps > 10000) { bad++; break; }
            } while (x >= n);
            if (steps > maxsteps) { maxsteps = steps; maxstepsn = n; }
            count++;
        }
        #pragma omp critical
        {
            if (peak > gpeak) { gpeak = peak; gpeakn = peakn; }
            if (maxsteps > gmaxsteps) { gmaxsteps = maxsteps; gmaxstepsn = maxstepsn; }
            gbad += bad; gcount += count;
        }
    }
    /* print the 128-bit peak in decimal */
    char buf[64]; int i = 63; buf[i] = 0; u128 t = gpeak; do { buf[--i] = '0' + (int)(t % 10); t /= 10; } while (t);
    printf("odd starts n = 3 mod 4 below 2^33 iterated: %llu\n", (unsigned long long)gcount);
    printf("starts not below themselves within 10000 odd steps: %llu\n", (unsigned long long)gbad);
    printf("largest 3x+1 met before descent: %s (start n = %llu)\n", &buf[i], (unsigned long long)gpeakn);
    printf("half of it (peak of the (3x+1)/2 map): ");
    t = gpeak / 2; i = 63; buf[i] = 0; do { buf[--i] = '0' + (int)(t % 10); t /= 10; } while (t); printf("%s\n", &buf[i]);
    printf("longest descent: %llu odd steps at n = %llu\n", (unsigned long long)gmaxsteps, (unsigned long long)gmaxstepsn);
    printf(gbad == 0 ? "RESULT: every odd n, 3 <= n < 2^33, falls below itself\n" : "RESULT: FAILURE\n");
    return gbad != 0;
}
