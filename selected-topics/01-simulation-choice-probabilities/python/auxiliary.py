import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_crude_step_function(shifts, probs):
    
    fig, ax = plt.subplots()

    ax.plot(shifts, probs)
    ax.set_xlabel(r"$\beta$")
    ax.set_ylabel(r"$\tilde{P}_{n1}$")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.01))
    
def plot_crude_zero_probability(num_draws, probs, ndim):
    
    fig, ax = plt.subplots()
    ax.set_title(f"{ndim} dimensions")
    ax.plot(num_draws, probs)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$\tilde{P}_{n1}$")
    ax.get_xaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    
def plot_smoothed_probability(levels, rslts):
    fig, ax = plt.subplots()

    for lambda_, values in rslts.items():
        ax.plot(levels[:, 0], values, label=f"{lambda_}")
    ax.axvline(0.0, color="#A9A9A9", linestyle="--")

    ax.set_xlabel(r"$U^r_{n1}$")
    ax.set_ylabel(r"$P^r_{n1}$")
    ax.legend()
