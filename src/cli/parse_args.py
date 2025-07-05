from argparse import Namespace, ArgumentParser

def parse_args() -> Namespace:
    """
    Argument parser for the Auto Clicker CLI.

    Defines subcommands (`set`, `status`, `start`) and global flags like `--debug`.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """

    parser = ArgumentParser(
        description="Auto Clicker CLI Tool",
        epilog="Developed by Haruji23"
        )
    parser.add_argument("-d","--debug", action="store_true", help="Enable debug logging")
    subparsers = parser.add_subparsers(dest="command", required=False)

    # config
    set_parser = subparsers.add_parser("set", help="Set manually, Load from JSON file, or reset Configs to default")
    # set_parser.set_defaults(command="set")
    set_parser.add_argument("-j","--json", help="Path to JSON configs file", required=False, metavar="JSON")
    set_parser.add_argument("-t","--toggle-key", type=str, required=False,default="f6", help="Set the Toggle Key", metavar="KEY")
    set_parser.add_argument("-e","--exit-key", type=str, required=False, default="f8", help="Set the Exit Key", metavar="KEY")
    set_parser.add_argument("-i","--interval", type=float, required=False, default=60.0, help="Set the Interval Timer", metavar="TIME(in sec)")
    set_parser.add_argument("-b","--button", choices=["left", "right", "middle"], required=False, default="right", help="Set the Mouse Button", metavar="MOUSE")
    set_parser.add_argument("-r","--reset", action="store_true", help="Reset to Default configs", required=False)

    # start
    start_parser = subparsers.add_parser("start", help="Start auto-clicker")
    # start_parser.set_defaults(command="start")

    # status
    status_parser = subparsers.add_parser("status", help="Show configs")
    # status_parser.set_defaults(command="status")

    return parser.parse_args()
