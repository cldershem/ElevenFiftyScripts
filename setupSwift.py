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
import platform
import subprocess
import os.path


"""
# def can_run_xcode():
    # if check_os_version:
        # print("you're good.")
        # check_xcode_version()
    # else:
        # print("No bueno.")
        """


def os_is_mavericks():
    version = platform.mac_ver()
    if version == "10.9" or version == "10.10":
        return True
    else:
        return False


def xcode_is_installed():
    if os.path.isfile("/Applications/Xcode.app"):
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
    print("installing xcode")


def update_osx():
    print("updating osx")


if __name__ == '__main__':
    print("begin")
    if xcode_is_installed():
        print("is installed")
        if xcode_version_is_right():
            print("is right version")
        else:
            print("not installed")
            if os_is_mavericks():
                print("right osx")
                install_xcode()
            else:
                print("wrong osx")
                update_osx()
                install_xcode()
    print("done")
