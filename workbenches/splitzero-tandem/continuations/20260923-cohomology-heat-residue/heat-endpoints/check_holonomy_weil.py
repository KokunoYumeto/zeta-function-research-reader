from pathlib import Path
import hashlib, json, re
import sympy as s
root = Path(__file__).resolve().parent
source = root / "HOLONOMY_AND_WEIL.tex"
text = source.read_text(encoding="utf-8")
checks = []
def verify(name, value):
    assert value, name
    checks.append(name)
verify("HW1 through HW64 once each", sorted(map(int,re.findall(r"\\tag\{HW(\d+)\}",text))) == list(range(1,65)))
labels = re.findall(r"\\label\{([^}]+)\}", text)
verify("unique labels", len(labels)==len(set(labels)))
verify("references resolve", set(re.findall(r"\\(?:eq)?ref\{([^}]+)\}",text)) <= set(labels))
verify("vocabulary constraint", re.search(r"\b"+"pl"+"ain"+r"\b",text,re.I) is None)
verify("no carriage-return corruption", "\r" not in text)
t,L=s.symbols("t L")
for m in range(1,7):
    unit=7+2*t+3*t**2+5*t**3
    inv=s.series(1/unit,t,0,m).removeO()
    pos=sum(L**j*t**j/s.factorial(j) for j in range(m))
    neg=sum((-L)**j*t**j/s.factorial(j) for j in range(m))
    verify(f"unit/exponential residue m={m}",s.rem(s.expand(pos*neg*inv-inv),t**m,t)==0)
    gp=s.diff(unit*t**m,t)
    for j in range(m):
        for k in range(m):
            verify(f"Jacobian m={m},j={j},k={k}",s.expand((-t)**j*t**k*inv*gp).coeff(t,m-1)==(m if j==0 and k==0 else 0))
    N=s.zeros(m)
    for j in range(m-1): N[j+1,j]=1
    expN=sum((L**j*N**j/s.factorial(j) for j in range(m)),s.zeros(m))
    verify(f"full exponential m={m}",expN==s.Matrix(m,m,lambda i,j:L**(i-j)/s.factorial(i-j) if i>=j else 0))
    if m>=2:
        delta=s.zeros(4);delta[3,1]=-s.Rational(1,16)
        Psi=s.zeros(m,4);Psi[m-2,1]=1;Psi[m-1,3]=-16*L
        verify(f"residue intertwiner m={m}",Psi*delta==L*N*Psi)
        verify(f"residue exponential m={m}",Psi*(s.eye(4)+delta)==expN*Psi)
q,qb=s.symbols("q qb",nonzero=True)
W=s.Matrix([[0,1],[1,0]])
verify("reflected offunit matrix isometry",s.diag(qb,1/q)*W*s.diag(q,1/qb)==W)
v=s.Matrix([1,-1]);verify("negative pair value",(v.T*W*v)[0]==-2)
verify("nonidentity unitary loop",W!=s.eye(2) and W.T*W==s.eye(2) and W**2==s.eye(2))
j=s.zeros(8,2);j[2,0]=j[3,0]=1/s.sqrt(2);j[4,1]=j[5,1]=1/s.sqrt(2)
QJ=s.eye(8)
for a,b in [(2,5),(3,4),(6,7)]:
    QJ[a,a]=QJ[b,b]=0;QJ[a,b]=QJ[b,a]=1
verify("exact endpoint embedding",j.T*QJ*j==W)
h=s.symbols("h",real=True);MZ=s.Matrix([[0,2*h],[1,0]])
verify("double-root operator",MZ**2==2*h*s.eye(2))
verify("double-root trace",s.Matrix([[2,s.trace(MZ)],[s.trace(MZ),s.trace(MZ**2)]])==s.diag(2,4*h))
beta=s.symbols("beta")
verify("original clock coefficient",(-2*(beta+3)/16/6).subs(beta,0)==-s.Rational(1,16))
delta=s.zeros(4);delta[3,1]=-s.Rational(1,16)
verify("residue rank and square",delta.rank()==1 and delta**2==s.zeros(4))
stack=[]
for kind,name in re.findall(r"\\(begin|end)\{([^}]+)\}",text):
    if kind=="begin": stack.append(name)
    else: verify("closes "+name,bool(stack) and stack.pop()==name)
verify("all environments closed",not stack)
body=text[text.index(r"\section{"):text.rindex(r"\end{document}")]
for key in re.findall(r"\\bibitem\{([^}]+)\}",body):
    body=body.replace(r"\bibitem{"+key+"}",r"\bibitem{HW-"+key+"}")
    body=body.replace(r"\cite{"+key+"}",r"\cite{HW-"+key+"}")
fragment=root/"HOLONOMY_AND_WEIL_fragment.tex"
fragment.write_text("% Exact body; bibliography keys use HW- prefixes.\n% Requires the standalone source's packages, macros and theorem environments.\n"+body,encoding="utf-8")
receipt={"status":"passed","count":len(checks),"checks":checks,
 "proof_source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
 "fragment_sha256":hashlib.sha256(fragment.read_bytes()).hexdigest(),
 "scope":"Exact auxiliary identities and source integrity only. Complete analytic proofs are in the TeX. No rendering or universal positivity certification."}
(root/"HOLONOMY_WEIL_CHECKS.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k!="checks"},indent=2))
