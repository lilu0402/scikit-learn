import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

xx = pd.read_csv("1.csv", thousands=',')
plt.plot(xx.iloc[:, 0], xx.iloc[:, 1])
plt.show()
