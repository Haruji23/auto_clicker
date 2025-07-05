from logging import info, debug, error
from utils import setup_logger
from core.state import State
from cli.parse_args import parse_args
from cli.status_display import show_status
from config.load import load_configs
from config.save import save_configs
from config.reset import reset_configs
from config.validate import check_configs
from config.constants import CONFIGS_PATH
from core.start_operation import start_auto_clicker

def command():
    """
    This function handles the high-level control flow for all supported CLI subcommands:
    - `set`    : Configure toggle/exit keys, click interval, and mouse button
                via manual input or config file. Supports resetting to defaults.
    - `status` : Display the current configuration in a stylized format.
    - `start`  : Launch the auto-clicker loop using the saved config state.

    It also initializes the logger immediately after parsing arguments. The `--debug` flag is
    available for all subcommands and enables verbose logging for development or troubleshooting.

    Raises:
        SystemExit: If invalid arguments are provided.
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
    elif args.command == "start" or args.command is None:
        
        # Load saved configs and update app state
        loaded_configs = load_configs(CONFIGS_PATH)
        info("[green]Loaded configs complete !!![/]")
        state.set_data_from_dict(loaded_configs)
        debug("Set configs to the state.")
        
        # Show startup summary to the user
        show_status(state.to_show_dict())
        info("[bold magenta]Keyboard Listener[/]'s [green]Ready !!![/]")

        # Launch main auto clicker logic (threads, listener, etc.)
        start_auto_clicker(state)
