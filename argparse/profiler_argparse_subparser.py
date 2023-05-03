import argparse

def main():
    # Create a top-level parser
    parser = argparse.ArgumentParser(description="Python Profiler Tool")
    parser.add_argument('--build_dir', type=str, help="Build directory")

    # Create subparsers for each op_kind
    subparsers = parser.add_subparsers(dest="op_kind", help="Operation kind")

    matmul_parser = subparsers.add_parser('all', help="All operations")

    # Create a subparser for matmul
    matmul_parser = subparsers.add_parser('matmul', help="Matrix multiplication operation")
    matmul_parser.add_argument('-m', type=int, help="Matrix M dimension")
    matmul_parser.add_argument('-n', type=int, help="Matrix N dimension")
    matmul_parser.add_argument('-k', type=int, help="Matrix K dimension")

    # Create a subparser for conv
    conv_parser = subparsers.add_parser('conv', help="Convolution operation")
    conv_parser.add_argument('-n', type=int, help="Number of input feature maps")
    conv_parser.add_argument('-w', type=int, help="Width of the input feature maps")
    conv_parser.add_argument('-c', type=int, help="Number of output feature maps")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the appropriate function based on the op_kind
    if args.op_kind == "matmul":
        # Call the matmul function with the specific arguments
        pass
    elif args.op_kind == "conv":
        # Call the conv function with the specific arguments
        pass
    elif args.op_kind == "all":
        # Call the matmul function with the specific arguments
        pass
    else:
        parser.print_help()
        exit(1)
    print(args)

if __name__ == "__main__":
    main()
