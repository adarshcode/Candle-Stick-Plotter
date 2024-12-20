# Candle-Stick-Plotter

A candle stick plotting application that can plot the candle sticks data from various Nifty Stocks.

I have created a class with a method to plot the data locally and also adjust the code according to the requirements.
Basically, you import the plotter class and instantiate it to use its plotting method. This method takes parameters such as Data File Path, Resistance Levels (list), Support Levels (list), Candle Stick Index (list), Cursor and Price Difference on Y-axis.

You can google these terms to know more except for the Candle Stick Index to mark all the candle sticks at those indexes and Cursor part which is a Boolean value for whether you want a cursor for your plot or not. You can see it in the video with yellow highlighted tooltip box.
It was a short project, and the plotter plots candle sticks for 1 day and 1 stock only. In future maybe I can scale this to support multiple stocks and multiple days. The challenging part here was to clean and process the data.

Libraries used: - Numpy, Pandas, Matplotlib, mpl_finance/mplfinance, mplcursors

#### [LinkedIn Post](https://www.linkedin.com/posts/adarsh-gupta-1086351a0_python-numpy-pandas-activity-7192920927469203457-08NA?utm_source=share&utm_medium=member_desktop)
