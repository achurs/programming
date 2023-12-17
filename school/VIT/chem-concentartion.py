import numpy as np
from scipy.optimize import curve_fit

def fit_reaction_rate(data):
    time, concentration = data
    def custom_func(t, k):
        return concentration[0] * np.exp(-k * t)
    popt, _ = curve_fit(custom_func, time, concentration)
    return popt[0]

# Theoretical data: Time and Concentration
time = np.linspace(0, 50, 100)
concentration = np.exp(-0.111 * time)
data = (time, concentration)

rate_parameter = fit_reaction_rate(data)
print(f"The estimated reaction rate parameter is {rate_parameter:.3f}.")
