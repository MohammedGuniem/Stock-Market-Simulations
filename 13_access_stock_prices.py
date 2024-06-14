import yfinance as yf
import matplotlib.pyplot as plt

print("yfinance also provides the stock prices of the given ticker.", "\n")

data = yf.Ticker('TSLA')
print("This will output the stock prices for the last month.")
print(data.history(), "\n")

print("We can provide a period parameter:")
print(data.history(period='5d'))

print("Valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.", "\n")

print("We can also provide custom start and end dates:")
print(data.history(start='2021-01-01', end='2021-06-30'), "\n")

print("Let's plot the daily Close price of Tesla stock for the last month:", "\n")
data = yf.Ticker('TSLA')
x = data.history()['Close']
x.plot()
plt.savefig("13_plots/plot_1.png")

print("Output the average Close price of Tesla stock for the last 3 months.")
data = yf.Ticker('TSLA')
x = data.history('3mo')['Close']
print(x.mean(), "\n")

print("In addition, yfinance allows you to download historical prices for more than one stock simultaneously.", "\n")

print("For example, let's take the stock prices of Apple, Microsoft and Tesla with one line:")
data = yf.download("AAPL MSFT TSLA", start='2021-01-01')
print(data['Close'], "\n")

print("Now we can plot the stock prices of all the 3 tickers:")
print("See /13_plots/plot_2.png")
data['Close'].plot()
plt.savefig('13_plots/plot_2.png')