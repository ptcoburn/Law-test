from phi_chi_x.control import simulate_single_agent, PHI

def test_phi_convergence():
    vals = simulate_single_agent(r0=2.2, chi=0.1, steps=40)
    assert abs(vals[-1] - PHI) < 0.005, "System did not converge to φ within tolerance"
