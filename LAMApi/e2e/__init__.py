from e2e.config import Config

import pytest
import pathlib
import os.path

parent = pathlib.Path(__file__).parent.absolute()
config_path = os.path.join(parent, 'config.json')
config = Config(config_path)

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = driver_path
    return chrome_options
