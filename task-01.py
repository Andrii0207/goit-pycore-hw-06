from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # name vocabulary
    pass


class Phone(Field):
    # phone vocabulary
    # validation 10 digital
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    # add phone number
    # delete phone number
    # change phone number
    # search phone number

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {"".join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self, *arg):
        print(arg)

    def add_record(self):
        print(self)

        # manage contact list
        # add phone record
        # search contact by name

        # Створення нової адресної книги
book = AddressBook("someDate")
print(book)


# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# Виведення: Contact name: John, phones: 1112223333; 5555555555
print(john)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
