
def input_list_of_tuples():
    n = int(input("Enter the number of tuple of strings to be entered: "))
    list_of_tuple_of_strings = []
    
    for _ in range(n):
        string1, string2 = input("Enter 2 space separated strings: ").split()
        list_of_tuple_of_strings.append((string1, string2))
        
    return list_of_tuple_of_strings

def list_of_tuples_to_concatinated_string(list_of_tuples):
    return ';'.join(['='.join(ele) for ele in list_of_tuples])

if __name__ == "__main__":
    list_of_tuple_of_strings = input_list_of_tuples()
    concatinated_string = list_of_tuples_to_concatinated_string(list_of_tuple_of_strings)
    print(concatinated_string)
