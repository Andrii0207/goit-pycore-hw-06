from decorator.input_error import input_error


@input_error
def delete_contact(args, address_book):
    name = args[0]

    # if not name in contacts.keys():
    #     return (f"Warning! {name} is not exist in contacts")

    # del contacts[name]
    # return f"Contact '{name}' has been deleted."
    # remove_phone

    record = address_book.find_record(name)

    if not record:
        raise KeyError("f{name} doesn't exist in contacts")

    address_book.delete(name)

    return "Delete successfully"
