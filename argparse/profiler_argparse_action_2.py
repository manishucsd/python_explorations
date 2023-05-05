import argparse

class OpKindAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print(f"OpKindAction: {values}")
        if values == "matmul":
            #namespace.operation = "matmul"
            parser.add_argument("--m", default='512', help="Matrix A's number of rows")
            parser.add_argument("--n", default='128', help="Matrix B's number of columns")
            parser.add_argument("--k", default='1024', help="Matrix A's number of columns and Matrix B's number of rows")
        elif values == "conv2d":
            #namespace.operation = "conv2d"
            parser.add_argument("--r", default='3', help="Height of the kernel")
            parser.add_argument("--s", default='3', help="Width of the kernel")
            parser.add_argument("--c", default='64', help="Number of input channels")

def main():
    parser = argparse.ArgumentParser(description="Profiler tool for matmul and conv2d operations")
    parser.add_argument("--build_dir", default=".", help="Directory to store build files (default: current directory)")
    parser.add_argument("--op-kind", action=OpKindAction, choices=["matmul", "conv2d"], default="matmul", help="Operation kind (default: matmul)")

    # Parse command line arguments
    args = parser.parse_args()
    
    '''
    # Further processing based on parsed arguments
    if args.operation == "matmul":
        print("Profiling matmul with m={}, n={}, k={}".format(args.m, args.n, args.k))
    elif args.operation == "conv2d":
        print("Profiling conv2d with r={}, s={}, c={}".format(args.r, args.s, args.c))
    '''

    print(args)
if __name__ == "__main__":
    main()
