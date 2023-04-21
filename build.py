import shutil
import sys
import os


def BuildFlutterApp():
    return False

def BundleWebsite():
    return False

def BuildServer():
    return False

def LaunchDocker():
    raise(NotImplementedError)



os.mkdir("build/")
os.mkdir("dist/")
