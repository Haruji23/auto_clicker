from src.config.state_loader import load_state_from_configs
from src.core.logger.setup_logger import setup_logger
from src.core.app_state.state import state
from src.app import AutoClickerApp
from logging import debug
from src.cli.argparse import create_parser

args = create_parser()
setup_logger(debug_mode=args.dev) # initialize logger
load_state_from_configs() # fill state object

debug(f"State: {state.app_state_dict()}")

if __name__ == "__main__":
    app = AutoClickerApp(state=state)
    app.run()