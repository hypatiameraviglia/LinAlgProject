#Reads data as .csv and sorts temperature, humuidity, and visibility by magnitude.

import numpy as np

#TODO check delimiter and skiprows
weather1970 = np.loadtxt('1970data.csv', delimiter=" ", skiprows=1)


