from matrix_class import Matrix
from dimension import Dimension


class Trainer:
    
    def __init__(self, network, learning_rate=0.1):
        try:
            self.net = network
            self.lr = float(learning_rate)  # prevent type errors
        except Exception as e:
            raise TypeError(f"Trainer initialization failed: {e}")

    # TRAINING FUNCTION (BACKPROPAGATION)
    def train(self, input_list, target_list):
        """Trains the network using ONE iteration of backpropagation."""
        try:
            # Convert input to Matrix
            inputs = Matrix.from_list(input_list)
        except Exception as e:
            raise ValueError(f"Invalid training input: {e}")

        # FEEDFORWARD (store the output)
        try:
            outputs = [inputs]  # store outputs of each layer

            for idx, layer in enumerate(self.net.layers):
                try:
                    # Weighted sum: W * x + b
                    z = Matrix.dot(layer.weights, outputs[-1])
                    z = z + layer.bias
                except Exception as e:
                    raise RuntimeError(f"Feedforward failed at layer {idx}: {e}")

                try:
                    # Activation
                    z.map(layer.activation)
                except Exception as e:
                    raise RuntimeError(
                        f"Activation failed at layer {idx}: {e}"
                    )

                outputs.append(z)

        except Exception as e:
            raise RuntimeError(f"Feedforward pass failed: {e}")

        # Convert target to Matrix
        try:
            target = Matrix.from_list(target_list)
        except Exception as e:
            raise ValueError(f"Invalid target list: {e}")

        # INITIAL ERROR = target - output
        try:
            errors = target - outputs[-1]
        except Exception as e:
            raise RuntimeError(f"Error calculation failed: {e}")

        # BACKPROPAGATION
        try:
            for i in reversed(range(len(self.net.layers))):

                layer = self.net.layers[i]
                out = outputs[i + 1]       # output of this layer
                prev_out = outputs[i]      # input to this layer

                # 1. Compute gradient: d(sigmoid) * error * lr
                try:
                    gradient = Matrix.map_static(out, layer.dactivation)
                    gradient = Matrix.multiply_elementwise(gradient, errors)
                    gradient = gradient * self.lr
                except Exception as e:
                    raise RuntimeError(
                        f"Gradient calculation failed at layer {i}: {e}"
                    )

                # 2. Weight delta = gradient . prev_out^T
                try:
                    prev_out_T = Matrix.transpose(prev_out)
                    weight_delta = Matrix.dot(gradient, prev_out_T)
                except Exception as e:
                    raise RuntimeError(
                        f"Weight delta failed at layer {i}: {e}"
                    )

                # 3. Update weights and biases
                try:
                    layer.weights = layer.weights + weight_delta
                    layer.bias = layer.bias + gradient
                except Exception as e:
                    raise RuntimeError(
                        f"Updating weights/bias failed at layer {i}: {e}"
                    )

                # 4. Compute error for previous layer
                if i != 0:
                    try:
                        wT = Matrix.transpose(layer.weights)
                        errors = Matrix.dot(wT, errors)
                    except Exception as e:
                        raise RuntimeError(
                            f"Backprop error propagation failed at layer {i}: {e}"
                        )

        except Exception as e:
            raise RuntimeError(f"Backpropagation failed: {e}")
