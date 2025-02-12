# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.internals import triweight, point_poly_WLS

# %%
x_in = np.random.uniform(0, 100, 100)
y_true = 4 - 0.2*x_in + 0.002*x_in**2 
y_in = y_true + np.random.normal(0, 1, 100)
x_out = np.arange(0, 100, 10, dtype='d')
# x_out = np.array([60.0])
# %%
plt.scatter(x_in, y_in)


x_sort = np.sort(x_in)
y_sort = y_in[x_in.argsort()]

x_out = np.sort(x_out)

len_out = x_out.shape[0]
len_in = x_sort.shape[0]
q = 1000


# %%
x_dist = np.empty_like(x_sort)
x_W = np.empty_like(x_sort)
y_out = np.empty(len_out, dtype='d')
y_out[:] = np.nan
# %%

for i in range(len_out):

	for j in range(len_in):

		x_dist[j] = np.abs(x_out[i] - x_sort[j])/q
		x_W[j] = triweight(x_dist[j])

	y_out[i] = point_poly_WLS(x_sort, y_sort, x_W, x_out[i], degree=4)



# %%
plt.scatter(x_in, y_in, alpha = 0.5)
plt.scatter(x_out, y_out)
plt.scatter(x_in, y_true, alpha=0.4)
# %%








		


# %%
