import numpy as np

# Data provided
data = np.array([
    [1.9, 3, 2.9, 1.6, 1.75],
    [1.55, 3.3, 4, 1.7, 1.65],
    [2, 3, 2.7, 1.8, 1.55],
    [1.9, 3, 2.9, 1.75, 1.6],
    [1.65, 3.2, 3.6, 1.7, 1.65],
    [2, 2.8, 2.9, 1.3, 2.3],
    [2, 2.8, 2.9, 1.35, 2.15],
    [1.65, 3.1, 3.75, 1.5, 1.85],
    [2.9, 2.8, 2, 1.3, 2.3]
])

# Calculate the probability of winning (p) and losing (q)
p = 1 / data.shape[1]  # Assuming equally likely outcomes
q = 1 - p

# Loop through each row (betting option)
for i in range(data.shape[0]):
    odds = data[i, :].astype(float)  # Extract odds for the current betting option
    b = np.where(odds > 1, odds, 1/odds)  # Convert odds to decimal format
    f_star = (b * p - q) / b  # Calculate optimal bet size using Kelly Criterion
    max_f_star = np.max(f_star)  # Find the maximum bet size
    print("Optimal bet size for betting option", i+1, ":", max_f_star)
