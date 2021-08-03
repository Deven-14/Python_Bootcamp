def input_2_numbers():
    numbers = [int(num) for num in input("Enter 2 numbers: ").strip().split()]
    return numbers[:2]

def add(num1, num2):
    return (num1 + num2)

def output_total(num1, num2, total):
    print("{} + {} = {}".format(num1, num2, total))

def main():
    num1, num2 = input_2_numbers()
    total = add(num1, num2)
    output_total(num1, num2, total)

if __name__ == "__main__":
    main()
