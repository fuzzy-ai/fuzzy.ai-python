import os
import unittest2


def all():
    path = os.path.dirname(os.path.realpath(__file__))
    return unittest2.defaultTestLoader.discover(path)
