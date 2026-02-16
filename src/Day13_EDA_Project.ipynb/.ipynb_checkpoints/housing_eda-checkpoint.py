import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# Create Housing Dataset
# ===============================
df = pd.DataFrame({
    "Price": [250000, 320000, 180000, 450000, 300000,
              275000, 500000, 350000, 220000, 400000],
    "City": ["Mumbai", "Delhi", "Pune", "Bangalore", "Mumbai",
             "Pune", "Bangalore", "Delhi", "Pune", "Mumbai"],
    "Bedrooms": [2, 3, 2, 4, 3, 2, 4, 3, 2, 4],
    "Area_sqft": [850, 1200, 780, 1600, 1100,
                  900, 1800, 1300, 820, 1500]
})

# Histogram + KDE
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Skewness & Kurtosis
print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())

# Count Plot
sns.countplot(x="City", data=df)
plt.title("Count of Houses by City")
plt.xticks(rotation=45)
plt.show()
