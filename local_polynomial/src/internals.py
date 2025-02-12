# %%
import numpy as np 

# %%
def triweight(value:float)->float:
	"""
	Triweight kernel.

	Args:
		value (float): Input value.

	Returns:
		float: Output value.
	"""	
	if value >= 1.0:
		return 0.0
	elif value <= 0.0:
		return 1.0
	else:
		return (1 - value**3)**3


# %%
def point_poly_WLS(
	x_in:np.array, y_in:np.array, w_in:np.array, point_x:float, degree:int
	)->float:
	"""
	Performs a point output for a polynomial WLS.

	Args:
		x_in (np.array): X values in.
		y_in (np.array): Y values in.
		w_in (np.array): Weights in.
		point_x (float): Point of output.
		degree (int, optional): Degree of polynomial.

	Returns:
		float: Point output.
	"""
	W = np.diag(w_in)
	X = np.empty([x_in.shape[0], degree+1])

	X[:, 0] = 1
	for i in range(degree):
		X[:, i+1] = x_in**(i+1)

	XWX = X.T.dot(W).dot(X)
	XWY = X.T.dot(W).dot(y_in)
	Bw = np.linalg.inv(XWX).dot(XWY)

	y_point_out = Bw[0]

	for i in range(degree):
		y_point_out += Bw[i+1]*point_x**(i+1)
	
	return y_point_out
