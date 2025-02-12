# %%
import numpy as np 
from local_polynomial.src.internals import triweight, point_poly_WLS

# %%
def local_polynomial(
	x_in:np.array, 
	y_in:np.array, 
	x_out:np.array, 
	q:float, 
	w_in:np.array=None, 
	degree:int=0
)->np.array:
	"""
	Local polynomial estimation.

	Args:
		x_in (np.array): X values in.
		y_in (np.array): Y values in.
		x_out (np.array): X values out.
		q (float): Kernel size.
		w_in (np.array, optional): Additional weighting to be applied to x_in. Defaults to None.
		degree (int, optional): Degree of polynomial. Defaults to 0.

	Returns:
		np.array: Y values out.
	"""
	arr_sort = x_in.argsort()
	x_sort = x_in[arr_sort]
	y_sort = y_in[arr_sort]

	y_out = np.empty_like(x_out, dtype='d')

	if w_in is None:
		w_in = np.ones_like(x_in, dtype='d')
	else:
		w_sort = w_in[arr_sort]
	
	x_W = np.empty_like(x_in, dtype='d')

	for i in range(x_out.shape[0]):
		for j in range(x_sort.shape[0]):
			x_W[j] = triweight(np.abs(x_out[i] - x_sort[j])/q) * w_sort[j]
		
		y_out[i] = point_poly_WLS(
			x_in=x_sort,
			y_in=y_sort, 
			w_in = x_W, 
			point_x = x_out[i], 
			degree=degree
		)	
	
	return y_out
		

