"""
Non-init module for doing convenient * imports from.
"""

# core
from confab.conffiles import ConfFiles, iterconffiles

# settings
from confab.definitions import Settings

# environment tasks
from confab.autotasks import generate_tasks

# jinja2 environment loading
from confab.loaders import FileSystemEnvironmentLoader, PackageEnvironmentLoader

# data loading
from confab.data import DataLoader

# options
from confab.options import assume_yes, Options

# fabric tasks
from confab.diff import diff
from confab.generate import generate
from confab.pull import pull
from confab.push import push

__ignore__ = [
    assume_yes,
    generate_tasks,
    ConfFiles,
    FileSystemEnvironmentLoader,
    PackageEnvironmentLoader,
    DataLoader,
    diff,
    generate,
    iterconffiles,
    pull,
    push,
    Options,
    Settings,
]
