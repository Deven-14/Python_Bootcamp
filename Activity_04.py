def input_2_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return (num1, num2)

def output_total(num1, num2, total):
    print("{} + {} = {}".format(num1, num2, total))

def main():
    num1, num2 = input_2_numbers()
    total = num1 + num2
    output_total(num1, num2, total)

if __name__ == "__main__":
    main()
