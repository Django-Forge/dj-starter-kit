import typer
import os
from pathlib import Path
from rich import print
from rich.prompt import Prompt
from rich.console import Console

app = typer.Typer()


def scratch_based_project():
    """
    Scaffold a new Django project.
    """
    print("Welcome to the scratch-based project setup!")


def template_based_project():
    project_name = typer.prompt("Enter the name of your project", default="my_project")
    while True:
        project_name = typer.prompt(
            "Enter the name of your project (must be a valid Django project name)",
            default="my_project",
        )
        if project_name.isidentifier():
            break
        print("[red]Invalid project name![/red] The name must be a valid Python identifier.")

    project_path = typer.prompt(
        "Enter the path where you want to create the project",
        default=str(Path.home() / project_name),
    )

    # Resolve the path to handle ., .., or ../../../ dynamically
    resolved_path = Path(project_path).expanduser().resolve()

    print(f"Creating project '{project_name}' at '{resolved_path}'...")

@app.command()
def wizard():
    """
    A simple wizard command to guide the user through multiple steps.
    """
    console = Console()
    console.print("Welcome to the wizard! :smiley:")

    project_type = Prompt.ask(
        "What type of project would you like to create?",
        choices=["template", "scratch"],
        default="template",
    )
    console.print(f"You selected: [bold]{project_type}[/bold] project type.")

    if project_type == "template":
        template_based_project()
    elif project_type == "scratch":
        scratch_based_project()
    else:
        console.print("[red]Invalid project type selected![/red]")
        raise typer.Exit(code=1)

    console.print("Wizard completed successfully!")
