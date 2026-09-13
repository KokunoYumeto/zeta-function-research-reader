# Independent audit of the endpoint product optimization

Date: 2026-09-13. Reviewer: the independent product-bound review agent.

Scope: the scalar identities and extrema in the first endpoint-product paste supplied in this session, and the sharper optimization proposed by the parent endpoint-product task. This record proves the scalar statements directly. It does not claim that every scalar extremizer is realized by an arithmetic moment measure. The exact observation map from an arithmetic window to these scalar data is recorded below; its extremizers are taken in its explicitly enlarged codomain.

The supplied text was read in full, including its treatment of the phase, the four endpoint volumes, the monic norm endpoints, the determinant and confluent-transfer cancellations, the literal-mass Gaussian fixture, and the selected representative. The separately supplied arithmetic-bound paste was also read in full to identify the intended analytic interface. Auditing its local zeta estimate is outside this independent scalar subtask.

## 1. Objects, domains, and the exact observation

Let r be an integer at least one. A scalar window consists of positive numbers omega_0,...,omega_r; positive volumes V_{-1},V_0,...,V_r with V_j <= V_{j-1}; nonnegative allowances epsilon_0,...,epsilon_{r-1}; and real phases phi_0,...,phi_{r-1}. Put

\[
d_j=V_j/V_{j-1}\in(0,1],\quad
a_j=\omega_{j+1}/\omega_j>0,\quad
\Omega=\omega_r/\omega_0=\prod_{j=0}^{r-1}a_j.
\]

The scalar window under audit has the exact equations

\[
\epsilon_j^2+\phi_j^2=a_jf_j,\qquad
f_j=(1-d_j)(d_{j+1}^{-1}-1)
=\frac{(1-d_j)(1-d_{j+1})}{d_{j+1}}.
\tag{R1}
\]

An original arithmetic window at degrees n,...,n+r maps to these coordinates by

\[
(\omega_{h,k,n+j},V_{h,k,n+j},\epsilon_{h,k,n+j},
 \sigma-\partial_\theta\log V_{h,k,n+j})
\longmapsto(\omega_j,V_j,\epsilon_j,\phi_j),
\tag{R2}
\]

where the target indices are obtained only by subtracting n. In (R2) the original theta, packet, tensor degree, source mass, and generator are retained. Formula (R1) is the supplied exact radius identity evaluated by this map. No surjectivity of (R2) is used in any bound for its image. The scalar constructions below prove surjectivity only onto the explicitly prescribed endpoint data inside the scalar domain (R1).

Multiplying the r equations (R1), with every phase present, yields

\[
K:=\prod_{j=0}^{r-1}(\epsilon_j^2+\phi_j^2)
=\Omega F(d_0,...,d_r),
\quad
F=\frac{(1-d_0)(1-d_r)}{d_r\prod_{j=1}^{r-1}d_j}
   \prod_{j=1}^{r-1}(1-d_j)^2.
\tag{R3}
\]

Indeed each interior numerator (1-d_j) occurs in the factors f_{j-1} and f_j, the endpoint numerators occur once, and the denominator is exactly d_1...d_r. The norm factors telescope to Omega. This proves the window identity without discarding an imbalance term.

## 2. Four fixed endpoint volumes: optimum and every boundary case

For r>=2 fix alpha=d_0, beta=d_r, and t=product_{j=1}^{r-1}d_j. Set s=r-1. The admissible endpoint ratios are alpha,beta,t in (0,1]. Every such triple occurs for a nonincreasing positive scalar volume sequence: choose an arbitrary positive V_{-1}, set d_0=alpha, each interior d_j=t^{1/s}, d_r=beta, and define V_j=V_{-1} product_{i=0}^j d_i. This construction retains the literal chosen initial volume.

The exact maximum of the contraction product is

\[
F_{\rm four}(\alpha,\beta,t)
=\frac{(1-\alpha)(1-\beta)}{\beta t}
 (1-t^{1/s})^{2s}.
\tag{R4}
\]

