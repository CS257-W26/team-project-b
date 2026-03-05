'''Handles graphing through matplotlib library'''
import matplotlib.pyplot as plt
import numpy as np
# from ProductionCode.datasource import DataSource
# from ProductionCode.core import Features

# core = Features()
# data = DataSource()

# values = data.get_country_co2('Canada')
# values = core.csv_helper(values)
values = [['2000','3'],['2001','3'],['2002','4']]


xvalues = []
yvalues = []
for row in values:
    if row[1] != "":
        xvalues.append(float(row[1]))
        yvalues.append(float(row[0]))

xpoints = np.array(xvalues)
ypoints = np.array(yvalues)

plt.plot(xpoints, ypoints)
plt.show()
