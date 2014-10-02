#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setupSwift.py
~~~~~~~~~~~~~~~~~

Checks to make sure machine (!Person) is ready for the iOS w/ Swift class.

:copyright: (c) 2014 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/ElevenFiftyScripts
"""
import platform
import subprocess
import os.path


def os_is_mavericks():
    version = platform.mac_ver()
    if version == "10.9" or version == "10.10":
        return True
    else:
        return False


def xcode_is_installed():
    if os.path.isdir("/Applications/Xcode.app"):
        return True
    else:
        return False


def xcode_version_is_right():
    command = "xcodebuild -version"
    version = subprocess.check_output(command.split())
    version_num = version.split()[1]
    if version_num >= "6.0":
        return True
    else:
        return False


def install_xcode():
    if not os_is_mavericks():
        update_osx
    # do the installing here
    print("installing xcode")


def update_osx():
    print("updating osx")


def update_xcode():
    print("updating xcode")


def main():
    if xcode_is_installed():
        if xcode_version_is_right():
            print("You won!")
        else:
            update_xcode()
    else:
        install_xcode()


if __name__ == '__main__':
    main()