For 0<t<1 and all interior d_j<1, put v_j=-log d_j. The function

\[
f(v)=\log(1-e^{-v}),\qquad
f''(v)=-e^{-v}/(1-e^{-v})^2<0
\]

is strictly concave for v>0. On the affine slice sum v_j=-log t, strict concavity gives

\[
\sum_{j=1}^s f(v_j)\le s f((-\log t)/s).
\]

Exponentiation proves product(1-d_j)<=(1-t^{1/s})^s, with equality precisely when every interior d_j=t^{1/s}. An interior d_j=1 makes the left product zero. If t<1 the right product is positive, so that case is strict. If t=1, all interior d_j=1, and both products are zero. Multiplication by the nonnegative endpoint factor in (R3) proves (R4).

When alpha=1 or beta=1, F is identically zero for every admissible interior sequence. Therefore uniqueness of the maximizing interior sequence may only be asserted when alpha<1, beta<1, and t<1. In that strictly contracting case the optimizer is unique. For s=1 there is only one interior variable and the same statement reduces to its forced value d_1=t.

The corresponding allowance bound is

\[
E:=\min_j\epsilon_j
\le U_{\rm four}:=(\Omega F_{\rm four})^{1/(2r)}.
\tag{R5}
\]

This follows from E^{2r}<=product epsilon_j^2<=K and (R3)-(R4). It is sharp among the scalar windows (R1), including all degenerate endpoints. In the strictly contracting case, choose the maximizing d_j, retain the prescribed norm ratio Omega, let U=(Omega product f_j)^{1/(2r)}, and set a_j=U^2/f_j, phi_j=0, epsilon_j=U. Then every a_j is positive and

\[
\prod_j a_j=U^{2r}/\prod_j f_j=\Omega.
\]

Starting at any literal positive omega_0, the recursion omega_{j+1}=a_j omega_j therefore reaches the prescribed omega_r=Omega omega_0. Every equation (R1) holds, and equality holds in (R5).

For alpha=1, beta=1, or t=1, at least one f_j is zero and U_four=0. Choose any positive norm ratios a_j with product Omega, take phi_j=0, and set epsilon_j=sqrt(a_j f_j). At least one allowance is zero, so E=0=U_four. This handles the zero case without using an undefined quotient U^2/f_j.

For r=1 there is no t coordinate and no power 1/(r-1). The exact formula is

\[
F=(1-\alpha)(1-\beta)/\beta,\qquad
E=\epsilon_0\le\sqrt{\Omega F}.
\tag{R6}
\]

Its sharpness follows by taking phi_0=0, including either endpoint equal to one.

## 3. Only the combined logarithmic budget fixed: the unique extremum

Fix B>=0 and impose

\[
B=-\log(d_0d_r\prod_{j=1}^{r-1}d_j^2).
\tag{R7}
\]

The coordinate map d_j=e^{-t_j} is a bijection from the admissible set onto the compact simplex

\[
t_j\ge0,\qquad t_0+t_r+2\sum_{j=1}^{r-1}t_j=B.
\tag{R8}
\]

The change of coordinates is exact; no source object or mass is changed. If B=0, every t_j=0, every d_j=1, and F=0.

Suppose B>0. The continuous function F attains a maximum on (R8). Every boundary point has some t_j=0 and hence F=0. Positive t_j satisfying (R8) exist, and at any such point F>0. Thus every maximizing point is in the relative interior. There

\[
\log F=\log(1-e^{-t_0})+\log(1-e^{-t_r})+t_r
       +\sum_{j=1}^{r-1}\{2\log(1-e^{-t_j})+t_j\}.
\tag{R9}
\]

The Hessian is diagonal. Its endpoint entries are -e^{t_j}/(e^{t_j}-1)^2, and its interior entries are -2e^{t_j}/(e^{t_j}-1)^2. Every entry is strictly negative. Consequently log F is strictly concave, including on the affine hyperplane (R8), so its maximizing point is unique.

The multiplier equations for (R8) are

