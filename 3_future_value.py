import numpy_financial as npf

"""
Let's assume you invest $1000 for 5 years at an annual return rate of 8%.
We need to calculate how much our investment will be worth after 5 years.
"""
res = npf.fv(rate=0.08, nper=5, pmt=0, pv=-1000)
print(res)  # result = 1469.3280768000006

"""
We imported the Numpy Financial package, and used its fv() function to calculate the future value based on the parameters.
The interest rate is given as a decimal, 1 representing 100%, thus 0.08 corresponds to 8%.
nper is the number of periods.
pv is the present value, which in our case is an investment of $1000, thus the negative sign.
pmt corresponds to periodic payments/investments, which in our case is 0.
"""