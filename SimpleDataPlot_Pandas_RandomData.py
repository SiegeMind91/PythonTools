import pandas
import matplotlib.pyplot as plt
import numpy as np

ts = pandas.Series(np.random.randn(1000), index=pandas.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()