# import threading
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

def show_status(config: dict):
    console = Console()
    title = Text("🚀 Auto Clicker Configs !", style="bold magenta", justify="center")
    panel = Panel.fit(title, border_style="bright_magenta", padding=(1, 4))
    table = Table(show_header=False, show_lines=False, padding=(1, 5))
    
    table.add_row("[bold green]Toggle Key[/]", config["toggle_key"])
    table.add_row("[bold red]Exit Key[/]", config["exit_key"])
    table.add_row("[bold cyan]Click Button[/]", config["button"])
    table.add_row("[bold yellow]Interval[/]", f"{config['interval']} sec")

    print("")
    console.print(Panel(table, title=title, expand=False))
    print("")
