from models.name import Name
from models.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone():
        pass

    def edit_phone():
        pass

    def find_phone(self, phone):
        result = (phone for phone in self.phones if phone.value == phone)

        if not result:
            raise ValueError
        return result

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
