import os
import sys
from codecs import open as codecs_open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['requests']

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'fuzzyai'))
from version import VERSION

setup(
    name='fuzzy.ai',
    cmdclass={'build_py': build_py},
    version=VERSION,
    description=u"fuzzy.ai API",
    long_description=long_description,
    author=u"Evan Prodromou",
    author_email='evan@fuzzy.ai',
    url='https://github.com/fuzzy-ai/fuzzy.ai-python',
    packages=['fuzzyai', 'fuzzyai.test'],
    license='Apache 2.0',
    install_requires=install_requires,
    test_suite='fuzzyai.test.all',
    tests_require=['unittest2', 'mock'],
    use_2to3=True,
    classifiers=[],
  )
