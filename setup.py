# coding=utf-8

from setuptools import setup

setup(name='adutils',
      license='MIT',
      url='http://github.com/benleb/adutils',
      author='Ben Lebherz',
      author_email='git@benleb.de',
      description='Helper and utilities for AppDaemon apps',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      packages=['adutils'],
      zip_safe=False,
      platforms='any',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      classifiers=[
          "Topic :: Software Development",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ]
      )
