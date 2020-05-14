
"""This module consists of my personal logging 'xp's"""

import logging
import warnings
import subprocess


try:
    subprocess.run(['cowsay', 'hi'], check=True, stdout=subprocess.PIPE)
except FileNotFoundError:
    warnings.warn("cowsay is not installed or cannot be accessed! CowFormatter will not run!")


class CowFormatter(logging.Formatter):
    """Formats a message in to the Unix `cowsay` command line utility style.
    It is recommended to keep text other than messages short as it might become
    hard to read and digest. However, in general it is just a great way to make
    your boring coding sessions less boring.

    **Please note that this formatter requires the cowsay utility to be
    installed and is available in PATH**
    """

    def __init__(self, *args, **kwargs):
        """"""
        super(CowFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        """Format using the default Formatter, then use cowsay to do a second
        round
        """
        orig_string = super(CowFormatter, self).format(record)
        try:
            return subprocess.run(['cowsay', orig_string],
                                  capture_output=True, check=True).stdout.decode()
        except FileNotFoundError:
            raise FileNotFoundError(
                "The cowsay utility either is not installed or not available in PATH")
        except Exception:
            raise
