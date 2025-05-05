

def get_items():
    input_from_user=input("Please enter a list of items separated by commas: ")
    items_list=input_from_user.split(",")
    items_tuple=tuple(items_list)

    return items_tuple

result=get_items()

print("Result (as a tuple):", result)