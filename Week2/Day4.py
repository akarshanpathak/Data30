import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Set style and color palette
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Create a boxplot: distribution of tips by day
plt.figure(figsize=(8,6))
sns.boxplot(x="day", y="tip", data=tips)

# Customize titles and labels
plt.title("Distribution of Tips by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Tip Amount ($)")
plt.show()
