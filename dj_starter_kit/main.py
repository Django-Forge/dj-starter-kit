import typer

app = typer.Typer(name="dj_starter_kit")


@app.command()
def start_project():
    print("Yooo!!!")


if __name__ == "__main__":
    app()
