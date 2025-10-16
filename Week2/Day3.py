import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [1500, 1800, 2200, 2000, 2500, 3000]

# Create a line chart
plt.plot(months, sales, color='green', marker='o', linestyle='--', linewidth=2)

# Customize title and axes
plt.title("Sales Growth Over Months")
plt.xlabel("Months")
plt.ylabel("Sales ($)")
plt.grid(True)  # Add grid lines
plt.ylim(0, max(sales)+500)  # Optional: set y-axis range
plt.show()

