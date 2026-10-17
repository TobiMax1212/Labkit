import labkit


def test_package_imports() -> None:
    assert labkit is not None


def test_main_runs(capsys) -> None:
    labkit.main()
    output = capsys.readouterr().out
    assert "labkit" in output
