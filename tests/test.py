# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from local_polynomial.local_polynomial import local_polynomial

# %%
X = np.linspace(0, 4*np.pi, 200)
Y = np.sin(X)

# %%
y_out =  local_polynomial(x_in = X, y_in = Y, x_out = X, q=0.3, degree=1)
plt.scatter(X, Y)
plt.scatter(X, y_out)

# %%
