'''
Write a class vector representing a vector of n dimension. Overload the + and * opretaor which
calculates the sum and the dot(.) product of them.
'''

class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __add__(self, v2):
        if len(self.components) != len(v2.components):
            raise ValueError("Vectors must have the same dimension!")
        return Vector(*[a + b for a, b in zip(self.components, v2.components)])

    def __mul__(self, v2):
        if len(self.components) != len(v2.components):
            raise ValueError("Vectors must have the same dimension!")
        return sum(a * b for a, b in zip(self.components, v2.components))

    def __str__(self):
        return f"{self.components}"


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)   # [5, 7, 9]
print(v1 * v2)   # 32  (dot product: 1*4 + 2*5 + 3*6)