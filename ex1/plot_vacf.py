import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("vacf")
plt.plot(data[:,0], data[:,1], "o-")
plt.xlabel("Delta T")
plt.ylabel("<V(0)V(DeltaT)>")
plt.show()
