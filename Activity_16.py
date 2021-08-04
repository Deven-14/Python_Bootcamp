
def input_concatinated_string():
    string = input("Enter a concatinated string: ");
    return string

if __name__ == "__main__":
    string = input_concatinated_string()
    list_of_strings = [(*ele.split('='), ) for ele in string.split(';')]
    print(list_of_strings)
