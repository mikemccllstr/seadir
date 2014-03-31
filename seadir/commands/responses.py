'''Command line handlers that address the responses in the Google Sheet'''

import logging
import os

from cliff.lister import Lister

import seadir.config as config
import seadir.model.responses as responses


class Dump(Lister):
    '''Dump the records from the Google Sheet to the screen'''

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        '''Method invoked by the Cliff framework'''

        # Obtain the data from the Google Sheet
        data = responses.Data(email=config.email,
                              password=config.password,
                              sheetname=config.spreadsheet,
                              tabname=config.worksheet)

        return (data.headers,
                data.raw_contents())


class Clean(Lister):
    '''Process all the records and perform any possible cleanups'''

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        return (('Name', 'Size'),
                ((n, os.stat(n).st_size) for n in os.listdir('.'))
                )


class Validate(Lister):
    '''Process all the records and flags any situations that seem erroneous'''

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        return (('Name', 'Size'),
                ((n, os.stat(n).st_size) for n in os.listdir('.'))
                )
