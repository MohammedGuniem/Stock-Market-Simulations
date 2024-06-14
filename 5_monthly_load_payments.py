import numpy_financial as npf

"""
Let's say we want to calculate how much we have to pay monthly to pay back a loan of 100,000 in 5 years. 
The yearly interest rate is 7%, and is calculated monthly.
"""
res = npf.pmt(rate=0.07 / 12, nper=5 * 12, pv=100000, fv=0)
print(res)  # results = -1980.1198540349467

"""
Note that aside from computing a monthly mortgage payment, 
the pmt() function can be used to return the periodic deposit one must make to achieve a specified future balance 
with a given interest rate.
"""
res = npf.pmt(rate=0.10/12, nper=5*12, pv=0, fv=50000)
print(res)  # results = -645.6855688967499
