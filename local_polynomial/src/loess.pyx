# cython: profile = True
import numpy as np
cimport numpy as np
cimport cython


cdef extern from "C_code/c_loess.h":
	int c_loess(
		double *y_out,
		double *y_in,
		int data_len,
		int q, 
		int asymmetric
	)


@cython.boundscheck(False)
@cython.cdivision(True)
cpdef loess(
	double[:] y_in,
	int q,
	int asymmetric
	):

	asymmetric = 1 if asymmetric else 0

	cdef int data_len = y_in.shape[0]
	cdef double[::1] y_out = np.zeros(data_len)

	result = c_loess(
		y_out = &y_out[0],
		y_in = &y_in[0],
		data_len = data_len,
		q = q,
		asymmetric = asymmetric
	)

	if result:
		raise("LOESS failed")
	
	return np.asarray(y_out)
