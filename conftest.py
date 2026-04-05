import pytest
from src.base_client import BaseClient

@pytest.fixture(scope="session")
def api_client():
    return BaseClient()