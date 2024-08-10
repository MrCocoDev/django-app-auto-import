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
            target_module = settings.AUTO_IMPORT
        except AttributeError as e:
            log.debug("No AUTO_IMPORT setting configured, exiting early... %s", e)
            return

        try:
            allow_list = settings.AUTO_IMPORT_ALLOW_LIST
        except AttributeError:
            allow_list = None
            log.debug("No AUTO_IMPORT_ALLOW_LIST setting configured")

        try:
            block_list = settings.AUTO_IMPORT_BLOCK_LIST
        except AttributeError:
            block_list = None
            log.debug("No AUTO_IMPORT_BLOCK_LIST setting configured")

        if isinstance(target_module, str):
            load_module(
                apps.get_app_configs(),
                target_module,
                allow_list=allow_list,
                block_list=block_list,
            )
        else:
            try:
                list_of_modules = [module for module in target_module]
            except TypeError:
                ...
            else:
                for module in list_of_modules:
                    load_module(
                        apps.get_app_configs(),
                        module,
                        allow_list=allow_list,
                        block_list=block_list,
                    )


def load_module(app_import_list: List[AppConfig], module_name, /, allow_list, block_list):
    for app in app_import_list:
        import_path = f"{app.name}.{module_name}"

        if allow_list and app.name not in allow_list:
            continue
        if block_list and app.name in block_list:
            continue

        try:
            log.debug("Auto-loading %s", import_path)
            import_module(import_path)
        except ModuleNotFoundError:
            log.debug("Could not load %s", import_path)
        else:
            print(f"Auto-loaded {import_path}",)
