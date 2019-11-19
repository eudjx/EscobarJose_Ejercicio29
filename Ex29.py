import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(15,10))
data = np.loadtxt("Ex29.dat")
plt.plot(np.linspace(0, len(data), len(data)), data)
plt.title("Diffusive equation")
plt.xlabel("t")
plt.ylabel("Diffusion")
plt.savefig("diff.png")
plt.show()
