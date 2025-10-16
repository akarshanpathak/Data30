import pandas as pd

# Step 1: Import the CSV file
data = pd.read_csv("students_marks.csv")

# Step 2: Display basic info about the dataset
print("📘 Basic Information:")
print(data.info())

# Step 3: Display top 5 rows
print("\n🔝 Top 5 Rows:")
print(data.head())

# Step 4: Display summary statistics
print("\n📊 Summary Statistics:")
print(data.describe())
