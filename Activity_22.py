import math

def input_angle():
    angle = int(input("Enter an angle in degrees: "))
    return angle      

def sin(x):
    value, alternate = 0, 1
    for i in range(1, 16, 2):
        temp = x ** i / math.factorial(i) 
        if alternate:
            value, alternate = value+temp, 0
        else:
            value, alternate = value-temp, 1
    return value

def output(x, sin_x):
    print(f"sin({x}) = {sin_x}")

if __name__ == "__main__":
    angle = input_angle()
    sin_x = sin(math.radians(angle))
    output(angle, sin_x)
