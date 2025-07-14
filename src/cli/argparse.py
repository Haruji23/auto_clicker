from argparse import ArgumentParser, Namespace

def create_parser() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-d", "--dev", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    return args