class Purse:
    def __init__(self, currency, name='Unknown'):
        if currency not in ('USD', 'EUR'):
            raise ValueError
        self.money = 0.00
        self.currency = currency
        self.name = name

    def topUpBalance (self, howmany):
        self.money = self.money + howmany
        return howmany

    def topDownBalance (self, howmany):
        if self.money - howmany < 0:
            print('not enough money')
            raise ValueError('not enough money')
        self.money = self.money - howmany
        return howmany

    def info(self):
        print(self.money)
        return self.money

    def __del__(self):
        print('was deleted')




x = Purse('USD')
y = Purse('EUR', 'Bill')
x.money = 100
y.topUpBalance(10)
x.topUpBalance(200)
print(y.info())
print(x.info())

x.topDownBalance(23)
x.topUpBalance(y.topDownBalance(7))
print(y.info())
print(x.info())