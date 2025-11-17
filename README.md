# local-polynomial

Fast Local Polynomial regression functions implemented in Python with Cython/C extensions for high performance.

## Features

- **Local Polynomial Regression**: Flexible polynomial degree support with customizable kernel bandwidth
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

## API Reference

### `local_polynomial`

Performs local polynomial regression using a triweight kernel.

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
y_out = local_polynomial(
    x_in=x_in,
    y_in=y_in,
    x_out=x_out,
    q=0.5,
    w_in=None,
    degree=2  # quadratic local polynomial
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

3. Build the package:
```bash
uv build
```

### Project Structure

```
local_polynomial/
├── local_polynomial/
│   ├── __init__.py
│   ├── local_polynomial.py      # Main local polynomial function
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

## License

MIT License - see [LICENSE](LICENSE) file for details.

Copyright (c) 2025 TurboVince

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
