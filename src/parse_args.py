import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Auto Clicker CLI")
    parser.add_argument("--toggle-key", default="f6")
    parser.add_argument("--exit-key", default="f8")
    parser.add_argument("--interval", type=float, default=10.0)
    parser.add_argument("--button", choices=["left", "right", "middle"], default="left")
    return parser.parse_args()
