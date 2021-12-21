class PaymentType:
    # reperesents a paymentType
    def __init__(self, type):
        # type is a number indicating the type (str)
        if type == '1': # if type is 1
            self.type = 'CASH' # type attribute is cash (str)
        # end if
        elif type == '2': # if type is 2
            self.type = 'DEBIT_CARD' # type attribute is debitcard (str)
        # end elif
        elif type == '3': # if type is 3
            self.type = 'CREDIT_CARD' # type attribute is credit card (str)
        # end elif
    # end __init__()

    def __str__(self):
        if self.type == 'CASH': # self.type is CASH 
            result = 'Cash' # set result to cash (str)
        # end if
        elif self.type == 'DEBIT_CARD': # if self.type is debit card
            result = 'Debit Card' # set result to debit card (str)
        # end elif
        elif self.type == 'CREDIT_CARD': # if self.type is credit card
            result = 'Credit Card' # set result to credit card (str)
        # end elif
        return result # return result
    # end __str__()
# end PaymentType()