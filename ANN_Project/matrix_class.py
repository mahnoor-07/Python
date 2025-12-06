"""
This matrix class includes:
- Create matrix
- Random matrix
- Addition
- Subtraction
- Scalar multiplication
- Matrix multiplication
- Element-wise map()
- Transpose"""

import random
import math

class Matrix:
    def __init__(self, rows, cols, fill=0.0):
        """Create a matrix with the given number of rows and columns.
        Every element is initialized with the value 'fill' (default = 0). """
        self.rows = rows
        self.cols = cols
        self.data = [[fill for _ in range(cols)] for _ in range(rows)]

    def from_list(lst):
        """Convert a python list into a column matrix."""
        m = Matrix(len(lst), 1)
        for i in range(len(lst)):
            m.data[i][0] = lst[i]
        return m

    def to_list(self):
        """Convert a column matrix back to a python list."""
        flat = []
        for i in range(self.rows):
            flat.append(self.data[i][0])
        return flat

    def randomize(self):
        """Fill matrix with random values between -1 and 1.
        Useful for initializing neural network weights."""
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random.uniform(-1, 1)

    #  MATRIX ADDITION
    def add(self, other):
        """Matrix addition (same size only)."""
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError("Matrix sizes do not match for addition.")
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += other.data[i][j]
        else:
            # Scalar addition
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += other

    #  MATRIX SUBTRACTION
    def subtract(a, b):
        """Return new matrix = a - b."""
        if a.rows != b.rows or a.cols != b.cols:
            raise ValueError("Matrix sizes do not match for subtraction.")

        result = Matrix(a.rows, a.cols)
        for i in range(a.rows):
            for j in range(a.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]
        return result

    #  SCALAR MULTIPLICATION
    def multiply(self, n):
        """Multiply all matrix elements by scalar n."""
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] *= n

    #  MATRIX MULTIPLICATION
    def dot(a, b):
        """Matrix multiplication: result = a * b"""
        if a.cols != b.rows:
            raise ValueError("Incompatible matrix sizes for multiplication.")

        result = Matrix(a.rows, b.cols)

        for i in range(a.rows):
            for j in range(b.cols):
                sum_val = 0
                for k in range(a.cols):
                    sum_val += a.data[i][k] * b.data[k][j]
                result.data[i][j] = sum_val
        return result

    #  ELEMENT-WISE ACTIVATION MAP
    def map(self, func):
        """Apply a function to each element.
        Example: applying sigmoid activation to all values."""
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    def map_static(matrix, func):
        """Return a new matrix with function applied."""
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.data[i][j] = func(matrix.data[i][j])
        return result

    #  MATRIX TRANSPOSE
    def transpose(matrix):
        """Transpose a matrix."""
        result = Matrix(matrix.cols, matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.data[j][i] = matrix.data[i][j]
        return result