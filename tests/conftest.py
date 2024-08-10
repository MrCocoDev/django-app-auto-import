"""
    Dummy conftest.py for auto_import.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import sys
from importlib import reload

import pytest


@pytest.fixture(autouse=True)
def automatic_cleanup():
    """
    Clean up imported modules under test and reset Django so
    that it can set up again.
    """
    from tests.example.example import settings as custom_settings
    reload(custom_settings)

    yield None
    for name in ('tests.example.other.custom', 'tests.example.third.custom', ):
        try:
            sys.modules.pop(name)
        except KeyError:
            ...

    from django.conf import settings
    for k in dir(settings):
        if k.startswith('AUTO_IMPORT'):
            delattr(settings, k)

    for k in dir(settings):
        assert not k.startswith('AUTO_IMPORT')
