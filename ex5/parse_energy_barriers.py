import numpy as np
import matplotlib.pyplot as plt


with open("log2.neb", "r") as f:
    lines=f.read()
    f.close()

data=lines.split()
timesteps = data[0] 
EBF = data[6]
RBF = data[7]
data = data[9:]
#print(data)
x=[]; y=[]
for i in range(0, len(data)-1,2):
    x.append(float(data[i]))
    y.append(float(data[i+1]))

print("timesteps = ", timesteps)

plt.figure()
plt.plot(x,y, 'b.')
plt.tight_layout()
plt.xlabel("Reaction Coordinate")
plt.ylabel("Energy (eV)")
plt.title(f"EBF = {EBF}, RBF = {RBF}")
plt.show()
plt.savefig("energy_barrier.png")


