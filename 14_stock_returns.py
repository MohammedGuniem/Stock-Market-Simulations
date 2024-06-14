import yfinance as yf
import matplotlib.pyplot as plt

print("We will start by calculating the daily returns of a stock.", "\n\n")

print("Let's get the stock prices for Tesla over the past year:")
data = yf.Ticker('TSLA')
price = data.history(period='10y')
print(price)

print("In order to calculate the daily returns, we will use the pct_change() function,")
print("which calculates the percentage change between the current element and a prior one.")
print("We will use it on the 'Close' column:")
pct_change = price['Close'].pct_change()
print(pct_change)

print("To visualize the results, we can create a plot for the daily returns:")
print("See /14_plots/plot_1.png")
pct_change.plot()
plt.savefig('14_plots/plot_1.png')
plt.clf()

print("We can also make a histogram to see the distribution:")
print("See /14_plots/plot_2.png")
pct_change.plot(kind="hist")
plt.savefig('14_plots/plot_2.png')
plt.clf()

print("After understanding how the returns are distributed, we can calculate the returns from an investment.")
print("For that, we need to calculate the cumulative returns, which can be done using the cumprod() function:")
returns = (pct_change + 1).cumprod()
print(returns)
print("Here is the plot:")
print("The plot shows how a $1 investment would grow.")
print("See /14_plots/plot_3.png")
returns.plot()
plt.savefig('14_plots/plot_3.png')
plt.clf()