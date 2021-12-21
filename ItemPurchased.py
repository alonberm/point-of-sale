class ItemPurchased:
    # represents an item to be purchased
    def __init__(self, name, price, quantity):
        self.name = name # name of item (str)
        self.quantity = quantity # quantity if item (int)
        self.price = price # sale price of item (float)
    # end __init__()

    def __str__(self):
        price = f'${self.price:.2f}' # format price with $ (str)
        cost = f'${self.price*self.quantity:.2f}' # format total cost with $ (str)         
        return f'{self.quantity:<4} {self.name[:20]:<20} {price:<7} {cost:>11}' # return formatted item attributed
    # end __str__
# end ItemPurchased