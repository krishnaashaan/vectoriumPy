import numpy as np

class Vectors:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("Vector must have at least one component")
        self.components = np.array(components, dtype=float)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __len__(self):
        return len(self.components)

    # ADDITION
    def __add__(self, other):
        self._check_dim(other)
        return Vectors(*(self.components + other.components))

    # SUBTRACTION
    def __sub__(self, other):
        self._check_dim(other)
        return Vectors(*(self.components - other.components))

    # SCALAR MULTIPLICATION
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Vectors can only be multiplied by a scalar")
        return Vectors(*(self.components * scalar))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    # MAGNITUDE
    def magnitude(self):
        return np.linalg.norm(self.components)

    # DOT PRODUCT
    def dot(self, other):
        self._check_dim(other)
        return float(np.dot(self.components, other.components))

    # CROSS PRODUCT
    def cross(self, other):
        if len(self) != 3 or len(other) != 3:
            raise ValueError("Cross product is only defined for 3D vectors")
        return Vectors(*np.cross(self.components, other.components))

    # UNIT VECTOR
    def unit_vector(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ZeroDivisionError("Cannot calculate unit vector of a zero vector")
        return Vectors(*(self.components / magnitude))

    # ANGLE BETWEEN VECTORS
    def angle_with(self, other):
        self._check_dim(other)
        denominator = self.magnitude() * other.magnitude()
        if denominator == 0:
            raise ZeroDivisionError("Cannot calculate angle with a zero vector")
        cosine = self.dot(other) / denominator
        cosine = np.clip(cosine, -1, 1)
        return float(np.degrees(np.arccos(cosine)))

    # CONVERSION
    def to_list(self):
        return self.components.tolist()

    # INTERNAL
    def _check_dim(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have same dimensions")
