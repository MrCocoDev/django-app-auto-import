import os
import sys

import pytest


def test_auto_import_with_submodule_name():
    assert "tests.example.other.custom" not in sys.modules
    assert "tests.example.third.custom" not in sys.modules

    from tests.example.example import settings as custom_settings
    custom_settings.AUTO_IMPORT = 'custom'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', custom_settings.__name__)

    import django
    django.setup()

    imported_modules = sys.modules
    assert "tests.example.other.custom" in imported_modules
    assert "tests.example.third.custom" in imported_modules


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

    from tests.example.example import settings as custom_settings
    custom_settings.AUTO_IMPORT = value

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', custom_settings.__name__)

    import django
    django.setup()

    imported_modules = sys.modules
    assert "tests.example.other.custom" in imported_modules
    assert "tests.example.third.custom" in imported_modules
