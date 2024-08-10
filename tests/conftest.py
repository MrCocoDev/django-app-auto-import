"""
    Dummy conftest.py for auto_import.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import sys

import pytest
from django.apps import apps


@pytest.fixture(autouse=True)
def automatic_cleanup():
    """
    Clean up imported modules under test and reset Django so
    that it can set up again.
    """
    yield None
    for name in ('tests.example.other.custom', 'tests.example.third.custom'):
        try:
            sys.modules.pop(name)
        except KeyError:
            ...

    # Trick Django into setting up again, maybe a little unpredictable
    apps.ready = False
    apps.loading = False
    apps.app_configs = {}
