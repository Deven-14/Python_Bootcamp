from itertools import groupby, product, combinations_with_replacement as cwr

def get_num_str():
    return input("Enter a series of numbers: ").strip()

def get_combination(num_str):
    keypad = {'2': "ABC", '3': "DEF", '4': "GHI", '5': "JKL", '6': "MNO",
              '7': "PQRS", '8': "TUV", '9': "WXYZ"}
    n_tms_btn_prsd = {char: index+1 for ele in keypad.values() for index, char in enumerate(ele)}
    
    num_group = [(key, len(list(grp))) for key, grp in groupby(num_str)]
    str_group = []
    
    for ele, freq in num_group:
        temp = []
        for i in range(1, freq+1):
            temp += [x for x in cwr(keypad[ele], i) if sum(n_tms_btn_prsd[char] for char in x) == freq]
        str_group.append([''.join(j) for j in temp])

    comb = [''.join(x) for x in product(*str_group)]
    
    return comb

if __name__ == "__main__":
    num_str = get_num_str()
    comb = get_combination(num_str)
    print(comb)
