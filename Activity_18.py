
def input_string():
    string = input("Enter a string: ");
    return string

def main():
    string = input_string()
    dict_of_strings = dict([(*ele.split('='), ) for ele in string.split(';')])
    #dict_of_strings = {ele.split('=')[0]: ele.split('=')[1] for ele in string.split(';')} works but i think it's bad
    #dict_of_strings = {[(*ele.split('='), ) for ele in string.split(';')]} not possible as it gives unhashable list error
    #dict_of_strings = {*[(*ele.split('='), ) for ele in string.split(';')], }
    #this becomes a set and not a dict coz it'll unpack as { (), (), () } and this is syntax for set
    #if we need dict with {} then inside {} it has to of the form x: y
    #or we can pass a list of tuples to dict() and it'll work fine
    #dict_of_strings = {x: y for ele in string.split(';') for x, y in zip(*ele.split('='))}
    print(dict_of_strings)

if __name__ == "__main__":
    main()
