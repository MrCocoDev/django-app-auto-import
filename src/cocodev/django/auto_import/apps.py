import logging
from importlib import import_module
from typing import List

from django.apps import AppConfig, apps
from django.conf import settings

log = logging.getLogger(__name__)


class AutoImportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cocodev.django.auto_import'

    def ready(self):
        try:
            app_settings = settings.AUTO_IMPORT
        except AttributeError as e:
            log.debug("No AUTO_IMPORT setting configured, exiting early... %s", e)
            return

        if isinstance(app_settings, str):
            load_module(apps.get_app_configs(), app_settings)
        else:
            try:
                list_of_modules = [module for module in app_settings]
            except TypeError:
                ...
            else:
                for module in list_of_modules:
                    load_module(apps.get_app_configs(), module)


def load_module(app_import_list: List[AppConfig], module_name, /):
    for app in app_import_list:
        import_path = f"{app.name}.{module_name}"

        try:
            log.debug(f"Auto-loading %s", import_path)
            import_module(import_path)
        except ModuleNotFoundError:
            log.debug("Could not load %s", import_path)
