'''Data model abstraction over the Google Sheet'''

import itertools

import gspread


class Data(object):
    '''Wraps all operations on the Responses spreadsheet'''

    def __init__(self, email, password, sheetname, tabname):
        '''Connect to Google and gets access to the Sheet'''

        # Login with a Google account
        gc = gspread.login(email, password)

        # Open the spreadsheet and worksheet
        spreadsheet = gc.open(sheetname)
        self.wks = spreadsheet.worksheet(tabname)

        # Save a copy of the headers
        self.headers = self.wks.row_values(1)


    def raw_contents(self):
        '''Generator that returns the original contents of the Sheet'''
        for row in itertools.islice(self.wks.get_all_values(), 1, None):
            yield row


    def replace(self):
        '''Replace a single row from the current Sheet with new contents'''
        pass


    def append(self):
        '''Append a single row to the current Sheet'''
        pass
