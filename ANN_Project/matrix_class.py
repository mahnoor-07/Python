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
from dimension import Dimension

class Matrix:
    def __init__(self, dim: Dimension, fill=0.0):
        """Create a matrix with the given number of rows and columns.
        Every element is initialized with the value 'fill' (default = 0). """
        try:
            self.rows = dim.rows
            self.cols = dim.cols
            self.data = [[fill for _ in range(self.cols)] for _ in range(self.rows)]
        except Exception as e:
            raise TypeError(f"Error during matrix creation: {e}")
        
    #  Create matrix from list
    def from_list(lst):
        """Convert a python list into a column matrix."""
        try:
            dim = Dimension(len(lst), 1) # Store the list size as matrix dimensions
            m = Matrix(dim)              # Create a column matrix using those dimensions
            for i, val in enumerate(lst):
                m.data[i][0] = val
            return m
        except Exception as e:
            raise ValueError(f"Cannot convert list to matrix: {e}")

    def to_list(self):
        """Convert a column matrix back to a Python list."""
        try:
            flat = []
            for i in range(self.rows):
                flat.append(self.data[i][0])
            return flat
        except Exception as e:
            raise ValueError(f"Cannot convert matrix to list: {e}")

     #  RANDOMIZE
    def randomize(self):
        """Fill matrix with random values between -1 and 1.
        Useful for initializing neural network weights."""
        try:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] = random.uniform(-1, 1)
        except Exception as e:
            raise RuntimeError(f"Failed to randomize matrix: {e}")
        
    #  MATRIX ADDITION
    def __add__(self, other):
        """Matrix addition (same size only)."""
        try:
            result = Matrix(Dimension(self.rows, self.cols))
            if isinstance(other, Matrix):
                if self.rows != other.rows or self.cols != other.cols:
                    raise ValueError("Matrix sizes do not match for addition.")

                for i in range(self.rows):
                    for j in range(self.cols):
                        result.data[i][j] = self.data[i][j] + other.data[i][j]
            else:
            # Scalar addition
                for i in range(self.rows):
                    for j in range(self.cols):
                        result.data[i][j] = self.data[i][j] + other

            return result
        except Exception as e:
            raise ValueError(f"Error during matrix addition: {e}")   

    #  MATRIX SUBTRACTION
    def __sub__(self, other):
        """Return new matrix = a - b."""
        try:
            result = Matrix(Dimension(self.rows, self.cols))

            if isinstance(other, Matrix):
                if self.rows != other.rows or self.cols != other.cols:
                    raise ValueError("Matrix sizes do not match for -.")

                for i in range(self.rows):
                    for j in range(self.cols):
                        result.data[i][j] = self.data[i][j] - other.data[i][j]
            else:  # scalar
                for i in range(self.rows):
                    for j in range(self.cols):
                        result.data[i][j] = self.data[i][j] - other
            return result
        except Exception as e:
            raise ValueError(f"Error during matrix subtraction: {e}")
        
    #  SCALAR MULTIPLICATION
    def __mul__(self, other):
        """Scalar multiplication only."""
        try:
            if isinstance(other, Matrix):
                raise TypeError("Use dot() for matrix multiplication.")
            result = Matrix(Dimension(self.rows, self.cols))

            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        except Exception as e:
            raise ValueError(f"Error during scalar multiplication: {e}")

    #  MATRIX MULTIPLICATION
    def dot(a, b):
        """Matrix multiplication: result = a * b"""
        try:
            if a.cols != b.rows:
                raise ValueError("Incompatible matrix sizes for multiplication.")

            result = Matrix(Dimension(a.rows, b.cols))

            for i in range(a.rows):
                for j in range(b.cols):
                    sum_val = 0
                    for k in range(a.cols):
                        sum_val += a.data[i][k] * b.data[k][j]
                    result.data[i][j] = sum_val
            return result
        except Exception as e:
            raise ValueError(f"Error during matrix multiplication: {e}")

    # ELEMENT-WISE MULTIPLICATION 
    @staticmethod
    def multiply_elementwise(a, b):
        """Element-wise multiplication (Hadamard product)."""
        try:
            if a.rows != b.rows or a.cols != b.cols:
                raise ValueError("Size mismatch in element-wise multiplication")

            result = Matrix(Dimension(a.rows, a.cols))

            for i in range(a.rows):
                for j in range(a.cols):
                    result.data[i][j] = a.data[i][j] * b.data[i][j]

            return result
        except Exception as e:
            raise ValueError(f"Error during element-wise multiplication: {e}")

    #  ELEMENT-WISE ACTIVATION MAP
    def map(self, func):
        """Apply a function to each element.
        Example: applying sigmoid activation to all values."""
        try:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] = func(self.data[i][j])
        except Exception as e:
            raise ValueError(f"Error applying map(): {e}")
    # Element-wise Map (returns new matrix)
    def map_static(matrix, func):
        """Return a new matrix with function applied."""
        try:
            result = Matrix(Dimension(matrix.rows, matrix.cols))
            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    result.data[i][j] = func(matrix.data[i][j])
            return result
        except Exception as e:
            raise ValueError(f"Error in map_static(): {e}")

    #  MATRIX TRANSPOSE
    def transpose(matrix):
        """Transpose a matrix."""
        try:
            result = Matrix(Dimension(matrix.cols, matrix.rows))
            for i in range(matrix.rows):
                for j in range(matrix.cols):
                    result.data[j][i] = matrix.data[i][j]
            return result
        except Exception as e:
            raise ValueError(f"Error during transpose: {e}")