from textual.app import App
from src.core.app_state.state import State

def switch_to_menu(app: App, state: State) -> None:
    from src.screens.menu import MenuScreen
    app.pop_screen()
    app.push_screen(MenuScreen(state))