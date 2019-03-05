import numpy as np
import matplotlib.pyplot as plt

# Interventional distribution

# Plot graph
mean = 0
sd = 1
fig, ax = plt.subplots()
x = np.random.normal(mean, sd, 1000)
count, bins, ignored = plt.hist(x, 30, density=True)
plt.plot(bins, 1/(sd * np.sqrt(2 * np.pi)) * np.exp(- (bins - mean)**2 / (2 * sd**2)), linewidth=2, color='r')

# Set labels, limits and title
ax.set_xlim(-3, 3)
ax.set_ylim(0, 0.55)
ax.set_xlabel('X')
ax.set_title('Interventional distribution of X|do(Y=3)')

plt.savefig('interventional_distribution.png')


# Conditional distribution

# Plot graph
sigma1 = 1
sigma2 = 6.0827625303  # sqrt(37)
rho = -0.98639392383  # -6/sigma2
mean = (sigma1/sigma2) * rho * 3
sd = 1 - rho ** 2
fig, ax = plt.subplots()
x = np.random.normal(mean, sd, 1000)
count, bins, ignored = plt.hist(x, 30, density=True)
plt.plot(bins, 1/(sd * np.sqrt(2 * np.pi)) * np.exp(- (bins - mean)**2 / (2 * sd**2)), linewidth=2, color='r')

# Set labels, limits and title
ax.set_xlabel('X')
ax.set_title('Conditional distribution of X|Y=3')

plt.savefig('conditional_distribution.png')
