# phi_chi_x_law/control.py
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
PSI = 1 / PHI

def phi_chi_x_update(r_t, r_prev=None, chi=0.1, X_prev=0.0, dt=1.0):
    if r_prev is None:
        r_prev = r_t
    kappa_t = r_t - r_prev
    r_next = r_t + PSI * (PHI - r_t) + chi * kappa_t
    X_next = X_prev + chi * dt
    return r_next, X_next

def simulate_single_agent(r0=0.5, chi=0.1, steps=30):
    r_vals = [r0]
    X = 0.0
    for t in range(1, steps):
        r_next, X = phi_chi_x_update(r_vals[-1], r_vals[-2] if t > 1 else r_vals[-1], chi, X)
        r_vals.append(r_next)
    return np.array(r_vals)

def variance_decay(agents, chi=0.1, psi=PSI, lam=0.1, steps=30):
    agents = np.array(agents, dtype=float)
    history = [agents.copy()]
    for _ in range(steps):
        mean_val = agents.mean()
        kappa = np.diff(np.concatenate([[agents[0]], agents]))
        agents += psi * (PHI - agents) + lam * (mean_val - agents) + chi * kappa
        history.append(agents.copy())
    return np.array(history)

