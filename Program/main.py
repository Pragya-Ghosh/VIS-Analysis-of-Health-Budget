import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("budget_data.csv")
budget = data['Budget Estimation (in Rs. crore)']
dept = data['Major Heads']

# Define colors for the pie chart slices
colors = plt.get_cmap('tab20').colors

# Exploding the smaller slices for better visualization
explode = [0.1 if size < 2000 else 0 for size in budget]

fig, ax = plt.subplots(figsize=(10, 8))  # Adjust the figure size for better readability

wedges, texts, autotexts = ax.pie(
    budget,
    labels=dept,
    autopct='%1.1f%%',
    colors=colors,
    startangle=140,
    explode=explode,
    pctdistance=0.85,
    textprops={'fontsize': 9}  # Font size for labels
)

# Improve label visibility
plt.setp(autotexts, size=10, weight="bold")  # Font size and weight for percentages

# Add a title
plt.title('Budget Estimation for Major Heads in 2023-24', fontsize=14, weight='bold')

plt.tight_layout()

# Show the plot
plt.show()
