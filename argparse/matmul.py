import enum
import os.path
import shutil


###############################################################################
def add_matmul_args(matmul_parser):
  matmul_parser.add_argument('--m, --problem-m', dest="m", default='', type=str)
  matmul_parser.add_argument('--n, --problem-n', dest="n", default='', type=str)
  matmul_parser.add_argument('--k, --problem-k', dest="k", default='', type=str)
  
  matmul_parser.add_argument('--tile-m', dest="cta_m", default='', type=str)
  matmul_parser.add_argument('--tile-n', dest="cta_n", default='', type=str)
  matmul_parser.add_argument('--tile-k', dest="cta_k", default='', type=str)
###############################################################################

