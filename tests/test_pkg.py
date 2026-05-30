import pytest

@pytest.fixture
def simple_fixture():
    return 5

def test_stupid_function(simple_fixture):
    assert simple_fixture == 5
