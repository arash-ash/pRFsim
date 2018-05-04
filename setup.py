"""
pyprf setup.

"""

import numpy as np
from setuptools import setup, Extension

with open('README.rst') as f:
    long_description = f.read()



setup(name='prfsim',
      version='0.1.0',
      description=('A free & open source python tool for population receptive \
                    field simulation of fMRI data.'),
      url='https://github.com/arash-ash/prfsim',
      download_url='https://github.com/arash-ash/prfsim/archive/v0.1.0.tar.gz',
      author='Arash Ash',
      author_email='arash.ashrafnejad@gmail.com',
      license='GNU General Public License Version 3',
      install_requires=['numpy', 'scipy', 'nibabel', 'pandas', 'seaborn'],
      keywords=['pRF', 'fMRI', 'retinotopy', 'simulation'],
      long_description=long_description,
      packages=['prfsim'],
      py_modules=['pyprf'],
      entry_points={
          'console_scripts': [
              'prfsim = prfsim.__main__:main',
              ]},
      )
