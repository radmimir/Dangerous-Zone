import pandas as pd
import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy

fig = pylab.figure()
axes = Axes3D(fig)
for i in 1,2:
    kills = pd.read_csv("C:\\kills"+str(i)+".csv")
    damage = pd.read_csv("C:\\damage_received"+str(i)+".csv")

    res = kills.merge(damage, how='inner', left_on='killer_recording_id', right_on='attacker_recording_id')
    k_coordinates = kills.merge(damage, how='inner', on='victim_recording_id').drop_duplicates(
        subset='victim_recording_id', keep='first')

    x_data = k_coordinates['victim_pos_x']
    y_data = k_coordinates['victim_pos_y']
    z_data = k_coordinates['victim_pos_z']

    x = x_data.as_matrix()
    y = y_data.as_matrix()
    z = z_data.as_matrix()
    plt.plot(x, y, z, 'o')

pylab.show()


