import os.path

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


import importwatch

           
setup(name='importwatch',
      version=importwatch.__version__,
      author="Scott Torborg",
      author_email="storborg@mit.edu",
      license="GPL",
      keywords="track imports profiler package modules",
      url="http://github.com/storborg/importwatch",
      description='Track packages.',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      long_description=read('README.rst'),
      test_suite='nose.collector',
      zip_safe=False,
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Programming Language :: Python"])
