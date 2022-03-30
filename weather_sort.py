#Reads data as .csv and sorts temperature, visibility, and weather indicator by magnitude.

import numpy as np
import pandas as pd

column_subset = [
        "DATE",
        "TEMP",
        "VISIB",
        "FRSHTT"
]

#TODO check rows
weather1970 = pd.read_csv('1970data.csv', usecols=column_subset, nrows=100)
weather1980 = np.loadtxt('1980data.csv', usecols=column_subset, nrows=100)
weather1990 = np.loadtxt('1990data.csv', usecols=column_subset, nrows=100)
weather2000 = np.loadtxt('2000data.csv', usecols=column_subset, nrows=100)
weather2010 = np.loadtxt('2010data.csv', usecols=column_subset, nrows=100)
weather2020 = np.loadtxt('2020data.csv', usecols=column_subset, nrows=100)

#Makes sure we got data
print(weather1970.head())


