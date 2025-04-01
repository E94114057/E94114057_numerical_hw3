import numpy as np
from scipy.interpolate import BarycentricInterpolator
from math import factorial, cos

x_vals = np.array([0.698, 0.733, 0.768, 0.803, 0.838])
y_vals = np.array([0.7661, 0.7432, 0.7193, 0.6946, 0.6691])
x_target = 0.750
true_value = 0.7317  

results = {}
errors = {}
error_bounds = {}

def lagrange_error_bound(x_vals, x_target, degree):
    if degree >= len(x_vals):
        return None  
    max_derivative = 1  
    product_term = np.prod([x_target - x_vals[i] for i in range(min(degree+1, len(x_vals)))])
    return abs(max_derivative * product_term / factorial(degree+1))

for degree in range(1, min(5, len(x_vals))):
    interpolator = BarycentricInterpolator(x_vals[:degree+1], y_vals[:degree+1])
    approx_value = interpolator(x_target)
    
    error = abs(approx_value - true_value)
    error_bound = lagrange_error_bound(x_vals[:degree+1], x_target, degree)
    
    results[f"Degree {degree}"] = approx_value
    errors[f"Degree {degree}"] = error
    error_bounds[f"Degree {degree}"] = error_bound

for degree in range(1, min(5, len(x_vals))):
    print(f"Degree {degree}: Approximated Value = {results[f'Degree {degree}']:.7f}, "
          f"Error = {errors[f'Degree {degree}']:.7f}, "
          f"Error Bound = {error_bounds[f'Degree {degree}']:.7f}")