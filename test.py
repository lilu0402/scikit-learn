import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn

xx = pd.read_csv("./data/housing.csv")
plt.plot(xx.iloc[:, 0][::1000], xx["total_rooms"][::1000],'g.')
plt.grid("true")
xx.plot(
    kind="scatter",
    x="longitude",
    y='latitude',
    alpha=0.4,
    s=xx["population"] / 100,
    label="population",
    c="total_rooms",
    cmap=plt.get_cmap("jet"),
    colorbar=True,
)
# plt.show()