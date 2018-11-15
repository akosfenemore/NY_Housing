# Import data manipulation modules
import pandas as pd
import numpy as np

# Import logger from framework
from custom_logger.log_framework import log

log.info('This is an info logger')
log.error('This is an error logger')

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

ax = sns.lineplot(x=week_avg.index, y=week_avg['SALE PRICE'])

bx = sns.barplot(x=week_avg.index, y=week_avg['SALE PRICE'])


new_house_data = house_data[house_data['SALE PRICE'] > 0]

new_house_data_win = winsorise_data(new_house_data)
sns.distplot(new_house_data_win['SALE PRICE'], bins=None, hist=True)

new_week_avg = new_house_data.groupby(new_house_data['WEEKDAY']).mean()
new_week_count = new_house_data.groupby(new_house_data['WEEKDAY']).count()


bx = sns.barplot(x=new_week_avg.index, y=new_week_avg['SALE PRICE'])



sns.distplot(new_house_data_win['SALE PRICE'], bins=None, hist=True)

new_week_avg = new_house_data.groupby(new_house_data['BOROUGH']).mean()
new_week_count = new_house_data.groupby(new_house_data['BOROUGH']).count()


bx = sns.barplot(x=new_week_avg.index, y=new_week_avg['SALE PRICE'])

corr = new_house_data.corr()

corr

sns.heatmap(corr)

house_data['MONTH SOLD']=house_data['SALE DATE'].map(lambda x: x.month)

sns.countplot(x='MONTH SOLD', data=house_data, palette='rainbow')
plt.title('Sales Rate from 2016-2017')