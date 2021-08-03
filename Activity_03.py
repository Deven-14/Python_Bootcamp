def input_2_strings():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    return (string1, string2)

def concatinate_strings(string1, string2):
    return (string1 + string2)

def output_string(string):
    print(string)

def main():
    string1, string2 = input_2_strings()
    concatinated_string = concatinate_strings(string1, string2)
    output_string(concatinated_string)
    output_string(concatinated_string * 5)

if __name__ == "__main__":
    main()
