import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.style.use('/home/fernbouv/Desktop/mystyle.mplstyle')

# === Read the file ===
with open("log2.neb", "r") as f:
    lines = f.read()

# Parse the data
data = lines.split()
timesteps = data[0]
EBF = data[6]
RBF = data[7]
data = data[9:]  # Skip headers

# Extract x and y data
x = []
y = []
for i in range(0, len(data) - 1, 2):
    x.append(float(data[i]))
    y.append(float(data[i + 1]))

data = np.array([x,y])
np.savetxt("barrier.txt", data.T)


# Convert to numpy arrays
x = np.array(x)
y = np.array(y)

# Shift energy values to set the minimum energy as zero
y_min = y.min()
y -= y_min

print("timesteps =", timesteps)

# === Spline interpolation ===
# Sort x (just in case)
sorted_indices = np.argsort(x)
x = x[sorted_indices]
y = y[sorted_indices]

# Generate smooth curve using cubic spline
x_smooth = np.linspace(x.min(), x.max(), 300)
spline = make_interp_spline(x, y, k=3, bc_type = "clamped")
y_smooth = spline(x_smooth)

# === Plotting ===
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'b.', markersize=12, label='NEB Images')
plt.plot(x_smooth, y_smooth, 'b-', label='Cubic Spline', linewidth=2)



plt.xlabel("Reaction Coordinate", fontsize=15)
plt.ylabel("Energy (eV)", fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.legend(fontsize=15)
plt.tight_layout()

# Save and show plot
plt.savefig("energy_barrier.png", format="png", dpi=300)
plt.show()


