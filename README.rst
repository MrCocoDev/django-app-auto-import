.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/django-app-auto-import.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/django-app-auto-import
    .. image:: https://readthedocs.org/projects/django-app-auto-import/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://django-app-auto-import.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/django-app-auto-import/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/django-app-auto-import
    .. image:: https://img.shields.io/pypi/v/django-app-auto-import.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/django-app-auto-import/
    .. image:: https://img.shields.io/conda/vn/conda-forge/django-app-auto-import.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/django-app-auto-import
    .. image:: https://pepy.tech/badge/django-app-auto-import/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/django-app-auto-import
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/django-app-auto-import

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/
.. image:: https://img.shields.io/pypi/v/django-app-auto-import.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/django-app-auto-import/
.. image:: https://github.com/mrcocodev/django-app-auto-import/actions/workflows/ci.yml/badge.svg?branch=main
    :alt: GitHub Test CI
    :target: https://github.com/mrcocodev/django-app-auto-import/actions/workflows/ci.yml
.. image:: https://pepy.tech/badge/django-app-auto-import/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/django-app-auto-import

|

======================
django-app-auto-import
======================


    Auto import a module from all yours apps!


Quick Start
===========

::

    # my.project.settings.py
    INSTALLED_APPS = [
        ...,
        'cocodev.django.auto_import',
        ...,
    ]
    AUTO_IMPORT = 'startup'  # Automatically imports `startup.py` in all apps

This is a pretty simple library so there is not much more to it.

Preventing Unwanted Code Execution
==================================

Through an allow listing:

::

    # my.project.settings.py
    AUTO_IMPORT = 'startup'  # Automatically imports `startup.py` in all apps
    AUTO_IMPORT_ALLOW_LIST = [
        'my.project.app.name',  # Will only import `my.project.app.name.startup`
    ]

Through a block list:

::

    # my.project.settings.py
    AUTO_IMPORT = 'startup'  # Automatically imports `startup.py` in all apps
    AUTO_IMPORT_BLOCK_LIST = [
        'my.project.app.name',  # Won't import `my.project.app.name.startup`
    ]

.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd django-app-auto-import
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.

.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
