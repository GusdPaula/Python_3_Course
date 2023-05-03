# Composition is an specialization of agregation.
# But in it, when an object "father" be erased, all
# relations of the "sons" objects will be erased as well.

class Custumer:
    def __init__(self, name) -> None:
        self.name = name
        self.address = []


    def insert_address(self, street, number):
        self.address.append(Address(street, number))
    
    def insert_external_address(self, external_address):
        self.address.append(external_address)

    
    def list_address(self):
        for address in self.address:
            print(address.street)
            print(address.number)
    
    def __del__(self):
        print('Erasing', self.name)


class Address:
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number

    def __del__(self):
        print('Erasing', self.street, self.number)

maria = Custumer('Maria')
maria.insert_address("Rua 01", 10)

adress_external = Address('Curuca', 16)
maria.insert_external_address(adress_external)

maria.list_address()

del maria

print("END")