\[
\frac1{e^{t_0}-1}=\lambda,\quad
1+\frac1{e^{t_r}-1}=\lambda,\quad
1+\frac2{e^{t_j}-1}=2\lambda\quad(1\le j<r).
\tag{R10}
\]

The second equation gives lambda>1. Define x=1/(2 lambda), so 0<x<1/2. Solving every equation (R10) gives

\[
d_0=\frac1{1+2x},\qquad d_r=1-2x,\qquad
d_j=\frac{1-x}{1+x}\quad(1\le j<r).
\tag{R11}
\]

Substitution into the exact budget (R7) gives

\[
B=2\operatorname{atanh}(2x)+4(r-1)\operatorname{atanh}x.
\tag{R12}
\]

The right side has derivative 4/(1-4x^2)+4(r-1)/(1-x^2)>0, tends to zero as x decreases to zero, and tends to infinity as x increases to 1/2. Thus for each B>0 there is exactly one x in (0,1/2) solving (R12). Equations (R11) give the unique maximizer of F on (R7), and direct substitution into (R3) gives

\[
F_{\rm budget}(B)
=\frac{4^r x^{2r}}{(1-4x^2)(1-x^2)^{r-1}}.
\tag{R13}
\]

The formula has the continuous extension F_budget(0)=0. The allowance consequence is E<=Omega^{1/(2r)} F_budget(B)^{1/(2r)}. For B>0 the construction following (R5), applied to (R11), proves scalar sharpness for any prescribed positive norm endpoints with ratio Omega. The B=0 construction uses all zero allowances and phases, with arbitrary positive norm ratios of the required product.

## 4. Exact comparison with the hyperbolic-sine bound

For any a,b in (0,1], direct expansion gives

\[
\sinh^2\!\left(-\frac12\log(ab)\right)
 -(1-a)(b^{-1}-1)
=\frac{(1-2a+ab)^2}{4ab}\ge0.
\tag{R14}
\]

Equality in this local inequality is exactly a(2-b)=1. Put s_j=-(log d_j+log d_{j+1})/2. Then sum_j s_j=B/2. If every f_j>0, every s_j>0, and

\[
F=\prod_j f_j\le\prod_j\sinh^2s_j
\le\sinh^{2r}(B/(2r)),
\tag{R15}
\]

because the second derivative of log sinh s is -1/sinh^2 s<0. If some f_j=0, F=0 and the same inequality follows directly. At a positive maximizing point, equality in (R15) requires all local equalities in (R14) and all s_j equal.

For r>1, those requirements contradict B>0. Indeed the latter equalities say d_j d_{j+1}=p=e^{-B/r}<1 for every j. The former say 1-2d_j+p=0, hence d_j=(1+p)/2 for every j=0,...,r-1. Since r>1, both d_0 and d_1 have this value. Their product equals p, giving (1+p)^2=4p, or (p-1)^2=0, a contradiction. The maximizing F is positive, so this proves the strict estimate

\[
F_{\rm budget}(B)<\sinh^{2r}(B/(2r))\quad(r>1,\ B>0).
\tag{R16}
\]

For r=1, (R12) gives 2x=tanh(B/2) and (R13) gives F_budget(B)=sinh^2(B/2). Equality is attained exactly by the local equality pair (R11). For any r, B=0 gives equality at zero. The strictness statement must retain both qualifications r>1 and B>0.

The four-endpoint maximum (R4) is computed over a subset of the budget slice (R7), so F_four<=F_budget(B). This is an exact inclusion of optimization domains: each sequence with fixed alpha,beta,t satisfies B=-log(alpha beta t^2). Consequently (R5) is never weaker than the original sinh bound. In the positive case, equality F_four=F_budget holds precisely when alpha,beta,t^{1/(r-1)} are the corresponding coordinates (R11). The arithmetic window itself maps into this same subset by (R2).

## 5. The phase polynomial, including zeros and infeasible data

Let a_j=phi_j^2>=0 and define

\[
P(y)=\prod_{j=0}^{r-1}(y+a_j),\qquad y\in[0,\infty).
\tag{R17}
\]

