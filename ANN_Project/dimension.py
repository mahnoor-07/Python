class Dimension:
    """Stores the dimensions (rows and cols) of a matrix."""

    def __init__(self, rows, cols):
        if rows <= 0 or cols <= 0:
            """ValueError is used when the input has the correct type but an invalid value.
            In matrix operations, it is raised when dimensions don't match for addition,
            subtraction, or multiplication. This helps clearly signal invalid matrix sizes."""
            
            raise ValueError("Rows and columns must be positive integers.")

        self.rows = rows
        self.cols = cols
