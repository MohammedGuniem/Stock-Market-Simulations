print("We can scrape Tesla's profile page on yahoo finance: ", "\n")
import pandas as pd
import requests

url_link = 'https://finance.yahoo.com/quote/TSLA/profile'
r = requests.get(
    url_link,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/91.0.4472.124 Safari/537.36'}
)

data = pd.read_html(r.text)
print(data[0], "\n")

print(
    "Now, we can access other financial metrics.\n \
    For example, let's scrape the Earnings Estimates from the Analysis page:\n "
)
url_link = 'https://finance.yahoo.com/quote/TSLA/analysis?p=TSLA'
r = requests.get(
    url_link,
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/91.0.4472.124 Safari/537.36'}
)
data = pd.read_html(r.text)
df = data[0]
print(df, "\n")

print("Now we can access the Avg. Estimate row from the table and plot it as a bar chart:\n")
import matplotlib.pyplot as plt

AvgEstimate = df[df["CURRENCY IN USD"] == "Avg. Estimate"]

# Select the first row of the filtered DataFrame (assuming you want to plot the first match)
row_to_plot = AvgEstimate.iloc[0]

# Drop the 'Company Name' column for the plot
data_to_plot = row_to_plot.drop('CURRENCY IN USD')

data_to_plot.plot(kind='bar', title=f'Avg. Estimate', ylabel='Values')
plt.savefig('8_plots/plot_1.png')
print(AvgEstimate, "\n")
