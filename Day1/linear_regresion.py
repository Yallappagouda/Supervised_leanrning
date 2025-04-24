import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
dataset = {
    "sqft": [10, 24, 90],
    "price": [300000, 600000, 200000]
}

# Prepare data for model
x = [[value] for value in dataset["sqft"]]
y = dataset["price"]

# Create and train model
model = LinearRegression()
model.fit(x, y)

# Predict price for 1500 sqft
predicted_price = model.predict([[1500]])
print("Predicted price for 1500 sqft:", predicted_price[0])

# Plotting
plt.scatter(dataset["sqft"], y, color='blue', label="Actual data")
plt.plot([0, 1600], model.predict([[0], [1600]]), color='red', label="Regression line")
plt.scatter(1500, predicted_price, color='green', label="Predicted (1500 sqft)")
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Linear Regression: Price vs. Sqft")
plt.legend()
plt.grid(True)
plt.show()
