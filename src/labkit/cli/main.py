import typer

from labkit.cli import subnet

app = typer.Typer(help="Labkit - homelab toolkit")
app.add_typer(subnet.app, name="subnet")


def main() -> None:
    app()
