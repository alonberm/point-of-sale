# POS with classes
# Alon
# 24/11/2020
# Creat a POS system using classes

import Inventory as inven # import Inventory module
import miscellaneous as misc # import miscellaneous module
import Transaction as transac # import transaction module

def initializeMain():
    '''initialize required variable for main()
    param: None
    return: inventory (list), exit (bool)
    '''
    inventory = inven.Inventory() # initialize inventory object (Inventory)
    exit = False # set exit flag to false (bool)
    return inventory, exit # return initialized variables
# end initializeMain

def main():
    '''
    main function of the program
    param: None
    return: null
    '''
    inventory, exit = initializeMain() # initialize required variables

    print(f'Welcome to {misc.STORENAME}!') # print welcome message
    while not(exit):
        userChoice = misc.getInputString('\n1. CASH REGISTER\n2. INVENTORY CONTROL\n3. SHUTDOWN\n\nChoose an option from the above:\t', ['1', '2', '3']) #getOptions() # gets valid userchoice from user (str)
        if userChoice == '1': # if user chose 1
            transaction = transac.Transaction(inventory.inventoryList) # create instance of transaction class (Transaction)
            transaction.printReceipt() # print the receipt for the transaction
        # end if
        elif userChoice == '2': # if the user chose 2
            inventory.inventoryMenu() # run the inventory menu
        #end elif
        elif userChoice == '3': # if the user chose 3
            inventory.exit() # execute exit method to save updated inventory
            exit = True # set exit to true to exit the loop
            print('Thanks for using the system. Goodbye.') # print goodbye message
        # end elif
    # end while

    return
# end main()


main()


