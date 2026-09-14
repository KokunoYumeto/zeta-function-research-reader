# Exact source-viscosity and cutoff-clock morphism

The retained A0656 states a viscosity-one NS stage (LF2866). A0706 displays cutoff viscosity \(r_c\) (LF3571–3577) and later the coordinate embedding \(\tau=t\) with unchanged spatial coordinates (LF3611–3627). The retained response does not display the equation-preserving conversion between those parameters. The linked full research package was not acquired by this bounded worker; this finding is about the retained response.

Keep the original source viscosity \(\nu_s>0\), source coordinates \((t,x)\), and the complete forced source equations

\[
\partial_tu_i+u^j\partial_ju_i-\nu_s\Delta u_i+\partial_ip=f_i,
\qquad \partial_iu^i=0.
\]

Keep the target cutoff parameter \(r_c>0\) and its coordinates \((\tau,x)\). Set

\[
b=\frac{r_c}{\nu_s},\qquad
t=b\tau,
\qquad v_i(\tau,x)=b\,u_i(b\tau,x),
\]

\[
P(\tau,x)=b^2p(b\tau,x),
\qquad f_i^{\mathrm{cut}}(\tau,x)=b^2f_i(b\tau,x).
\]

Here \(b\) has the time-coordinate conversion units required by the displayed equations; no equality of source and cutoff clocks is presumed. The map on points is

\[
\jmath_c^{\nu_s,r_c}:(t,x)\longmapsto
\left(\tau=\frac{\nu_s}{r_c}t,r=r_c,x\right).
\]

Direct differentiation gives

\[
\partial_\tau v_i=b^2\partial_tu_i,
\quad v^j\partial_jv_i=b^2u^j\partial_ju_i,
\quad r_c\Delta v_i=r_cb\Delta u_i=b^2\nu_s\Delta u_i,
\quad \partial_iP=b^2\partial_ip.
\]

All right-hand source fields are evaluated at \((b\tau,x)\). Consequently

\[
\partial_\tau v_i+v^j\partial_jv_i-r_c\Delta v_i+\partial_iP
=f_i^{\mathrm{cut}},
\qquad \partial_iv^i=b\partial_iu^i=0.
\]

The map is invertible: \(\tau=t/b\), \(u_i(t,x)=b^{-1}v_i(t/b,x)\), \(p(t,x)=b^{-2}P(t/b,x)\), and \(f_i(t,x)=b^{-2}f_i^{\mathrm{cut}}(t/b,x)\). This is an exact bijection between the displayed forced-equation data, with the original viscosity retained. It is not a modification of the source solution.

The source's cutoff proper clock is \(dt_c=\sqrt{r_c}\,d\tau/c\). With origins chosen at source \(t=0\), the same morphism gives

\[
t_c=\frac{\nu_s}{c\sqrt{r_c}}t.
\]

The original source endpoint \((t=1,x=0)\) is therefore sent, under this particular same-spatial-coordinate map, to

\[
\left(\tau=\frac{\nu_s}{r_c},r=r_c,x=0\right),
\qquad t_c=\frac{\nu_s}{c\sqrt{r_c}}.
\]

The simple identification \(\tau=t\), \(v=u\), \(P=p\), and unchanged spatial coordinates intertwines these equations only in the parameter-matching case \(r_c=\nu_s\): otherwise the target residual differs by \((\nu_s-r_c)\Delta u_i\). One may instead use a different explicitly typed spatial-coordinate conversion, but it must be written and its action on the source support, wavelengths, force, and norms must be carried through.

For this exact map, the source spatial support and wave numbers at corresponding times are unchanged, whereas

\[
\int |v(\tau,x)|^2dx=b^2\int|u(b\tau,x)|^2dx,
\]

\[
\int_{\tau_0}^{\tau_1}\int|\nabla v|^2dx\,d\tau
=b\int_{b\tau_0}^{b\tau_1}\int|\nabla u|^2dx\,dt.
\]

These follow from the pointwise factor \(b\) in \(v\) and the exact change \(dt=b\,d\tau\). The displayed Brown–York coefficient therefore becomes

\[
[\mathfrak B_2(v,P)]_{\tau\tau}
=\frac{c^4b^2}{16\pi G_5\sqrt{r_c}}|u(b\tau,x)|^2.
\]

Finally, this change of clock does not remove the actual higher-derivative problem. At the corresponding source Fourier wave number \(k\), the magnitude ratio of the displayed correction \(-\tfrac32r_c^2\Delta^2v_i\) to \(-r_c\Delta v_i\) remains exactly \(\tfrac32r_c|k|^2\). Its growth must still be calculated on the source's actual decreasing wavelengths.
