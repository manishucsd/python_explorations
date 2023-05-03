import argparse

class CustomArgumentParser(argparse.ArgumentParser):
    def parse_args(self):
        print("CustomArgumentParser.parse_args()    args: ", args)  
        args, remaining_args = self.parse_known_args()
        if args.help:
            if args.op_kind == "matmul":
                self.matmul_parser.print_help()
            elif args.op_kind == "conv":
                self.conv_parser.print_help()
            else:
                self.print_help()
            exit(0)
        return args, remaining_args

def add_common_arguments(parser):
    """Adds common arguments to the parser."""
    parser.add_argument("--build-dir", default=".", \
                        help="IREE top-level build directory is used to generate "\
                            "operations and npy files.This should be same that used "\
                            "to call generated.py")
    
    parser.add_argument("--verbose", default='False', \
                        help='Prints verbose output and commands executed.')
    

def add_generator_arguments(parser):
    """Adds generator related arguments to the parser."""
    generator_parser = parser.add_argument_group('Generator', 'Generator related options.')

    generator_parser.add_argument("--dispatches", default='', help="Comma delimited list to "\
                        "filter dispatches by name. A dispatch is a combination of "\
                        "operation and tuning configuration.")
    generator_parser.add_argument("--mlir-dialect",
                        default='linalg',
                        help='MLIR dialect entry "\
                        "point at which operation is emitter. For example, "\
                        "linalg*, mhlo, etc.')

def add_compilation_arguments(parser):
    """Adds compilation related arguments to the parser."""
    compilation_parser = parser.add_argument_group('Compilation', 'Compilation related options.')

    compilation_parser.add_argument("--force-compile", default='False', \
                        type=str, help="Force re-compilation of the operation even "\
                        "if .vmfb file is present.")
    compilation_parser.add_argument("--compile-only", default='False', \
                        type=str, help="Compiles the operation "\
                            "without running verification and profiling.")

def add_verification_arguments(parser):
    """Adds verification related arguments to the parser."""
    verification_parser = parser.add_argument_group('Verification', 'Verification related options.')

    verification_parser.add_argument("--verification-enabled", "--verify", default='True', \
                        type=str, help="Verify the operation.")

    verification_parser.add_argument("--verification-providers", default='numpy', \
                        type=str, help="Comma delimited list of verification providers.")


def add_profiling_arguments(parser):
    """Adds profiling related arguments to the parser."""
    profiling_parser = parser.add_argument_group('Profiling', 'Profiling related command line arguments.')

    profiling_parser.add_argument("--profiling-enabled", "--benchmark", default='True', \
                        type=str, help="Benchmark the operation.")
    profiling_parser.add_argument('--batch-size', '--benchmark-dispatch-repeat-count', \
                        default=100, help="Number of times dispatch is launched "\
                            "in a loop to amortize the launch overhead.")
    profiling_parser.add_argument("--benchmark-repetitions", default=5,
                        type=int, help="Number of times benchmark is repeated "\
                        "and min, max, median, and average runtimes/gflops are "\
                        "reported.")