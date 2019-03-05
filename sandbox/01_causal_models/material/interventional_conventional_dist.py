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

plt.savefig('interventional_distribution.png')


# Conditional distribution

# Plot graph
mean = [0, 0]
rho = -6
cov = [[1, rho], [rho, 37]]
fig, ax = plt.subplots()
x, y = np.random.multivariate_normal(mean, cov, 1000).T
ax.plot(x, y, 'x')

# Set labels, limits and title
ax.set_xlim(-4, 4)
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.savefig('conditional_distribution.png')
