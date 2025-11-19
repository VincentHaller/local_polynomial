#ifndef C_INTERNAL_H
#define C_INTERNAL_H

#include <math.h>


void kernel_s_e(
	long *k_s, long *k_e, 
	long n, long i, long data_len, char *has_value
);

void asy_kernel_s_e(
	long *k_s, long *k_e, 
	long n, long i, long data_len, char *has_value
);

double triweight(double value);

double point_WLS(
	double W_sum, 
	double W_mean_x,
	double W_mean_y, 
	double W_var_xx,
	double W_cov_yx, 
	long i
);

#endif