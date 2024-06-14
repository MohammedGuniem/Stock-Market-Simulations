import numpy_financial as npf

"""
Let's assume we invested 5000 and got the following payments back: 500, 700, 1000, 3000.
"""
cashflow = [-5000, 500, 700, 1000, 3000]
print(npf.irr(cashflow))  # results = 0.012164656866492818

"""
Let's use the irr() function to compare two investment opportunities and decide which one is better.
Option 1:

Requires 50K in investment
Will pay 10K, 25K, 25K, 35K, 42K each year for the next 5 years.
Option 2:

Requires 30K in investment
Will pay 10K, 13K, 18K, 25K, 20K each year for the next 5 years.

Let's calculate the IRR for each investment and compare:
"""
cf1 = [-50000, 10000, 25000, 25000, 35000, 42000]
cf2 = [-30000, 10000, 13000, 18000, 25000, 20000]

print("Option 1: ", npf.irr(cf1))  # results = 0.3605982754620045
print("Option 2: ", npf.irr(cf2))  # results = 0.4094208743397143
print("Option 2 is better because is has a higher IRR")

