import plotly.graph_objects as go
import pandas as pd
from find_missing_dates import find_missing_dates
from symbol2name import *

def make_plot(stock):
    ##stock = 'MSFT'
    ## import csv first
    datanya = pd.read_csv('data/'+stock+'.csv')
    ##print(datanya)

    ##dat = yf.Ticker(stock)
    ##bagian ini untuk print info sederhana
    ##for key, value in dat.info.items():
    ##    print(f'{key}: {value}')
    existing_symbol = load_symbol_data('data/tickername.csv')
    nama_stock = get_symbol_name(stock, existing_symbol)

    ## find missing dates
    missing_dates = find_missing_dates(datanya['Date'])

    ## define fig
    fig = go.Figure(data=[go.Candlestick(x=datanya['Date'],
                    open = datanya['Open'],
                    high = datanya['High'],
                    low = datanya['Low'],
                    close = datanya['Close'])])
    ## [:-1] should be limit candles on "finished candle only"/"1 day delayed data" chart 

    fig.update_layout(xaxis_rangeslider_visible=False,
                    title = nama_stock+' ('+stock+')',
                    xaxis=dict(
                            rangebreaks=[dict(values=missing_dates)]  # Hide weekends
                                ))
    ##fig.show()
    return fig