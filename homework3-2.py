import numpy as np
from scipy.interpolate import BarycentricInterpolator

def inverse_interpolation(x_vals, y_vals, max_iters=10, tol=1e-10):
    """
    Perform iterated inverse interpolation to find x such that x - e^(-x) = 0.
    """
    x_guess = np.interp(0, y_vals - x_vals, x_vals) 
    
    for _ in range(max_iters):
        interpolator = BarycentricInterpolator(y_vals - x_vals, x_vals)  
        new_x_guess = interpolator(0)  
        
        if abs(new_x_guess - x_guess) < tol:
            break
        x_guess = new_x_guess
    
    return x_guess

x_vals = np.array([0.3, 0.4, 0.5, 0.6])
y_vals = np.exp(-x_vals)  

approx_x = inverse_interpolation(x_vals, y_vals)

print(f"Approximated solution for x - e^(-x) = 0: x ≈ {approx_x:.10f}")