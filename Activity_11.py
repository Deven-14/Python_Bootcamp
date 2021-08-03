def input_number():
    num = float(input("Enter a number: "))
    return num

def add(num1, num2):
    return (num1 + num2)

def output(num1, num2, total):
    print("{} + {} = {}".format(num1, num2, total))

def main():
    num1 = input_number()
    num2 = input_number()
    total = add(num1, num2)
    output(num1, num2, total)

if __name__ == "__main__":
    main()
