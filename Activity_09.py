import math

class Tromboloid:

    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.height = 0
        self.characteristic_dimension = 0
        self.volume = 0

    def input_lenght_breadth_height(self):
        self.length = float(input("Enter the length of the Tromboloid: "))
        self.breadth = float(input("Enter the Breadth of the Tromboloid: "))
        self.height = float(input("Enter the height of the Tromboloid: "))

    def calculate_volume(self):
        temp = (self.breadth ** 2) * (self.height ** 2)
        self.characteristic_dimension = self.length ** 2 + self.breadth ** 2 + self.height ** 2
        self.volume = (temp / math.sqrt(self.characteristic_dimension))
        return self.volume

    def output_volume(self):
        print(f"The volume of the Tromboloid with length = {self.length:.3f}, breadth = {self.breadth:.3f}"
              f" and height = {self.height:.3f} is = {self.volume:.3f}")

def get_sphere_radius_given_volume(volume):
    temp = 3 * volume / 4 * math.pi
    return (temp ** (1/3))

def output_sphere_raduis(radius):
    print(f"The radius of the sphere is = {radius:.3f}")

def main():
    t = Tromboloid()
    t.input_lenght_breadth_height()
    t.calculate_volume()
    t.output_volume()
    radius = get_sphere_radius_given_volume(t.volume)
    output_sphere_raduis(radius)

if __name__ == "__main__":
    main()
    
