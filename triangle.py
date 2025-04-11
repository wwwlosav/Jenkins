import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def perimeter(self):
        if self.is_valid():
            return self.a + self.b + self.c
        else:
            return None

    def area(self):
        if self.is_valid():
            s = self.perimeter() / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        else:   
            return None

triangle1 = Triangle(3, 4, 5)
triangle2 = Triangle(5, 12, 13)
triangle3 = Triangle(1, 2, 5)

def main():
    print(f"Периметр первого треугольника: {triangle1.perimeter()}")
    print(f"Площадь первого треугольника: {triangle1.area()}")

    print(f"Периметр второго треугольника: {triangle2.perimeter()}")
    print(f"Площадь второго треугольника: {triangle2.area()}")

    print(f"Периметр третьего треугольника: {triangle3.perimeter()}")
    print(f"Площадь третьего треугольника: {triangle3.area()}")

if __name__ == "__main__":
    main()