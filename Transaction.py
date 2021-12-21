import miscellaneous as misc # import miscellaneous module
import ItemPurchased as itemPurchased # import ItemPurchased module
import Receipt as rec # import Receipt module
import PaymentType as payType # import PaymentType module
import Payment as pay # import Payment module
import FindItem as find # import the FindItem module

class Transaction:
    # represents a transaction
    def __init__(self, inventoryList):
        self.inventoryList = inventoryList # set the inventory to an inventory attribute (list)
        self.findItem = find.FindItem(self.inventoryList, self.printHeaders, self.printItem) # initilize instance of FindItem class (FindItem)
        self.listOfItems = self.getListOfItems() # get the list of items being purchased to transaction attribute (list)
        if len(self.listOfItems) > 0: # check purchases were actually made
            self.computeSubtotal() # compute subtotal 
            self.computeTax() # compute tax
            self.computeTotal() # compute total
            self.takePayment() # take payment from user
        # end if
    # end __init__()

    def printReceipt(self):
        # print the receipt for the transaction 
        # param: none 
        # return: null
        if len(self.listOfItems) > 0: # check purchases were actually made
            receipt = rec.Receipt(self) # create instance of receipt class (Receipt)
            print(receipt.getReceiptString()) # print the receipt
        # end if
        return 
    # end printReceipt()

    def printHeaders(self):
        # print the headers of item attributes to be displayed 
        # param: None
        # return: Null 
        sku, name, price = 'SKU', 'Name', 'Price' # initialize headers (str)
        print(f'{sku:<8} {name[:20]:<20} {price:>7}') # print formatted headers
        return
    # end printHeaders()

    def printItem(self, item):
        # print relevant attributes of item
        # param: item is the item to be printed (ItemInInventory)
        # return: null
        sale = f'${item.currentPrice:.2f}' # format currentPrice with $ (str)
        print(f'{item.sku:<8} {item.name[:20]:<20} {sale:>7}') # print the formatted attributes
        return
    # end printItem()

    def getValidItem(self):
        # get the the item to be purchased in the inventory list
        # param: none
        # return: index of item
        exit = False # set exit flag to false (bool)
        while not(exit): # while not exit
            item = self.findItem.getItem() # get an item from the user (ItemInInventory)
            if item.quantity > 0: # if item is in stock
                exit = True # exit the loop
            else:
                print('Item is not in stock. Choose a different item.') # print error
        return item # return the itemIndex
    # end getValidItem()

    def getAmount(self, item):
        # get the amount to be purchased
        # param: item is the item in the inventory (ItemInInventory)
        # return: itemAmount (int) 
        exit = False # set exit to false (bool)
        while not(exit): # while not exit
            itemAmount = input(f'There are {item.quantity} in stock.\nEnter the amount you want to purchase:\t') # get the amount to be purchased from the user (str)
            if misc.isInteger(itemAmount) and int(itemAmount) <= item.quantity and int(itemAmount) >= 0: # check if it's valid
                if misc.getInputString('Are you sure this is the right amount? (y/n)\t', ['y', 'n']) == 'y': # get confirmation
                    exit = True # set exit to true
                # end if
            # end if
            else: # not valid
                print('Entered amount is not valid. Try again.') # print amount is not valid
            # end else
        # end while
        return int(itemAmount) # return the itemAmount
    # end getAmount()

    def getListOfItems(self):
        # gets the items to be purchased from the user
        # param: none
        # return list of items to be purchased
        exit = False # set exit flag to false (bool)
        listOfItems = [] # initilize list of items (list)
        print('Find the items you would like to purchase') # print message prompt
        while not(exit): # while not exit
            item = self.getValidItem() # get item index of item to be purchased (ItemInInventory)
            if misc.getInputString('Are you sure you want to purchase this item? (y/n)\t', ['y', 'n']) == 'y': # if it's in stock
                itemAmount = self.getAmount(item) # get the amount the user wants to purchase (int)
                if itemAmount != 0: # make sure amount is not 0
                    listOfItems.append(itemPurchased.ItemPurchased(item.name, item.currentPrice, itemAmount)) # append the ItemPurchased object to listOfitems using the relevant attributes
                    item.quantity -= itemAmount # decrease the amount of the item in stock by the amount purchased
                # end if
            # end if
            choice = misc.getInputString('Would you like to purchase more items? (y/n)\t', ['y', 'n']) # ask if user wants to purchase more items
            if choice == 'n': # if not
                exit = True # set exit to true to exit the loop
            # end if
        # end while
        return listOfItems # return the list of items to be purchased
    # end getListItems()

    def computeSubtotal(self):
        # compute the subtotal of the transaction
        # param: none
        # return subtotal (float)
        self.subtotal = 0.0 # set initial subtotal to 0.0 (float)
        for item in self.listOfItems: # iterate through list of items
            self.subtotal += item.price * item.quantity # add to subtotal the price of each item times its amount
        # end for
        return self.subtotal # return the subtotal
    # end computeSubtotal()

    def computeTax(self):
        # compute the tax of the transaction
        # param: none
        # return tax amount (float)
        self.tax = self.subtotal * misc.TAX # compute the tax from subtotal (float)
        return self.tax # return the tax
    # end computeTax()

    def computeTotal(self):
        # compute the total of the transaction
        # param: none
        # return the total (float)
        self.total = self.subtotal + self.tax # compute the total (float)
        return self.total # return the total
    # end computeTotal()
    
    def takePayment(self):
        # take payments from the user and store in list
        # param: none
        # return null
        self.listOfPayments = [] # initilize list of payments (list)

        amountLeft = round(self.total,2) # set amountLeft to pay to the total rounded to 2 decimals (float)
        exit = False # set exit flag to false (bool)
        while not(exit): # while not exit
            print(f'Amount owed: ${amountLeft:.2f}') # print the amount owed
            choice = misc.getInputString('How would you like to pay?\n1. Cash\n2. Debit\n3. Credit\n\nEnter choice:\t', ['1', '2', '3']) # get how the user would like to pay (str)
            paymentType = payType.PaymentType(choice) # create instance of PaymentType with user's choice (PaymentType)
            amount = self.getAmountPaid(paymentType, amountLeft) # get the amount the user would to pay with that type
            self.listOfPayments.append(pay.Payment(paymentType, amount)) # append to list of payments instance of Payemnt using the paymentsType and amount
            amountLeft = round(amountLeft - amount, 2) # calculate the amount left to be paid
            if round(amountLeft,2) <= 0: # if amountleft is 0
                exit = True # set exit to true
                self.change = -1*amountLeft # calculate the change owed (float)
            # end if
        # end while

        return # return
    # end takePayment()

    def getAmountPaid(self, paymentType, amountLeft):
        # get the amount user wants to pay with the type
        # param: paymentType is type of payement user uses (PayementType), amountLeft is the amount left to be paid (float)
        # return: amount to be paid (float)
        exit = False # set exit flag to false (bool)
        while not(exit): # while not exit
            amount = input('Enter amount:\t') # get the amount from the user (str)
            if misc.isNum(amount) and float(amount) > 0 and len(amount[amount.find('.'):]) <= 3 and paymentType.type == 'CASH': # if the amount is cash and valid: it's a number greater than 0 and doesnt have more than 2 decimals
                exit = True # set exit to true
            # end if
            elif misc.isNum(amount) and float(amount) > 0 and (paymentType.type == 'DEBIT_CARD' or paymentType.type == 'CREDIT_CARD') and amountLeft - float(amount) >= 0 and len(amount[amount.find('.'):]) <= 3: # if the amount is valid and is credit or debit and not more than the amount owed
                exit = True # set exit to true
            # end elif
            else: # otherwise
                print('Entered amount is not valid. Try again') # print amount is not valid
            # end else
        # end while
        return float(amount) # return the amount
    # getAmountPaid
# end Transaction