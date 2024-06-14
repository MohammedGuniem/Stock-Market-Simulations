import pandas as pd

prices = [42.8, 102.03, 240.38, 80.9]
s = pd.Series(prices)
print("Accessing the second element in array using s[1]: ", s[1], "\n")
print("Using the describe() function to see the key statistics: ", s.describe(), "\n")
print("Getting the standard deviation: ", s.describe()["std"], "\n")

print("Creating a DataFrame, which holds prices and their corresponding dates: ")
data = {
  'date': ['2021-06-10', '2021-06-11', '2021-06-12', '2021-06-13'],
  'prices': [42.8, 102.03, 240.38, 80.9]
}
df = pd.DataFrame(data)
print(df, "\n")