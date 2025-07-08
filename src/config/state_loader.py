from src.config.load import load_configs
from src.core.state import state
from src.config.constants import CONFIGS_PATH
from logging import exception

def load_state_from_configs() -> None:
    data = load_configs(CONFIGS_PATH)
    try:
        state.set_data_from_dict(data)
    except TypeError:
        exception("[bold red]TypeError[/] from [bold cyan]set_data_from_dict[/]")
    except KeyError as ke:
        exception(f"[bold red]Missing config key[/]: [bold cyan]{ke}[/]")
    except AttributeError as ae:
        exception(f"[bold red]AttributeError[/]: [bold cyan]{ae}[/]")
    except ValueError as ve:
        exception(f"[bold red]ValueError[/]: [bold cyan]{ve}[/]")
