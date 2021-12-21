import miscellaneous as misc # import miscellaneous module

class Receipt:
    # represents a receipt for a transaction
    def __init__(self, transaction):
        # transaction is the transaction of the receipt (Transaction)
        self.transaction = transaction # set Transaction object to an attribute (Transaction)
        self.cashier = input('Enter your name:\t') # set cashier attribute to inputted name (str)
    # end __init__()

    def getHeading(self):
        # format the heading of the receipt
        # param: none
        # return the formatted section
        # append all that is to be printed to result
        result = f'{misc.LINES}\n' # str
        result += '\n'
        result += f'{misc.STORENAME:^45}\n'
        result += '\n'
        result += f'{misc.LINES}\n'
        result += '\n'
        result += f'Cashier: {self.cashier}\n'
        result += '\n'
        result += f'{misc.LINES}\n'
        result += '\n'
        return result
    # end getHeading
    
    def getItems(self):
        # format the items of the receipt
        # param: none
        # return the formatted section
        result = '' # initialize result (str)
        for item in self.transaction.listOfItems: # iterate through listOfItems
            result += item.__str__() + '\n' # # increment formatted items to result
            result += '\n' 
        # end for
        return result # return the result
    # end getItems

    def getTotals(self):
        # format the totals section of the receipt
        # param: none
        # return the formatted section
        # append all that is to be printed to result
        subtotal = f'${self.transaction.subtotal:.2f}' # format subtotal (str)
        tax = f'${self.transaction.tax:.2f}' # format tax (str)
        total = f'${self.transaction.total:.2f}' # format total (str)
        totalLines = len(total)*'=' # initialize (str) that is the lines printed under the total
        result = misc.LINES + '\n' # str
        result += '\n'
        result += f'{"Subtotal":>23}{subtotal:>22}\n'
        result += '\n'
        result += f'{"Tax":>18}{tax:>27}\n'
        result += '\n'
        result += f'{totalLines:>45}\n'
        result += '\n'
        result += f'{"Total":>20}{total:>25}\n'
        result += '\n'
        return result # return the result
    # end getTotals()
    
    def getPayments(self):
        # format the payment section of the receipt
        # param: none
        # return the formatted section
        # append all that is to be printed to result
        total = f'${self.transaction.total:.2f}' # format total with $ (str)
        totalLines = len(total)*'=' # format total lines (str)
        balance = f'-${self.transaction.change:.2f}' if self.transaction.change != 0 else f'${self.transaction.change*-1:.2f}' # format balance correctly with or without - (str)
        result = '' # initialize result (str)
        for payment in self.transaction.listOfPayments: # iterate throught the list of payments
            # format each payment
            amount = f'-${payment.amount:.2f}' # format amount
            result += f'{"":<15}{payment.paymentType.__str__():<20}{amount:>10}\n'
            result += '\n'
        # end for
        result += f'{totalLines:>45}\n'
        result += '\n'
        result += f'{"Balance":>22}{balance:>23}\n'
        result += '\n'
        return result # return result
    # end getPayements()
    
    def getGoodbye(self):
        # format the goodbye section of the receipt
        # param: none
        # return the formatted section
        goodbye = 'Thanks for shopping!' # initilize goodbye message (str)
        result = misc.LINES + '\n' # str
        result += '\n'
        result += f'{goodbye:^45}\n'
        result += '\n'
        result += misc.LINES
        return result # return the result
    # end getGoodbye

    def getReceiptString(self):
        # add all sections together
        # param: none
        # return the final formatted receipt
        result = self.getHeading() # get the heading
        result += self.getItems() # get the items
        result += self.getTotals() # get the total section
        result += self.getPayments() # get the payemnts section 
        result += self.getGoodbye() # get the goodbye section
        return result # return the result
    # end getReceiptString()
# end Receipt