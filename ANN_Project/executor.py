from matrix_class import Matrix
from dimension import Dimension

class Executor:
    """Executes a trained network on any input."""

    def run(network, input_list):
        """ Run the network safely and return output list.
        it includes the following steps:
        1. Validate input_list shape
        2. Convert to Matrix
        3. Call network.feedforward()
        4. Convert output back to Python list"""
        try:
            # Step 1
            if not isinstance(input_list, (list, tuple)):
                raise TypeError("Executor.run() expects a list or tuple as input.")
            # Step 2
            input_matrix = Matrix.from_list(input_list)
            # Step 3
            output_matrix = network.feedforward(input_list)

            # Step 4
            return output_matrix.to_list()

        except Exception as e:
            raise RuntimeError(f"Executor failed to run the network: {e}")
