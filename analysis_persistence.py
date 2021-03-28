import os
import pandas as pd
import numpy as np
import datetime
from pathlib import Path


import _funcs.py as cm
import _data_processing.py as dp

tickers, stock_df_list = dp.unpack_wrds('data/wrds_russell.csv', datetime.datetime(year=2017, month=12, day=31))



corr_matrix = cm.correlation_matrix(stock_df_list, tickers, lead_lag=1, window_size=15, offset=0)





