# -*- coding: utf-8 -*-
"""
    Common functions
    :copyright: © 2018 by Nuno Gonçalves
    :license: MIT, see LICENSE for more details.
"""

from json import load
from os import devnull
from os.path import join
from subprocess import call
from core.constants import KEEPER_HOME, IS_NT


def load_config():
    """
    loads configuration from json file
    :return: returns a configuration dict
    """

    with open(join(KEEPER_HOME, "config", "keeper.json")) as config:
        return load(config)


def exec_command(command):
    """
    executes a given command
    :param command: command to be executed
    :return: whether the command was executed successfully
    """

    try:
        with open(devnull, "wb") as dev_null:
            return call(command, stdout=dev_null, stderr=dev_null, shell=IS_NT) == 0
    except Exception:
        return False
