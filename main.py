from parser import parse_input
from handlers import add, all_contacts, change, show, delete
from models.address_book import AddressBook
from models.record import Record


def main():
    contacts_book = AddressBook()

    record1_init = Record("Alex")
    record1_init.add_phone("0671234567")
    record1_init.add_phone("0501234567")
    contacts_book.add_record(record1_init)

    record2_init = Record("Oleg")
    record2_init.add_phone("0981112233")
    contacts_book.add_record(record2_init)

    record3_init = Record("Vitaly")
    record3_init.add_phone("0662223344")
    contacts_book.add_record(record3_init)

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add.add_contact(args, contacts_book))

        elif command == "change":
            print(change.change_contact(args, contacts_book))

        elif command == "phone":
            print(show.show_phone(args, contacts_book))

        elif command == "all":
            print(all_contacts.show_all(args, contacts_book))

        elif command == "delete":
            print(delete.delete_contact(args, contacts_book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
