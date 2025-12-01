# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from local_polynomial.local_polynomial import local_polynomial
from local_polynomial.loess import loess
from local_polynomial.src.cy_loess import cy_loess
import cProfile

# %%
X = np.linspace(-0.5, 4.2*np.pi, 500)
Y = np.sin(X)
Y += np.random.uniform(-0.1, 0.1, 500)
nan_locs = np.random.choice(50, 85)
Y[nan_locs] = np.nan

# %%
y_out =  local_polynomial(x_in = X, y_in = Y, x_out = X, q=0.3, degree=1)
y_out_2 = loess(y_in=Y,q=5, asymmetric=False)
y_out_3 = cy_loess(y_in=Y, q=5, asymmetric=0)
plt.scatter(X, Y)
plt.scatter(X, y_out_2)

# %%
np.where(~np.isnan(Y))[0]
# %%
import math
# n = Y.shape[0]
has_val_locs = np.where(~np.isnan(Y))[0]
n = has_val_locs.shape[0]
# n = 51
k_folds = 10
loc_matrix = np.zeros([k_folds, math.ceil(n/k_folds)], dtype='l')
loc_matrix[:] = -1

# %%
q_max = n if n%2 else n+1
q_options = np.linspace(5, q_max, (q_max-2)//2)
# %%
q_score = np.zeros_like(q_options)
arr_loss = np.zeros_like(Y)
for n_q, q in enumerate(q_options):
	arr_loss[:] = 0
	for k in range(k_folds):
		min_loc_matrix = loc_matrix.min()
		k_locs = loc_matrix[k] if min_loc_matrix > 0 else loc_matrix[k][:-1]

		y_test = Y.copy()
		y_test[k_locs] = np.nan
		
		est = loess(y_in = y_test, q=q)
		arr_loss[k_locs] = est[k_locs] - Y[k_locs]
		
	q_score[n_q] = np.mean(arr_loss**2)
# %%
plt.plot(q_options, np.log(q_score))
plt.title('ln(RMSE) by Kernel width')




# %% good for 
np_range = has_val_locs.copy()
np.random.shuffle(np_range)
for i in range(n):
	x = i%k_folds
	y = i // k_folds
	val = np_range[i]
	loc_matrix[x, y] = val
# %%
loc_matrix[1][:-1].min()

# %%

Y[loc_matrix[k]]
# %%
loc_matrix
# %%
loc_matrix[i]
# %%


# %%
def cv_loess(
		y_in, k_folds:int=10, 
		asymmetric:bool=False, 
		out_sample_start:int=None
		):
	pass