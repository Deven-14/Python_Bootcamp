from itertools import groupby, product, combinations_with_replacement as cwr

def get_num_str():
    num_str = input("Enter a series of numbers: ").strip()
    return num_str

def get_combination(num_str):
    keypad = {'2': "ABC", '3': "DEF", '4': "GHI", '5': "JKL", '6': "MNO",
              '7': "PQRS", '8': "TUV", '9': "WXYZ"}
    
    num_group = [(key, len(list(grp))) for key, grp in groupby(num_str)]
    #print(num_group)
    str_group = []
    for ele, length in num_group:
        rank = {key: index+1 for index, key in enumerate(keypad[ele])}
        #print(rank)
        temp = []
        for i in range(1, length+1):
            #print(*cwr(keypad[ele], i), i)
            #for x in cwr(keypad[ele], i):
            #    print(sum(rank[j] for j in x), i, x)
            temp += [x for x in cwr(keypad[ele], i) if sum(rank[j] for j in x) == length]
        str_group.append(temp)

    str_group = [[''.join(j) for j in i] for i in str_group]
    comb = [''.join(x) for x in product(*str_group)]
    #using while to remove the first ele where list len > 1 is wrong (1,2), (3,4), coz we even need 23 which will be lost if we removed so cartesian product
    print(str_group)
    print(comb)
    return comb

if __name__ == "__main__":
    num_str = get_num_str()
    comb = get_combination(num_str)
    print(comb)
