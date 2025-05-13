import pytest
from themis import App


@pytest.fixture
def app() -> App:
    """Create a test app"""
    return App()


def test_add_1(app: App):
    """Tests the add functionality of the app"""
    result = app.add(1, 1)
    assert result == 2


def test_add_2(app: App):
    """Tests the add functionality of the app"""
    result = app.add(0, 0)
    assert result == 0


def test_add_3(app: App):
    """Tests the add functionality of the app"""
    result = app.add(-1, 1)
    assert result == 0
