
class BankFast:
    def __init__(self, balance=0):
        self.balance = balance

    def run(self):
        while True:
            if self.choice == 1:
                money = int(input('enter the amount to deposit\n'))
                self.balance = self.balance + money
            elif self.choice == 2:
                money = int(input('enter the amount of money to withdraw:'))
                if self.balance > money:
                    self.balance = self.balance - money
                    print('Take your money, please...')
                else:
                    print('you do not have enough money...')
            elif self.choice == 3:
                print(f'The balance is {self.balance}')
            else:
                print('Your choice is not allowed')

            self.choice = int(input('1>deposit\n 2>withdraw\n 3> check balance\n'))

bank = BankFast()
bank.choice = int(input('1>deposit\n 2>withdraw\n 3> check balance\n'))
bank.run()
