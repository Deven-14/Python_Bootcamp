def input_3_numbers():
    numbers = [float(num) for num in input("Enter 3 numbers: ").strip().split()]
    return numbers[:3]

def max_of_three_numbers(num1, num2, num3):
    if num2 <= num1 >= num3:
        return num1
    elif num2 >= num3:
        return num2
    else:
        return num3

def output(num1, num2, num3, greatest_num):
    print("{} is the greatest number among {}, {} and {}".format(greatest_num, num1, num2, num3))

def main():
    num1, num2, num3 = input_3_numbers()
    greatest_num = max_of_three_numbers(num1, num2, num3)
    output(num1, num2, num3, greatest_num)

if __name__ == "__main__":
    main()
