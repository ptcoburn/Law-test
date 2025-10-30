from phi_chi_x.control import simulate_single_agent, PHI
import matplotlib.pyplot as plt

r_vals = simulate_single_agent(r0=2.2, chi=0.1, steps=40)
plt.plot(r_vals, label="Active φ–χ control")
plt.axhline(PHI, color="gray", linestyle="--", label="φ ≈ 1.618")
plt.xlabel("Iteration")
plt.ylabel("r")
plt.legend()
plt.title("Convergence to φ under Active φ–χ Regulation")
plt.show()
