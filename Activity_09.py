import math

def input_lenght_breadth_height():
    length = float(input("Enter the length of the Tromboloid: "))
    breadth = float(input("Enter the Breadth of the Tromboloid: "))
    height = float(input("Enter the height of the Tromboloid: "))
    return length, breadth, height

def calculate_volume(length, breadth, height):
    temp = (breadth ** 2) * (height ** 2)
    characteristic_dimension = length ** 2 + breadth ** 2 + height ** 2
    volume = (temp / math.sqrt(characteristic_dimension))
    return volume

def output_volume(length, breadth, height, volume):
    print(f"The volume of the Tromboloid with length = {length:.3f}, breadth = {breadth:.3f}"
          f" and height = {height:.3f} is = {volume:.3f}")

def get_sphere_radius_given_volume(volume):
    temp = 3 * volume / 4 * math.pi
    return (temp ** (1/3))

def output_sphere_raduis(radius):
    print(f"The radius of the sphere is = {radius:.3f}")

if __name__ == "__main__":
    length, breadth, height = input_lenght_breadth_height()
    volume = calculate_volume(length, breadth, height)
    output_volume(length, breadth, height, volume)
    radius = get_sphere_radius_given_volume(volume)
    output_sphere_raduis(radius)
    
