import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()

@app.command(short_help='adds an item')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")

@app.command()
def show():
    tasks = [("Todo1", "Study"), ("Todo2", "Sports")]
    console.print("[bold magenta]Todos[/bold magenta]!", "_")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

if __name__ == "__main__":
    app()