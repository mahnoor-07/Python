# **ANN Implementation Using a Custom Matrix Class**

### *Artificial Neural Network built from scratch using Python, without external libraries*

## **1. Introduction**

This project implements a **fully functional Artificial Neural Network (ANN)** completely from scratch using Python.
All mathematical operations required for neural network training — including matrix multiplication, addition, transpose, scalar operations, element-wise functions, and backpropagation — are performed using a **self-written Matrix class**, not NumPy.

This project demonstrates:

* Understanding of linear algebra operations
* ANN architecture and feedforward computation
* Backpropagation and gradient descent
* Python OOP design using multiple classes
* Clean modular implementation

## **2. Project Requirements**

The project meets the following core requirements:

### **Write your own Matrix class**

The `Matrix` class includes:

* Matrix creation
* Random initialization
* Matrix addition & subtraction
* Scalar multiplication
* Matrix multiplication (dot product)
* Element-wise multiplication (Hadamard product)
* Element-wise map() for activations
* Matrix transpose
  All operations are implemented manually using loops, NOT external libraries.

### **Implement an ANN using this Matrix class**

The ANN includes:

* Custom `Layer` class
* Custom `Network` class
* Feedforward functionality
* Backpropagation training
* Sigmoid activation + derivative
* Weight updates using gradient descent

### **Train and test the ANN**

## **3. Project Structure**

ANN_Project/
│
├── matrix_class.py       # Full matrix operations (written from scratch)
├── dimension.py          # Stores rows and columns info
├── layers.py             # Layer class + activation functions
├── network.py            # Neural network (manages layers + feedforward)
├── trainer.py            # Backpropagation training logic
├── executor.py           # Safe execution wrapper for the trained model
├── main.py               # Demonstration: training + running ANN
└── README.md             # Project documentation

## **4. Implementation Details**

### **4.1 Matrix Class**

The `Matrix` class is at the core of the ANN.
It implements all foundational operations required for neural networks:

#### **Linear Algebra Operations**

* `__add__()` 
* `__sub__()` 
* `__mul__()`
* `dot()`
* `transpose()` 
* `multiply_elementwise()` 

#### **Activation Support**

* `map()` – Apply a function to every element
* `map_static()` – Return a new matrix with function applied

## **4.2 Neural Network Architecture**

The ANN is built using a layered design:

### **Layer**

Stores:

* Weight matrix
* Bias matrix
* Activation + derivative

### **Network**

Handles:

* Ordering of layers
* Feedforward computation

### **Trainer**

Implements backpropagation:

1. Forward pass
2. Error calculation
3. Gradient computation
4. Weight update
5. Bias update
6. Error propagation to previous layers

## **5. Training Demonstration**

The `main.py` file trains the ANN with:

for _ in range(1000):
    trainer.train([1, 0], [1])

After training, the network is executed:

result = Executor.run(net, [1, 0])
print("ANN Output:", result)

Example output:

ANN Output: [0.9602]


## **6. Key Features**

* **Zero external dependencies** — no NumPy, TensorFlow, PyTorch
* **Pure Python implementation** of ANN math
* **Readable modular architecture**
* **Robust error handling throughout the project**
* **Object-oriented design**


## **7. How to Run**

### **Run the Project**

main.py

The script will:

1. Create and randomize a matrix
2. Build the ANN
3. Train the network
4. Test the output

## **8. Conclusion**

This project successfully demonstrates **the complete implementation of an Artificial Neural Network using only pure Python code and a self-written Matrix class**.