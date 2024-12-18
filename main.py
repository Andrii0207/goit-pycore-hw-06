from parser import parse_input
from handlers import add, all, change, show, delete
from models.address_book import AddressBook
# from models.record import Record


def main():

    contacts_book = AddressBook()

    # record1 = Record("Alex")
    # record1.add_phone("0671234567")
    # record1.add_phone("0501234567")

    # record2 = Record("Oleg")
    # record2.add_phone("0981112233")

    # record3 = Record("Vitaly")
    # record3.add_phone("0662223344")

    print("Welcome to the assistant bot!")

    # contacts = {"John": "0987654321"}

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
            print(all.show_all(args, contacts_book))
        elif command == "delete":
            print(delete.delete_contact(args, contacts_book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
