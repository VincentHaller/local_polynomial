# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from local_polynomial.local_polynomial import local_polynomial
from local_polynomial.loess import loess

# %%
X = np.linspace(-0.5, 4.5*np.pi, 200)
Y = np.sin(X)

# %%
y_out =  local_polynomial(x_in = X, y_in = Y, x_out = X, q=0.3, degree=1)
y_out_2 = loess(y_in=Y,q=15, asymmetric=1)
plt.scatter(X, Y)
plt.scatter(X, y_out_2)

# %%
y_out_2

# %%
Y


# %%
y_out.shape

# %%
X.shape
# %%
y_out_2.shape

# %%
