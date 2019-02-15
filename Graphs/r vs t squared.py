import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
r = [0.1819, 0.1400, 0.1751, 0.1456, 0.1769] #radius
rIdeal = []
t = [2.76, 2.14, 1.52, 2.13, 2.54] #period
tSqr = []
rUncertain = 0.0005 #uncertainty in the radius
tUncertain = 0.25 #uncertainty in the period
tSqredUncertain = []

for i in range(0,len(t)): #generate individualized uncertainties in t
    tSqredUncertain.append(t[i] * (2*(tUncertain/t[i])**2)**(1/2))
    tSqr.append(t[i]**2)
plt.figure()
#scatterplot
plt.errorbar(tSqr, r, yerr=tSqredUncertain , xerr=rUncertain, linestyle = '', label = "Observed Data")

#line of best fit
slope, intercept, r_value, p_value, std_err = sp.linregress(tSqr,r)
plt.plot(np.unique(tSqr), np.poly1d(np.polyfit(tSqr, r, 1))(np.unique(tSqr)),
         label = 'line of best fit, Slope: %.2f' % (float(slope)))

#idealized value
for i in range(0,len(r)):
    rIdeal.append((0.245 / (4 * 3.1415 * 0.20813)) * tSqr[i])
plt.plot(tSqr, rIdeal, label = 'Ideal Slope: %.2f' % (0.245 / (4 * 3.1415 * 0.20813)))

plt.title("Figure 2: R as a function of T Squared")
plt.ylabel("Radius (m)")
plt.xlabel("Period Squared (seconds)")
plt.legend();
plt.show()
