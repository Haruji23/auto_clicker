from argparse import ArgumentParser, Namespace

def parse_args() -> Namespace:
    parser = ArgumentParser(description="Auto Clicker CLI")
    parser.add_argument("-d","--debug", action="store_true", help="Enable debug logging")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # config
    config_parser = subparsers.add_parser("set", help="Set manually, Load from JSON file, or reset Configs to default")
    config_parser.add_argument("-j","--json", help="Path to JSON configs file", required=False, metavar="JSON")
    config_parser.add_argument("-t","--toggle-key", type=str, required=False,default="f6", help="Set the Toggle Key", metavar="KEY")
    config_parser.add_argument("-e","--exit-key", type=str, required=False, default="f8", help="Set the Exit Key", metavar="KEY")
    config_parser.add_argument("-i","--interval", type=float, required=False, default=60.0, help="Set the Interval Timer", metavar="TIME(in sec)")
    config_parser.add_argument("-b","--button", choices=["left", "right", "middle"], required=False, default="right", help="Set the Mouse Button", metavar="MOUSE")
    config_parser.add_argument("-r","--reset", action="store_true", help="Reset to Default configs", required=False)

    # start
    subparsers.add_parser("start", help="Start auto-clicker")

    # status
    subparsers.add_parser("status", help="Show configs")

    return parser.parse_args()
