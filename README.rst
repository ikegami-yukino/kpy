kpy
==========
|travis| |coveralls| |downloads| |version| |license|

Kpy stands for Keitai (Japanese mobile phone) model name extractor on Python.

This module extracts model name of mobile phone/tablet from user agent string.

Currently, This module supports 1007 Japanese mobile phones/tablets.

- Docomo: 561 models (F501i, 1999. - SO-03H, 2015)
- au: 91 models (IS01, 2010 - SOV32, 2015; currently supporting only Android models)
- SoftBank (J-PHONE, Vodafone, Disney mobile, EMOBILE, WILLCOM, Y!mobile): 357 models (J-SH02, 1999. - Nexus 6P, 2015)

INSTALATION
===========
::

 $ pip install kpy

USAGE
===========

.. code:: python

    import kpy
    ua = ('Mozilla/5.0 (Linux; U; Android 4.1.1; ja-jp; HTL21 Build/JRO03C) '
          'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
    kpy.extract(ua)
    # => 'HTL21'

TODO
===========
- Supports other countries' mobilephone
- Output model series name of mobilephone

Contributions are welcome.

License
=========
- MIT License


.. |travis| image:: https://travis-ci.org/ikegami-yukino/kpy.svg?branch=master
    :target: https://travis-ci.org/ikegami-yukino/kpy
    :alt: travis-ci.org

.. |coveralls| image:: https://coveralls.io/repos/ikegami-yukino/kpy/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/ikegami-yukino/kpy?branch=master
    :alt: coveralls.io

.. |downloads| image:: https://img.shields.io/pypi/dm/kpy.svg
    :target: http://pypi.python.org/pypi/kpy/
    :alt: downloads

.. |version| image:: https://img.shields.io/pypi/v/kpy.svg
    :target: http://pypi.python.org/pypi/kpy/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/kpy.svg
    :target: http://pypi.python.org/pypi/kpy/
    :alt: license
