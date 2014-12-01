kpy
==========
.. image:: https://badge.fury.io/py/kpy.svg
    :target: http://badge.fury.io/py/kpy
.. image:: https://travis-ci.org/ikegami-yukino/kpy.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/kpy
.. image:: https://coveralls.io/repos/ikegami-yukino/kpy/badge.png
  :target: https://coveralls.io/r/ikegami-yukino/kpy

Kpy stands for Keitai (Japanese mobile phone) model name extractor on Python.

This module extracts model name of mobile phone/tablet from user agent string.

Currently, This module supports 774 Japanese mobile phones/tablets.

INSTALATION
===========
::

 $ pip install kpy

USAGE
===========
>>> import kpy
>>> ua = ('Mozilla/5.0 (Linux; U; Android 4.1.1; ja-jp; HTL21 Build/JRO03C) '
          'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
>>> kpy.extract(ua)
HTL21

TODO
===========
- Supports other countries' mobilephone
- Output model series name of mobilephone 

Contributions are welcome.

License
=========
- MIT License

