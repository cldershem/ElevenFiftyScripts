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
    version, nothing, architecture = platform.mac_ver()
    if version == "10.9" or version == "10.10":
        return True
    else:
        return False


def xcode_is_installed():
    # command = "which xcodebuild"
    # if subprocess.check_output(command.split()) == "/usr/bin/xcodebuild\n":
    path_to_xcode = "/Applications/Xcode.app"
    if os.path.isdir(path_to_xcode):
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
        update_osx()
    # print("Please update Xcode via the App Store")
    # url = "http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12"
    # subprocess.Popen(["open", url])
    print("Installing Xcode")
    command = "hdiutil mount /Volumes/EF/xcode_6.0.1.dmg"
    subprocess.call(command.split())
    command = "sudo cp -R /Volumes/Xcode/Xcode.app /Applications"
    subprocess.call(command.split())
    command = "hdiutil unmount /Volumes/Xcode"
    subprocess.call(command.split())
    print("Finished installing Xcode")
    return True


def update_osx():
    print("Please update OSX via the App Store")
    url = "https://itunes.apple.com/us/app/os-x-mavericks/id675248567?mt=12"
    subprocess.Popen(["open", url])


def update_xcode():
    print("Updating xcode.")
    command = "softwareupdate --list"
    subprocess.call(command.split())
    command = "softwareupdate --install Xcode*"
    subprocess.call(command.split())
    if xcode_is_installed() and xcode_is_installed():
        print("Finished updating xcode.")
        return True
    else:
        print("something didn't go right while updating")
        return False


def setup_swift():
    if xcode_is_installed():
        if xcode_version_is_right():
            print("You won!")
        else:
            if update_xcode():
                print("Sweet!")
    else:
        if install_xcode():
            print("You're all good now!")


if __name__ == '__main__':
    setup_swift()
