# =====================================================
# MINI PROJECT 1 - COMPLETE EDA IN ONE FILE
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("========== MINI PROJECT 1: EDA ==========")

# =====================================================
# PHASE 1: DETECTIVE WORK (DATASET CREATION & INSPECTION)
# =====================================================

print("\n--- PHASE 1: DATA INSPECTION ---")

# Create dataset
data = {
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Age": [20, 21, 20, 22, 21, None, 23, 20],
    "Gender": ["Female", "Male", "Female", "Female", "Male", "Male", None, "Female"],
    "Marks": [85, 78, 92, 88, None, 74, 90, 81],
    "Attendance": [90, 85, 95, 88, 80, None, 92, 87]
}

df = pd.DataFrame(data)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# =====================================================
# PHASE 2: DATA CLEANING
# =====================================================

print("\n--- PHASE 2: DATA CLEANING ---")

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill numeric missing values with median
for col in df.select_dtypes(include="number"):
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values with mode
for col in df.select_dtypes(include="object"):
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nData Cleaning Completed Successfully.")

# =====================================================
# PHASE 3: UNIVARIATE ANALYSIS
# =====================================================

print("\n--- PHASE 3: UNIVARIATE ANALYSIS ---")

df.hist(figsize=(10, 8))
plt.suptitle("Univariate Analysis (Histograms)")
plt.show()

print("Observation: Most students are aged 20-22 with generally high marks and attendance.")

# =====================================================
# PHASE 3: BIVARIATE ANALYSIS
# =====================================================

print("\n--- PHASE 3: BIVARIATE ANALYSIS ---")

sns.scatterplot(x="Attendance", y="Marks", data=df)
plt.title("Attendance vs Marks")
plt.show()

print("Observation: Higher attendance generally corresponds to higher marks.")

sns.boxplot(x="Gender", y="Marks", data=df)
plt.title("Marks Distribution by Gender")
plt.show()

print("Observation: Marks distribution between genders is fairly balanced.")

# =====================================================
# PHASE 4: MULTIVARIATE ANALYSIS
# =====================================================

print("\n--- PHASE 4: MULTIVARIATE ANALYSIS ---")

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

print("\n========== EXECUTIVE SUMMARY ==========")
print("1. Attendance shows strong positive correlation with Marks.")
print("2. Missing values were handled using median (numerical) and mode (categorical).")
print("3. Student performance is generally consistent with high attendance rates.")
print("\n========== EDA COMPLETED SUCCESSFULLY ==========")