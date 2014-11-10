#!/usr/bin/env python

from distutils.core import setup

setup(name='pushbullet_log_handler',
      version='0.1',
      description='Pushbullet Logging Handler',
      author='Mathias Ose, Øyvind Robertsen',
      author_email='m@thiaso.se, me@oyvindrobertsen.com',
      url='http://github.com/mathiasose/pushbullet_logger',
      packages=['pushbullet_log_handler'],
      install_requires=['pushbullet.py>=0.5.0'],
      )
