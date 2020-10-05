import numpy as np

r = 1   # This represents the radius of the helix
theta = np.linspace(0, 10 * np.pi, 1000)    # Using the Numpy module and setting the parameters

# Setting the arrays x, y, z
x = r * np.cos(theta)
y = r * np.sin(theta)
z = theta

import matplotlib.pyplot as plt # Necessary module for python plotting
import mpl_toolkits.mplot3d as Axes3D   # This module is useful for displaying the helix in a 3D graph

#
fig = plt.figure('parametric curves')
axis = fig.add_subplot(111, projection='3d')

axis.plot(x, y, z, '-r', linewidth=3)

axis.set_xlabel('X', fontweight='bold', fontsize = 16)
axis.set_ylabel('Y', fontweight='bold', fontsize = 16)
axis.set_zlabel('Z', fontweight='bold', fontsize = 16)

plt.title('Parametric Curve', fontweight='bold', fontsize=18)

plt.show()