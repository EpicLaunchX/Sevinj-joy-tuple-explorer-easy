

def get_items():
    input_from_user=input("Please enter a list of items separated by commas: ")
    items_list = [item.strip() for item in input_from_user.split(',')]
    items_tuple=tuple(items_list)

    display_tuple(items_tuple)

    return items_tuple

#result=get_items()

#print("Result (as a tuple):", result)

def display_tuple(t):
    print(" Tuple : ", t)


if __name__== "__main__":
    get_items()