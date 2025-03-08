import gradio as gr
from make_plot import make_plot
from data_update import data_update

def grafik_lilin(display_name):
    # Convert display name to ticker symbol first
    stock = key2val_dropdown(display_name)
    data_update(stock)
    return make_plot(stock)

## define function to map keys to values
def key2val_dropdown(chosen):
    ## dict content
    isi_dropdown = ['Apple Inc. (AAPL)',
                    'JPMorgan Chase & Co. (JPM)',
                    'Johnson & Johnson (JNJ)',
                    'Caterpillar Inc. (CAT)',
                    'Alphabet Inc. (GOOGL)',
                    'The Home Depot, Inc. (HD)',
                    'Gold (GC=F)',
                    'Crude Oil (CL=F)',
                    'Natural Gas (NG=F)',
                    'Gasoline (RB=F)',
                    'Bitcoin (BTC-USD)',
                    'Ethereum (ETH-USD)',
                    'Ripple (XRP-USD)',
                    'Binance Coin (BNB-USD)']
    isi_tick = ['AAPL',
                'JPM',
                'JNJ',
                'CAT',
                'GOOGL',
                'HD',
                'GC=F',
                'CL=F',
                'NG=F',
                'RB=F',
                'BTC-USD',
                'ETH-USD',
                'XRP-USD',
                'BNB-USD']
    ini_dict = {isi_dropdown[i]: isi_tick[i] for i in range(len(isi_dropdown))}
    return ini_dict.get(chosen, '---')

with gr.Blocks() as demo:

    ##globals
    isi_dropdown = ['Apple Inc. (AAPL)',
                    'JPMorgan Chase & Co. (JPM)',
                    'Johnson & Johnson (JNJ)',
                    'Caterpillar Inc. (CAT)',
                    'Alphabet Inc. (GOOGL)',
                    'The Home Depot, Inc. (HD)',
                    'Gold (GC=F)',
                    'Crude Oil (CL=F)',
                    'Natural Gas (NG=F)',
                    'Gasoline (RB=F)',
                    'Bitcoin (BTC-USD)',
                    'Ethereum (ETH-USD)',
                    'Ripple (XRP-USD)',
                    'Binance Coin (BNB-USD)']

    gr.Markdown(
        """
        # mr-simple-candlestick
        Simple app to visualize (some) financial data
        """
    )
    symbol_choice = gr.Dropdown(isi_dropdown, label='Available Ticker')
    submit_button = gr.Button("Submit", variant='primary')
    plot_result = gr.Plot(label='candlestick-chart', format='png')
    gr.Markdown(
        """
        ## How it works
        1. Choose 1 of available tickers.
        2. Click Submit
        3. Wait for the chart to appear (especially the first chart). 
        4. Move cursor to the candle to see detailed info about OHLC and price direction.
        
        Data is taken from yahoo finance. Note that the displayed data might be delayed.
        """
    )

    # symbol_choice.change(fn=key2val_dropdown, inputs=symbol_choice, outputs=symbol_choice)
    submit_button.click(fn=grafik_lilin, inputs=symbol_choice, outputs=plot_result)

demo.launch()