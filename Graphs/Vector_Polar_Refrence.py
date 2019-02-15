import numpy as np #Imports numpy
import matplotlib.pyplot as plt #Imports the graphing library

#array of the force vectors along with an associated color for differentiation
vectors = [[0.0, .10462 * 9.81,'#345678'], [(90.1/360)*(2*3.14), .15441 * 9.81,'#338458'], [(235.6/360)*(2*3.14), .18657 * 9.81,'#582341']]



# Polar plotting
fig = plt.figure(figsize=(3, 3))  # Size
ax = plt.subplot(111, polar=True)  # Create subplot
plt.grid(color='#888888')  # Color the grid
ax.set_theta_zero_location('N')  # Set zero to North, or the top
plt.title("Figure 2: Plot of the Force Vectors on the Ring in Polar Coordinates")

for v in vectors:
    ax.plot((0, v[0]), ( 0, v[1]), c = v[2], zorder = 3) #graphs force vectors
    ax.scatter((0, v[0]), ( 0, v[1]), c=v[2], s=(3.14*0.001 * (((0.1/360)*(2*3.14)*v[1]/9.81)))) #adds uncertainty elipsies based on known uncertainty
fig.show()
