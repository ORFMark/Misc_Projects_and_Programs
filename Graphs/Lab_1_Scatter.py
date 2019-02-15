import matplotlib.pyplot as plt #import the library, any procedures with plt.* come form this lib
import numpy as np #imports numpy for standard deviation
trials = []
for i in range(1,31):
    trials.append(i) #sets up the X axis

#Y axis
data = [2.5105, 2.5100, 2.5103, 2.5091, 2.5101, 2.5101, 2.5103, 2.5098, 2.5098, 2.5100, 2.5090, 2.5099, 2.5101, 2.5091, 2.5100, 2.5099, 2.5089, 2.5097, 2.5099, 2.5099, 2.5099, 2.5096, 2.5099, 2.5121, 2.5094, 2.5102, 2.5090, 2.5101, 2.5089, 2.5100]

#plots the scatter with errorbars
plt.errorbar(trials, data, yerr = 0.0005, marker = '+', linestyle = '', label = "Data")

#axis labels/title
plt.xlabel("Trial Number")
plt.ylabel("Diameter of the Sphere(cm)")
plt.title("Fig. 5: Diameter of a Steel Sphere with Mean and Standard Deviation")

#mean
plt.plot([0]+trials, [2.5099]*31, c = 'red', marker = '', label = 'Mean')

#std dev
print(np.std(data))
plt.plot([0]+trials, [2.5099+np.std(data)]*31, c = 'green', marker = '', label = 'Standard Deviation')
plt.plot([0]+trials, [2.5099-np.std(data)]*31, c = 'green', marker = '')

plt.legend()#generates the legend
plt.show()#displays the plot
