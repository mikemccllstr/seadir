'''Config object for the seadir project'''

import ConfigParser
import os.path

CONFIG_FILENAME = 'seadir.ini'
CONFIG_SEARCH_PATH = ['.']

# Try and read in the configuration file and set the necessary
# variables

_config = ConfigParser.SafeConfigParser()

_config.read([os.path.join(dirname, CONFIG_FILENAME)
              for dirname in CONFIG_SEARCH_PATH])

# These are the values we expect to find
email       = _config.get('Response Data', 'email')
password    = _config.get('Response Data', 'password')
spreadsheet = _config.get('Response Data', 'spreadsheet')
worksheet   = _config.get('Response Data', 'worksheet')
