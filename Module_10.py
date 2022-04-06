from collections import UserDict

class Field:
    pass


class Name(Field):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.name)


class Phone(Field):

    def __init__(self, phone):
        self.phone = phone

    def __repr__(self):
        return str(self.phone)

    def __str__(self):
        return str(self.phone)


class Record:
    def __init__(self, name: Name, *args):
        self.name = name
        self.phones = []
        for i in args:
            self.phones.append(Phone(i))

    def __str__(self):
        if len(self.phones) > 0:
            return f"Your record Name: {self.name} Phones: {self.phones}"
        return f"Your record Name: {self.name}"

    def add_phone(self, phone: Phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone: Phone):
        self.phone.remove(Phone(phone))

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        self.add_phone(Phone(new_phone))
        self.delete_phone(Phone(old_phone))


class AddressBook(UserDict):

    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name] = record







