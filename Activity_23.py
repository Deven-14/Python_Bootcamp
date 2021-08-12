from itertools import combinations_with_replacement as cwr

def get_num_str():
    num_str = input("Enter a series of numbers: ").strip()
    return num_str

def create_string_comb(comb):
    string_comb = []

    temp_comb = []
    for ele in comb:
        len_ = len(ele)
        temp_comb.append([])
                
    return string_comb

def get_combination(num_str):
    keypad = {'2': "ABC", '3': "DEF", '4': "GHI", '5': "JKL", '6': "MNO",
              '7': "PQRS", '8': "TUV", '9': "WXYZ"}

    comb = [[] for _ in range(len(num_str))]
    len_num_str = len(num_str)
    i = 0

    comb_len = []
    prev_ele = ["", 0]
    for i, ele in enumerate(num_str):
        if prev_ele[0] == ele:
            prev_ele[1] += 1
        else:
            prev_ele = [ele, 1]
            comb_len.append(prev_ele)

    print(comb_len)

    temp_comb = []
    for ele in comb_len:
        temp = []
        for i in range(ele[1]):
            temp.append(["".join(t) for t in cwr(keypad[ele[0]][:ele[1]], ele[1]-i)])
        temp_comb.append(temp)

    print(temp_comb)
    
    return comb_len


def output(combinations):
    for ele in combinations:
        print(ele, end=', ')

if __name__ == "__main__":
    num_str = get_num_str()
    comb = get_combination(num_str)
    output(comb)
