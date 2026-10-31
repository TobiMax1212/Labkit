import typer

app = typer.Typer(help="Subnet calculator")


@app.callback(invoke_without_command=True)
def calc(network: str) -> None:
    typer.echo(f"TODO: calculate {network}")
