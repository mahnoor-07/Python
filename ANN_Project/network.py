from matrix_class import Matrix
from dimension import Dimension

"""Network = A collection of layers.
    This class manages the Layer order, Dimension checking, Feedforward execution"""
class Network:
    def __init__(self, *layers):
        try:
                # Store all layers inside a list
                self.layers = list(layers)
                # Check that each layer fits with the next layer
                # Example: Layer1 output size must match Layer2 input size
                for i in range(len(self.layers) - 1):
                    if self.layers[i].output_size != self.layers[i+1].input_size:
                        raise ValueError("Layer size mismatch!")
        except Exception as e:
            raise TypeError(f"Network initialization failed: {e}")
        
    def feedforward(self, inputs):
        """Send input through every layer one by one."""
        try:
             # Convert input list → column matrix
            output = Matrix.from_list(inputs)
            # Pass through each layer
            for layer in self.layers:
            # Multiply weights with input
                output = Matrix.dot(layer.weights, output)
                # Add bias
                output = output + layer.bias
                # Apply activation function
                output.map(layer.activation)
            # Final output after all layers
            return output
        except Exception as e:
            raise RuntimeError(f"Feedforward failed: {e}")