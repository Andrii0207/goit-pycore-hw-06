from decorator.input_error import input_error


@input_error
def show_phone(args, contacts):
    name = args[0]

    # print("show_contacts:", contacts)
    # for key, value in contacts.items():
    #     if key == args[0]:
    #         print(f"Result \n>>> {key}: {value}")
    #         break
    #     return f"There's no phone number {args[0]} in contacts"

    # if not name in contacts:
    #     raise KeyError(f"There is no contact with name {name}")
    # return contacts[name]

    result = contacts.find_record(name)

    if not result:
        raise KeyError("f{name} doesn't exist in contacts")

    return result
