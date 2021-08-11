def get_num_str():
    num_str = input("Enter a series of numbers: ").strip()
    return num_str

def create_string_comb(comb):
    string_comb = []
    
    while(True):
        string_comb.append("".join([str1[0] for str1 in comb]))
        j = len(comb) - 1
        while(j >= 0 and len(comb[j]) == 1):
            j -= 1
            
        if(j == -1):
            break

        del comb[j][0]
        i, j = 0, j+1
        while(i < len(comb[j-1])):
            del comb[j][0]
            if not comb[j]:
                del comb[j]
            else:
                j += 1
            i += 1
                
    return string_comb

def get_combination(num_str):
    keypad = {'2': "ABC", '3': "DEF", '4': "GHI", '5': "JKL", '6': "MNO",
              '7': "PQRS", '8': "TUV", '9': "WXYZ"}

    comb = [[] for _ in range(len(num_str))]
    len_num_str = len(num_str)
    i = 0
    
    while(i < len_num_str):
        
        if(num_str[i] not in keypad):
            i += 1
            continue

        node = comb[i]
        node.append(keypad[num_str[i]][0])
        
        j, k = i+1, 1
        while(j < len_num_str and num_str[j] == num_str[i]):
            node.append(keypad[num_str[i]][k])
            j, k = j+1, ((k+1) % len(keypad[num_str[i]]))
        i += 1

    temp_comb = [ele for ele in comb if len(ele) != 0]
    string_comb = create_string_comb(temp_comb)
    
    return string_comb


def output(combinations):
    for ele in combinations:
        print(ele, end=', ')

if __name__ == "__main__":
    num_str = get_num_str()
    comb = get_combination(num_str)
    output(comb)
