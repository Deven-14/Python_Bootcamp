
def input_dictionary():
    n = int(input("Enter the number of key, value pairs to be entered: "))
    dict_ = {}
    for _ in range(n):
        key, value = input("Enter a key and a value: ").split()
        dict_[key] = value
    return dict_

if __name__ == "__main__":
    dict_ = input_dictionary()
    print("dictionary: ", dict_)
    sorted_dict = dict(sorted(dict_.items()))
    print("Sorted dictionary: ", sorted_dict)

#sorted_dict = {k: v for k, v in sorted(dict_.items())} becomes a dict

#sorted_dict = {*sorted(dict_.items()), } becomes a set

#so simply pass sorted() to dict() as sorted returns a LIST always, here it'll return a list of tuples
    
