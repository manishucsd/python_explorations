import enum
import os.path
import shutil


###############################################################################
def add_conv_args(conv_parser):
  conv_parser.add_argument('--conv-n', '--conv_n', dest="conv_n", default='', type=str)
  conv_parser.add_argument('--conv-h', '--conv_h', dest="conv_h", default='', type=str)
  conv_parser.add_argument('--conv-w', '--conv_w', dest="conv_w", default='', type=str)
  conv_parser.add_argument('--conv-c', '--conv_c', dest="conv_c", default='', type=str)
  conv_parser.add_argument('--conv-k', '--conv_k', dest="conv_k", default='', type=str)
  conv_parser.add_argument('--conv-p', '--conv_p', dest="conv_p", default='', type=str)
  conv_parser.add_argument('--conv-q', '--conv_q', dest="conv_q", default='', type=str)
  conv_parser.add_argument('--conv-r', '--conv_r', dest="conv_r", default='', type=str)
  conv_parser.add_argument('--conv-s', '--conv_s', dest="conv_s", default='', type=str)
###############################################################################

