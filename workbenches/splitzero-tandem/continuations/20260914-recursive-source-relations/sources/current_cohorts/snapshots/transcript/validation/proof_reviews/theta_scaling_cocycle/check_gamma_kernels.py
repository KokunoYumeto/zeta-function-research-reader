"""Numerical independent sign/constant checks; the analytic proof is in the note."""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 60
WORK = Path(__file__).resolve().parent

def phi(x):
    return (4*mp.pi**2*x**4-6*mp.pi*x**2)*mp.exp(-mp.pi*x**2)

def gamma_kernel(rho, t, x, quartic_coefficient=2):
    low = mp.pi*x*x*mp.exp(-2*t)
    high = mp.pi*x*x
    return (mp.exp(t*rho)*x**(-rho)*mp.pi**(-rho/2) *
            (quartic_coefficient*mp.gammainc(rho/2+2,low,high)
             -3*mp.gammainc(rho/2+1,low,high)))

rows = []
for rho in (mp.mpc('0.3','2.1'), mp.mpc('0.5','14.134725'), mp.mpc('0.7','-3')):
    for t in (mp.mpf('-0.8'),mp.mpf('0'),mp.mpf('0.65')):
        for x in (mp.mpf('0.3'),mp.mpf('1.2')):
            for j in range(3):
                direct = mp.quad(lambda r: mp.exp(r*rho)*r**j/mp.factorial(j)*phi(x*mp.exp(r-t)), [0,t])
                closed = mp.diff(lambda w: gamma_kernel(w,t,x),rho,j)/mp.factorial(j)
                error = abs(direct-closed)/max(1,abs(direct))
                if error > mp.mpf('1e-45'):
                    raise RuntimeError(f'Kernel mismatch: {rho=} {t=} {x=} {j=} {error=}')
                rows.append({'rho':str(rho),'t':str(t),'x':str(x),'j':j,'scaled_error':str(error)})

# Deliberate controls detect a lost Gaussian coefficient and a reversed orientation.
rho,t,x = mp.mpc('0.3','2.1'),mp.mpf('-0.8'),mp.mpf('0.3')
direct = mp.quad(lambda r: mp.exp(r*rho)*phi(x*mp.exp(r-t)), [0,t])
mutations = {
    'lost_quartic_factor_two':gamma_kernel(rho,t,x,quartic_coefficient=1),
    'negative_time_orientation_reversed':-gamma_kernel(rho,t,x),
}
mutation_errors = {}
for name,bad in mutations.items():
    error = abs(direct-bad)
    if error <= mp.mpf('1e-20'):
        raise RuntimeError('Mutation control failed to detect ' + name)
    mutation_errors[name] = str(error)

record = {'status':'pass','precision_decimal_digits':mp.mp.dps,'case_count':len(rows),
          'max_scaled_error':str(max(mp.mpf(row['scaled_error']) for row in rows)),
          'cases':rows,'mutation_controls_detected':mutation_errors,
          'scope':'Checks original Gaussian source kernels, full parameter derivatives j=0,1,2, and negative-time orientation. Parameter samples are not certified arithmetic zeros. Analytic proof supplies all orders and all times.'}
(WORK/'gamma_kernel_checks.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in record.items() if key!='cases'},indent=2))
