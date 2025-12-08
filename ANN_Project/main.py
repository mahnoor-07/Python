from matrix_class import Matrix
from dimension import Dimension

from layers import Layer
from network import Network
from trainer import Trainer
from executor import Executor


"""This line checks if the file is being run directly.
Code inside this block runs ONLY when you execute main.py yourself,
and it will NOT run when another file imports main.py."""

if __name__ == "__main__":
    print("Creating and randomizing a matrix\n")

    dim = Dimension(3, 3)
    m = Matrix(dim)
    m.randomize()

    for row in m.data:
        print(row)

    # ANN: BUILDING THE LAYER-BASED NETWORK
    print("Building ANN Architecture...")

    # Layer(input_size, output_size)
    l1 = Layer(2, 4)   # First hidden layer
    l2 = Layer(4, 4)   # Second hidden layer
    l3 = Layer(4, 1)   # Output layer

    net = Network(l1, l2, l3)
    trainer = Trainer(net, learning_rate=0.1)

    print("Training ANN")

    # Train on simple example
    for _ in range(1000):
        trainer.train([1, 0], [1])

    # ANN TESTING
    print("Testing ANN with input [1, 0]...")
    result = Executor.run(net, [1, 0])
    
    print("ANN Output:", result)