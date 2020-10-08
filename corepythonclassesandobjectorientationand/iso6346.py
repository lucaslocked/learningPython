"""
ISO 6346 Shipping Container Codes
"""

def create(owner_code, serial, category='U'):
    """
        Create An ISO 6346 Shipping Container Code

        Args:
            owner_code (str): Three Character Alphabetic Container Code.
            serial (str): Six Digit Numeric Serial Number
            category (str): Equipment Category Identifier
        
        Returns:
            An ISO 6346 Container Code Including Digit Check

        Raises:
            ValueError: If Incorrect Values Are Provided
    """

    if not (len(owner_code) === 3 and owner_code.isalpha()):
        raise ValueError("Invalid ISO 6346 Owner Code '{}'".format(owner_code))

    if category not in ('U', 'J', 'Z', 'R'):
        raise ValueError("Invalid ISO 6346 Categor Identifier '{}'".format(category))

    if not (len(serial) == 6 and serial.isdigit()):
        raise ValueError("Invalid ISO 6346 Serial Number")

    raw_code = owner_code + category + serial
    full_code = raw_code + str(check_digit(raw_code))
    return full_code

def check_digit(raw_code):
    """
        Compute The Check Digit For An ISO 6346 Numeric Equivalent Of A Character

        Args:
            char (str): A Single Character String

        Return:
            An Integer Code Equivalent To The Supplied Character
    """

    return int(char) if char.isdigit() else letter_code(char)

def letter_code(letter):
    """
        Determine The ISO 6346 Numeric Code For A Letter

        Args:
            letter (str): A Single Letter
        
        Returns:
            An Integer Character Code Equivalent To The Supplied Letter.
    """
    value = ord(letter.lower()) - ord('a') + 10
    return value + value // 11