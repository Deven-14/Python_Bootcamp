def input_5_numbers():
    numbers = [int(num) for num in input("Enter 5 numbers: ").split()]
    return numbers[:5]
    
if __name__ == "__main__":
    numbers = input_5_numbers()
    sliced_list = numbers[0:3]
    print("Sliced list: ", sliced_list)
    numbers[0] = numbers[-1] = 0
    sliced_list[0] = sliced_list[-1] = 0
    print("Replaced list1: ", numbers)
    print("Replaced list2: ", sliced_list)

