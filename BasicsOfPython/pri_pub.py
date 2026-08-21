class Account:

    def __init__(self, acc_no, acc_pass):

        self.acc_no = acc_no
        self.__acc_pass = acc_pass # Private Data


    def reset_pass(self):

        print(self.__acc_pass) # Password is in the Method = Privately


acc = Account("123456", "gandocho")

print(acc.acc_no) # Publicly Access

print(acc.reset_pass()) # Privately Access

