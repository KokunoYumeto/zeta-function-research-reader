"""Complete, individually reviewed ASCII-equation to TeX display map.

Each source string must match its entire original CodeBlock byte for byte.
No formula block may be omitted, reordered, or silently altered.
"""
DISPLAY_MAP=[
("w_h(t)=|(g/h)(1/2+it)|^2/(2pi), m_(h,k)=w_h^{*k},\nomega_(h,k,j)=inf_(P monic, degree j) integral |P(k/2+iu)|^2 m_(h,k)(u) du.",r"""\[
\begin{aligned}
w_h(t)&=\frac{|(g/h)(1/2+it)|^2}{2\pi},\qquad m_{h,k}=w_h^{*k},\\
\omega_{h,k,j}&=\inf_{\substack{P\text{ monic}\\\deg P=j}}
\int |P(k/2+iu)|^2m_{h,k}(u)\,du.
\end{aligned}
\]"""),
("m_(h,k)(u) >= c_h vartheta_h^(k-3)\n   exp[-a(|u|+k-3)] (1+|u|+k-3)^(-B),  k>=3,",r"""\[
m_{h,k}(u)\ge c_h\vartheta_h^{k-3}
\exp[-a(|u|+k-3)](1+|u|+k-3)^{-B},\qquad k\ge3,
\]"""),
("ell_n(L) = [2 L^(2n+1)/(2n+1)] [2^n (n!)^2/(2n)!]^2.",r"""\[
\ell_n(L)=\frac{2L^{2n+1}}{2n+1}
\left[\frac{2^n(n!)^2}{(2n)!}\right]^2.
\]"""),
("A_(h,k,n,r) := (omega_(h,k,n+r)/omega_(h,k,n))^(1/(2r))\n  <= [(2(n+r))! b^(-2(n+r)) (M_+^k+M_-^k)\n       exp[a(L+k-3)] (1+L+k-3)^B\n       / (c_h vartheta_h^(k-3) ell_n(L))]^(1/(2r)).       (BW1)",r"""\[
\begin{aligned}
A_{h,k,n,r}&:=\left(\frac{\omega_{h,k,n+r}}{\omega_{h,k,n}}\right)^{1/(2r)}\\
&\le\left[
\frac{(2(n+r))!b^{-2(n+r)}(M_+^k+M_-^k)
\exp[a(L+k-3)](1+L+k-3)^B}
{c_h\vartheta_h^{k-3}\ell_n(L)}\right]^{1/(2r)}.
\end{aligned}\tag{BV.1}
\]"""),
("A_(h,k,n,r) <= Cbal_h n,                              (BW2)\nCbal_h = 256 exp(pi) max(1,3/c_h) X K\n            max(1,b^(-3)) 6^(B/3).                  (BW3)",r"""\[
A_{h,k,n,r}\le\mathrm{Cbal}_h n,\tag{BV.2}
\]
\[
\mathrm{Cbal}_h=256\exp(\pi)\max(1,3/c_h)XK
\max(1,b^{-3})6^{B/3}.\tag{BV.3}
\]"""),
("n * 4 * 8^(n/r) * [(2n+1)/(c_h n)]^(1/(2r))\n  <= 256 n max(1,3/c_h).",r"""\[
n\cdot4\cdot8^{n/r}\left[\frac{2n+1}{c_hn}\right]^{1/(2r)}
\le256n\max(1,3/c_h).
\]"""),
("X^(k/(2r)) <= X,\nvartheta_h^(-(k-3)/(2r)) <= K,\nb^(-(n+r)/r) <= max(1,b^(-3)),\nexp[a(n+k-3)/(2r)] <= exp(2a)=exp(pi).",r"""\[
\begin{aligned}
X^{k/(2r)}&\le X,\\
\vartheta_h^{-(k-3)/(2r)}&\le K,\\
b^{-(n+r)/r}&\le\max(1,b^{-3}),\\
\exp[a(n+k-3)/(2r)]&\le\exp(2a)=\exp(\pi).
\end{aligned}
\]"""),
("(1+n+k-3)^(B/(2r)) <= (2n)^(B/n) <= 6^(B/3).",r"""\[
(1+n+k-3)^{B/(2r)}\le(2n)^{B/n}\le6^{B/3}.
\]"""),
("min_(n<=N<n+r) epsilon_N\n   <= (Lambda_(n+r)/Lambda_n)^(1/(2r))\n   = A_(h,k,n,r) (V_n/V_(n+r))^(1/(2r)).              (BW4)",r"""\[
\begin{aligned}
\min_{n\le N<n+r}\epsilon_N
&\le\left(\frac{\Lambda_{n+r}}{\Lambda_n}\right)^{1/(2r)}\\
&=A_{h,k,n,r}\left(\frac{V_n}{V_{n+r}}\right)^{1/(2r)}.
\end{aligned}\tag{BV.4}
\]"""),
("log(V_n/V_(n+r)) >= 2r log[L_(h,k)/(Cbal_h n)].        (BW5)",r"""\[
\log\frac{V_n}{V_{n+r}}\ge2r\log\left[\frac{L_{h,k}}{\mathrm{Cbal}_hn}\right].\tag{BV.5}
\]"""),
("q=q_k=[1+k(m-1)](k+1)^2,\nL_(h,k)=2delta[1+k(m-1)](k+1)floor((k+1)^2/4),\nq>=k>=3, L_(h,k)/q>=delta k/2.",r"""\[
\begin{aligned}
q=q_k&=[1+k(m-1)](k+1)^2,\\
L_{h,k}&=2\delta[1+k(m-1)](k+1)
\left\lfloor\frac{(k+1)^2}{4}\right\rfloor,\\
q&\ge k\ge3,\qquad L_{h,k}/q\ge\delta k/2.
\end{aligned}
\]"""),
("C_k=log(V_q/V_(2q-1)).",r"""\[
C_k=\log\frac{V_q}{V_{2q-1}}.
\]"""),
("C_k >= 2(q-1) log[delta k/(2 Cbal_h)].                 (BW6)",r"""\[
C_k\ge2(q-1)\log\left[\frac{\delta k}{2\mathrm{Cbal}_h}\right].\tag{BV.6}
\]"""),
("log(V_(q-1)/V_(2q-1)) >= C_k,\nlog(V_q/V_(2q)) >= C_k.",r"""\[
\log\frac{V_{q-1}}{V_{2q-1}}\ge C_k,\qquad
\log\frac{V_q}{V_{2q}}\ge C_k.
\]"""),
("B_k >= 2 C_k >= 4(q-1) log[delta k/(2 Cbal_h)],\nliminf_(k->infinity) B_k/(q_k log k) >= 4.            (BW7)",r"""\[
\begin{aligned}
B_k&\ge2C_k\ge4(q-1)\log\left[\frac{\delta k}{2\mathrm{Cbal}_h}\right],\\
\liminf_{k\to\infty}\frac{B_k}{q_k\log k}&\ge4.
\end{aligned}\tag{BV.7}
\]""")]

