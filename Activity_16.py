
def input_string():
    string = input("Enter a string: ");
    return string

def main():
    string = input_string()
    list_of_strings = [(*ele.split('='), ) for ele in string.split(';')]
    print(list_of_strings)

if __name__ == "__main__":
    main()
