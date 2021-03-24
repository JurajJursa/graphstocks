import os
import pandas as pd
import numpy as np
import correlation_matrix.py as cm
from pathlib import Path

#CONFIG VALUES
DATA_SUBDIR = "stocks"      #name of the subdir within \data\
MIN_SIZE = 500              #Min size for # of days in a stock file
MAX_SIZE = 500              #Max size for # of days in a stock file
CORR_LAG = 1
CORR_SIZE = 200            #How many last days to look at
TEST_SIZE = 100

stock_files = os.listdir('data\\'+DATA_SUBDIR)
stock_files.sort()

russell_df = pd.read_excel("russell_2000.xlsx")
russell_tickers = list(russell_df["Ticker"].str.lower())
stock_df_list = []
tickers = []

#Creates list of dataframes for each ticker that there is data for in subdir within data\
#and is longer than MIN_SIZE
c = 0    
for i in range(len(russell_tickers)):
    name = russell_tickers[i]+".us.txt"
    
    if name in stock_files and Path("data\\stocks\\"+name).stat().st_size > 0:
        tmp = pd.read_csv("data\\stocks\\"+russell_tickers[i]+".us.txt", dtype={"Date":str, 
                                                                                "Open":np.float64,
                                                                                "Close":np.float64,
                                                                                "High":np.float64,
                                                                                "Low":np.float64,
                                                                                "Volume":np.float64,
                                                                                "OpenInt":np.float64
                                                                                }, parse_dates=['Date']
                                                                                ).tail(MAX_SIZE)

        tmp.reset_index(inplace=True)
        if tmp.shape[0] >= MIN_SIZE:
            stock_df_list.append(tmp)
            stock_df_list[c]['daily_change'] = stock_df_list[c]['Close'].pct_change(1)
            tickers.append(russell_tickers[i])
            c += 1
        
print("Reading in data done!")
print("Total # of stocks read in:", len(stock_df_list))

corr_matrix = cm.correlation_matrix(stock_df_list, tickers, lead_lag=1, window_size=30, offset=0)

