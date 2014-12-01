"""kpy

Kpy stands for Keitai (Japanese mobile phone) model name extractor on Python.
This module extracts model name of mobile phone, especially Japanese phone,
from user agent."""
from . import kpy

VERSION = (0, 1)
__version__ = '0.1'
__all__ = ['extract']

extract = kpy.extract
