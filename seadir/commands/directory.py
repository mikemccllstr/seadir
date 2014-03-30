''' Command line handlers that help produce the actual directory files
'''

import logging
import os

from cliff.lister import Lister


class Generate(Lister):
    """Produces the actual directory files
    """

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        return (('Name', 'Size'),
                ((n, os.stat(n).st_size) for n in os.listdir('.'))
                )
