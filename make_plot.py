import plotly.graph_objects as go
import pandas as pd
from find_missing_dates import find_missing_dates
from symbol2name import *

def make_plot(stock, sma_val):
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
                    close = datanya['Close'],
                    name=stock)])
    ## [:-1] should be limit candles on "finished candle only"/"1 day delayed data" chart

    ## SMA computation belong here
    sma_period = int(sma_val)
    if sma_period >= 2 and sma_period <= 20:
        # print('apik')
        datanya['SMA'] = datanya['Close'].rolling(window=sma_period).mean()
        # print(datanya['SMA'])
        fig.add_trace(
        go.Scatter(
            x=datanya['Date'],  # Your x-axis data
            y=datanya['SMA'],  # Your y-axis data
            mode='lines',      # 'lines', 'markers', or 'lines+markers'
            name=f'SMA-{sma_period}',  # Legend entry
            line=dict(color='blue', width=1.5)  # Customize line appearance
        )
        )
    # else:
    #     print('tidak apik')

    fig.update_layout(xaxis_rangeslider_visible=False,
                      title = nama_stock+' ('+stock+')',
                      showlegend = True,
                      xaxis=dict(
                            rangebreaks=[dict(values=missing_dates)]  # Hide weekends
                                ),
                      legend=dict(
                      orientation="h",  # horizontal orientation
                      yanchor="top",
                      y=-0.2,          # position below the plot
                      xanchor="center",
                      x=0.5            # centered horizontally
                          )
                     )
    ##fig.show()
    return fig