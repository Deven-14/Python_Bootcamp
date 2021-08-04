
def input_list_of_strings():
    list_of_strings = input("Enter space separated strings: ").split()
    return list_of_strings

if __name__ == "__main__":
    list_of_strings = input_list_of_strings()
    list_of_strings.sort()
    new_list_of_strings = sorted(list_of_strings)
    print("Sorted list using sort(): ", list_of_strings)
    print("Sorted list using sorted(): ", new_list_of_strings)
