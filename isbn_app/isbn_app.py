import sys
def isbn_10_num_sum(isbn: str):
    """
Sums an ISBN-10 for a check digit.

Takes the first 9 digits of an ISBN-10.
Returns an integer sum.
"""
    # calculation
    total = 0
    for index, char in enumerate(isbn):
        multiplier = 10 - index
        total += int(char) *  multiplier
    return total

def isbn_13_num_sum(isbn: str):
    """
Sums an ISBN-13 for a check digit.

Takes the first 12 digits of an ISBN-13. 
Returns an integer sum.
"""
    # calculation 
    total = 0
    evry_2nd = isbn[1::2] # every second digit
    the_rest = isbn[::2]
    for i in the_rest:
        total += int(i)
    for i in evry_2nd:
        total += (3 * int(i))
    return total

def validate_isbn(isbn: str, mode: int):
    """
Validates a proposed ISBN is completely numerical, and is 1 smaller than the mode.

Takes an ISBN, of any length, and the mode the ISBN is in (10, or 13)
Returns a Boolean, and a reason ("non-numeric", "wrong-length", "valid-isbn").
"""
    if not isbn.isnumeric():
        return False, "non-numeric"
    elif len(isbn) != mode-1:
        return False, "wrong-length"
    else:
        return True, "valid-isbn"

def gen_isbn_10_check_digit(isbn: str):
    """
Generates an ISBN-10 check digit.

Takes a 9 digit ISBN, without a checksum.
Returns an integer check digit, but occasionally an 'X' (string)
"""
    # validation
    valid, reason = validate_isbn(isbn, 10)
    if not valid:
        return "Invalid ISBN-10: " + reason

    # calculation       
    check_digit_mod = (isbn_10_num_sum(isbn) % 11)

    # normalisation
    #TODO - fix anomalies
    if check_digit_mod == 0:
            check_digit = 0
    elif check_digit_mod == 1:
        check_digit = 'X'
    else:
        check_digit = 11 - check_digit_mod
        
    return check_digit

def gen_isbn_13_check_digit(isbn: str):
    """
Generates an ISBN-13 check digit.

Takes a 12 digit ISBN, without a checksum.
Returns an integer check digit.
"""
    # validation
    valid, reason = validate_isbn(isbn, 13)
    if not valid:
        return "Invalid ISBN-13: " + reason

    # calculation
    check_digit_mod = isbn_13_num_sum(isbn) % 10
    if check_digit_mod > 0:
        check_digit = 10 - check_digit_mod
    else:
        check_digit = 0
    
    return check_digit

def cli_ui():
    """
Displays a console user interface for this program.

No parameters, no return value.
"""
    global gen_check_func
    print("Welcome to the ISBN Checksum Generator!\n")
    
    mode = input("Do you have a ten digit ISBN, or a thirteenn digit one [10/13]? ")
    if mode == "10":
        gen_check_func = gen_isbn_10_check_digit
        isbn = input("Please enter the first 9 digits of your ISBN-10: ")
    elif mode == "13":
        gen_check_func = gen_isbn_13_check_digit
        isbn = input("Please enter the first 12 digits of your ISBN-13: ")
    else:
        print("Invalid mode.")
        input("Press enter to exit.")
        sys.exit(1)
        
    check_gen = input("Would you like to check the checksum, or generate the checksum [c/g]? ")

    checksum = gen_check_func(isbn)

    if check_gen.lower() == "g":
        print("The checksum of your ISBN-"+mode+" (the "+mode+"th digit) is:", checksum)
    elif check_gen.lower() == "c":
        guess = input("What do you think the checksum is? ")
        if guess == str(checksum):
            print("I agree. ")
        else:
            print("I disagree. I think it is "+checksum+".")
    else:
        print("Invalid input. Your checksum: "+checksum+".")

    input("Press enter to exit. ")
    

# UI only runs when program runs
if __name__ == '__main__':
    cli_ui()
