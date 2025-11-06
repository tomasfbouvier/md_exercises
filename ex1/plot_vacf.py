import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def parse_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        ec_indices = [i for i, line in enumerate(lines) if line.strip().startswith("ec")] 
        header_line_index = ec_indices[0] - 1 
        header = ["ec"] + lines[header_line_index].split() 
        data_lines = [lines[i].split() for i in ec_indices[0:]] 
        df = pd.DataFrame(data_lines, columns=header) 
        df = df.apply(pd.to_numeric, errors="ignore")
    return df



df = parse_file("log_basic.txt")
df_filtered = df[df.index % 10 == 0]
print(df_filtered)

plt.figure()
plt.plot(df.iloc[:, 2], df.iloc[:, -1])


data = np.loadtxt("vacf")
plt.xlabel("Delta T")
plt.ylabel("<V(0)V(DeltaT)>")
plt.savefig("vacf")
