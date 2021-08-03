
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
    sorted_dict = dict(sorted(dict_.items(), key=lambda kv: kv[1]))
    print("Sorted dictionary: ", sorted_dict)

if __name__ == "__main__":
    main()
