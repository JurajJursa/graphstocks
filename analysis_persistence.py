import os
import pandas as pd
import numpy as np
import datetime
from pathlib import Path


import _funcs as func
import _data_processing as dp

tickers, stock_df_list = dp.unpack_wrds('data/wrds_russell.csv', datetime.datetime(year=2017, month=12, day=31))

print(stock_df_list[0].head())

for i in range(30):
    corr_matrix = func.correlation_matrix(stock_df_list, tickers, lead_lag=1, window_size=15, offset=i+1)
    #sparse_matrix = corr_matrix.mask(abs(corr_matrix) < 0.1, 0)
    corr_matrix.to_csv(f'data/daily_persistence/corr_matrix_{i}.csv')
    
for i in range(30):
    corr_matrix = func.correlation_matrix(stock_df_list, tickers, lead_lag=1, window_size=15, offset=i*30+1)
    #sparse_matrix = corr_matrix.mask(abs(corr_matrix) < 0.1, 0)
    corr_matrix.to_csv(f'data/monthly_persistence/corr_matrix_{i}.csv')
    



