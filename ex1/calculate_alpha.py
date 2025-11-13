import glob
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('/home/fernbouv/Desktop/mystyle.mplstyle')
def box_length(file):
    with open(file) as f:
        for line in f:
            if line.strip().endswith("xlo xhi"):
                xlo, xhi, _, _ = line.split()
                return float(xhi) - float(xlo)

# Load data
temps = []
lengths = []

for file in glob.glob("cell.data_*"):
    temp = float(file.split("_")[-1])
    temps.append(temp)
    lengths.append(box_length(file))

# Sort by temperature
temps, lengths = zip(*sorted(zip(temps, lengths)))

# Compute deltas w.r.t 300 K
L300 = lengths[temps.index(300)]
delta_T = np.array(temps) - 300
delta_L = (np.array(lengths) - L300)/L300

# Linear fit
slope, intercept = np.polyfit(delta_T, delta_L, 1)

plt.figure(figsize=(8,4))
# Plot
plt.plot(delta_T, delta_L, "o")
plt.plot(delta_T, slope*delta_T + intercept, "-")
plt.xlabel("ΔT (K)")
plt.ylabel("ΔL/L (Å)")
plt.title(f"Coefficient of Thermal expansion α = {slope:.2g} K⁻¹")
plt.savefig("expansion_coefficient")
plt.show()


