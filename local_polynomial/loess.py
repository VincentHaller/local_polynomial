# %%
from local_polynomial.src.cy_loess import cy_loess

# %%
def loess(y_in:float, q:int, asymmetric:bool=False):
	"""
	LOESS (Locally Weighted Scatterplot Smoothing) regression.
	
	Performs local linear regression smoothing on input data using a triweight kernel.
	This function smooths the input y-values by fitting local linear polynomials
	at each point using weighted least squares, where weights are determined by
	the triweight kernel function based on the distance to neighboring points.
	
	Args:
		y_in (np.array): Input y-values to be smoothed. Must be a 1D array.
		q (int): Number of nearest neighbors to use for each local regression.
			Controls the bandwidth of the smoothing. Must be at least 3.
			Larger values result in smoother output.
		asymmetric (bool, optional): If True, uses asymmetric kernel windows that
			extend further in one direction. If False, uses symmetric windows.
			Defaults to False.
	
	Returns:
		np.array: Smoothed y-values of the same shape as y_in. NaN values in
			input are preserved in output.
	
	Note:
		This function uses a C implementation for high performance. The algorithm
		handles NaN values by excluding them from local regressions. If there are
		fewer than 3 valid (non-NaN) data points, all output values will be NaN 
		and an error will be raised.
	
	Example:
		>>> import numpy as np
		>>> from local_polynomial.loess import loess
		>>> y = np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100)
		>>> y_smooth = loess(y_in=y, q=15, asymmetric=False)
	"""
	asymmetric = 1 if asymmetric else 0
	y_out = cy_loess(y_in=y_in, q=q, asymmetric=asymmetric)
	return y_out
