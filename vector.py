from sklearn.datasets import load_iris

data = load_iris()
X, y = data["data"], data["target"] 
#shape of the data
print("Shape of the data ", X.shape)

#The value of X
print("\nThe value of X is \n", X)

#The value of y
print("\nThe value of y is \n", y)

