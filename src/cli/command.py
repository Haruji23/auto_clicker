from logging import info, debug
from utils import setup_logger
from core.state import State
from cli.parse_args import parse_args
from cli.status_display import show_status
from config.load_save_reset_configs import load_configs, save_configs, reset_configs, check_configs
from config.constants import CONFIGS_PATH
from core.start_operation import start_auto_clicker

def command():
    """
    Main entry point for the Auto Clicker CLI program.

    This function handles the high-level control flow for the three CLI subcommands:
    - `set`: Allows the user to configure toggle/exit keys, click interval, and mouse button,
             either via manual arguments or JSON config file. Supports resetting to defaults.
    - `status`: Displays the current config in a stylized console format.
    - `start`: Loads config, displays current state, and launches the auto-clicker loop.

    It also initializes the logger before parsing the command-line arguments.
    The logging level is dynamically adjusted for the `start` command via the `--debug` flag.
    """

    # Initialize a state of program (data pool)
    state = State()
    
    # Parse all CLI arguments into the `args` namespace
    args = parse_args()

    # Enable debug mode logger if --debug flag is set
    setup_logger(debug_mode=args.debug)

    # --- Handle `set` command ---
    if args.command == "set":
        
        # If user requests --reset → reset all configs to default values
        if args.reset:  
            reset_configs()
        else:
            config = {}
            if args.json:
                
                # Load configs from specified JSON file and update global state
                state.set_data_from_dict(load_configs(args.json))
                debug(f"Configurations dict in State : {state.to_dict()}")
                config = state.to_show_dict()
                debug(f"Configurations dict for JSON : {config}")
            else:
                
                # Manually parse values from CLI args into a config dictionary
                for key in ["toggle_key", "exit_key", "button", "interval"]:
                    value = getattr(args, key)
                    if value is not None:
                        config[key] = value
                debug(f"Configurations dict by manually input: {check_configs(config=config)}")
            # Save config to file and confirm via log message
            save_configs(config)
            info("[green]Configs saved !!!")

    # --- Handle `status` command ---
    elif args.command == "status":
        
        # Load saved configs from disk and display them (formatted with color/styling)
        loaded_configs = load_configs(CONFIGS_PATH)
        info("[green]Loaded configs complete !!!")
        show_status(loaded_configs)

    # --- Handle `start` command ---
    elif args.command == "start":
        
        # Load saved configs and update app state
        loaded_configs = load_configs(CONFIGS_PATH)
        info("[green]Loaded configs complete !!!")
        state.set_data_from_dict(loaded_configs)
        info("Set configs to the state.")
        
        # Show startup summary to the user
        show_status(state.to_show_dict())

        # Launch main auto clicker logic (threads, listener, etc.)
        start_auto_clicker(state)