# Inline mathematical strings in the Markdown prose are plain ASCII rather
# than delimited math. Protect them before Markdown can treat carets as paired
# superscript delimiters. These maps change mathematical typography only.
INLINE_MAP=[
('g=2xi',r'g=2\xi'),('d=deg h',r'd=\deg h'),('S=k/2+iu',r'S=k/2+iu'),
('mu_h^k',r'\mu_h^k'),('a=pi/2',r'a=\pi/2'),('B=42+2d',r'B=42+2d'),
('c_h=b_h c_h^(1)>0',r'c_h=b_hc_h^{(1)}>0'),
('b_h=min_(|v|<=1)(w_h*w_h)(v)>0',r'b_h=\min_{|v|\le1}(w_h*w_h)(v)>0'),
('vartheta_h=integral_[-1,1] w_h>0',r'\vartheta_h=\int_{[-1,1]}w_h>0'),
('0<b<a',r'0<b<a'),
('M_+=integral exp(bt)w_h(t)dt',r'M_+=\int\exp(bt)w_h(t)\,dt'),
('M_-=integral exp(-bt)w_h(t)dt',r'M_-=\int\exp(-bt)w_h(t)\,dt'),
('X=max(1,M_+,M_-)',r'X=\max(1,M_+,M_-)'),
('K=max(1,vartheta_h^(-1))',r'K=\max(1,\vartheta_h^{-1})'),
('i^n',r'i^n'),('n>=0',r'n\ge0'),('r>=1',r'r\ge1'),('k>=3',r'k\ge3'),('L>0',r'L>0'),
('n>=k>=3',r'n\ge k\ge3'),('n/2<=r<=n',r'n/2\le r\le n'),('L=n',r'L=n'),
('ell_n(n)>=2 n^(2n+1)/[(2n+1)4^n]',r'\ell_n(n)\ge2n^{2n+1}/[(2n+1)4^n]'),
('(2(n+r))!<=(4n)^(2(n+r))',r'(2(n+r))!\le(4n)^{2(n+r)}'),
('M_+^k+M_-^k<=2X^k',r'M_+^k+M_-^k\le2X^k'),
('c_h',r'c_h'),('n/r<=2',r'n/r\le2'),('(2n+1)/n<=3',r'(2n+1)/n\le3'),
('0<1/(2r)<=1',r'0<1/(2r)\le1'),('1+n+k-3<=2n',r'1+n+k-3\le2n'),
('2r>=n',r'2r\ge n'),('log(2x)/x',r'\log(2x)/x'),('x>=3',r'x\ge3'),
('[1-log(2x)]/x^2<0',r'[1-\log(2x)]/x^2<0'),
('V_N=det G_N>0',r'V_N=\det G_N>0'),('Lambda_N=omega_N/V_N',r'\Lambda_N=\omega_N/V_N'),
('L_(h,k)',r'L_{h,k}'),('1/2 +/- delta +/- i gamma',r'1/2\pm\delta\pm i\gamma'),
('delta,gamma>0',r'\delta,\gamma>0'),('m>=1',r'm\ge1'),
('n=q',r'n=q'),('r=q-1',r'r=q-1'),('q>=3',r'q\ge3'),
('q/2<=q-1<=q',r'q/2\le q-1\le q'),('q,...,2q-2',r'q,\ldots,2q-2'),
('V_(q-1)>=V_q',r'V_{q-1}\ge V_q'),('V_(2q-1)>=V_(2q)',r'V_{2q-1}\ge V_{2q}'),
('B_k=log[V_(q-1)V_q/(V_(2q-1)V_(2q))]',r'B_k=\log[V_{q-1}V_q/(V_{2q-1}V_{2q})]'),
('q_k>= (k+1)^2',r'q_k\ge(k+1)^2'),('(q_k-1)/q_k',r'(q_k-1)/q_k'),
('delta/(2Cbal_h)',r'\delta/(2\mathrm{Cbal}_h)'),('O_h(q_k)',r'O_h(q_k)'),
('r=q',r'r=q'),
('log(V_q/V_(2q))>=2q log[delta k/(2Cbal_h)]',r'\log(V_q/V_{2q})\ge2q\log[\delta k/(2\mathrm{Cbal}_h)]'),
('limsup B_k/(q_k log k)<4',r'\limsup B_k/(q_k\log k)<4'),
('B_k',r'B_k'),('C_k',r'C_k')]

def protect_inline_math(raw):
    lines=raw.decode('utf-8').splitlines(keepends=True)
    result=[];changes=[]
    ordered=sorted(INLINE_MAP,key=lambda p:len(p[0]),reverse=True)
    for line_number,line in enumerate(lines):
        if line.startswith(('    ','#')):
            result.append(line);continue
        pieces=[];i=0;length=0
        while i<len(line):
            match=next(((old,new) for old,new in ordered if line.startswith(old,i)),None)
            if match is None:pieces.append(line[i]);i+=1;length+=1;continue
            old,new=match;rendered=r'\('+new+r'\)'
            changes.append({'line':line_number,'new_start':length,'source':old,'TeX':rendered})
            pieces.append(rendered);i+=len(old);length+=len(rendered)
        result.append(''.join(pieces))
    restored=list(result)
    for edit in reversed(changes):
        line=restored[edit['line']];start=edit['new_start'];end=start+len(edit['TeX'])
        assert line[start:end]==edit['TeX']
        restored[edit['line']]=line[:start]+edit['source']+line[end:]
    assert ''.join(restored).encode()==raw
    return ''.join(result).encode(),changes
