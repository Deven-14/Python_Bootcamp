from math import pi

def input_angle():
    angle = int(input("Enter an angle in degrees: "))
    return angle

def degree_to_radian(angle):
    return angle * pi / 180

def sin(x):
    return (x - (x ** 3 / 6) + (x ** 5 / 120) - (x ** 7 / 5040))

def output(x, sin_x):
    print(f"sin({x}) = {sin_x}")

if __name__ == "__main__":
    angle = input_angle()
    sin_x = sin(degree_to_radian(angle))
    output(angle, sin_x)
