#!/usr/bin/env python
import os
import sys
from subprocess import call
from time import sleep

use_cls = True
use_sleep = True


def cls():
    if use_cls:
        # check and make call for specific operating system
        _ = call('clear' if os.name == 'posix' else 'cls')


def _sleep(seconds):
    if use_sleep:
        sleep(seconds)


def clear_line():
    if use_cls:
        sys.stdout.write("\033[K")


def back_to_prev_line():
    if use_cls:
        sys.stdout.write("\033[F")
