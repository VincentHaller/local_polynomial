# %%
import numpy as np 

# %%
def triweight(value:float):
	if value >= 1.0:
		return 0.0
	elif value <= 0.0:
		return 1.0
	else:
		return (1 - value**3)**3

# %%
def point_WLS( W_sum, W_mean_x, W_mean_y, W_var_xx, W_cov_yx, x ):

	b_1_num = W_cov_yx - (W_mean_x*W_mean_y*W_sum)
	b_1_den = W_var_xx - (W_mean_x*W_mean_x*W_sum)
	b_1 = b_1_num/b_1_den
	b_0 = W_mean_y - b_1*W_mean_x
	out = b_0 + b_1*x

	return out

# %%
def point_poly_WLS(x_in, y_in, w_in, point_x, poly:int=1):

	W = np.diag(w_in)
	X = np.empty([x_in.shape[0], poly+1])

	X[:, 0] = 1
	for i in range(poly):
		X[:, i+1] = x_in**(i+1)

	XWX = X.T.dot(W).dot(X)
	XWY = X.T.dot(W).dot(y_in)
	Bw = np.linalg.inv(XWX).dot(XWY)

	y_point_out = Bw[0]

	for i in range(poly):
		y_point_out += Bw[i+1]*point_x**(i+1)
	
	return y_point_out
