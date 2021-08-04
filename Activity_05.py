def input_5_numbers():
    numbers = [int(num) for num in input("Enter 5 numbers: ").strip().split()]
    return numbers[:5]

def output_total(total):
    print("The sum of all the numbers is = ", total)

if __name__ == "__main__":
    numbers = input_5_numbers()
    total = sum(numbers)
    output_total(total)
