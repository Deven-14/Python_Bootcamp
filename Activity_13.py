from math import sqrt, ceil

def input_number():
    num = int(input("Enter an integer: "))
    return num


def is_prime(num):
    if(num <= 1):
        return False
    
    for x in range(2, ceil(sqrt(num))):
        if num % x == 0:
            return False
    
    return True


def output(num, is_num_prime):
    if(is_num_prime):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")


if __name__ == "__main__":
    num = input_number()
    is_num_prime = is_prime(num)
    output(num, is_num_prime)
