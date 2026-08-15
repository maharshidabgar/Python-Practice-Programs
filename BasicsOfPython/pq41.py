'''Create Account class with 2 Attributes - Balance & Account no.
Create methods for debit, credit & printing thr balance.'''

class Account:

    def __init__(self, bal, accno):

        self.bal = bal
        self.accno = accno

    # Debit - Method
    def debit(self, amount):

        self.bal -= amount

        print("Rs. ",amount, "was Debited from your Account !")

        print("Your Account Current Balance = ", self.getBal())

    # Credit - Method
    def credit(self, amount):

        self.bal += amount

        print("Rs. ", amount, "was Credited from your Account !")

        print("Current Balance = ", self.getBal())

    # Printing Balance Method

    def getBal(self):

        return self.bal

acc = Account(45000, 3521174589)

acc.debit(4000) # Upad

acc.credit(6000) # Jama
