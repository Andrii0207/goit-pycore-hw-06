from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        if name in self.data:
            return self.data[name]
