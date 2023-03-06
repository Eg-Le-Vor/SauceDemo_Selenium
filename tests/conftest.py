import pytest


@pytest.fixture()
def set_up():
    print('\n\nНачало теста.\n')
    yield
    print('\nКонец теста.')

@pytest.fixture(scope="module")
def set_group():
    print('\nВход в систему.')
    yield
    print('\nВыход из системы.')