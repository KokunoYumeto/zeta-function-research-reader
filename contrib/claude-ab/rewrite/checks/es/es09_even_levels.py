# claude-ab: independent check of the even-level (3,4,inf) covers of ES-09 (matrices from es_s6_counterfactual/src/core.tex).
# The affine action of a 4x4 matrix [[1,0],[t,M]] on (Z/D)^3: v -> t + M v.  Orbits of <A1,A2>; genus by Riemann-Hurwitz,
# g = 1 + (n - c(A1) - c(A2) - c(Ainf))/2 on an orbit of size n, c = number of cycles.
A1=[[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]]
A2=[[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]]
Ai=[[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]]
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
I=[[int(i==j) for j in range(4)] for i in range(4)]
assert mul(mul(A1,A1),A1)==I and mul(mul(A2,A2),mul(A2,A2))==I and mul(mul(A1,A2),Ai)==I
def act(A,v,D):
    x=(1,)+v
    return tuple(sum(A[i][k]*x[k] for k in range(4))%D for i in range(1,4))
def analyse(D):
    pts=[(x,y,z) for x in range(D) for y in range(D) for z in range(D)]
    maps=[{v:act(A,v,D) for v in pts} for A in (A1,A2,Ai)]
    seen=set(); out=[]
    for v in pts:
        if v in seen: continue
        orb={v}; st=[v]
        while st:
            w=st.pop()
            for m in maps[:2]:
                u=m[w]
                if u not in orb: orb.add(u); st.append(u)
        seen|=orb
        cyc=[]
        for m in maps:
            done=set(); c=0
            for w in orb:
                if w in done: continue
                c+=1; t=w
                while t not in done: done.add(t); t=m[t]
            cyc.append(c)
        n=len(orb); g2=n-sum(cyc)+2   # 2g
        out.append((n, g2//2 if g2%2==0 else g2/2))
    return sorted(out)
for D in (2,4,8,16,32):
    r=analyse(D); print(D, r, " sizes D^3/4, 3D^3/4:", [n for n,_ in r]==[D**3//4, 3*D**3//4])
