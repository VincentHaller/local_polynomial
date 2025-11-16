double point_WLS(
	double W_sum, 
	double W_mean_x,
	double W_mean_y, 
	double W_var_xx,
	double W_cov_yx, 
	long i
)
{
	double b_1_num, b_1_den, b_1, b_0, out;
	b_1_num = W_cov_yx - (W_mean_x*W_mean_y*W_sum);
	b_1_den = W_var_xx - (W_mean_x*W_mean_x*W_sum);
	b_1 = b_1_num/b_1_den;
	b_0 = W_mean_y - b_1*W_mean_x;
	out = b_0 + b_1*(double)i;

	return out;
}


double triweight(double value)
{
	if (value <= 0.0)
		return 1.0;
	else if (value >= 1.0)
		return 0.0;
	else
	{
		value = 1 - value*value*value;
		value = value*value*value;
		return value;
	}
}

void kernel_s_e(
	int *k_s, int *k_e, 
	int n, int i, int data_len, char *has_value
)
{
	long k_w_s, k_w_e, vc;
	vc = 0;

	for (
		k_w_s = n/2, k_w_e = n/2;
		vc < n;
		k_w_s++, k_w_e++
	)
	{
		vc = 0;

		*k_s = max(i-k_w_s, 0);
		*k_e = min(i+1+k_w_e, data_len);

		for (int j = *k_s; j < *k_e; j++)
			vc += has_value[j];
	}

	return;
}


void asy_kernel_s_e(
	int *k_s, int *k_e, 
	int n, int i, int data_len, char *has_value
)
{
	long k_w_s, k_w_e, vc;
	for (
		k_w_s = n-1, k_w_e = 0;
		vc < n;
		k_w_s ++
	)
	{
		vc = 0;

		k_s = max(i-k_w_s, 0);
		k_e = min(i+1+k_w_e, data_len);

		for (j = *k_s; j < *k_e; j++ )
			vc += has_value[j];

		if ( *k_s == 0)
			k_w_e++;

		if ( (k_w_e > 0) && (*k_e >= i) )
			break;
	}

	return;
}