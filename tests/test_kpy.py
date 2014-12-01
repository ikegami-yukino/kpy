import os
import json
import kpy
from nose.tools import assert_equals


JSONS = ('ymobile', 'docomo', 'docomo_android', 'softbank',
         'android_au', 'softbank_android')
OSX_UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/'
          '534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24')


def test_extract():
    test_dir = os.path.abspath(os.path.dirname(__file__))
    json_open = lambda x: json.load(open(os.path.join(test_dir, x + '.json')))
    for d in map(json_open, JSONS):
        for (name, uas) in d.items():
            for ua in uas:
                got = kpy.extract(ua)
                assert_equals(got, name)
    assert_equals(kpy.extract(OSX_UA), None)
