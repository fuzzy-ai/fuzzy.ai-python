from codecs import open as codecs_open
from setuptools import setup, find_packages

# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(name='fuzzyio',
      version='0.1.2',
      description=u"fuzzy.io API",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Evan Prodromou",
      author_email='evan@fuzzy.io',
      url='https://github.com/fuzzy-io/python',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'test': ['pytest'],
      }
      )
