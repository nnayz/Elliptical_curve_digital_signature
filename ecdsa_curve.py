import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple

# Define the constants
a = 0; b = 7
# Define the function
def f(X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    # Returns the tuple for both +ve and -ve
    return (np.sqrt(X**3 + a*X + b), -np.sqrt(X**3 + a*X + b)) # Returns a tuple both for +ve and -ve y


plt.figure(figsize=(10, 6))
plt.grid(True)
X = np.linspace(-4, 4, 100)
y_pos, y_neg = f(X)
plt.plot(X, y_pos, label="y^2 = x^3 + a^x + b", c="b")
plt.plot(X, y_neg, label="y^2 = x^3 + a^x + b", c="b")
plt.legend()
plt.show()
