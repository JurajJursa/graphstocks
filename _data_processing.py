import pandas as pd
import os
import datetime

def unpack_wrds(file:str, day_limit:datetime.datetime):
    df = pd.read_csv(file)
    tickers = list(df['TICKER'].unique())
        
    gb = df.groupby("TICKER")
    
    stock_df_list = [gb.get_group(x) for x in gb.groups if datetime.strptime(gb.get_group(x).head()['date'], "%d/%m/%Y") > day_limit]

    return tickers, stock_df_list
    


    
