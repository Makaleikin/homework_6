import pytest
import os

file_path = os.path.abspath('./resources/test.zip')


@pytest.fixture(scope='session', autouse=True)
def delete_zip():
    if os.path.exists(file_path):
        os.remove(file_path)
    yield
    os.remove(file_path)
