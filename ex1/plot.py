import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import glob
import os



plt.style.use('/home/fernbouv/Desktop/mystyle.mplstyle')


N_values = [2,3,4,5,6, 8]
dt_values = [0.0001, 0.0005, 0.001, 0.003, 0.01]
tau_T_values = [1.0,0.1,0.01]


def parse_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        ec_indices = [i for i, line in enumerate(lines) if line.strip().startswith("ec")] 
        header_line_index = ec_indices[0] - 1 
        header = ["ec"] + lines[header_line_index].split() 
        data_lines = [lines[i].split() for i in ec_indices[1:]] 
        df = pd.DataFrame(data_lines, columns=header) 
        df = df.apply(pd.to_numeric, errors="ignore")
    return df


fig, axes = plt.subplots(3, 1, figsize=(12, 10))
plt.subplots_adjust(hspace=0.35)

# ---------------------------------------------------------
# 1️⃣ Pressure vs Time for varying N
# ---------------------------------------------------------
ax = axes[0]
for N in N_values:
    file_name = f"log_lammps_{N}_0.001_0.1"  # keep dt and tau_T constant
    if os.path.exists(file_name):
        df = parse_file(file_name)

        ax.plot(df["Time"], df["Press"], label=f"N={N}")
    else:
        print(f"⚠️ Missing file: {file_name}")
ax.set_title("Pressure vs Time varying N")
ax.set_xlabel("Time")
ax.set_ylabel("Pressure")
ax.legend(ncols=2)

# ---------------------------------------------------------
# 2️⃣ Total Energy vs Time for varying dt
# ---------------------------------------------------------
ax = axes[1]
for dt in dt_values:
    file_name = f"log_lammps_2_{dt}_0.1"  # keep N and tau_T constant
    if os.path.exists(file_name):
        df = parse_file(file_name)
        total_energy = df["KinEng"] + df["PotEng"]
        ax.plot(df["Time"], total_energy, label=f"dt={dt}")
    else:
        print(f"⚠️ Missing file: {file_name}")
ax.set_title("Energy Conservation for varying dt")
ax.set_xlabel("Time")
ax.set_ylabel("Total Energy")
ax.legend()

# ---------------------------------------------------------
# 3️⃣ Temperature vs Time for varying tau_T
# ---------------------------------------------------------
ax = axes[2]
for tau_T in tau_T_values:
    file_name = f"log_lammps_2_0.001_{tau_T}"  # keep N and dt constant
    if os.path.exists(file_name):
        df = parse_file(file_name)
        ax.plot(df["Time"], df["Temp"], label=f"tau_T={tau_T}")
    else:
        print(f"⚠️ Missing file: {file_name}")
ax.set_title("Temperature vs Time varying tau_T")
ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend()

# ---------------------------------------------------------
plt.tight_layout()
plt.savefig("parameter_test.png")
plt.show()
