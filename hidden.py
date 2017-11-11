import numpy
from scipy.special import expit


def neural_net():

    # x is XOR input and y is XOR target output
    x = numpy.matrix([[1, 1], [1, 0.0009], [0.0009, 1], [0.0009, 0.0009]])
    y = numpy.matrix([[0], [1], [1], [0]])

    # Forward Pass

    # input layer random weights and hidden layer random weights initialization
    input_layer_weights = numpy.matrix([[0.8, 0.4, 0.3], [0.2, 0.9, 0.5]])
    hidden_layer_weights = numpy.matrix([[0.3, 0.5, 0.9]])
    iterations = 1000

    while iterations:

        for index, elem in enumerate(x):
            # compute the x*weights and take its sigmoid
            hidden_product = elem.dot(input_layer_weights)
            hidden_sigmoid = numpy.matrix(expit(hidden_product))

            # compute the y*weights and take its sigmoid
            output_product = hidden_sigmoid.dot(hidden_layer_weights.T)
            output_predicted = expit(output_product)

            # BackPropagation

            # Error calculation for hidden layer
            total_error = y[index] - output_predicted
            dx_sigmoid = output_predicted*(1 - output_predicted)
            delta_sum = total_error*dx_sigmoid

            # distribution of error in hidden layer weights
            delta_weights = (delta_sum / hidden_sigmoid)*0.7
            new_hidden_weights = numpy.add(hidden_layer_weights, delta_weights)
            print(new_hidden_weights)

            # Error calculation for input layer
            hidden_error = delta_sum / hidden_layer_weights
            dx_ip_sigmoid = numpy.multiply(hidden_sigmoid, 1 - hidden_sigmoid)
            delta_hidden = numpy.multiply(hidden_error, dx_ip_sigmoid)
            delta_ip = numpy.divide(delta_hidden, elem.T)*0.7
            new_input_weights = numpy.add(input_layer_weights, delta_ip)
            print(new_input_weights)

            input_layer_weights = new_input_weights
            hidden_layer_weights = new_hidden_weights
            iterations = iterations - 1


if __name__ == "__main__":
    neural_net()









