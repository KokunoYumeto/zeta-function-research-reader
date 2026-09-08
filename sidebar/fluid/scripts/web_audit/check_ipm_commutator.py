# Portable adaptation of ipm/commutator/replay.py
# Only import/output/inventory handling changed; the delimited mathematics is a raw source byte slice.
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import sympy as s
import sympy as sp
import sympy as S
from portable_common import begin, finish
begin('ipm_commutator')
# BEGIN UNCHANGED MATHEMATICAL BODY
checks = []

def exact(label, left, right):
    left_entries = list(left) if isinstance(left, sp.MatrixBase) else [left]
    right_entries = list(right) if isinstance(right, sp.MatrixBase) else [right]
    assert len(left_entries) == len(right_entries)
    residuals = [sp.cancel(sp.expand(l-r)) for l,r in zip(left_entries,right_entries)]
    if any(r != 0 for r in residuals):
        raise AssertionError((label,residuals))
    checks.append({'label':label,'original_left':str(left),'original_right':str(right),
                   'exact_residuals':[str(r) for r in residuals],'status':'pass'})

k1,k2,sigma = sp.symbols('k1 k2 sigma', real=True)
k = sp.Matrix([k1,k2]); e2 = sp.Matrix([0,1]); norm2 = k1*k1+k2*k2
m = sp.Matrix([k1*k2/norm2,-k1*k1/norm2])
exact('nonzero symbol transverse',k.dot(sigma*m),0)
exact('nonzero symbol squared norm',(sigma*m).dot(sigma*m),sigma*sigma*k1*k1/norm2)
exact('Darcy pressure symbol',-sp.I*k*(sigma*sp.I*k2/norm2)-sigma*e2,sigma*m)

r,u,rs,us,sru,constant = sp.symbols('r u rs us sru constant')
increments_product = sru-r*us-u*rs+r*u
product_of_increments = (rs-r)*(us-u)
exact('complete covariance increment expansion',increments_product-product_of_increments,sru-rs*us)
exact('zero mode cancels in flux',sru+constant*rs-rs*(us+constant),sru-rs*us)

chi,ct,rt,r = sp.symbols('chi chi_t rho_t rho')
gx,gy,rx,ry,ux,uy,ex,ey = sp.symbols('chi_x chi_y rho_x rho_y u_x u_y E_x E_y')
g=sp.Matrix([gx,gy]); dr=sp.Matrix([rx,ry]); U=sp.Matrix([ux,uy]); E=sp.Matrix([ex,ey])
F=rt+U.dot(dr)
q_t=ct*r+chi*rt; q_grad=r*g+chi*dr; v=chi*U+E
expanded_force=chi*F+r*ct+chi*(chi-1)*U.dot(dr)+chi*r*U.dot(g)+r*E.dot(g)+chi*E.dot(dr)
exact('complete cutoff residual',q_t+v.dot(q_grad),expanded_force)

theta,tt,tx,ty,wx,wy = sp.symbols('theta theta_t theta_x theta_y w_x w_y')
dtheta=sp.Matrix([tx,ty]); w=sp.Matrix([wx,wy])
G=tt+U.dot(dtheta)+w.dot(dr)
child_direct=ct*theta+chi*tt+U.dot(theta*g+chi*dtheta)+(chi*w+E).dot(dr)+(chi*w+E).dot(theta*g+chi*dtheta)
child_expected=chi*G+theta*(ct+U.dot(g))+E.dot(dr)+chi**2*w.dot(dtheta)+chi*E.dot(dtheta)+chi*theta*w.dot(g)+theta*E.dot(g)
exact('all localized child terms',child_direct,child_expected)

A,alpha,h,hp,x2 = sp.symbols('A alpha h hprime x2')
rate=A*k1*k1/norm2
rho_aff=A*x2+alpha*h; U_aff=alpha*m*h
grad_aff=A*e2+alpha*k*hp
grad_P=-A*x2*e2-alpha*k2/norm2*k*h
exact('affine full Darcy law',-grad_P-rho_aff*e2,U_aff)
exact('affine full transport',rate*alpha*h+U_aff.dot(grad_aff),0)
exact('affine self advection',U_aff.dot(alpha*k*hp),0)
F_aff=ct*rho_aff+chi*(chi-1)*U_aff.dot(grad_aff)+chi*rho_aff*U_aff.dot(g)+rho_aff*E.dot(g)+chi*E.dot(grad_aff)
F_explicit=ct*(A*x2+alpha*h)-chi*(chi-1)*(A*k1*k1/norm2)*alpha*h+chi*alpha*(A*x2+alpha*h)*h*m.dot(g)+(A*x2+alpha*h)*E.dot(g)+chi*E.dot(A*e2+alpha*k*hp)
exact('plane finite-energy force explicit substitution',F_aff,F_explicit)
exact('plane localized actual density equation',ct*rho_aff+chi*rate*alpha*h+(chi*U_aff+E).dot(rho_aff*g+chi*grad_aff),F_explicit)

# END UNCHANGED MATHEMATICAL BODY
finish('ipm_commutator', checks)
