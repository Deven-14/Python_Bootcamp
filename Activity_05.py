def input_5_numbers():
    numbers = list(map(int, input("Enter 5 numbers: ").strip().split()))
    return numbers[:5]

def output_total(total):
    print("The sum of all the numbers is = ", total)

def main():
    numbers = input_5_numbers()
    total = sum(numbers)
    output_total(total)

if __name__ == "__main__":
    main()
