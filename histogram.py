import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
axes = Axes3D(fig)
for i in 1,2:
    kills = pd.read_csv("C:\\kills"+str(i)+".csv")
    damage = pd.read_csv("C:\\damage_received"+str(i)+".csv")

    res = kills.merge(damage, how='inner', left_on='killer_recording_id', right_on='attacker_recording_id')
    k_coordinates = kills.merge(damage, how='inner', on='victim_recording_id').drop_duplicates(subset='victim_recording_id', keep='first')

    x_data = k_coordinates['victim_pos_x']
    y_data = k_coordinates['victim_pos_y']
    z_data = k_coordinates['victim_pos_z']

    x = x_data.as_matrix()
    y = y_data.as_matrix()
    z = z_data.as_matrix()

    ax = fig.add_subplot(111, projection='3d')
    hist, xedges, yedges = np.histogram2d(x, y, bins=[37,22], range=[[0, 2], [0, 2]])


    # Construct arrays for the anchor positions of the 16 bars.
    # Note: np.meshgrid gives arrays in (ny, nx) so we use 'F' to flatten xpos,
    # ypos in column-major order. For numpy >= 1.7, we could instead call meshgrid
    # with indexing='ij'.
    xpos, ypos = np.meshgrid(xedges[:-1] + 1, yedges[:-1] + 1)
    xpos = xpos.flatten('F')
    ypos = ypos.flatten('F')
    zpos = np.zeros_like(xpos)

    # Construct arrays with the dimensions for the 16 bars.
    dx = 1
    dy = 1
    dz = hist.flatten()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
    plt.show()



