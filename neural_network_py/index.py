import numpy as np
import random
import math

# activation function
def treshold(x):
    if(x <= 0):
        return 0
    else:
        return 1


def count_output_perceptron(input_array, input_weights, bias_weight):
    inputs = input_array
    in_o = np.dot(inputs, input_weights) + bias_weight
    print(in_o)
    for input in in_o:
        out_o = treshold(input)
        print(out_o)


# OR
input_features = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output_target_or = np.array([[0, 1, 1, 1]])
# reshape output to a vector
output_target_or = output_target_or.reshape(4, 1)
# normally assign random weights to the input. Later will be modiefied to be more optimized
input_weights = np.array([[1], [1]])
# normally bias weight the same as input weights is assign to random at first, later will be optimized (value of bias = 1)
bias = 1
bias_weight = -0.5

count_output_perceptron(input_features, input_weights, bias_weight)

# AND
print("AND___________________________________________")
bias_weight = -1.5
output_target_and = np.array([[0, 0, 0, 1]]).reshape(4, 1)
count_output_perceptron(input_features, input_weights, bias_weight)

# NOT
print("NOT___________________________________________")
input_features = np.array([[0, 1]]).reshape(2, 1)
print(input_features)
output_target_not = np.array([[1, 0]]).reshape(2, 1)
print(output_target_not)
input_weight = -2
bias_weight = 1

count_output_perceptron(input_features, input_weight, bias_weight)

# XOR
print("XOR____________________________________________")

# note that this only works for a single layer of depth
INPUT_NODES = 2
OUTPUT_NODES = 1
HIDDEN_NODES = 2

# 15000 iterations is a good point for playing with learning rate
MAX_ITERATIONS = 130000

# setting this too low makes everything change very slowly, but too high
# makes it jump at each and every example and oscillate. I found .5 to be good
LEARNING_RATE = .2


class network:
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        self.total_nodes = input_nodes + hidden_nodes + output_nodes
        self.learning_rate = learning_rate

        # set up the arrays
        self.values = np.zeros(self.total_nodes)
        self.expectedValues = np.zeros(self.total_nodes)
        self.thresholds = np.zeros(self.total_nodes)

        # the weight matrix is always square
        self.weights = np.zeros((self.total_nodes, self.total_nodes))

        # set random seed! this is so we can experiment consistently
        random.seed(10000)

        # set initial random values for weights and thresholds
        # this is a strictly upper triangular matrix as there is no feedback
        # loop and there inputs do not affect other inputs
        for i in range(self.input_nodes, self.total_nodes):
            self.thresholds[i] = random.random() / random.random()
            for j in range(i + 1, self.total_nodes):
                self.weights[i][j] = random.random() * 2

    def process(self):
        # update the hidden nodes
        for i in range(self.input_nodes, self.input_nodes + self.hidden_nodes):
            # sum weighted input nodes for each hidden node, compare threshold, apply sigmoid
            W_i = 0.0
            for j in range(self.input_nodes):
                W_i += self.weights[j][i] * self.values[j]
            W_i -= self.thresholds[i]
            self.values[i] = 1 / (1 + math.exp(-W_i))

        # update the output nodes
        for i in range(self.input_nodes + self.hidden_nodes, self.total_nodes):
            # sum weighted hidden nodes for each output node, compare threshold, apply sigmoid
            W_i = 0.0
            for j in range(self.input_nodes, self.input_nodes + self.hidden_nodes):
                W_i += self.weights[j][i] * self.values[j]
            W_i -= self.thresholds[i]
            self.values[i] = 1 / (1 + math.exp(-W_i))

    def processErrors(self):
        sumOfSquaredErrors = 0.0

        # we only look at the output nodes for error calculation
        for i in range(self.input_nodes + self.hidden_nodes, self.total_nodes):
            error = self.expectedValues[i] - self.values[i]
            # print error
            sumOfSquaredErrors += math.pow(error, 2)
            outputErrorGradient = self.values[i] * (1 - self.values[i]) * error
            # print outputErrorGradient

            # now update the weights and thresholds
            for j in range(self.input_nodes, self.input_nodes + self.hidden_nodes):
                # first update for the hidden nodes to output nodes (1 layer)
                delta = self.learning_rate * \
                    self.values[j] * outputErrorGradient
                # print delta
                self.weights[j][i] += delta
                hiddenErrorGradient = self.values[j] * (
                    1 - self.values[j]) * outputErrorGradient * self.weights[j][i]

                # and then update for the input nodes to hidden nodes
                for k in range(self.input_nodes):
                    delta = self.learning_rate * \
                        self.values[k] * hiddenErrorGradient
                    self.weights[k][j] += delta

                # update the thresholds for the hidden nodes
                delta = self.learning_rate * -1 * hiddenErrorGradient
                # print delta
                self.thresholds[j] += delta

            # update the thresholds for the output node(s)
            delta = self.learning_rate * -1 * outputErrorGradient
            self.thresholds[i] += delta
        return sumOfSquaredErrors


