import os
from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
include_dirs = [np.get_include()]
