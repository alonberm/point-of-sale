class Payment:
    # represents a payment
    def __init__(self, PaymentType, amount):
        # PaymentType is the type of payment (PaymentType)
        # amount is the amount paid with that type (flat)
        self.paymentType = PaymentType # set PaymentType object to an attribute (PaymentType)
        self.amount = amount # set amount to attribute (int)
    # end __init__()
# end Payment