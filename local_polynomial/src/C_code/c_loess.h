#ifndef C_ASY_LOESS_H
#define C_ASY_LOESS_H

long c_asy_loess(
	double *y_out,
	double *y_in,
	double *y_W_in,
	long data_len,
	long q, 
	long asymmetric
);

#endif