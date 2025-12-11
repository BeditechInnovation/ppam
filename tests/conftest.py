import pytest

@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    # Prevent tests from actually calling pip over the network.
    monkeypatch.setenv("PIP_DISABLE_PIP_VERSION_CHECK", "1")