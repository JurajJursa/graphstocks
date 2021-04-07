import pandas as pd
import os
from datetime import datetime

def unpack_wrds(file:str, day_limit:datetime):
    df = pd.read_csv(file)
    #tickers = list(df['TICKER'].unique())
    tickers = [] 
    
    gb = df.groupby("TICKER")
    
    stock_df_list = [gb.get_group(x) for x in gb.groups if datetime.strptime(gb.get_group(x)['date'].iloc[0], "%d/%m/%Y") > day_limit]
    
    
    for df in stock_df_list:
        df.reset_index(inplace=True)
        tickers.append(df['TICKER'].iloc[0])
        df['PRC'] = df['PRC'].apply(abs)
        df['daily_change'] = df['PRC'].pct_change(1)

    return tickers, stock_df_list
    


    