class sampleMaker:
    def __init__(self, network):
        self.counter = 0
        self.network = network

    def setXor(self, x):
        if x == 0:
            self.network.values[0] = 1
            self.network.values[1] = 1
            self.network.expectedValues[4] = 0
        elif x == 1:
            self.network.values[0] = 0
            self.network.values[1] = 1
            self.network.expectedValues[4] = 1
        elif x == 2:
            self.network.values[0] = 1
            self.network.values[1] = 0
            self.network.expectedValues[4] = 1
        else:
            self.network.values[0] = 0
            self.network.values[1] = 0
            self.network.expectedValues[4] = 0

    def setNextTrainingData(self):
        self.setXor(self.counter % 4)
        self.counter += 1


# start of main program loop, initialize classes
net = network(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, LEARNING_RATE)
samples = sampleMaker(net)

for i in range(MAX_ITERATIONS):
    samples.setNextTrainingData()
    net.process()
    error = net.processErrors()

    # prove that we got the right answers(ish)!
    if i > (MAX_ITERATIONS - 5):
        output = (net.values[0], net.values[1],
                  net.values[4], net.expectedValues[4], error)
        print(output)

# display final parameters
print('number of input')
print(INPUT_NODES)
print('weights')
print(net.weights)
print('second')
print(net.thresholds)


# XNOR
print("XNOR____________________________________________")


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def initialize_parameters(n_x, n_h, n_y):
    W1 = np.random.randn(n_h, n_x)
    b1 = np.zeros((n_h, 1))
    W2 = np.random.randn(n_y, n_h)
    b2 = np.zeros((n_y, 1))

    parameters = {"W1": W1, "b1": b1,
                  "W2": W2, "b2": b2}
    return parameters


def forward_propagation(X, Y, parameters):
    m = X.shape[1]
    W1 = parameters["W1"]
    W2 = parameters["W2"]
    b1 = parameters["b1"]
    b2 = parameters["b2"]
    Z1 = np.dot(W1, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    cache = (Z1, A1, W1, b1, Z2, A2, W2, b2)
    logprobs = np.multiply(np.log(A2), Y) + \
        np.multiply(np.log(1 - A2), (1 - Y))
    cost = -np.sum(logprobs) / m
    return cost, cache, A2


def backward_propagation(X, Y, cache):
    m = X.shape[1]
    (Z1, A1, W1, b1, Z2, A2, W2, b2) = cache

    dZ2 = A2 - Y
    dW2 = np.dot(dZ2, A1.T) / m
    db2 = np.sum(dZ2, axis=1, keepdims=True)

    dA1 = np.dot(W2.T, dZ2)
    dZ1 = np.multiply(dA1, A1 * (1 - A1))
    dW1 = np.dot(dZ1, X.T) / m
    db1 = np.sum(dZ1, axis=1, keepdims=True) / m

    gradients = {"dZ2": dZ2, "dW2": dW2, "db2": db2,
                 "dZ1": dZ1, "dW1": dW1, "db1": db1}
    return gradients


def update_parameters(parameters, grads, learning_rate):
    parameters["W1"] = parameters["W1"] - learning_rate * grads["dW1"]
    parameters["W2"] = parameters["W2"] - learning_rate * grads["dW2"]
    parameters["b1"] = parameters["b1"] - learning_rate * grads["db1"]
    parameters["b2"] = parameters["b2"] - learning_rate * grads["db2"]
    return parameters


X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
Y = np.array([[0, 1, 1, 0]])  # XOR
n_h = 2
n_x = X.shape[0]
n_y = Y.shape[0]
parameters = initialize_parameters(n_x, n_h, n_y)
num_iterations = 100000
learning_rate = 0.01
losses = np.zeros((num_iterations, 1))

for i in range(num_iterations):
    losses[i, 0], cache, A2 = forward_propagation(X, Y, parameters)
    grads = backward_propagation(X, Y, cache)
    parameters = update_parameters(parameters, grads, learning_rate)

print(parameters)
cost, _, A2 = forward_propagation(X, Y, parameters)
pred = (A2 > 0.5) * 1.0
print(A2)
print(pred)
