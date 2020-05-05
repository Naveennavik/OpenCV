import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate

centers = [(458, 508), (458, 509), (459, 507), (459, 509), (459, 510), (459, 510), (459, 510), (459, 510), (459, 510), (459, 510), (460, 511), (460, 511), (460, 512), (460, 512), (460, 513), (460, 514), (461, 513), (464, 539), (465, 546), (465, 555), (465, 565), (465, 573), (465, 605), (465, 654), (465, 701), (465, 719), (466, 583), (466, 595), (466, 629), (466, 643), (466, 671), (466, 687), (466, 761), (467, 617), (467, 743), (467, 785), (467, 810), (467, 901), (467, 993), (468, 837), (468, 868), (468, 938), (468, 991), (468, 992), (468, 992), (468, 992), (468, 992), (468, 992), (468, 993), (468, 993)]
print(len(centers))

x = np.array([xc[0] for xc in centers])
#x = np.reshape(a, newshape)
#print(x)
x = np.reshape(x,(-1,5))


y = np.array([xc[1] for xc in centers])
y = np.reshape(y,(-1,5))


plt.figure(figsize = (5.15,5.15))
plt.subplot(111)
for i in range(5):
    x_val = np.linspace(x[0, i], x[-1, i], 100)
    x_int = np.interp(x_val, x[:, i], y[:, i])
    tck = interpolate.splrep(x[:, i], y[:, i], k = 2, s = 4)
    y_int = interpolate.splev(x_val, tck, der = 0)
    plt.plot(x[:, i], y[:, i], linestyle = '--', marker = 'o')
    plt.plot(x_val, y_int, linestyle = ':', linewidth = 0.25, color =  'black')
plt.xlabel('X')
plt.ylabel('Y')
plt.show() 
