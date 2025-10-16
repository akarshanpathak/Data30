import pandas as pd

# Step 1: Import the dataset
data = pd.read_csv("students.csv")

print("Original Data:")
print(data)

# Step 2: Handle missing values
# Option 1: Drop rows with any missing values
# data_clean = data.dropna()

# Option 2: Fill missing values (e.g., with column mean)
data_clean = data.fillna(data.mean(numeric_only=True))

print("\nCleaned Data:")
print(data_clean)

# Step 3: Group by 'Class' and calculate average Math marks
grouped = data_clean.groupby('Class')['Math'].mean()

print("\nAverage Math Marks by Class:")
print(grouped)



