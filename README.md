# local-polynomial

Fast Local Polynomial regression functions implemented in Python with Cython/C extensions for high performance.
This is a personal, free-time project. 

## Features

- **Local Polynomial Regression**: Flexible polynomial degree support with customizable kernel bandwidth
- **LOESS Smoothing**: Fast LOESS (Locally Weighted Scatterplot Smoothing) regression for time series and data smoothing
- **Triweight Kernel**: Robust kernel function for local weighting
- **Weighted Least Squares**: Support for additional weighting in polynomial estimation
- **Optimized Performance**: C extensions for computationally intensive operations

## Installation

### Using pip

```bash
pip install git+https://github.com/VincentHaller/local_polynomial
```

## Requirements

- Python >= 3.12
- NumPy >= 2.3.4
- Pandas >= 2.3.3
- Cython >= 3.1.6 (for building from source)

## Quick Start

### Local Polynomial Regression

```python
import numpy as np
from local_polynomial.local_polynomial import local_polynomial

# Generate sample data
x_in = np.linspace(0, 10, 100)
y_in = np.sin(x_in) + np.random.normal(0, 0.1, 100)

# Define output points
x_out = np.linspace(0, 10, 200)

# Perform local polynomial regression
# q: kernel bandwidth
# degree: polynomial degree (0 = local constant, 1 = local linear, etc.)
y_out = local_polynomial(
    x_in=x_in,
    y_in=y_in,
    x_out=x_out,
    q=1.0,  # kernel size
    degree=1  # linear polynomial
)
```

### LOESS Smoothing

```python
import numpy as np
from local_polynomial.loess import loess

# Generate sample data
y_in = np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100)

# Perform LOESS smoothing
# q: number of nearest neighbors (controls smoothness)
# asymmetric: use asymmetric kernel windows
y_smooth = loess(
    y_in=y_in,
    q=15,  # number of neighbors
    asymmetric=False  # symmetric windows
)
```

## API Reference

### `local_polynomial`

Performs local polynomial regression using a triweight kernel.
Does not have C backend yet!

**Parameters:**
- `x_in` (np.array): Input x-coordinates
- `y_in` (np.array): Input y-values
- `x_out` (np.array): Output x-coordinates where predictions are made
- `q` (float): Kernel bandwidth (kernel size)
- `w_in` (np.array, optional): Additional weights for each input point
- `degree` (int, optional): Degree of the local polynomial. Default is 0 (local constant)

**Returns:**
- `np.array`: Predicted y-values at `x_out` points

**Example:**
```python
from local_polynomial.local_polynomial import local_polynomial

y_out = local_polynomial(
    x_in=x_in,
    y_in=y_in,
    x_out=x_out,
    q=0.5,
    w_in=None,
    degree=2  # quadratic local polynomial
)
```

### `loess`

Performs LOESS (Locally Weighted Scatterplot Smoothing) regression using a triweight kernel.

**Parameters:**
- `y_in` (np.array): Input y-values to be smoothed. Must be a 1D array.
- `q` (int): Number of nearest neighbors to use for each local regression. Controls the bandwidth of the smoothing. Must be at least 3. Larger values result in smoother output.
- `asymmetric` (bool, optional): If True, uses asymmetric kernel windows that extend further in one direction. If False, uses symmetric windows. Defaults to False.

**Returns:**
- `np.array`: Smoothed y-values of the same shape as `y_in`. NaN values in input are preserved in output.

**Note:**
This function uses a C implementation for high performance. The algorithm handles NaN values by excluding them from local regressions. If there are fewer than 3 valid (non-NaN) data points, all output values will be NaN and an error will be raised.

**Example:**
```python
from local_polynomial.loess import loess 

y_smooth = loess(
    y_in=y_in,
    q=15,
    asymmetric=False
)
```

## Development

### Building from Source

1. Clone the repository:
```bash
git clone <repository-url>
cd local_polynomial
```

2. Install build dependencies:
```bash
uv sync --dev
```

Thats it you can now play around and modify the package!


### Project Structure

```
local_polynomial/
├── local_polynomial/
│   ├── __init__.py
│   ├── local_polynomial.py      # Main local polynomial function
│   ├── loess.py                 # LOESS smoothing function
│   └── src/
│       ├── internals.py         # Internal helper functions
│       └── C_code/
│           ├── c_loess.c        # C implementation
│           ├── c_loess.h        # C headers
│           ├── c_internals.c    # Internal C functions
│           └── c_internals.h    # Internal C headers
├── tests/
│   └── test.py
├── pyproject.toml
└── README.md
```

## Algorithm Details

### Triweight Kernel

The triweight kernel function is defined as:
- `K(u) = (1 - u³)³` for |u| < 1
- `K(u) = 0` for |u| ≥ 1

This kernel provides smooth, bounded weights for local regression.

### Local Polynomial Regression

For each output point `x_out[i]`:
1. Compute weights using the triweight kernel: `w[j] = K(|x_out[i] - x_in[j]| / q)`
2. Apply additional weights if provided: `w[j] *= w_in[j]`
3. Fit a polynomial of specified degree using weighted least squares
4. Evaluate the polynomial at `x_out[i]` to get the prediction

### LOESS Smoothing

The LOESS algorithm performs local linear regression at each data point:
1. For each point `i`, select the `q` nearest neighbors (excluding NaN values)
2. Compute weights using the triweight kernel based on distance from point `i`
3. Fit a local linear polynomial using weighted least squares
4. Evaluate the polynomial at point `i` to get the smoothed value
5. The `asymmetric` parameter controls whether the kernel window extends symmetrically or asymmetrically around each point

## License

MIT License - see [LICENSE](LICENSE) file for details.

Copyright (c) 2025 TurboVince

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
