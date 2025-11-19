# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from local_polynomial.local_polynomial import local_polynomial
from local_polynomial.loess import loess

# %%
X = np.linspace(-0.5, 4.2*np.pi, 50)
Y = np.sin(X)

# %%
y_out =  local_polynomial(x_in = X, y_in = Y, x_out = X, q=0.3, degree=1)
y_out_2 = loess(y_in=Y,q=5, asymmetric=False)
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
