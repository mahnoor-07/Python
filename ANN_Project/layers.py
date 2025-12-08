from matrix_class import Matrix
from dimension import Dimension
import math

# ACTIVATION FUNCTIONS
def sigmoid(x):
    """Sigmoid activation function."""
    try:
        return 1 / (1 + math.exp(-x))
    except Exception as e:
        raise ValueError(f"Sigmoid error: {e}")

def dsigmoid(y):
    """Derivative of sigmoid.
    Input must be sigmoid(x)."""
    try:
        return y * (1 - y)
    except Exception as e:
        raise ValueError(f"dSigmoid error: {e}")

# LAYER CLASS
class Layer:
    """A single neural network layer."""

    def __init__(self, input_size, output_size,
                 activation=sigmoid, dactivation=dsigmoid):
        """ Creates a fully-connected layer:
        weights: output_size x input_size
        bias:    output_size x 1"""
        try:
            # Store sizes
            self.input_size = input_size
            self.output_size = output_size

            # Initialize weights using Dimension class
            self.weights = Matrix(Dimension(output_size, input_size))
            self.weights.randomize()

            # Initialize bias
            self.bias = Matrix(Dimension(output_size, 1))
            self.bias.randomize()

            # Store activation functions
            self.activation = activation
            self.dactivation = dactivation

        except Exception as e:
            raise RuntimeError(f"Layer initialization failed: {e}")
