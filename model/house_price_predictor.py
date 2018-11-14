# Import data manipulation modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
house_data = house_data[house_data['SALE PRICE'] != ' -  ']

#
house_data.head()

sns.tsplot(house_data['SALE DATE'].astype('datetime64[ns]'), house_data['SALE PRICE'].astype('float64'))

ax = sns.lineplot(x='SALE DATE', y='SALE PRICE', data=house_data)

sns.scatterplot(house_data['SALE DATE'].astype('datetime64[ns]'), house_data['SALE PRICE'].astype('float64'))

plt.scatter(house_data['SALE DATE'].astype('datetime64[ns]'), house_data['SALE PRICE'].astype('float64'))

house_data.dtypes

# pd.plotting.scatter_matrix(house_data, figsize=(6, 6))
pd.plotting.scatter_matrix(house_data, figsize=(12, 12))
plt.savefig('scatter.png')
