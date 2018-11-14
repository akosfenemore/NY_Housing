# Import data manipulation modules
import pandas as pd
import numpy as np

# Import logger from framework
from custom_logger.log_framework import log

log.info('This is an info logger')
log.error('This is an error logger')

# Read data from csv and pass it to a Pandas dataframe
house_data = pd.read_csv('data/nyc-rolling-sales.csv')

