"""Exact differential-algebra replay of first_stage_section.tex.

No sampling is used.  F0,F1,F2,Q0 are independent profile jets with
dQ/dq=F0 and dF_j/dq=F_(j+1).  Every original coordinate and scale
remains symbolic.  The comparison/root existence proof is in the TeX;
this script verifies its algebraic maps and the full PDE residuals.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent/'sources/alpoge_buckmaster_boussinesq.pdf'
checks: list[dict] = []


def reduced(expr):
    return sp.cancel(sp.trigsimp(sp.expand(expr)))


def exact(name, expr):
    entries = list(expr) if isinstance(expr, sp.MatrixBase) else [expr]
    residuals = [reduced(e) for e in entries]
    ok = all(e == 0 for e in residuals)
    checks.append({"name": name, "passed": ok, "residuals": [str(e) for e in residuals]})
    if not ok:
        raise AssertionError((name, residuals))


x1, x2, alpha, alpha_d, alpha_dd, s = sp.symbols("x1 x2 alpha alpha_d alpha_dd s", real=True)
A0, K1, mu, lam1, nu_time = sp.symbols("A0 K1 mu lambda1 nu_time", positive=True)
theta_amp, omega_amp, w, wd = sp.symbols("Theta1 Omega1 w1 w1_d", real=True)
nu_phys, kappa_phys = sp.symbols("nu_phys kappa_phys", nonnegative=True)
F0, F1, F2, Q0 = sp.symbols("F0 F1 F2 Q0", real=True)
x = sp.Matrix([x1, x2])
J = sp.Matrix([[0, -1], [1, 0]])
e2 = sp.Matrix([0, 1])
R = sp.Matrix([[sp.cos(alpha), -sp.sin(alpha)], [sp.sin(alpha), sp.cos(alpha)]])
es = sp.Matrix([sp.sin(s), sp.cos(s)])
zeta = sp.Matrix([sp.sin(s-alpha), sp.cos(s-alpha)])
G = -A0 * R * e2
D = alpha_d * J
a = A0 * sp.sin(s) / K1
b = K1 * zeta[0]
phase = K1 * zeta.dot(x)
phase_t = K1 * alpha_d * (J * zeta).dot(x)

exact("rotation_unit_length", zeta.dot(zeta)-1)
exact("rotation_phase_map", R*es-zeta)
exact("phase_transport", phase_t + (K1*zeta).dot(D*x))
exact("actual_a_from_rotating_parent", -(J*zeta).dot(G)/K1-a)
exact("trace_free_background", sp.trace(D))

def dx(expr, idx):
    return (sp.diff(expr, [x1, x2][idx]) + K1*zeta[idx] *
            (sp.diff(expr, Q0)*F0 + sp.diff(expr, F0)*F1 + sp.diff(expr, F1)*F2))


def dt(expr):
    return (sp.diff(expr, alpha)*alpha_d + sp.diff(expr, alpha_d)*alpha_dd +
            sp.diff(expr, theta_amp)*a*omega_amp + sp.diff(expr, omega_amp)*b*theta_amp +
            sp.diff(expr, w)*wd + phase_t*(sp.diff(expr, Q0)*F0 +
            sp.diff(expr, F0)*F1 + sp.diff(expr, F1)*F2))


def grad(expr):
    return sp.Matrix([dx(expr, 0), dx(expr, 1)])


def lap(expr):
    return dx(dx(expr, 0), 0) + dx(dx(expr, 1), 1)


theta = G.dot(x) + w*theta_amp*F0
velocity = D*x + w*omega_amp/K1 * J*zeta*F0
pressure = (alpha_d**2*x.dot(x)/2 + x2*G.dot(x)/2 +
            (2*w*omega_amp*alpha_d/K1**2 + w*theta_amp*zeta[1]/K1)*Q0)
f_theta_0 = wd*theta_amp*F0
f_u_0 = (alpha_dd - A0*sp.sin(alpha)/2)*J*x + wd*omega_amp/K1*J*zeta*F0
theta_lap = lap(theta)
velocity_lap = velocity.applyfunc(lap)

exact("full_uncut_divergence", dx(velocity[0], 0)+dx(velocity[1], 1))
exact("full_uncut_scalar_residual", dt(theta)+velocity.dot(grad(theta))-f_theta_0)
momentum_left = sp.Matrix([dt(velocity[i])+velocity.dot(grad(velocity[i])) for i in range(2)])
exact("full_uncut_momentum_residual_including_pressure", momentum_left+grad(pressure)-theta*e2-f_u_0)
exact("full_uncut_temperature_laplacian", theta_lap-w*theta_amp*K1**2*F2)
exact("full_uncut_velocity_laplacian", velocity_lap-w*omega_amp*K1*J*zeta*F2)
f_theta_visc = f_theta_0-kappa_phys*w*theta_amp*K1**2*F2
f_u_visc = f_u_0-nu_phys*w*omega_amp*K1*J*zeta*F2
exact("retained_thermal_diffusion_full_PDE", dt(theta)+velocity.dot(grad(theta))-kappa_phys*theta_lap-f_theta_visc)
exact("retained_momentum_viscosity_full_PDE", momentum_left+grad(pressure)-theta*e2-nu_phys*velocity_lap-f_u_visc)

G2 = G+w*K1*theta_amp*zeta
D2 = D+w*omega_amp*(J*zeta)*zeta.T
G2dot = G2.applyfunc(dt)
D2dot = D2.applyfunc(dt)
expectedG2dot = alpha_d*J*G2+(K1*wd*theta_amp+w*A0*sp.sin(s)*omega_amp)*zeta
expectedD2dot = (alpha_dd*J+(wd*omega_amp+w*K1*zeta[0]*theta_amp)*(J*zeta)*zeta.T +
                w*omega_amp*alpha_d*(-zeta*zeta.T+(J*zeta)*(J*zeta).T))
exact("inherited_background_G_derivative", G2dot-expectedG2dot)
exact("inherited_background_D_derivative", D2dot-expectedD2dot)
exact("inherited_background_scalar_residual", G2dot+D2.T*G2-K1*wd*theta_amp*zeta)
core_vorticity = D2[1, 0]-D2[0, 1]
exact("inherited_background_core_vorticity", core_vorticity-2*alpha_d-w*omega_amp)
exact("inherited_background_vorticity_residual", dt(core_vorticity)-G2[0]-(2*alpha_dd-A0*sp.sin(alpha)+wd*omega_amp))

Pb, A1, s2, K2 = sp.symbols("P_b A1 s2 K2", positive=True)
Gfinal = sp.Matrix([A0*sp.sin(s), -A0*sp.cos(s)-A1])
exact("endpoint_full_gradient", G2.subs({alpha:s, w:1, theta_amp:-Pb})-Gfinal.subs(A1,K1*Pb))
exact("endpoint_gradient_norm_squared", Gfinal.dot(Gfinal)-(A0**2+A1**2+2*A0*A1*sp.cos(s)))
e_s2 = sp.Matrix([sp.sin(s2), sp.cos(s2)])
a2 = (A1*sp.sin(s2)+A0*sp.sin(s+s2))/K2
exact("actual_second_growth_a2", -(J*e_s2).dot(Gfinal)/K2-a2)
exact("actual_second_growth_gamma_squared", a2*K2*sp.sin(s2)-(A1*sp.sin(s2)+A0*sp.sin(s+s2))*sp.sin(s2))

P, Pt, z, tau, Pent = sp.symbols("P Pt z tau P_ent", real=True)
Gamma = nu_time*sp.sin(s)
amap = a.subs(A0,nu_time**2)
exact("inverse_original_temperature_equation", -Pent*Gamma*Pt-amap*(-K1/nu_time*Pent*Pt))
exact("inverse_original_vorticity_equation", -K1/nu_time*Pent*Gamma*z*P-K1*sp.sin(s)*z*(-Pent*P))
exact("Riccati_from_exact_multiplier", (z*P*P-Pt**2)/P**2-(z-(Pt/P)**2))
C, m, h, chi, chiy = sp.symbols("Lambda1 m h chi chi_y", positive=True)
exact("compressed_pulse_quotient", C*((-m*h/C*chi)*chi-chiy**2)/chi**2-(-m*h-(C*chiy/chi)**2/C))
T_h = sp.symbols("T_h", nonnegative=True)
holdB = sp.Matrix([[0,Gamma],[0,0]])
exact("hold_generator_nilpotent", holdB*holdB)
exact("exact_hold_propagator_ODE", sp.diff(sp.eye(2)+T_h*holdB,T_h)-holdB*(sp.eye(2)+T_h*holdB))

Z, Zd, Zdd = sp.symbols("Z Z_d Z_dd", real=True)
alphadZ = -Zd/sp.sqrt(1-Z**2)
exact("exact_second_control_derivative", sp.diff(alphadZ,Z)*Zd+sp.diff(alphadZ,Zd)*Zdd-
      (-Zdd/sp.sqrt(1-Z**2)-Z*Zd**2/(1-Z**2)**sp.Rational(3,2)))

k = sp.symbols("k1", integer=True, nonnegative=True)
exact("physical_seed_threshold_frequency_power", (-k-6)+(k+5+sp.Rational(1,8))+sp.Rational(7,8))

# Actual two-wave feedback fields with the full released-profile defect.
d = sp.symbols("d", positive=True)
T, H0, H1, H2, Qold = sp.symbols("T H0 H1 H2 Qold", real=True)
zeta2 = sp.Matrix([sp.sin(s2), sp.cos(s2)])
G0 = sp.Matrix([A0*sp.sin(s), -A0*sp.cos(s)])
Gd = G0+K1*T*e2
a2d = -(J*zeta2).dot(Gd)/K2
b2d = K2*sp.sin(s2)
delta2 = d*K2**2

def dx_feedback(expr, idx):
    oldjet = K1*e2[idx]*(sp.diff(expr,Qold)*H0+sp.diff(expr,H0)*H1+sp.diff(expr,H1)*H2)
    newjet = K2*zeta2[idx]*(sp.diff(expr,Q0)*F0+sp.diff(expr,F0)*F1+sp.diff(expr,F1)*F2)
    return sp.diff(expr,[x1,x2][idx])+oldjet+newjet


def dt_feedback(expr):
    return (sp.diff(expr,T)*(-d*K1**2*T)+sp.diff(expr,w)*wd+
            sp.diff(expr,theta_amp)*(a2d*omega_amp-delta2*theta_amp)+
            sp.diff(expr,omega_amp)*(b2d*theta_amp-delta2*omega_amp))


def grad_feedback(expr):
    return sp.Matrix([dx_feedback(expr,0),dx_feedback(expr,1)])


def lap_feedback(expr):
    return dx_feedback(dx_feedback(expr,0),0)+dx_feedback(dx_feedback(expr,1),1)


th2 = G0.dot(x)+T*H0+w*theta_amp*F0
u2 = w*omega_amp/K2*J*zeta2*F0
p2 = x2*G0.dot(x)/2+T/K1*Qold+w*theta_amp*zeta2[1]/K2*Q0
cross = w*omega_amp/K2*sp.sin(s2)*K1*T*(H1-1)*F0
ft2 = -d*K1**2*T*(H0+H2)+wd*theta_amp*F0-d*K2**2*w*theta_amp*(F0+F2)+cross
fu2 = -A0*sp.sin(s)/2*J*x+wd*omega_amp/K2*J*zeta2*F0-d*K2*w*omega_amp*J*zeta2*(F0+F2)
exact("two_wave_full_scalar_feedback_PDE",dt_feedback(th2)+u2.dot(grad_feedback(th2))-d*lap_feedback(th2)-ft2)
mo2 = sp.Matrix([dt_feedback(u2[i])+u2.dot(grad_feedback(u2[i])) for i in range(2)])
exact("two_wave_full_momentum_feedback_PDE",mo2+grad_feedback(p2)-th2*e2-d*u2.applyfunc(lap_feedback)-fu2)
exact("two_wave_divergence",dx_feedback(u2[0],0)+dx_feedback(u2[1],1))
exact("two_wave_exact_scalar_interaction",u2.dot(grad_feedback(G0.dot(x)+T*H0)-Gd)-cross)
exact("linear_core_force_gradient",sp.diff((-d*K1**2*T*K1*x2),x2)-(-d*K1**3*T))

r, qr, c0, c1, delta, bconst = sp.symbols("r q c0 c1 delta2 b2",positive=True)
Wfun=sp.Function('W')(r)
Omega2=sp.exp(-delta*r)*Wfun
Theta2=sp.exp(-delta*r)*sp.diff(Wfun,r)/bconst
exact("feedback_scalar_inverse_vorticity",sp.diff(Omega2,r)-(bconst*Theta2-delta*Omega2))
temp_res=sp.diff(Theta2,r)-((c0+c1*sp.exp(-qr*r))/bconst*Omega2-delta*Theta2)
exact("feedback_scalar_inverse_temperature",temp_res.subs(sp.diff(Wfun,r,2),(c0+c1*sp.exp(-qr*r))*Wfun))
xx, vv, n, aprev=sp.symbols("x vartheta n a_prev",positive=True)
f, fp, fpp=sp.symbols("f f_prime f_second",real=True)
xxd=-qr*xx/2
xxdd=qr**2*xx/4
exact("feedback_independent_variable_operator",fpp*xxd**2+fp*xxdd-(c0+qr**2*xx**2/4)*f-
      qr**2/4*(xx**2*fpp+xx*fp-(xx**2+4*c0/qr**2)*f))
exact("feedback_convergent_series_recurrence",((vv+2*n)**2-vv**2)*aprev/(4*n*(n+vv))-aprev)
If, Ip, Ipp=sp.symbols("I I_prime I_second",real=True)
g=f*If
gp=fp*If+f*Ip
gpp=fpp*If+2*fp*Ip+f*Ipp
gode=gpp+gp/xx-(1+vv**2/xx**2)*g
subsg={fpp:(1+vv**2/xx**2)*f-fp/xx,Ip:1/(xx*f**2),Ipp:-1/(xx**2*f**2)-2*fp/(xx*f**3)}
exact("feedback_second_fundamental_solution",gode.subs(subsg,simultaneous=True))
exact("feedback_nonzero_wronskian",(f*gp-fp*g).subs(Ip,1/(xx*f**2))-1/xx)
W0,W1,f0,fp0,x0=sp.symbols("W0 W1 f0 fp0 x0",real=True,nonzero=True)
cf=W0/f0
cg=-2*f0/qr*(W1+qr*x0/2*cf*fp0)
exact("feedback_initial_value_map",cf*f0-W0)
exact("feedback_initial_derivative_map",(-qr*x0/2)*(cf*fp0+cg/(x0*f0))-W1)

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


receipt = {
    "status":"passed", "arithmetic":"exact symbolic differential algebra; no floating-point checks",
    "checks_count":len(checks), "checks":checks,
    "proof_scope":"Full comparisons and root existence are proved in first_stage_section.tex; this replay checks algebraic morphisms, inherited feedback, pressure, activation and diffusion residuals.",
    "excluded_claims":["infinite viscous cascade", "compact support of the uncut PDE realization", "terminal-time summability of compensation"],
    "symbols_preserved":["A0", "lambda0", "mu=lambda0", "nu_time=sqrt(A0)", "K1=mu*lambda1", "Lambda1 compression", "nu_phys", "kappa_phys", "x1", "x2", "laboratory e2"],
    "sha256":{p.name:sha256(p) for p in [Path(__file__), HERE/'first_stage_section.tex', HERE/'evolving_diffusive_parent_section.tex', SOURCE]},
}
(HERE/'replay_receipt.json').write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"status":receipt["status"], "checks_count":len(checks), "receipt":"replay_receipt.json"}))
