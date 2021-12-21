class ItemInInventory:
    # represents an item in the invnetory
    def __init__(self, sku, name, category, quantity, minQuantity, vendorPrice, markUp, regularPrice, discount, currentPrice):
        self.sku = sku # sku of item (str)
        self.name = name # name of item (str)
        self.category = category # category of item (str)
        self.quantity = quantity # quantity of item (int)
        self.minQuantity = minQuantity # minimum quantity of item (int)
        self.vendorPrice = vendorPrice # price of item from vendor (float)
        self.markUp = markUp # % increase from vendor price (int)
        self.regularPrice = regularPrice # regular price of item (float)
        self.discount = discount # discount as percent (int)
        self.currentPrice = currentPrice # sale price of item after mark up and discount (float)
    # end __init__

    def __str__(self):
        price = f'${self.regularPrice:.2f}' # format regularPrice wth $ (str)
        sale = f'${self.currentPrice:.2f}' # format currentPrice with $ (str)
        profit = f'${round(self.currentPrice-self.vendorPrice, 2):.2f}' # calculate profit and format with $ (str)
        return f'{self.sku:<8} {self.name[:20]:<20} {self.category:<9} {self.quantity:>5} {self.minQuantity:>5} {price:>7} {sale:>7} {profit:>6}' # return formatted attributes
    # end __str__
# end ItemInInventory