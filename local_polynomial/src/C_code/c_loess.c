// includes
#include <stdlib.h>
#include "c_internals.h"

// declares 
	// In header file.
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

// functions
long c_loess(
	double *y_out, 
	double *y_in,
	long data_len,
	long q,
	long asymmetric
)
{
	long i, j, m, n, p_n, count_nan;
	char *has_value;
	double kernel_multi;
	has_value =  (char*)malloc(data_len * sizeof(char));

	count_nan = 0;
	for (i = 0; i < data_len; i++)
	{
		if (isnan(y_in[i]))
		{
			has_value[i] = 0;
			count_nan += 1;
		}
		else
			has_value[i] = 1;
	}

	p_n = data_len - count_nan;
	
	if (p_n < 3)
	{
		for ( i = 0; i < data_len; i++)
			y_out[i] = NAN;
		free(has_value);
		return 1;
	}

	q = max(3, q);
	m = max(5, q);
	n = min(q, p_n);

	kernel_multi = (double)m / (double)n;

	double *y;
	double *x;
	double *y_x;
	double *x_x;

	y = (double*)malloc(p_n *sizeof(double));
	x = (double*)malloc(p_n *sizeof(double));
	y_x = (double*)malloc(p_n *sizeof(double));
	x_x = (double*)malloc(p_n *sizeof(double));

	for ( i = 0, j = 0; i < data_len; i++ )
	{
		if (has_value[i] == 1)
		{
			y[j] = y_in[i];
			x[j] = i;
			j++;
		}
	}

	for ( i = 0; i < p_n; i++ )
	{
		x_x[i] = x[i]*x[i];
		y_x[i] = y[i]*x[i];
	}

	double W, k_W, W_sum, W_mean_x, W_mean_y, W_cov_yx, W_var_xx;
	long k_s, k_e, k_w, k_w_s_j, k_w_e_j;

	for (i = 0; i < data_len; i++ )
	{

		if ( asymmetric )
			asy_kernel_s_e(&k_s, &k_e, n, i, data_len, has_value);
		else
			kernel_s_e(&k_s, &k_e, n, i, data_len, has_value);

		k_w = max(i -k_s, k_e -1 -i);
		k_W = (double)k_w * kernel_multi;

		W_sum = W_mean_x = W_mean_y = W_var_xx = W_cov_yx = 0;
		k_w_s_j = k_w_e_j = 0;

		for ( j = 0; j < k_s; j++ )
			k_w_s_j += has_value[j];

		for ( j = 0; j < k_e; j++ )
			k_w_e_j += has_value[j];

		for ( j = k_w_s_j; j < k_w_e_j; j++ )
		{
			W = fabs(x[j] - i);
			W /= k_W;
			W = triweight(W);

			W_sum += W;
			
			W_mean_x += W*x[j];
			W_mean_y += W*y[j];
			W_var_xx += W*x_x[j];
			W_cov_yx += W*y_x[j];
		}

		y_out[i] = point_WLS(
			W_sum, 
			W_mean_x, 
			W_mean_y, 
			W_var_xx, 
			W_cov_yx, 
			i
		);
	}

	free(has_value);
	free(y);
	free(x);
	free(y_x);
	free(x_x);

	return 0;

}