class Address:
    def __init__(self, city):
        self.city = city
        
        
class Person:
    def __init__(self, name, city):
        self.name = name
        self.address = Address(city)

    def show(self):
        print(self.name, self.address.city)
p1 = Person("Tobias", "New York")
p1.show()
