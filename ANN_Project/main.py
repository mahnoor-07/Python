from matrix_class import Matrix
from dimension import Dimension


"""This line checks if the file is being run directly.
Code inside this block runs ONLY when you execute main.py yourself,
and it will NOT run when another file imports main.py."""

if __name__ == "__main__":
    print("Day 1: Creating and randomizing a matrix\n")

    dim = Dimension(3, 3)
    m = Matrix(dim.rows, dim.cols)
    m.randomize()

    for row in m.data:
        print(row)
