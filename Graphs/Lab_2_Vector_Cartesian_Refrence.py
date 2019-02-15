import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
ells = [];
xUncertain = 0.0001
yUncertain = 0
vectors = [[0.0, .10462 * 9.81,'#345678']
           , [(90.1/360)*(2*3.14), .15441 * 9.81,'#338458']
           , [(235.6/360)*(2*3.14), .18657 * 9.81,'#582341']]
fig, ax = plt.subplots(subplot_kw = {'aspect': 'equal'})
for v in vectors:
    x = v[1] * np.cos(v[0])
    y = v[1]* np.sin(v[0])
    yUncertain = (0.1/(2*3.14) * (v[1]/9.81))
    ax.plot([0,x], [0, y], c = v[2])
    ells.append(Ellipse(xy=[x,y]
                , width=xUncertain, height=yUncertain
                , angle = 0));
for i in range(0, len(ells)):
    ax.add_artist(ells[i])
    ells[i].set_alpha(np.random.rand())
    ells[i].set_facecolor([0.2, 0.4, 0.4])
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
plt.title("Figure 3: Plot of the Vectors in the Cartesian plane")
plt.show();
