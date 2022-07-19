"""
The "pytdllib" package helps to manage the "pytube" library,
i.e. it makes it easier to save playlists or individual videos in any format:
	mp4, txt.
This package supports loading/unloading links via a text file.

Artamonov Mikhail [https://github.com/maximalisimus]
maximalisimus121@mail.ru
# License: GPL3
"""
__author__ = 'Mikhail Artamonov'

try:
    from .version import version
except ImportError:
    version = "1.0.0"

__version__ = version

from .filesdir import *
from .pytubedl import *

