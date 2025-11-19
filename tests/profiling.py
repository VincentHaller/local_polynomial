# %%
import numpy as np
import cProfile

from local_polynomial.local_polynomial import local_polynomial
from local_polynomial.loess import loess
from local_polynomial.src.cy_loess import cy_loess

# %%
X = np.linspace(-0.5, 4.2*np.pi, 800)
Y = np.sin(X)

# %%
y_out =  local_polynomial(x_in = X, y_in = Y, x_out = X, q=0.3, degree=1)
# %%
y_out_2 = loess(y_in=Y,q=5, asymmetric=False)
y_out_3 = cy_loess(y_in=Y, q=5, asymmetric=0)
# %%
cProfile.run("local_polynomial(x_in = X, y_in = Y, x_out = X, q=0.3, degree=1)")
# %%
cProfile.run("loess(y_in=Y,q=5, asymmetric=False)")

# %%
cProfile.run("cy_loess(y_in=Y,q=5, asymmetric=0)")

# %%
