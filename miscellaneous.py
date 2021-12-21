LINES = '=============================================' # initialize lines for receipt (str)
STORENAME = 'Alon\'s Store' # initilize name of store (str)
TAX = 0.13 # initialize tax rate (float)

def isNum(num):
    # checks if num is a number
    # num is number to be checked (str)
    # return result (bool)
    try: # try to convert num to float
        float(num) # try to convert num to float
        result = True # set result to true (bool)
    # end try
    except: # exception is raised
        result = False # set result to false
    # end except
    return result # return result
# end isNum()

def isInteger(num):
    '''
    checks if num is an integer
    param: num is the variable to be checked (str)
    return: bool indicating if it is integer
    '''
    try: # try to convert num to int
        int(num) # try to convert num to int
        result = True # set result to true (bool)
    # end try 
    except: # error is raised
        result = False # set result to false
    # end except
    return result # return result
# end isInteger()

def getInputInt(message):
    '''
    gets a valid integer input from the user
    param: message is the input prompt to be displayed (str)
    return: valid user input (int)
    '''
    exit = False # initialize exit to false (bool)
    while not(exit): # WHILE the flag is not false
        userInput = input(f'{message}') # prompt user to enter input (str)
        if isInteger(userInput): # check if user input is an integer
            exit = True # YES: set exit to true to exit the loop
        # end if
        else:
            print('Input is not valid. Try again.') # NO: prompt user to try again
        # end else 
    # end while

    return int(userInput) # return the valid userInput once while loop exits
# end getInputInt()

def getInputString(message, validInput):
    '''
    gets a valid input from the user
    param: validInput is a list of all accepted inputs (list)
    message is the input prompt to be displayed (str)
    return: valid user input (str)
    '''

    exit = False # initialize exit to false (bool)
    while not(exit): # WHILE the flag is not false
        userInput = input(f'{message}') # prompt user to enter input (str)
        if userInput in validInput: # check if user input is in list of valid inputs
            exit = True # YES: set exit to true to exit the loop
        # end if
        else:
            print('Input is not valid. Try again.') # NO: prompt user to try again
        # end else 
    # end while

    return userInput # return the valid userInput once while loop exits
# end getInputString()

def confirm():
    # get user's confirmation that they want to continue 
    # param: None
    # return: result (bool)
    if getInputString('Confirm you want to continue: (y/n)\t', ['y', 'n']) == 'y': # ask user user confirm they want to continue (str)
        result = True # set result to true(bool)
    # end if
    else:
        result = False # set result to false (bool)
    # end else
    return result
# end confirm()