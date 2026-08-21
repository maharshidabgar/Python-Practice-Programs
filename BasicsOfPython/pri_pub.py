class Account:

    def __init__(self, acc_no, acc_pass):

        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc = Account("123456", "gandocho")

print(acc.acc_pass)

print(acc)

