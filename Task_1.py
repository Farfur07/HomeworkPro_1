class IPhones:
    def __init__(self, model, memory, color, price):
        self.model = model
        self.memory = memory
        self.color = color
        self.price = price


x = IPhones('iPhone X', '256', 'silver', '14000')
y = IPhones('iPhone 12', '256', 'purple', '30000')
z = IPhones('iPhone 13', '256', 'gold', '40000')



print(x.color)
print(y.price)
print(z.memory)

class Customers:
    def __init__(self, name, surname, email, number):
        self.name = name
        self.surname = surname
        self.email = email
        self.number = number

    def __str__(self):
        return f'Customer {self.name} {self.surname}\n {self.email}\n {self.number}'

a = Customers('Mark', 'Mara', 'Marma54@gmail.com', '0958756743')
b = Customers('Alise', 'Yang', 'MGHma74@gmail.com', '0958766749')
print(a.__str__())

class OrdersBox:
    def __init__(self, items):
        if isinstance(items, str):
            items = [items]
            self._needed = set(items)
            self._purchased = set()


    def add_new_items(self, items):
        if isinstance(items, str):
            items = [items]
            self._needed.update(items)

    def list_purchased_items(self):
        return sorted(self._purchased)














#    def __str__(self):
#        return f'Customer {self.name} {self.surname}\n {self.email}\n {self.number} :\n Orders: '


