## Read file with 2 parameters specific for Time Series 
#Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv("climate_change.csv",parse_dates["date"],index_col="date")


##Time Series plot (index as x axis)
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
ax.plot(climate_change.index, climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()

import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax= plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index,seventies["co2"])

# Show the figure
plt.show()