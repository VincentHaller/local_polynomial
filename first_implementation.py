"""
Create first python implementation of local_polynomial function to prove algorithm.

Function inputs:
	- x_in 
	- y_in 
	- q : kernal width
	- x_out : output on which to calculate y_out
	- additional weighting (for now all == 1)

Function steps:
	1. sort input 
	2. sort output
	3. find kernel width -> what points to include
	4. create point weighting.
	5. find sum of weighting 
	6. do WLS regression 
	7. generate output. 

Edge Case:
	- how do deal with sparse areas 
	- how to deal with very large kernels 
"""
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
def triweight(value:float):
	if value >= 1.0:
		return 0.0
	elif value <= 0.0:
		return 1.0
	else:
		return (1 - value**3)**3

def point_WLS( W_sum, W_mean_x, W_mean_y, W_var_xx, W_cov_yx, x ):

	b_1_num = W_cov_yx - (W_mean_x*W_mean_y*W_sum)
	b_1_den = W_var_xx - (W_mean_x*W_mean_x*W_sum)
	b_1 = b_1_num/b_1_den
	b_0 = W_mean_y - b_1*W_mean_x
	out = b_0 + b_1*x

	return out

# %%
x_in = np.random.uniform(0, 100, 100)
y_in = 4 - 0.2*x_in + 0.002*x_in**2
x_out = np.arange(0, 100, 10, dtype='d')
# %%
plt.scatter(x_in, y_in)


x_sort = np.sort(x_in)
y_sort = y_in[x_in.argsort()]

x_out = np.sort(x_out)

len_out = x_out.shape[0]
len_in = x_sort.shape[0]
q = 100 


# %%
x_dist = np.empty_like(x_sort)
x_W = np.empty_like(x_sort)
y_out = np.empty(len_out, dtype='d')
y_out[:] = np.nan
for i in range(len_out):
	W_sum = W_mean_x = W_mean_y = W_var_xx = W_cov_yx = 0

	for j in range(len_in):

		x_dist[j] = np.abs(x_out[i] - x_sort[j])
		x_W[j] = triweight(x_dist[j]/q)

		W_sum += x_W[j]

		W_mean_x += x_W[j]*x_sort[j]
		W_mean_y += x_W[j]*y_sort[j]
		W_var_xx += x_W[j]*x_sort[j]*x_sort[j]
		W_cov_yx += x_W[j]*x_sort[j]*y_sort[j]
	
	W_mean_x /= W_sum
	W_mean_y /= W_sum

	y_out[i] = point_WLS(W_sum, W_mean_x, W_mean_y, W_var_xx, W_cov_yx, x_out[i])
		

	plt.plot(x_dist)
	plt.plot(x_W)
	plt.show()
# %%
plt.scatter(x_out, y_out)
plt.scatter(x_sort, y_sort)






# %%
def local_poly(y_in, x_in, q):
	x_sort = np.sort(x_in)
	y_sort = y_in[x_in.argsort()]
	
	x_out = 

