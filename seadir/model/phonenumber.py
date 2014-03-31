'''Class for cleaning phone numbers'''

import phonenumbers

def standardize_phone(number):
    '''Do the best we can in trying to standardize the given phone number'''

    try:
        parsed_number = phonenumbers.parse(number, 'US')
        return phonenumbers.format_number(parsed_number,
                                          phonenumbers.PhoneNumberFormat.NATIONAL)
    except phonenumbers.NumberParseException as npe:
        return ""
