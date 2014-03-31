'''Data model abstraction over the Google Sheet'''

import itertools

import gspread

from seadir.model.phonenumber import standardize_phone


# Give easier names to the column headings in the Sheet
TIMESTAMP="Timestamp"
STUDENTS_NAME="Student's Name"
CLASSROOM_TEACHER="Classroom / Teacher"
SUBMITTER_EMAIL="Submitter's email address"
CONTACTS_NAME="Contact's name"
CONTACTS_PHONE="Contact's phone number"
CONTACTS_ALT_PHONE="Contact's alternate phone number"
CONTACTS_EMAIL="Contact's email address"
CONTACTS_MAILING="Contact's mailing address"
SECOND_CONTACTS_NAME="Second Contact's name"
SECOND_CONTACTS_PHONE="Second Contact's phone number"
SECOND_CONTACTS_ALT_PHONE="Second Contact's alternate phone number"
SECOND_CONTACTS_EMAIL="Second Contact's email address"
SECOND_CONTACTS_MAILING="Second Contact's mailing address"
ACTION="Action"


def remove_dupe(second, prime):
    '''Remove secondary values that match the primary

    Also treat the value 'same' as a match

    '''
    if second == prime or second == 'same':
        return ''
    else:
        return second


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

        # Save a copy of the items
        self.raw_items = itertools.islice(self.wks.get_all_values(), 1, None)


    def raw_contents(self):
        '''Generator that returns the original contents of the Sheet'''
        for row in self.raw_items:
            yield row

    def scrubbed_contents(self):
        '''Return the contents of the Sheet as dicts, cleansed and ready for output'''

        # Create a clean dict from each row
        last_timestamp = None
        results = {}
        for idx, row_contents in enumerate(self.raw_items):
            # Build the initial dict from the stripped contents
            rdict = dict(zip(self.headers, [v.strip() for v in row_contents]))
            rdict['row_number'] = idx - 2

            # Clean up the telephone numbers
            rdict[CONTACTS_PHONE] = standardize_phone(rdict[CONTACTS_PHONE])
            rdict[CONTACTS_ALT_PHONE] = standardize_phone(rdict[CONTACTS_ALT_PHONE])
            rdict[SECOND_CONTACTS_PHONE] = standardize_phone(rdict[SECOND_CONTACTS_PHONE])
            rdict[SECOND_CONTACTS_ALT_PHONE] = standardize_phone(rdict[SECOND_CONTACTS_ALT_PHONE])

            # Remove duplicate information from secondary values
            rdict[SECOND_CONTACTS_NAME] = remove_dupe(rdict[SECOND_CONTACTS_NAME],
                                                      rdict[CONTACTS_NAME])
            rdict[SECOND_CONTACTS_PHONE] = remove_dupe(rdict[SECOND_CONTACTS_PHONE],
                                                       rdict[CONTACTS_PHONE])
            rdict[SECOND_CONTACTS_ALT_PHONE] = remove_dupe(rdict[SECOND_CONTACTS_ALT_PHONE],
                                                           rdict[CONTACTS_ALT_PHONE])
            rdict[SECOND_CONTACTS_EMAIL] = remove_dupe(rdict[SECOND_CONTACTS_EMAIL],
                                                       rdict[CONTACTS_EMAIL])
            rdict[SECOND_CONTACTS_MAILING] = remove_dupe(rdict[SECOND_CONTACTS_MAILING],
                                                       rdict[CONTACTS_MAILING])

            # Fill in missing timestamps
            if rdict[TIMESTAMP] == '':
                rdict[TIMESTAMP] = last_timestamp
            else:
                last_timestamp = rdict[TIMESTAMP]

            # Remove the entry with no key
            del rdict[None]

            # Save the results by student name, so we replace with later items
            results[rdict[STUDENTS_NAME]] = rdict

        # Loop through each result
        for rdict in results.values():
            yield rdict


    def replace(self):
        '''Replace a single row from the current Sheet with new contents'''
        pass


    def append(self):
        '''Append a single row to the current Sheet'''
        pass
