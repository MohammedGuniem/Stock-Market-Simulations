import yfinance as yf

"""
We can also use the yfinance package to access data on company investors.
"""
data = yf.Ticker("TSLA")

# Let's output the list of Tesla's major holders:
print("data.major_holders\n", data.major_holders, "\n")

# We can also get the list of the institutional holders:
print("data.institutional_holders\n", data.institutional_holders, "\n")

"""
These fields are actually DataFrames. 
This means that you can use all the DataFrame functions and filtering options on the data. 
For example, you can use .info() to see all the columns available in the DataFrame.
"""

print("Output only the institutional investors of Tesla that have more than 90M shares", "\n")
x = data.institutional_holders
print(x[x['Shares'] > 90000000], "\n")

print("The .recommendations field provides data on historic recommendations by investment banks.", "\n")
data = yf.Ticker("TSLA")
x = data.recommendations
print(x, "\n")

"""
Let's apply what we've learned: create a function that will take a ticker as its parameter, 
and output the ROE value for that ticker.
This will allow you to compare the ROE values of different companies:
"""
def RoE(ticker):
  data = yf.Ticker(ticker)
  roe = data.info['returnOnEquity']
  name = data.info['shortName']
  print(name, ":", roe)

RoE('AAPL')
RoE('MSFT')