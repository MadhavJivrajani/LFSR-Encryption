import lfsr
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

rnglol = lfsr.LFSR(14, "fib", [0,0,0,0,0,0,0,0,0,0,1,1,1,1])
a = rnglol.generate_output_stream()
a = a.tolist()
a.append(0)
print(len(a))
print(a.count(1))
print(a.count(0))
plt.imsave('filename.png', np.array(a).reshape(128,128), cmap=cm.gray)
