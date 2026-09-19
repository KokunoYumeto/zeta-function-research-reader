"""Exact finite checks of TR1, TR4, TR5 and TR9--10.

The diagnostic uses positive finite resolvent sums, not arithmetic zeta
data. It tests the matrix identities/inequalities, including complex
observations, all masses and two deliberate wrong-direction controls.
The all-degree analytic statements are proved in the companion LaTeX.
"""
import itertools
import sympy as s

count = 0
def check(label, statement):
    global count
    if not statement:
        raise RuntimeError(label)
    count += 1
    print('PASS '+label, flush=True)

def psd(a):
    a = a.applyfunc(s.cancel)
    if any(s.cancel(x) != 0 for x in a-a.H):
        return False
    return all(s.cancel(a.extract(ix, ix).det()) >= 0
               for n in range(1, a.rows+1)
               for ix in itertools.combinations(range(a.rows), n))

def quotient(h, a):
    return (a*h.inv()*a.H).inv()

# Pi is kept as a common positive mass factor symbolically. The matrices
# below are pi times their counterparts for the literal 2/pi,4/pi series;
# every quotient scales by exactly the same factor, never by mass one.
points = [s.Rational(1,4), s.Rational(1), s.Rational(9,4), s.Rational(4)]
weights = [s.Rational(2), s.Rational(3,2), s.Rational(5,3), s.Rational(7,4)]
J = 2
full_terms = 7
def coefficient(x, terms):
    return 2 + 4*sum(x/(x+4*j*j) for j in range(1, terms+1))
def gram(terms):
    return s.Matrix(3,3,lambda i,j: sum(w*x**(i+j)*coefficient(x,terms)
                                      for x,w in zip(points,weights)))
H = gram(full_terms)
HJ = gram(J)
Kx = s.Matrix(3,3,lambda i,j:sum(w*x**(i+j+1) for x,w in zip(points,weights)))
upper = HJ + Kx/J
check('TR1 omitted positive resolvent terms',psd(H-HJ))
check('TR1 exact finite tail bound',psd(upper-H))
check('all original masses retained',HJ[0,0] != 1 and H[0,0] != 1)
A = s.Matrix([[1,s.I,2],[0,1,1-s.I]])
QJ,Q,QU = [quotient(g,A) for g in (HJ,H,upper)]
check('TR5 actual complex quotient lower bound',psd(Q-QJ))
check('TR5 actual complex quotient upper bound',psd(QU-Q))
check('negative control: reversed quotient order fails',not psd(QJ-Q))
lift = H.inv()*A.H*Q
check('original attained lift',(A*lift-s.eye(2)).applyfunc(s.cancel) == s.zeros(2))
check('original attained lift energy',(lift.H*H*lift-Q).applyfunc(s.cancel) == s.zeros(2))
eps = s.Rational(1,2)
check('TR4 finite relative inequality',psd(HJ-(1-eps)*H))
check('TR5 finite relative quotient inequality',psd(QJ/(1-eps)-Q))
Cbar=s.Matrix([[1,2+s.I]])
T=quotient(Q,Cbar)
TJ=quotient(QJ,Cbar)
check('TR9 successive original quotient equals composite',
      (T-quotient(H,Cbar*A)).applyfunc(s.cancel)==s.zeros(1))
check('TR9 conductor lower bound',psd(T-TJ))
check('TR9 conductor relative upper bound',psd(TJ/(1-eps)-T))
full=s.Symbol('physical_mass',positive=True)
check('physical mass scales quotient without being discarded',
      (quotient(full*H,A)-full*Q).applyfunc(s.cancel)==s.zeros(2))
label=s.Matrix([[1,2-s.I,3]])
defect=label.H*T*label
approx=label.H*TJ*label
check('TR10 original defect energy bracket',psd(defect-approx) and psd(approx/(1-eps)-defect))
wrong=quotient(s.diag(*[H[i,i] for i in range(3)]),A)
check('negative control: dropping source cross terms changes metric',
      (wrong-Q).applyfunc(s.cancel)!=s.zeros(2))
print(f'{count} exact finite checks passed; two negative controls detected. No native phase evaluated.')
