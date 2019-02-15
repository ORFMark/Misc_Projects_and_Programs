import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
f = [0.3484,0.1512,0.4924,0.0568,0.5464] #Force
fIdeal = []
t = [2.03,2.68,1.63,4.02,1.66] #period
oneOverTSqr = []
fUncertain = 0.0005 #uncertainty in the force
tUncertain = 0.25 #uncertainty in the period
oneOverTSqredUncertain = []

for i in range(0,len(t)): #generate individualized uncertainties in t
    oneOverTSqredUncertain.append(t[i] * (2*(tUncertain/t[i])**2)**(1/2))
    oneOverTSqr.append(1/(t[i]**2))
plt.figure()
#scatterplot
plt.errorbar(oneOverTSqr, f, yerr=oneOverTSqredUncertain , xerr=fUncertain, linestyle = '', label = "Observed Data")

#line of best fit
slope, intercept, r_value, p_value, std_err = sp.linregress(oneOverTSqr,f)
plt.plot(np.unique(oneOverTSqr), np.poly1d(np.polyfit(oneOverTSqr, f, 1))(np.unique(oneOverTSqr)),
         label = 'line of best fit, Slope: %.2f' % (float(slope)))

#idealized value
for i in range(0,len(f)):
    fIdeal.append((0.245 / (4 * 3.1415 * 0.20813)) * oneOverTSqr[i])
plt.plot(oneOverTSqr, fIdeal, label = 'Ideal Slope: %.2f' % (4 * 3.1415**2 * 0.20813 * .1500))

plt.title("Figure 3: Force as a function of 1 over T")
plt.ylabel("Centripedal Force: N")
plt.xlabel("1 over Period Squared (seconds)")
plt.legend();
plt.show()
