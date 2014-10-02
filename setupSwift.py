#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setupSwift.py
~~~~~~~~~~~~~~~~~

Checks to make sure machine (!Person) is ready for the iOS w/ Swift class.

:copyright: (c) 2014 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/repo
"""
import os
import platform


def check_os_version():
    print(os.system("uname -r"))
    print(platform.mac_ver())


def check_xcode_version():
    pass


if __name__ == '__main__':
    check_os_version()
