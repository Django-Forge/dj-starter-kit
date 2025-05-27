import typer
import subprocess
from pathlib import Path

app = typer.Typer()

@app.command()
def project(name: str):
    """
    Scaffold a new Django project.
    """
    typer.echo(f"Creating project: {name}")
    subprocess.run(["django-admin", "startproject", name])
    typer.echo(f"✅ Project '{name}' created successfully!")
