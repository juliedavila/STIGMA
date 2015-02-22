#!/usr/bin/env python

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='stigma',
      version='0.1',
      description='OpenSCAP results parser',
      author='Jonathan I. Davila',
      author_email='jdavila@ansible.com',
      license='MIT',
      url='https://github.com/defionscode/STIGMA',
      packages=['stigma', 'tests'],
      keywords=['stig', 'openscap', 'scap', 'disa', 'security'],
      install_requires=['tabulate','untangle','pytest'],
      tests_requires=['pytest'],
      long_description=read('README.md')
     )