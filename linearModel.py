import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Download and prepare the data

lifesat = pd.read_csv("lifesat.csv")
print(lifesat)

X = lifesat[["GDP"]].values
y = lifesat[["Life satisfaction"]].values

#visualize the data
lifesat.plot(kind = "scatter", grid = True,
             x = "GDP", y = "Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

#select a linear model
model = LinearRegression()

#train the model
model.fit(X, y)

#Make a prediction for Nepal gdp of nepal = 1154

X_nepal = [[1_154]]
print("\nLife satisfaction of Nepal is ",model.predict(X_nepal))
