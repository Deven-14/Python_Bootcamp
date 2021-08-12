from math import pi

def input_angle():
    angle = int(input("Enter an angle in degrees: "))
    return angle

def degree_to_radian(angle):
    return angle * pi / 180

#def get_next_fact(start, stop, step):
#    fact, num1, num2 = 1, 1, 1
#    for ele in range(start, stop, step):
#        yield fact
#        fact *= (ele+1)*(ele+2)        

def sin(x):
    num = 1
    fact = (num := num*(i+1)*(i+2) for i in range(1, 16, 2))
    elements = [x] + [x ** i / next(fact) for i in range(3, 16, 2)]
    value = sum(elements[::2]) - sum(elements[1::2])
    return value

def output(x, sin_x):
    print(f"sin({x}) = {sin_x}")

if __name__ == "__main__":
    angle = input_angle()
    sin_x = sin(degree_to_radian(angle))
    output(angle, sin_x)
