# Import data manipulation modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from winsorizer import winsorise_data


# Configure Pandas
pd.options.display.max_columns = 22

# Import logger from framework
from custom_logger.log_framework import log
# log.info('This is an info logger')
# log.error('This is an error logger')

# Read data from csv and pass it to a Pandas dataframe
house_data = pd.read_csv('data/nyc-rolling-sales.csv')

# Clean data:
# Reformat SALE DATE from object to datetime format
house_data['SALE DATE'] = house_data['SALE DATE'].astype('datetime64')

# Remove rows where house prices are missing, i.e. have ' -  ' rather than house price
house_data.loc[(house_data['SALE PRICE'] == ' -  '), 'SALE PRICE'] = 0
house_data['SALE PRICE'] = house_data['SALE PRICE'].astype('int')

# Plot time series plot of price vs. time
ax = sns.lineplot(x='SALE DATE', y='SALE PRICE', data=house_data)

# Create a new column to note days of the week
house_data['WEEKDAY'] = house_data['SALE DATE'].map(lambda x: x.weekday())

# Examine the data for different days of the week
week_avg = house_data.groupby(house_data['WEEKDAY']).mean()
week_count = house_data.groupby(house_data['WEEKDAY']).count()

# Plot distribution plot of house prices
house_data_win = winsorise_data(house_data)
sns.distplot(house_data_win['SALE PRICE'], bins=None, hist=True)