import sys

import pytest


def test_auto_import_with_submodule_name():
    assert "tests.example.other.custom" not in sys.modules
    assert "tests.example.third.custom" not in sys.modules

    from django.conf import settings
    settings.AUTO_IMPORT = 'custom'

    from django.apps import apps
    apps.get_app_config('auto_import').ready()

    imported_modules = sys.modules
    assert "tests.example.other.custom" in imported_modules
    assert "tests.example.third.custom" in imported_modules


def test_auto_import_with_submodule_name_with_allow_list():
    assert "tests.example.other.custom" not in sys.modules
    assert "tests.example.third.custom" not in sys.modules

    from django.conf import settings
    settings.AUTO_IMPORT = 'custom'
    settings.AUTO_IMPORT_ALLOW_LIST = {'tests.example.other', }

    from django.apps import apps
    apps.get_app_config('auto_import').ready()

    imported_modules = sys.modules
    assert "tests.example.other.custom" in imported_modules
    assert "tests.example.third.custom" not in imported_modules


def test_auto_import_with_submodule_name_with_block_list():
    assert "tests.example.other.custom" not in sys.modules
    assert "tests.example.third.custom" not in sys.modules

    from django.conf import settings
    settings.AUTO_IMPORT = 'custom'
    settings.AUTO_IMPORT_BLOCK_LIST = {'tests.example.third', }

    from django.apps import apps
    apps.get_app_config('auto_import').ready()

    imported_modules = sys.modules
    assert "tests.example.other.custom" in imported_modules
    assert "tests.example.third.custom" not in imported_modules


@pytest.mark.parametrize(
    "value",
    [
        ['custom', ],
        ('custom', ),
        {'custom', },
    ]
)
def test_auto_import_with_list_of_submodule_names(value):
    assert "tests.example.other.custom" not in sys.modules
    assert "tests.example.third.custom" not in sys.modules

    from django.conf import settings
    settings.AUTO_IMPORT = value

    from django.apps import apps
    apps.get_app_config('auto_import').ready()

    imported_modules = sys.modules
    assert "tests.example.other.custom" in imported_modules
    assert "tests.example.third.custom" in imported_modules
