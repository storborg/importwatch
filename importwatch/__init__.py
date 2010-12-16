import sys
import re
import logging
import __builtin__

__version__ = '0.2'

log = logging.getLogger(__name__)

orig_import = __builtin__.__import__


def make_with_regex(regex=None):
    if regex:
        matcher = re.compile(regex)
    else:
        matcher = None
    def new_import(name, *args, **kwargs):
        if name not in sys.modules:
            if (not matcher) or matcher.match(name):
                log.info("'%s' imported.", name)
        return orig_import(name, *args, **kwargs)
    return new_import
                

def start(regex=None, echo=False):
    __builtin__.__import__ = make_with_regex(regex)
    if echo:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console.setFormatter(formatter)
        log.setLevel(logging.DEBUG)
        log.addHandler(console)
