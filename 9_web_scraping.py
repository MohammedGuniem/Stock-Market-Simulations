print(
    "For example, let's scrape the list of S&P 500 companies from Wikipedia.\n \
    The list is available on the Wikipedia article page as a table.\n \
    We simply need to call the read_html() function with the URL of the page as the parameter:\n "
)

print(
    "Each table on the web page is stored as the DataFrame at a separate index.\n \
    The first table has the index 0, the second table - the index 1, and so on.\n \
    Let's access and output the first table:\n "
)

import pandas as pd

data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = data[0]
print(df, "\n")

print("Let's select and output only the Symbol and Security columns: ")
print(df[df['Security'] == 'Apple Inc.'], "\n")

print("The info() function can be used to see all available columns: ", "\n")
print(df.info(), "\n")