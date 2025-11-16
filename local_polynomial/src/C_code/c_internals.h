#ifndef C_INTERNAL_H
#define C_INTERNAL_H

#include <math.h>

#define max(a,b) \ 
	({
		__typeof__(a) _a = (a); \
		__typeof__(b) _b = (b); \ 
		_a > _b ? _a : _b; \
	})

#define min(a,b) \ 
	({
		__typeof(a) _a = (a); \
		__typeof(b) _b = (b); \
		_a < _b ? _a : _b; \
	})

void kernel_s_e(
	int *k_s, int *k_e, 
	int n, int i, int data_len, char *has_value
);

void asy_kernel_s_e(
	int *k_s, int *k_e, 
	int n, int i, int data_len, char *has_value
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