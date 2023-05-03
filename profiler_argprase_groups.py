from matmul import *
from options import *

if __name__ == "__main__":
  ###############################################################################
  # Parse command line arguments
  ###############################################################################
  parser = CustomArgumentParser(description="IREE Python profiler tool for "\
                                   "verifcation and performance profiling tool "\
                                    "for IREE-compiled MLIR operations.")
  ###############################################################################
  # Subparser based on operation kind
  parser.add_argument("--op-kind, --operation-kind", dest="op_kind", \
    default='matmul', choices=['matmul', 'conv'], help='Operation kind: matmul or conv')
  parser.add_argument("--help", action="store_true", help="Show this help message and exit")


  #op_kind_parser = parser.add_subparsers(dest='op_kind', \
  #                                       help='Operation kind to profile.')
  #
  #matmul_parser = op_kind_parser.add_parser('matmul', help='Profile matmul operation C = A * B.')
  #conv2d_parser = op_kind_parser.add_parser('conv2d', help='Profile conv2d operation Output = fprop(Activation * Weight).')

  #add_matmul_args(matmul_parser)
  ################################################################################

  add_common_arguments(parser)
  add_generator_arguments(parser)
  add_compilation_arguments(parser)
  add_verification_arguments(parser)
  add_profiling_arguments(parser)




  matmul_parser =  CustomArgumentParser(add_help=False)
  add_matmul_args(matmul_parser)
  parser.matmul_parser = matmul_parser
  

  ###############################################################################
  args, remaining_args = parser.parse_args()
  ###############################################################################
  
  print(args)

  if args.op_kind == "matmul":
    op_args = matmul_parser.parse_args(remaining_args)

  args = argparse.Namespace(**vars(args), **vars(op_args))



  print(args)
