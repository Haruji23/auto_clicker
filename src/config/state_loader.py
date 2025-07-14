from src.config.load import load_configs
from src.core.app_state.state import state
from src.config.constants import CONFIGS_PATH
from logging import exception

def load_state_from_configs() -> None:
    data = load_configs(CONFIGS_PATH)
    try:
        state.set_data_from_dict(data)
    except TypeError:
        exception("TypeError from set_data_from_dict")
    except KeyError as ke:
        exception(f"Missing config key: {ke}")
    except AttributeError as ae:
        exception(f"AttributeError: {ae}")
    except ValueError as ve:
        exception(f"ValueError: {ve}")
