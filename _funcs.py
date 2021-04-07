import os
import pandas as pd
import time
from pathlib import Path
import numpy as np

from typing import List



'''
This function takes in a list of tickers, which are strings, corresponding to the stock_df_list.
Stock_df_list is a list of dataframes, each one contains daily_change column, and all of them work with the
same date range.
'''

def correlation_matrix(stock_df_list:List[pd.DataFrame], tickers:List[str], lead_lag:int, window_size:int, offset:int):
    stock_closes_df = pd.DataFrame()
    for i in range(len(tickers)):
        stock_closes_df[tickers[i]] = stock_df_list[i]['daily_change']
    print("Dataframe of daily changes for each stock is created!")
    
    print(stock_closes_df.head())
    
    corr_a = stock_closes_df.iloc[offset:(offset+window_size)].copy()
    corr_b = stock_closes_df.iloc[(offset+lead_lag):(offset+window_size+lead_lag)].copy()
    corr_a.reset_index(inplace=True)
    corr_b.reset_index(inplace=True)
    corr_a.drop(columns=["index"], inplace=True)
    corr_b.drop(columns=["index"], inplace=True)
    
    corr_b.rename(columns=lambda x: x+"_lagged", inplace=True)
    temp = pd.merge(corr_a, corr_b, how='left', left_index=True, right_index=True)
        
    print("About to calculate corr matrix!")
    corr_matrix = temp.corr()
            
    l = len(tickers)
    corr_matrix = corr_matrix.iloc[0:l, l:]
    corr_matrix.rename(columns=lambda x: x[:-7], inplace=True)
    
    return corr_matrix