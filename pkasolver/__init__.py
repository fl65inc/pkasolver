"""
pkasolver
toolset for predicting the pka values of small molecules
"""

# Add imports here
from .pkasolver import *
from .dimorphite_dl.dimorphite_dl import run_with_mol_list

# Static version
__version__ = "1.0.0"

import logging

# format logging message
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)1s()] %(message)s"
# set logging level
logging.basicConfig(format=FORMAT, datefmt="%d-%m-%Y:%H:%M", level=logging.INFO)
