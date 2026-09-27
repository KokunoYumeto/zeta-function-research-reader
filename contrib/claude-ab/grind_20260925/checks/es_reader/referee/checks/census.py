from fractions import Fraction as F
rows = [("71", 4590432000, 4212008640, 378423360),
        ("191", 71900438400, 24762018720, 47138419680),
        ("83", 3865350413760, 934648428742, 2930701985018),
        ("167", 486496529512988, 115851891806170, 370644637706818),
        ("239", 88213423774222684, 20524419041579843, 67689004732642841)]
refresh_forced, refresh_surv = 39025685947842, 67649979046694999
for name, dom, f, s in rows:
    print(name, "forced+surv==dom:", f + s == dom, " forced share = %.4f" % (f/dom))
for (n1, d1, f1, s1), (n2, d2, f2, s2), q in zip(rows, rows[1:], (191, 83, 167, 239)):
    print(f"domain({n2}) == surv({n1})*(q-1), q={q}:", s1*(q-1) == d2)
final = 4590432000*190*82*166*238
print("final domain:", final, final == 2825569908564480000)
print("refresh: forced+surv == post-239 survivors:", refresh_forced + refresh_surv == rows[-1][3])
cum_forced = final - refresh_surv
print("cumulative forced:", cum_forced, cum_forced == 2757919929517785001, " proportion:", float(F(cum_forced, final)))
print("first row fractions:", F(4212008640, 4590432000), F(378423360, 4590432000))
print("survivor share: %.5f%%" % (100*refresh_surv/final))
# sum of forced counts lifted to the final domain, as an independent consistency check of the cumulative figure
lift = {"71": 190*82*166*238, "191": 82*166*238, "83": 166*238, "167": 238, "239": 1}
cum2 = sum(f*lift[n] for n, d, f, s in rows) + refresh_forced
print("cumulative forced by lifting each step's forced count:", cum2, cum2 == 2757919929517785001)
# decomposition of the first domain
print(4590432000 == 30*4*18*22*30*46*70)
