import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv('CPI.csv') 

# Extract features and target
X = data[['year']]  # Feature (must be 2D for sklearn)
y = data['CPI']   # Target

# Create and train the model

model = LinearRegression()
model.fit(X, y)

# Predict value for a new year
prediction_years = np.array([[2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035]]).reshape(-1, 1)
predicted_CPI = model.predict(prediction_years)

predictions_df = pd.DataFrame({
    'year': prediction_years.flatten(),
    'predicted_value': predicted_CPI
})

predictions_df.to_csv('CPI_prediction.csv')

plt.scatter(X, y, color='blue', label='CPI data')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.scatter(prediction_years, predicted_CPI, color='green', label='CPI prediction')
plt.xlabel("Year")
plt.ylabel("CPI")
plt.title("Linear regression model of CPI")
plt.legend()
plt.grid(True)
plt.show()