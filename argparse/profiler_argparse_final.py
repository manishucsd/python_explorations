import argparse
from options import *
from matmul import add_matmul_args
from conv import add_conv_args


parser = argparse.ArgumentParser(add_help=False, description="Profiling tool for matmul and convolution operations.")
add_common_arguments(parser)

parser.add_argument("--op-kind", dest="op_kind", default='all', choices=["all", "matmul", "conv"], help="Operation kind")
parser.add_argument("--help", action='store_true', help="Show help message and exit")

# Add operation-specific arguments with help messages
matmul_parser = argparse.ArgumentParser(add_help=False, description="Matrix multiplication profiling options")
add_matmul_args(matmul_parser)

conv_parser = argparse.ArgumentParser(add_help=False, description="Convolution profiling options")
add_conv_args(conv_parser)

# Parse the arguments without operation-specific arguments first
args, remaining_args = parser.parse_known_args()

# Add operation-specific arguments based on the op_kind value
operation_args = argparse.Namespace()
if args.op_kind == "matmul":
    operation_args = matmul_parser.parse_args(remaining_args)
elif args.op_kind == "conv":
    operation_args = conv_parser.parse_args(remaining_args)


# Combine the main and operation-specific arguments
args = argparse.Namespace(**vars(args), **vars(operation_args))

# Print the arguments
print(args)

# Display help message and exit if --help is specified
if args.help:
    if args.op_kind == "matmul":
        matmul_parser.print_help()
    elif args.op_kind == "conv":
        conv_parser.print_help()
    else:
        parser.print_help()
    exit(0)


# Process the arguments based on the selected operation
if args.op_kind == "matmul":
    print(f"Profiling matmul with M: {args.m}, N: {args.n}, K: {args.k}")
elif args.op_kind == "conv":
    print(f"Profiling conv with N: {args.conv_n}, H: {args.conv_h}, W: {args.conv_w}, C: {args.conv_c}, K: {args.conv_k}, R: {args.conv_r}, S: {args.conv_s}")
else:
    print(f"Profiling all operations")
