import os
import pandas as pd
import time
from pathlib import Path
import numpy as np







def correlation_matrix(stock_df_list:list[pd.DataFrame], tickers:list[str], lead_lag:int, window_size:int, offset:int, to_csv:bool =False):
    stock_closes_df = pd.DataFrame()
    for i in range(len(tickers)):
        stock_closes_df[tickers[i]] = stock_df_list[i]['daily_change']
    print("Dataframe of daily changes for each stock is created!")
    
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
    
    if to_csv:
        corr_matrix.to_csv(f"corr_matrix_{lead_lag}_{window_size}_{offset}.csv")
    return corr_matrix