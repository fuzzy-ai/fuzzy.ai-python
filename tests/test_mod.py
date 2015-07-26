import fuzzyio
from types import *

API_KEY = ""

def test_has_class():
    assert type(fuzzyio.FuzzyIO) is ClassType

def test_constructor():
    f = fuzzyio.FuzzyIO(API_KEY)
    assert type(f) is InstanceType
