""" Module storing basic constant values
"""

# Import modules
from enum import Enum, auto


class JsonFormat(Enum):
    """ Enum for JSON file formats
    """

    DICTIONARY = auto()
    LIST = auto()


class Encoding():
    """ Enum for JSON file encodings
    """

    ISO = "iso"
    ASCII = "ascii"
    KOI8 = "koi8"
    CP866 = "cp866"
    UTF16 = "utf-16"
    UTF8 = "utf-8"
    ANSI = "ansi"


class Constants:
    """ Class containing basic constant values
    """

    file_format = JsonFormat
    encoding = Encoding