This polynomial is continuous, tends to infinity, and is strictly increasing on [0,infinity). To verify strictness at the endpoint as well, let 0<=u<v. Every v+a_j is positive. If P(u)=0, P(v)>0=P(u). If P(u)>0, every u+a_j is positive and every ratio (v+a_j)/(u+a_j)>1; multiplication gives P(v)>P(u). This proof does not require P'(0)>0, which can fail when several phases vanish.

For a finite K>=0, the equation P(y_*)=K has exactly one nonnegative solution if and only if K>=P(0). If K=P(0), the solution is y_*=0. If K>P(0), it is positive. If K<P(0), there is no admissible y; reporting a zero threshold in this case would conceal inconsistency.

For the actual product K in (R3), one always has K>=P(0), because each epsilon_j^2+phi_j^2>=phi_j^2. Since E^2<=epsilon_j^2 for every j, one obtains

\[
P(E^2)\le K,\qquad E\le\sqrt{y_*}.
\tag{R18}
\]

If an endpoint estimate supplies only an upper bound K_bar>=K, the same monotonicity gives the valid but possibly larger threshold P^{-1}(K_bar). When all phases vanish, P(y)=y^r, so y_*=K^{1/r}. When K=0, at least one phase vanishes and the unique nonnegative threshold is zero, even when other phases do not vanish. The exact equations additionally force a zero allowance at an index where its radius factor is zero, as (R1) records.

The equality classification in (R18) requires care. If K>0 and P(E^2)=K, all factors in both products are positive. Each factor epsilon_j^2+phi_j^2 is at least E^2+phi_j^2, so equality of the positive products forces epsilon_j=E at every index. If K=0, one vanishing factor can make both products zero while other allowances differ; it would be incorrect to infer equal allowances in that case.

## 6. Independent finite-check design and limits

The companion `endpoint_product_independent_checker_20260913.py` checks the displayed local remainder symbolically, the budget maximizer and multiplier equations at exact rational x, exact budget-preserving perturbations, the fixed-endpoint optimizer under exact product-preserving perturbations, sharp scalar realization with literal initial norm seven and initial volume thirteen, the r=1 and zero cases, and polynomial thresholds with repeated zero phases. Its tests use explicit comparisons and exceptions, so optimized Python does not remove them. The checker offers deliberate mutation modes for the local remainder, budget denominator, endpoint orientation, phase feasibility, and squared interior multiplicity. Those controls test concrete formula failures, not a disabled assertion guard.

The mathematical proofs are (R1)-(R18) and their derivations above. Finite cases do not supply an arithmetic realization theorem, a growing-degree volume estimate, or a numerical enclosure of any arithmetic constant. The exact arithmetic relationship is the observation map (R2), its product identity (R3), and the inclusion of its image in the scalar optimization domains (R4) and (R7).

## Review conclusion

The proposed unique budget optimizer and maximum are correct. Strict improvement over the combined sinh bound holds exactly in the asserted positive-budget, r>1 regime. The phase-polynomial threshold is correct with the feasibility condition K>=P(0); equality at P(0), repeated zero phases, and zero endpoint products must be included explicitly. Fixed-endpoint sharpness is valid for the relaxed scalar domain, with the separate zero-case construction above. The source image remains related to that domain by the exact, unaltered map (R2).

### Executed checks

The unmodified checker completed 2,453 checks with zero failures in both normal and optimized Python. The full result records are retained separately. The concrete mutations were rejected in both modes with identical per-check records: local remainder, one failure; budget denominator, 218 failures; endpoint orientation, 120 failures; phase feasibility, eight failures; squared interior multiplicity, three failures. The orientation mutant executes 2,451 checks because its altered endpoint values change which candidate perturbations satisfy the original admissibility inequalities; both modes execute the same 2,451 checks. The other mutations execute 2,453 checks. These deliberately incorrect runs return exit code one; the two unmodified runs return zero. The receipt builder compares every paired normal/optimized result record and checks the expected failure counts and current checker hash.
