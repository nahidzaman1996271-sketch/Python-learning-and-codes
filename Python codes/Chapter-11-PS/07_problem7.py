# Override the __len__() method on vector of problem 5 to display the dimension of the 
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
        labels = ['i', 'j', 'k']
        parts = []
        for idx, val in enumerate(self.components):
            sign = '+' if val >= 0 else '-'
            parts.append(f"{sign}{abs(val)}{labels[idx]}")
        return ' '.join(parts)

    def __len__(self):
        return len(self.components)


v1 = Vector(7, 8, 10)
print(v1)        # +7i +8j +10k
print(len(v1))   # 3