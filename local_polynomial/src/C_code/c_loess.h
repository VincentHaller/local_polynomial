#ifndef C_LOESS_H
#define C_LOESS_H

long c_loess(
	double *y_out,
	double *y_in,
	long data_len,
	long q, 
	long asymmetric
);

#endif