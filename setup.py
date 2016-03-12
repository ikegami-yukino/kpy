# -*- coding: utf-8 -*-
from codecs import open
import os
import re
from setuptools import setup

with open(os.path.join('kpy', '__init__.py'), 'r', encoding='utf8') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='kpy',
    packages=['kpy'],
    version=version,
    license='MIT License',
    platforms=['POSIX', 'Windows', 'Unix', 'MacOS'],
    description='mobile-phone\'s model name extractor from user agent',
    author='Yukino Ikegami',
    author_email='yukino0131@me.com',
    url='https://github.com/ikegami-yukino/kpy',
    keywords=['mobile-phone', 'smartphone', 'cell-phone', 'user agent'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    data_files=[('', ['README.rst', 'CHANGES.rst'])],
    long_description='%s\n\n%s' % (open('README.rst', encoding='utf8').read(),
                                   open('CHANGES.rst', encoding='utf8').read())
)
