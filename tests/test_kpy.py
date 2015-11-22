import glob
import os
import json
import kpy
from nose.tools import assert_equals


OSX_UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/'
          '534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24')


def test_extract():
    json_pattern = os.path.join(os.path.abspath(os.path.dirname(__file__)), '*.json')
    load_json = lambda x: json.load(open(x))
    for d in map(load_json, glob.glob(json_pattern)):
        for (name, uas) in d.items():
            for ua in uas:
                got = kpy.extract(ua)
                assert_equals(got, name)
    assert_equals(kpy.extract(OSX_UA), None)
