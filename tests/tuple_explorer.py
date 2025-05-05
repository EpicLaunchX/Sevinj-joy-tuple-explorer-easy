

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


def access_element(t, index):
    try:

        element = t[index]
        return element
    except IndexError:

        return f"Error: Index {index} is out of range."

if __name__ == "__main__":
    t = get_items()
    index = int(input("Enter the index of the element you want to access: "))
    result = access_element(t, index)
    print(result)