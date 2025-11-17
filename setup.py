import os
from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

cython_dir = os.path.join("local_polynomial", "src")

extensions = [
	Extension(
		"local_polynomial.loess",
		[
			os.path.join(cython_dir, "loess.pyx"),
			os.path.join(cython_dir, "C_code", "c_loess.c"),
			os.path.join(cython_dir, "C_code", "c_internals.c"),
		],
		include_dirs=[np.get_include(), cython_dir]
	)
]

setup(
	ext_modules=cythonize(
		extensions,
		include_path=[cython_dir],
		annotate=False,
		language_level=3
	)
)