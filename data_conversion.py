import scipy.io as sio
import numpy as np

WB = np.array(sio.loadmat('sandstone_data.mat')['Data'])
WB = WB.astype('int8')
# Y_data = np.array(sio.loadmat('sandstone_data.mat')['L'])

np.savetxt('sandstone_structure_data.csv', WB, delimiter=',', fmt='%d')
