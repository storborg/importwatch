==================================================================================
importwatch - See what your code is importing, and when.
==================================================================================

:Authors:
    Scott Torborg (storborg)
:Version: 0.1

This library tracks module imports. That's it.

*Note* Use at your own risk!


Installation
============

Simple as::
    
    $ pip install importwatch

Or with easy_install::

    $ easy_install importwatch

Or if you prefer, download the source and then::

    $ python setup.py build
    $ python setup.py install


Example
=======

>>> import importwatch
>>> importwatch.start()
>>> run_lots_of_code_which_imports_stuff()
>>> # That's it!

Just care about your package?

>>> import importwatch
>>> importwatch.start('^myapp')


Logging Configuration
=====================

To make importwatch more useful, you'll want to configure some special logging.
Do it like:

    [logger_importwatch]
    level = INFO
    handlers = console
    qualname = importwatch


License
=======

Packagetrack is released under the GNU General Public License (GPL). See the
LICENSE file for full text of the license.


.. # vim: syntax=rst expandtab tabstop=4 shiftwidth=4 shiftround
