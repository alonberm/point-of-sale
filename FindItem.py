import miscellaneous as misc

class FindItem:
    # gets an item from the inventory
    def __init__(self, inventoryList, printHeaders, printItem):
        self.inventoryList = inventoryList # set inventoryList to inventoryList attribute (list of ItemsInInventory)
        self.printHeaders = printHeaders # set printHeaders method to printHeaders attribute (method)
        self.printItem = printItem # set printItem method to printItem attribute (method)
    # end __init__()

    def getValidSKU(self):
        # gets a valid sku from user
        # param: none 
        # return: valid sku
        exit = False # set exit to false
        while not(exit): # while exit is not false
            sku = input('Enter SKU:\t') # read sku from user (str)
            if sku[:3].upper() in ['VEG', 'FRU', 'OTH', 'MEA'] and misc.isInteger(sku[4:8]) and '-' not in sku[4:8] and len(sku) == 8 and sku[3] == '-': # check if sku is correct format
                exit = True # set exit to false
            # end if
            else:
                print('SKU is not valid. Try Again.') # print sku is not valid
            # end else
        # end while
        return sku.upper()
    # end getValidSKU() 

    def skuSearch(self):
        # search to  display an item by its sku
        # param: None
        # return: the item 
        sku = self.getValidSKU() # get a valid sku from user (str)
        result = None # initialize result
        for item in self.inventoryList: # iterate through inventory list 
            if item.sku == sku: # if the sku is same as item sku
                self.printHeaders() # print the headers
                self.printItem(item) # print the item
                result = item # set result equal to item
            # end if
        # end for
        if result == None: # if result is none
            print('That item does not exist.') # print item does not exist
        # end if
        return result # return the item 
    # end skuSearch()

    def nameSearch(self):
        # search to display an item by its name
        # param: None
        # return: the item 
        name = input('Enter name:\t') # read item name from the user (str)
        result = [] # initialize result (list)
        self.printHeaders() # print the headers
        for item in self.inventoryList: # iterate through inventory list 
            if item.name.lower() == name.lower(): # if the name is same as item name
                self.printItem(item) # print the item
                result.append(item) # append item to result
            # end if
        # end for
        if result == []: # if result is empty: no item was found
            print('That name does not exist.') # orint the error
        # end if
        return result # return the item 
    # end nameSearch()

    def getItemByName(self):
        # get an item from user by name 
        # param: none 
        # return: the item (ItemInInventory)
        exit = False # set exit to false (bool)
        while not(exit): # while exit is not false
            item = self.nameSearch() # get item from user by name (ItemInInventory)
            if len(item) == 1: # if the list only contains one element
                exit = True # set exit to true
                item = item[0] # set item to that element
            # end if
            elif len(item) > 1: # if there is more than 1 item in the list
                exit = True
                choiceList = [] # initialize choice list (list of str)
                for i in range(len(item)): # iterate through item list
                    print(f'{i+1}. {item[i].sku}') # print the sku of the items
                    choiceList.append(str(i+1)) # append the number to the choice list
                choice = misc.getInputString('Choose your item:\t', choiceList) # get user's choice for item
                item = item[int(choice)-1] # set final item value to user's choice
            # end elif
        # end while
        return item 
    # end getItemByName()

    def getItemBySKU(self):
        # get an item by its sku 
        # param: none 
        # return: the item (ItemInInventory)
        exit = False # set exit to false (bool)
        while not(exit): # while exit is not false
            item = self.skuSearch() # get item from user by sku
            if item != None: # if item is not none
                exit = True # set exit to true to exit the loop
            # end if
        # end while
        return item 
    # end getItemBySku()

    def getItem(self):
        # get an item from the user
        # param: None
        # return: item 
        choice = misc.getInputString('1. Search by name\n2. Search by SKU\n\nEnter choice:\t', ['1', '2']) # get user's choice (str)
        if choice == '1':
            item = self.getItemByName() # get the item by name
        # end if
        elif choice == '2':
            item = self.getItemBySKU() # get the item by its sku
        # end elif
        return item
    # end getItem()
# end FindItem