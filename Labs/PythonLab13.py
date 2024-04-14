import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to simulate throwing balls into bins
def simulate_balls_into_bins(N):
    bins = np.zeros(N)  # Initialize bins
    for _ in range(N):
        ball = np.random.randint(N)  # Randomly choose a bin
        bins[ball] += 1  # Increment the chosen bin
    non_empty_bins = np.sum(bins > 0)  # Count non-empty bins
    return non_empty_bins

# Run simulations for each value of N from 1 to 1000
N_values = np.arange(1, 1001)
results = [simulate_balls_into_bins(N) for N in N_values]

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(N_values, results, label='Simulation Results', color='blue', alpha=0.5)

# Perform linear regression
slope, intercept, rvalue, _, _ = linregress(N_values, results)

# Plot the best fit line
plt.plot(N_values, slope * N_values + intercept, color='red', label='Best Fit Line')

plt.title('Monte Carlo Simulation Results')
plt.xlabel('Number of Bins (N)')
plt.ylabel('Number of Non-empty Bins')
plt.legend()

plt.show()

# Print regression results
print("SciPy Linear Regression Solution")
print("Slope:", slope)
print("Intercept:", intercept)
print("rvalue:", rvalue)