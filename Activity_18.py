
def input_string():
    string = input("Enter a string: ");
    return string 

if __name__ == "__main__":
    string = input_string()
    dict_of_strings = {x:y for x, y in (ele.split('=') for ele in string.split(';'))}
    print(dict_of_strings)

    
    
    
#dict_of_strings = {x:y for x, y in [ele.split('=') for ele in string.split(';')]} creating list is redundant here    
    
#dict_of_strings = dict([(*ele.split('='), ) for ele in string.split(';')]) WORKS

#dict_of_strings = {ele.split('=')[0]: ele.split('=')[1] for ele in string.split(';')} works but i think it's bad

#dict_of_strings = {[(*ele.split('='), ) for ele in string.split(';')]} not possible as it gives unhashable list error

#dict_of_strings = {*[(*ele.split('='), ) for ele in string.split(';')], }

#this becomes a set and not a dict coz it'll unpack as { (), (), () } and this is syntax for set

#if we need dict with {} then inside {} it has to of the form x: y
    
#or we can pass a list of tuples to dict() and it'll work fine
    
#dict_of_strings = {x: y for ele in string.split(';') for x, y in zip(*ele.split('='))} this is wrong, it'll give us only the first character
