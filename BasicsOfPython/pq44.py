'''Create a class Order which stores item & its price.
Use Dunder function __gt__() = greater than function to convoy that:
 order1 > order2 if price of order1 > price of order2'''

class order:

    def __init__(self, item, price):

        self.item = item
        self.price = price

    # Dunder Greater Then Function

    def __gt__(self, ord2):

        return self.price > ord2.price
    
ord1 = order("Chips", 25)
ord2 = order("Cofee", 20)

print(ord1 > ord2) # True