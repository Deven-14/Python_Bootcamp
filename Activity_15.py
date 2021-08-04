
def input_sentense():
    list_of_strings = [string for string in input("Enter a Sentense: ").split()]
    return list_of_strings

if __name__ == "__main__":
    list_of_strings = input_sentense()
    list_of_strings.sort()
    new_list_of_strings = sorted(list_of_strings)
    print("Sorted list using sort(): ", list_of_strings)
    print("Sorted list using sorted(): ", new_list_of_strings)
