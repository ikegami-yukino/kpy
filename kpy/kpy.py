import re


REGEXES = map(re.compile, (' (?P<name>[A-Z]{6,7} [A-Z0-9]{3,9}) ',
                           ' (Sony)?(Ericsson)?(?P<name>[A-Z\-]{,5}[0-9]{2,}[A-Z\-0-9]{,6}) ',
                           '/(?P<name>[A-Z0-9\-]{4,9}[eflpsu]{,4})/',
                           '\((?P<name>[A-Z0-9\-]{4,8}[lpsu]{,4})\)',
                           '(?P<name>Galaxy Nexus)',
                           '(?P<name>SmartTVStick)',
                           '/(?P<name>[A-Z\-]{,5}[0-9][A-Z\-0-9]{,4})\)',
                           ' (?P<name>[A-Z0-9\-]{4,7})$',
                           ' (?P<name>[A-Z0-9\-]{4,7})\)',
                           '[/ ](?P<name>[A-Z0-9\-]{4,7})[;\)]',
                           ' (?P<name>[A-Z0-9\-]{4,7}i?[2emBCDEFSTWX]?[iwyCGLMPSV]?[\+uzCLOS]?)\(',
                           '[;\(_](?P<name>[A-Z\-]{,5}[0-9][A-Z\-0-9pes]{,5})[; \(]',
                           '(?P<name>Nexus \d{1,})',
                           '(?P<name>BlackBerry ?[0-9]*)[/;]',
                           ' (?P<name>((Nokia)|(Series))[\-a-zA-Z0-9]+)/',
                           '\A(?P<name>[A-Z0-9\-]{3,})[/;]'))
REGEXES = list(REGEXES)
OTHER_MODELS = ('dtab01', )


def extract(ua):
    """
    Extract model name of mobile phone from UserAgent

    Arg:
        <str> ua
    Return:
        <str> phone_name
    """
    for regex in REGEXES:
        match = regex.search(ua)
        if match:
            return match.group('name')
    for other_model in OTHER_MODELS:
        if other_model in ua:
            return other_model
