import sys
import re
import logging
import imp

__version__ = '0.1'

log = logging.getLogger(__name__)


class ImportWatcher(object):
    """
    An instance of this class gets installed with PEP302-style import hooks to
    monitor all module imports.
    """
    def __init__(self, regex=None):
        if regex:
            self.regex = re.compile(regex)
        else:
            self.regex = None

    def find_module(self, fullname, path=None):
        if (not self.regex) or self.regex.match(fullname):
            log.info("'%s' imported." % fullname)


def start(regex=None, echo=False):
    sys.meta_path.insert(0, ImportWatcher(regex))
    if echo:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        console.setFormatter(formatter)
        log.setLevel(logging.DEBUG)
        log.addHandler(console)
