import yfinance as yf

print("The Ticker module allows us to access company data based on their market ticker symbol: ")
data = yf.Ticker("TSLA")
print("Now, we can access the company information under the corresponding fields: ")
print(data.info, "\n")
print("Let's output the profit margins and RoE: ")
print("data.info['profitMargins'] = ", data.info['profitMargins'], "\n")
print("data.info['returnOnEquity'] = ", data.info['returnOnEquity'], "\n")

print("In addition to the info fields, the data object provides the following fields: ", "\n")
# show dividends
print("data.dividends\n", data.dividends, "\n")
# show splits
print("data.splits\n", data.splits, "\n")
# show balance sheet
print("data.balance_sheet\n", data.balance_sheet, "\n")
# show cashflow
print("data.cashflow\n", data.cashflow, "\n")
# show earnings
print("data.cashflow\n", data.earnings_dates, "\n")

print("plot the cash flow table as bar charts\n")
x = data.earnings_dates
import matplotlib.pyplot as plt
x.plot(kind="bar")
plt.savefig("11_plots/plot_1.png")