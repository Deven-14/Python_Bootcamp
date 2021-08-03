
def input_dictionary():
    n = int(input("Enter the number of key, value pairs to be entered: "))
    dict_ = {}
    for _ in range(n):
        key, value = input("Enter 2 space spearated numbers: ").strip().split()
        dict_[int(key)] = int(value)
    return dict_

def main():
    dict_ = input_dictionary()
    print("dictionary: ", dict_)
    sorted_dict = dict(sorted(dict_.items()))
    #sorted_dict = {*sorted(dict_.items()), } becomes a set
    #sorted_dict = {k: v for k, v in sorted(dict_.items())} becomes a dict
    #so simply pass sorted() to dict() as sorted returns a LIST always, here it'll return a list of tuples
    print("Sorted dictionary: ", sorted_dict)

if __name__ == "__main__":
    main()
