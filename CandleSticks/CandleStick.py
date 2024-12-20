# Copyright (c) 2024 adarshcode
# This script is released under the MIT License.

import pandas as pd
import numpy as np 

from mpl_finance import candlestick_ohlc 
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
import mplcursors 


class CandleStickPlotter:

    def __init__(self):
        pass

    def __processAndCleanData(self, df):
        
        # df['open'] = df['open'].astype(str)
        # non_numeric_values = df[~df['open'].str.match(r'^-?\d+\.?\d*$')]['open'].unique()
        # print("Non-numeric values:", non_numeric_values)

        # df['open'] = pd.to_numeric(df['open'], errors='coerce')
        # # Drop rows with NaN values in the 'open' column
        # df = df.dropna(subset=['open'])

        df['open'] = pd.to_numeric(df['open'], errors='coerce')
        df['close'] = pd.to_numeric(df['close'], errors='coerce')
        df['high'] = pd.to_numeric(df['high'], errors='coerce')
        df['low'] = pd.to_numeric(df['low'], errors='coerce')
        df['volume'] = pd.to_numeric(df['volume'], errors='coerce')

        return df
    
    # def __getCandleStickData(self, path):
    #     data = pd.read_csv(path)
    #     return data
    
    def plotCandleSticks(self, filePath, resistanceLevels=[], supportLevels=[], candleIndex=[], cursor=False, priceDifference=2.5):
        df = pd.read_csv(filePath) #self.__getCandleStickData(filePath)
        processedDF = self.__processAndCleanData(df)
        self.__generatePlot(processedDF, resistanceLevels, supportLevels, candleIndex, cursor, priceDifference)
    
    def __customize_cursor(self, ax):
        # Create the cursor object with hover enabled
        cursor = mplcursors.cursor(ax, hover=True)

        # Define the callback function to handle the annotation
        def on_hover(sel):
            # Display the annotation based on the y-coordinate only
            sel.annotation.set_text(f"Y: {sel.target[1]:.2f}")
            # Set the annotation position (choose one from "E", "W", "N", "S")
            # "E" for East (right side), "W" for West (left side),
            # "N" for North (above), and "S" for South (below)
            #sel.annotation.set(position="E")  # Change "E" as needed

        # Connect the callback function to the cursor's "add" event
        cursor.connect("add", on_hover)
        return cursor
    
    def __generatePlot(self, df, resistanceLevels, supportLevels, candleIndex, cursor, priceDifference):
        ohlc = df.loc[:, ['date', 'open', 'high', 'low', 'close']] 
        ohlc['date'] = pd.to_datetime(ohlc['date']) 
        ohlc['date'] = ohlc['date'].apply(mpl_dates.date2num) 
        ohlc = ohlc.astype(float) 

        # Creating Subplots 
        fig, ax = plt.subplots(figsize=(12, 6))  # Increase figure width

        candle_width = np.diff(ohlc['date']).min() * 0.9  # Adjust the factor as needed

        candlestick_ohlc(ax, ohlc.values, width=candle_width,  # Adjust candle width
                        colorup='green', colordown='red', alpha=0.8) 
    
        # Setting labels & titles 
        # Setting labels & titles using plt
        plt.xlabel('Date') 
        plt.ylabel('Price') 

        #plt.gca().xaxis.set_major_locator(mpl_dates.MinuteLocator(interval=5))  

        date_format = mpl_dates.DateFormatter('%d-%m-%Y') 
        plt.gca().xaxis.set_major_formatter(date_format) 

        fig.autofmt_xdate() 

        plt.gca().yaxis.set_major_locator(MultipleLocator(priceDifference))
        #fig.tight_layout() 

        #print(len(ohlc))

        if(candleIndex):
            for index in candleIndex:
                highlight_candle = ohlc.iloc[index]
                plt.plot(highlight_candle.iloc[0], (highlight_candle.iloc[1] + highlight_candle.iloc[4])/2, 
                        marker='o', markersize=5, color='blue', label='Highlighted Candle')

        # Draw horizontal lines
        if(resistanceLevels):
            for line in resistanceLevels:
                plt.axhline(y=line, color='red', linestyle='--', linewidth=0.75)

        if(supportLevels):
            for line in supportLevels:
                plt.axhline(y=line, color='green', linestyle='--', linewidth=0.75)

        if(cursor):
            self.__customize_cursor(ax)
            
            
        plt.show() 