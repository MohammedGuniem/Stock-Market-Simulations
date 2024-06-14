import matplotlib.pyplot as plt

"""
Let's assume we have a company's 5 month revenue data in an array:
We want to plot a chart visualizing the revenue data.
To do that, we simply need to call the plot function on our data:
"""
rev = [18000, 25000, 20000, 45000, 32000]
plt.plot(rev)
plt.savefig('7_plots/plot_1.png')

"""
The plot() function can also take values for both the x and y axis.
Let's add the month names on the horizontal axis:
"""
rev = [18000, 25000, 20000, 45000, 32000]
months = ['June', 'July', 'August', 'September', 'October']
plt.plot(months, rev)
plt.savefig('7_plots/plot_2.png')