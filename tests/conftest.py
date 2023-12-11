from collections.abc import Generator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from typer import Typer

from tests.example_app import wheke
from wheke_auth.settings import settings


@pytest.fixture
def client(tmp_path: Path) -> Generator[TestClient, None, None]:
    previous_db_path = settings.auth_db
    settings.auth_db = str(tmp_path / "auth.db")

    yield TestClient(wheke.create_app())

    settings.auth_db = previous_db_path


@pytest.fixture
def cli() -> Typer:
    return wheke.create_cli()
