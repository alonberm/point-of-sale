import miscellaneous as misc # import miscellaneous module
import pytz # import pytz module
import datetime # import datetime module
import ItemInInventory as itemInInventory # import ItemInInventory module
import FindItem as find # import the FindItem module
import os # import os module

class Inventory:
    # represents the inventory control in store
    def __init__(self):
        self.inventoryList = self.getInventoryList() # get the inventoryList and set it to inventoryList attribute (list of ItemsInInventory)
        self.findItem = find.FindItem(self.inventoryList, self.printHeaders, self.printItem) # initilize instance of FindItem class (FindItem)
    # end __init__()

    def printHeaders(self):
        # print the headers of report 
        # param: None
        # return: Null 
        sku, name, category, quantity, minQuantity, price, sale, profit = 'SKU', 'Name of product', 'Ctgy', 'Qty', 'R.Qty', 'Price', 'Sale', 'Profit' # initialize headers (str)
        print(f'{sku:<8} {name[:20]:<20} {category:<9} {quantity:>5} {minQuantity:>5} {price:>7} {sale:>7} {profit:>6}') # print formated headers
        return
    # end printHeaders()

    def printItem(self, item):
        # print all relevant attributes of an item 
        # param: item is the item to be printed (ItemInInventory)
        # return: null 
        print(item) # print the item
        return 
    # end printItem

    def inventoryMenu(self):
        # main menu of the inventory control section
        # param: none
        # return: null
        choice = misc.getInputString('1. Print report\n2. Search item\n3. Add stock\n4. Modify item\n5. Add item\n6. Delete item\n7. Go back\n\nEnter choice:\t', ['1', '2', '3', '4', '5', '6', '7']) # get user's choice of what they want to do (str)
        # run appropriate method based on user's choice
        if choice == '1':
            self.reportMenu() # run the report menu
        # end if
        elif choice == '2':
            self.searchMenu() # run the search menu
        # end elif
        elif choice == '3':
            self.addStockMenu() # run the add stock menu
        # end elif
        elif choice == '4':
            self.modifyMenu() # run the modify menu
        # end elif
        elif choice == '5':
            self.addItem() # add item 
        # end elif
        elif choice == '6':
            self.deleteItem() # delete item
        # end elif
        return
    # endInventoryMenu()

    def reportMenu(self):
        # menu of the report section 
        # param: None
        # return: null
        choice = misc.getInputString('1. Print report by category\n2. Print report by quantity\n3. Print report of all items\n4. Print report of all items for which a warning has been issued\n5. Go back\n\nEnter choice:\t', ['1', '2', '3', '4', '5']) # get user's choice (str)

        # run the appropriate method based on user's choice
        if choice == '1':
            self.categoryReport() # print category report
        # end if
        elif choice == '2':
            self.quantityReport() # print quantity report
        # end elif
        elif choice == '3':
            self.allReport() # print report of all items
        # end elif
        elif choice == '4':
            self.warningReport() # print report of items if warning has been generated
        # end elif
        elif choice == '5':
            self.inventoryMenu() # go back to inventoryMenu()
        # end elif
        return
    # end reportMenu()

    def searchMenu(self):
        # menu of item search section 
        # param: None
        # return: null
        choice = misc.getInputString('1. Search by SKU\n2. Search by name\n3. Go back\n\nEnter choice:\t', ['1', '2', '3']) # get user's choice (str)

        # run the appropriate method based on user's choice
        if choice == '1':
            self.findItem.skuSearch() # search by sku
        # end if
        elif choice == '2':
            self.findItem.nameSearch() # search by name
        # end elif
        elif choice == '3':
            self.inventoryMenu() # go back to inventoryMenu()
        # end elif
        return
    # end searchMenu()

    def addStockMenu(self):
        # menu of add stock section 
        # param: None
        # return: null
        choice = misc.getInputString('1. Add stock to an individual item\n2. Add stock all item below a certain quantity\n3. Add stock to all items below their minimum quantity\n4. Go back\n\nEnter choice:\t', ['1', '2', '3', '4']) # get user's choice (str)

        # run the appropriate method based on user's choice
        if choice == '1':
            self.addStockItem() # add stock to an individual item
        # end if
        elif choice == '2':
            self.addStockQuantity() # add stock to items below a certain quantity
        # end elif
        elif choice == '3':
            self.addStockWarning() # add stock to all items below their minimum quantity
        # end elif
        elif choice == '4':
            self.inventoryMenu() # go back to inventoryMenu()
        # end elif
        return
    # end addStockMenu

    def modifyMenu(self):
        # menu of modify section 
        # param: None
        # return: null
        choice = misc.getInputString('1. Modify name\n2. Modify quantity\n3. Modify minimum quantity\n4. Modify vendor price\n5. Modify mark up\n6. Modify discount\n7. Modify discount by category\n8. Go back\n\nEnter choice:\t', ['1', '2', '3', '4', '5', '6', '7', '8']) # get user's choice (str)

        # run appropriate method based on user's choice
        if choice == '1':
            self.modifyName() # modify the name of an item
        # end if
        elif choice == '2':
            self.modifyQuantity() # modify the quantity of an item
        # end elif
        elif choice == '3':
            self.modifyMinQuantity() # modify the minimum quantity of an item
        # end elif
        elif choice == '4':
            self.modifyVendorPrice() # modify the vendor price of an item
        # end elif
        elif choice == '5':
            self.modifyMarkup() # modify the markup of an item
        # end elif
        elif choice == '6':
            self.modifyDiscount() # modify the discount percentage of an item
        # end elif
        elif choice == '7':
            self.modifyDiscountByCategory() # modify discount by category
        # end elif
        elif choice == '8':
            self.inventoryMenu() # go back to inventoryMenu()
        # end elif
        return
    # end modifyMenu()

    def getInventoryList(self):
        # get the inventory list
        # param: None
        # return: inventory list
        inventoryList = [] # initilize inventory list (list)
        inputFile = open('inventory.txt', 'r') # open the inventory file for reading
        for line in inputFile: # iterate through every line in file
            item = line.rstrip().split(',') # strip EOL and split by commas (str)
            inventoryList.append(itemInInventory.ItemInInventory(item[0], item[1], item[2], int(item[3]), int(item[4]), float(item[5]), int(item[6]), float(item[7]), int(item[8]), float(item[9]))) # append ItemInInventory object to inventory list using attributes of item from file
        # end for
        inputFile.close() # close the file
        return inventoryList # return the list of items
    # end getInventoryList

    def getCategory(self):
        # gets a category from the user
        # param: None
        # return: null
        choice = misc.getInputString('Choose a category:\n1. FRUIT\n2. VEGETABLE\n3. MEAT\n4. OTHER\n\nEnter choice:\t', ['1', '2', '3', '4']) # get choice from user (str)
        # assign proper category to result
        if choice == '1':
            result = 'FRUIT'
        # end if
        elif choice == '2':
            result = 'VEGETABLE'
        # end elif
        elif choice == '3':
            result = 'MEAT'
        # end elif
        elif choice == '4':
            result = 'OTHER'
        # end elif
        return result # return the result
    # end getCategory

    def categoryReport(self):
        # print a report by category
        # param: None
        # return: null
        #      123456789012345678901234567890123456789012345678901234567890123456789012
        category = self.getCategory() # get the category from user (str)
        count = 0 # initiate count (int)
        self.printHeaders() # print the headers
        for index in range(len(self.inventoryList)): # iterate through inventoryList
            if self.inventoryList[index].category == category: # check if item in list is of chosen category
                print(self.inventoryList[index]) # print the item
                count += 1 # increment count
            # end if
            if count % 24 == 0 and count != 0: # check if 24 have been printed
                input('Press enter to continue') # ask user to press enter to continue
            # end if
        # end for
        return
    # end categoryReport()

    def quantityReport(self):
        # print report by quantity
        # param: None
        # return: null
        quantityChoice = misc.getInputInt('Enter quantity:\t') # get the quantity from the user
        count = 0 # initiate count (int)
        self.printHeaders() # print the headers
        for index in range(len(self.inventoryList)): # iterate through inventoryList
            if self.inventoryList[index].quantity <= quantityChoice: # check if item has the right quantity
                print(self.inventoryList[index]) # print the item
                count += 1 # increment count
                if count % 24 == 0 and count != 0: # check if 24 have been printed
                    input('Press enter to continue') # ask user to press enter to continue
                # end if
            # end if
        # end for
        return
    # end quantityReport()

    def warningReport(self):
        # print rport of all items whose quantity is less than their min quantity
        # param: None
        # return: None
        count = 0 # initiate count (int)
        self.printHeaders() # print the headers
        for index in range(len(self.inventoryList)): # iterate through inventoryList
            if self.inventoryList[index].quantity < self.inventoryList[index].minQuantity: # check if item's quantity is less than minQuantity
                print(self.inventoryList[index]) # print the item
                count += 1 # increment count
                if count % 24 == 0 and count != 0: # check if 24 have been printed
                    input('Press enter to continue') # ask user to press enter to continue
                # end if
            # end if
        # end for
        return
    # end warningReport()       
    
    def allReport(self):
        # print report of all item 
        # param: None
        # return: null
        self.printHeaders() # print the headers
        count = 0 # initialize count (int)
        for index in range(len(self.inventoryList)): # iterate through inventoryList
            print(self.inventoryList[index]) # print the item
            count += 1 # increment count
            if count % 24 == 0 and count != 0: # check if 24 have been printed
                input('Press enter to continue') # ask user to press enter to continue
            # end if
        # end for
        return
    # end allReport()

    def getValidStock(self, msg):
        # get a valid stock value from the user 
        # param: msg is the prompt to be displayed (str)
        # return: null
        exit = False # set exit to false (bool)
        while not(exit): # while exit is not false
            stock = input(msg) # get stock input from user (str)
            if misc.isInteger(stock) and int(stock) >= 0: # check that stock is an integer and is not negative
                exit = True # set exit to false
            # end if
            else:
                print('Invalid input. Try again.') # print error
            # end else 
        # end while 
        return int(stock) 
    # end getValidStock()

    def addStockItem(self):
        # add stock by individual item 
        # param: none 
        # return: null
        item = self.findItem.getItem() # get an item from the user (ItemInInventory)
        addStock = self.getValidStock('Enter amount you would like to add:\t') # get a valid stock from the user (int)
        if misc.confirm(): # get user's confirmation
            if item.quantity <= item.minQuantity: # check if current stock is less than minimum stock
                item.quantity += item.minQuantity + addStock - item.quantity # add the stock to the items quantity
            else:
                item.quantity += addStock # add addStock to item quantity
        # end if
        return
    # end addStock()

    def addStockQuantity(self):
        # add stock to all items below a certain quantity
        # param: None
        # return: null
        minStock = self.getValidStock('Enter minimum amount:\t') # get a valid minStock from the user (int)
        addStock = self.getValidStock('Enter amount to be added:\t') # get a valid amount to be added from user (int)
        if misc.confirm(): # get user's confirmation
            for item in self.inventoryList: # iterate through all items in the inventory
                if item.quantity < minStock and item.quantity <= item.minQuantity: # check if quantity of item is less than minimum stock and item quantity is less equal to its min quantity
                    item.quantity += item.minQuantity + addStock - item.quantity # add the stock to the item's quantity
                # end if
                elif item.quantity < minStock: # if item quantity is less than the min stock
                    item.quantity += addStock # add addStock to item quantity
                # end elif
            # end for
        # end if
        return
    # end addStockQuantity()

    def addStockWarning(self):
        # add stock to all items below their minimum quantity
        # param: None
        # return: null
        addStock = self.getValidStock('Enter amount to be added:\t') # get a valid amount to be added from user (int)
        if misc.confirm(): # get user's confirmation
            for item in self.inventoryList: # iterate through all items in the inventory
                if item.quantity < item.minQuantity: # check if quantity of item is less than its minimum quantity
                    item.quantity += item.minQuantity + addStock - item.quantity # add the stock to the item's quantity
                # end if
            # end for
        # end if
        return
    # end addStockWarning()

    def deleteItem(self):
        # delete an item from the Inventory
        # param: None
        # return null
        item = self.findItem.getItem() # get an item from the user (ItemInInventory)
        if misc.confirm(): # get user's confirmation
            del self.inventoryList[self.inventoryList.index(item)] # delete the item from the inventory
        # end if
        return
    # end deleteItem()

    def exit(self):
        name = "inventory." + datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%d-%m-%y") +".txt" # format name using the date (str)
        os.rename('inventory.txt', name) # renmae inventory file to name
        inventoryFile = open('inventory.txt', 'w') # open inventory file for writing
        for item in self.inventoryList: # iterate through inventoryList
            inventoryFile.write(f'{item.sku},{item.name},{item.category},{item.quantity},{item.minQuantity},{item.vendorPrice},{item.markUp},{item.regularPrice},{item.discount},{item.currentPrice}\n') # write to the inventory file all the items
        # end for
        inventoryFile.close() # close inventory file
        return
    # end exit()

    def getValidName(self):
        # get a valid name from the user 
        # param: None
        # return null
        exit = False # set exit to false (bool)
        while not(exit):
            name = input('Enter name of the item:\t')
            if name != '' and name != ' '*len(name): # if name is not empty or all spaces 
                exit = True # set exit to false
            # end if 
            else:
                print('Name is not valid. Try again.') # print error
            # end else 
        # end while
        return name.strip() # return the name stripped of any leading or trailing whitespaces
    # end getValidName()

    def getValidPrice(self, item=None):
        # get a valid price from the user 
        # param: item is the item to be modified if any (ItemInInventory)
        # return: valid price (float)
        exit = False # set exit to false (bool)
        while not(exit): # while exit is not False
            price = input('Enter the vendor price:\t') # get price from the user (str)
            if (item == None and misc.isNum(price) and float(price) > 0) or (item != None and misc.isNum(price) and float(price) > 0 and round(price*(1+int(item.markUp)/100)*(1-item.discount/100),2) > price): # check price is valid or the sale price is more than the new vendor price
                exit = True # set exit to true
            # end if
            else:
                print('Price is not valid. Try again') # print error message
            # end else 
        # end while
        return round(float(price),2) 
    # end getValidStock()

    def getValidMarkup(self, item=None):
        # get a valid markup percentage from the user 
        # param: item is the item to be modified if any (object)
        # return: markup percentage (int)
        exit = False # set exit to false (bool)
        while not(exit): # while exit is not False
            markup = input('Enter the markup percentage:\t') # get markup from the user (str)
            if (item == None and misc.isInteger(markup) and int(markup) > 0) or (item != None and misc.isInteger(markup) and int(markup) > 0 and round(item.vendorPrice*(1+int(markup)/100)*(1-item.discount/100),2) > item.vendorPrice): # check markup is valid or new markup does not make currentPrice less than the vendor price
                exit = True # set exit to true
            # end if
            else:
                print('Markup is not valid. Try again') # print error message
            # end else 
        # end while
        return int(markup) 
    # end getValidMarkup()

    def getValidDiscount(self, vendorPrice, markup):
        # get a valid disocunt percentage from the user for an individual item
        # param: vendorPrice is the vendor price of the item (float), markUp is the markup percentage of th item (int)
        # return: disocunt percentage (int)
        exit = False # set exit to false (bool)
        while not(exit): # while exit is not False
            discount = input('Enter the discount perecentage:\t') # get discount from the user (str)
            if misc.isInteger(discount) and round(vendorPrice*(1+markup/100)*(1-int(discount)/100),2) > vendorPrice and int(discount) >= 0 and int(discount) < 100: # check disocunt is valid. new sale price is more than vendor price
                exit = True # set exit to true
            # end if
            else:
                print('Discount is not valid. Try again') #print error message
            # end else 
        # end while
        return int(discount) 
    # end getValidDicountp()

    def getValidDiscountBatch(self):
        # get a valid disocunt percentage from the user for a batch of items
        # param: vendorPrice is the vendor price of the item (float), markUp is the markup percentage of th item (int)
        # return: disocunt percentage (int)
        exit = False # set exit to false (bool)
        while not(exit): # while exit is not False
            discount = input('Enter the discount perecentage:\t') # get discount from the user (str)
            if misc.isInteger(discount) and int(discount) >= 0 and int(discount) < 100:
                exit = True # set exit to true
            # end if
            else:
                print('Discount is not valid. Try again') # print error message
            # end else 
        # end while
        return int(discount) 
    # end getValidDicountBatch()

    def getNewSKU(self, category):
        # get a valid new sku 
        # param: category (str)
        # return: sku (str)    
        previousSKU = self.inventoryList[0].sku # store sku of first item (str)
        for item in self.inventoryList[1:]: # iterate through inventory list starting from index 1
            if item.sku[:3] == category[:3] and (item.sku[4:] > previousSKU[4:] or previousSKU[:3] != category[:3]): # if item category is equal to caetgory and item number is greater than previous number of previous category is not equal to the category
                previousSKU = item.sku # set previous sku to item sku
            # end if
        # end for
        result = previousSKU[:4] + f'{int(previousSKU[4:])+1:04}' # get the next sku using the highest existing sku (str)
        return result
    # end getNewSKU()

    def addItem(self):
        # add an item to the Inventory
        # param: None
        # return: null
        name = self.getValidName() # get the name of new item from user (str)
        category = self.getCategory() # get the category from the user (str)
        sku = self.getNewSKU(category) # get the new sku for the item (str)
        quantity = self.getValidStock('Enter the stock of the item:\t') # get the stock of the item from the user (int)
        minQuantity = self.getValidStock('Enter the minimum quantity of the item:\t') # get the minimum quantity of the item (int)
        vendorPrice = self.getValidPrice() # get a valid vendor price from user (float)
        markup = self.getValidMarkup() # get a valid markup from the user (int)
        regularPrice = round(vendorPrice*(1+markup/100), 2) # calculate the regular price (float)
        discount = self.getValidDiscount(vendorPrice, markup) # get valid discount percent from the user (int)
        currentPrice = round(regularPrice*(1-discount/100),2) # calculate the current price of the item (float)
        if misc.confirm(): # get user's confirmation
            self.inventoryList.append(itemInInventory.ItemInInventory(sku, name, category, quantity, minQuantity, vendorPrice, markup, regularPrice, discount, currentPrice)) # append a new item object to the inventory using required attrbiutes
        # end if
        return
    # end addItem()

    def modifyName(self):
        # change the name of a product 
        # param: self 
        # return: null 
        item = self.findItem.getItem() # get the item from the user (ItemInInventory)
        name = self.getValidName() # get the name of the item from the user (str)
        if misc.confirm(): # get user's confirmation
            item.name = name # set the item name to the new name
        # end if
        return
    # end changeName()

    def modifyQuantity(self):
        # change the quantity of the product
        # param: none
        # return: null
        item = self.findItem.getItem() # get the item from the user (ItemInInventory)
        quantity = self.getValidStock('Enter new quantity:\t') # get the new quantity from the user (int)
        if misc.confirm(): # get user's confirmation
            item.quantity = quantity # set the item quantity to the new minimum quantity
        # end if
        return
    # end modifyQuantity()

    def modifyMinQuantity(self):
        # modify the minimum quantity
        # param: None
        # return: null
        item = self.findItem.getItem() # get the item from the user (ItemInInventory)
        minQuantity = self.getValidStock('Enter new minimum quantity:\t') # get the minimum quantity from the user (int)
        if misc.confirm(): # get user's confirmation
            item.minQuantity = minQuantity # set the item minimum quantity to the new minimum quantity
        # end if
        return
    # end modifyMinQuantity()

    def modifyVendorPrice(self):
        # modify the vendor price of an item
        # param: None
        # return: null
        item = self.findItem.getItem() # get the item from the user (ItemInInventory)
        vendorPrice = self.getValidPrice() # get vendor price from the user (float)
        if misc.confirm(): # get user's confirmation
            item.vendorPrice = vendorPrice # set the item vendor price to the new vendor price
            item.regularPrice = round(item.vendorPrice * (1+item.markUp/100),2) # calculate the new regular price
            item.currentPrice = round(item.regularPrice * (1-item.discount/100),2) # calculate the new current price
        # end if
        return
    # end modifyVendorPrice()

    def modifyMarkup(self):
        # modify the markup of an item 
        # param: none 
        # return: null 
        item = self.findItem.getItem() # get the item from the user (str)
        markUp = self.getValidMarkup(item) # get a valid markup percentage from the user (int)
        if misc.confirm(): # get user's confirmation
            item.markUp = markUp # set the item markup to the new markup
            item.regularPrice = round(item.vendorPrice * (1+item.markUp/100),2) # calculate the new regular price
            item.currentPrice = round(item.regularPrice * (1-item.discount/100),2) # calculate the new current price
        # end if
        return
    # end modifyMarkup

    def modifyDiscount(self):
        # modify the discount percentage of an item 
        # param: None
        # return: null
        item = self.findItem.getItem() # get the item from the user (str)
        discount = self.getValidDiscount(item.vendorPrice, item.markUp) # get a valid discount from the user (int)
        if misc.confirm(): # get user's confirmation
            item.discount = discount # set the item discount to the new discount
            item.currentPrice = round(item.regularPrice * (1-item.discount/100),2) # calculate the new current price
        # end if
        return
    # end modifyDiscount()

    def modifyDiscountByCategory(self):
        # put items on sale by category 
        # param: None
        # return: null
        category = self.getCategory() # get a valid category from the user (str)
        discount = self.getValidDiscountBatch() # get a valid discount from the user (int)
        if misc.confirm(): # get user's confirmation
            for item in self.inventoryList:
                if item.regularPrice*(1-discount/100) > item.vendorPrice and item.category == category: # check new sale price is more than vendor price and item category is chosen category
                    item.discount = discount # set the item discount into the new dscount
                    item.currentPrice = round(item.regularPrice * (1-item.discount/100),2) # calculate the new current price
                # end if
            # end for
            return
        # end if
    # end modifyDiscountByCategory()
    
# end Inventory