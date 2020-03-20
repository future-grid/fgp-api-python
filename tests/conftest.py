import pytest
import fgp


@pytest.fixture(scope='session')
def client():
    return fgp.ApiClient(url='http://localhost:8082', application='ada')

