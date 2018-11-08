import pandas as pd
import math
import numpy as np

kills = pd.read_csv("kills1.csv")
damage = pd.read_csv("damage_received1.csv")
data_map = {'server_coor':[-246400],'Corner0_y':[-266400],'Corner0_z':[-78840],'Corner1_x':[159990],'Corner1_y':[140000],'Corner1_z':[-78600],'Length':[574729.375],'Unnamed: 0':[0],'map_name':['Chora_Insurgency']}
map_coordinates =pd.DataFrame(data_map)
print(map_coordinates)
''' kills coordinates'''
res = kills.merge(damage,how='inner',  left_on='killer_recording_id',right_on='attacker_recording_id')
k_coordinates = kills.merge(damage, how='inner', on='victim_recording_id').drop_duplicates(subset='victim_recording_id',keep='first')

victim_pos_x=k_coordinates['victim_pos_x']
victim_pos_y=k_coordinates['victim_pos_y']
victim_pos_z=k_coordinates['victim_pos_z']
'''make matrix from columns'''
k_x = victim_pos_x.as_matrix()
k_y = victim_pos_y.as_matrix()
'''get coordinates'''
xmax = k_x.max()
xmin = k_x.min()
ymax = k_y.max()
ymin = k_y.min()
'''get intervals'''
n = 1+math.trunc(math.log2(len(k_x)))
'''step length'''
len_x=xmax-xmin
d_x=math.trunc(len_x/(8*n))
len_y=ymax-ymin
d_y=math.trunc(len_y/(8*n))
'''map length'''
len_map_x=map_coordinates['Corner1_x'][0]-map_coordinates['server_coor'][0]
len_map_y=map_coordinates['Corner1_y'][0]-map_coordinates['Corner0_y'][0]
'''amount of zones'''
n_x=math.ceil(len_map_x/d_x)
n_y=math.ceil(len_map_y/d_y)
'''array of coordinates left up corner of each zone'''
x_z=[map_coordinates['server_coor'][0]]
y_z=[map_coordinates['Corner0_y'][0]]
for i in range(1,n_x+1):
    x_z.append(x_z[i-1]+d_x)
for i in range(1,n_y+1):
    y_z.append(y_z[i-1]+d_y)
x_zone = np.array(x_z)
y_zone = np.array(y_z)
'''amount of kills in each zone'''
n_z=[]
for i in range (0,n_x+1):
    n_z.append([])
    for j in range(0, n_y+1):
        n_z[i].append(0)
n_zone = np.array(n_z)
dx=np.ones(10)
dy=np.ones(10)
for i in range(0,len(k_x)):
    xx= (k_x[i]-map_coordinates['server_coor'][0])/d_x
    x=math.trunc(xx)
    yy=(k_y[i]-map_coordinates['Corner0_y'][0])/d_y
    y=math.trunc(yy)
    n_zone[x][y]=n_zone[x][y]+1
'''this file help us to see the most dangerous zone'''
np.savetxt('text.txt',n_zone,fmt='%0.0f',delimiter=' ', newline='\r\n')

