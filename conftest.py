import pytest

@pytest.fixture(scope="class", autouse=False)
def print_fixture_use():
    print("fxture wurde aufgerufen")

