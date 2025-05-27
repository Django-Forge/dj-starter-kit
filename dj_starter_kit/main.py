import typer
from dj_starter_kit import commands

app = typer.Typer(name="dj_starter_kit")

app.add_typer(commands.wizard.app)

if __name__ == "__main__":
    app()