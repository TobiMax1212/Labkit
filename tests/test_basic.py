from typer.testing import CliRunner

from labkit.cli.main import app

runner = CliRunner()


def test_help_runs() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "subnet" in result.output


def test_subnet_command_runs() -> None:
    result = runner.invoke(app, ["subnet", "192.168.1.0/24"])
    assert result.exit_code == 0
