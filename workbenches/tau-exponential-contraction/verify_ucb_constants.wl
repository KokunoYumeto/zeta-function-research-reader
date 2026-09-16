(* Exact universal-constant checks for UCB_REVIEW_AND_PENALTY_TAIL.md.
   This expression was evaluated in a remote Wolfram kernel on 16 Sep 2026:
   all eight Boolean tests returned True. It is not a Lean certificate,
   an arithmetic-packet computation, or a local script/CI replay.
   All enclosures below use exact integers and rationals; no N[] is used.

   Let a_n=(Binomial[2n,n]/4^n)^2 and m=1-r^2.
   Kbar=Sum[a_n m^n,n>=0], Ebar=1-Sum[a_n m^n/(2n-1),n>=1].
   The term ratio is m*((2n-1)/(2n))^2 < m. Directed integer
   rounding encloses every term. Geometric tails enclose both series.
   Machin's identity and alternating arctangent tails enclose pi.
   The positive atanh series with its geometric tail encloses logarithms.
   Root uniqueness follows from the analytic monotonicity proof in the note.
*)

Module[{scale=10^80,nn=4096,dec,ell,logB,atanB,sqrtB,
  rl,ru,bl,bu,p5,p239,piL,piU,eL,eU,mL,mU,sqL,sqU,
  aL,aU,cL,cU,zL,zU,checks},

 dec[s_] := FromDigits[StringReplace[s,"."->""]]/
   10^StringLength[Last[StringSplit[s,"."]]];

 ell[r_] := Module[
   {m=1-r^2,num,den,lo=scale,hi=scale,skl=scale,sku=scale,
    sel=0,seu=0,fnum,fden,kt,et},
   num=Numerator[m]; den=Denominator[m];
   Do[
     fnum=num(2 i-1)^2; fden=den(2 i)^2;
     lo=Quotient[lo fnum,fden];
     hi=Quotient[hi fnum+fden-1,fden];
     skl+=lo; sku+=hi;
     sel+=Quotient[lo,2 i-1];
     seu+=Quotient[hi+2 i-2,2 i-1],
     {i,1,nn}];
   kt=Ceiling[hi num/(den-num)];
   et=Ceiling[hi num/((den-num)(2 nn+1))];
   {skl/scale,(sku+kt)/scale,1-(seu+et)/scale,1-sel/scale}
 ];

 (* Used with even n, so the displayed partial sum is a lower bound. *)
 atanB[x_,n_] := With[
   {v=Sum[(-1)^i x^(2 i+1)/(2 i+1),{i,0,n-1}]},
   {v,v+x^(2 n+1)/(2 n+1)}];

 (* Every call below has x>1. *)
 logB[x_] := Module[{z=(x-1)/(x+1),v},
   v=2 Sum[z^(2 i+1)/(2 i+1),{i,0,19}];
   {v,v+2 z^41/(41(1-z^2))}];

 sqrtB[x_] := With[{s=Floor[Sqrt[Floor[scale^2 x]]]},
   {s/scale,(s+1)/scale}];

 rl=dec["0.16010167095771835588456745"];
 ru=dec["0.16010167095771835588456746"];
 bl=ell[rl]; bu=ell[ru];
 p5=atanB[1/5,128]; p239=atanB[1/239,32];
 piL=Floor[scale(16p5[[1]]-4p239[[2]])]/scale;
 piU=Ceiling[scale(16p5[[2]]-4p239[[1]])]/scale;
 eL=piL bl[[3]]/2; eU=piU bu[[4]]/2;
 mL=1-ru^2; mU=1-rl^2;
 sqL=sqrtB[mL][[1]]; sqU=sqrtB[mU][[2]];
 aL=logB[(1+rl)sqL/eU^2][[1]];
 aU=logB[(1+ru)sqU/eL^2][[2]];
 cL=logB[eL/sqU][[1]];
 cU=logB[eU/sqL][[2]];
 zL=mL/eU^2; zU=mU/eL^2;

 checks=<|
   "root_lower_sign"->(2rl bl[[2]]-bl[[3]]<0),
   "root_upper_sign"->(2ru bu[[1]]-bu[[4]]>0),
   "a1_lower"->(aL>dec["0.06651895202027"]),
   "a1_upper"->(aU<dec["0.06651895202028"]),
   "c1_lower"->(cL>dec["0.04748604398475"]),
   "c1_upper"->(cU<dec["0.04748604398476"]),
   "geometric_constant_lower"->
     ((1+zL)^2/(1-zL)>dec["40.2398920641"]),
   "geometric_constant_upper"->
     ((1+zU)^2/(1-zU)<dec["40.2398920642"])|>;

 <|"exact_rational_tests"->checks,
   "all_pass"->And@@Values[checks],
   "elliptic_terms"->nn,"rounding_denominator"->scale,
   "log_terms"->20,
   "scope"->"Exact rational enclosures of universal constants; no arithmetic packet integration or Lean execution"|>
]

(* Additional independently executed symbolic/finite checks, separate from
   the eight rational enclosure tests above. Mathematica's EllipticK/E
   argument below is the parameter m, not the modulus sqrt(m). *)
Module[{m,kk,ee,s,t,ps,deriv},
 kk=EllipticK[m]; ee=EllipticE[m]; s=Sqrt[1-m];
 t=ee/(s kk)-1;
 ps=Log[(1+s)/ee]+t Log[Sqrt[m]/ee];
 deriv=FullSimplify[D[ps,m]-D[t,m]Log[Sqrt[m]/ee],
   Assumptions->0<m<1];
 <|"derivative_residual"->deriv,
   "small_rank_margin"->Together[3/7-1/90-3/50-1/5000-1/3],
   "legendre_norms"->Table[
     Integrate[(LegendreP[n,2 x-1]/Binomial[2 n,n])^2,{x,0,1}]
       ==1/((2 n+1)Binomial[2 n,n]^2),{n,0,8}]|>
]
