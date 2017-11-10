import random
import numpy


class Synapse:
    def __init__(self, inputs):
        self.num_inputs = len(inputs)
        ips = list(inputs)
        ips.append(-1)
        self.inputs = numpy.array(ips)
        self.input_weights = []
        for i in range(0, self.num_inputs+1):
            weight = random.random()
            self.input_weights.append(weight)
        self.input_weights = numpy.array(self.input_weights)

    def assign_input_weights(self, wt):
        self.input_weights = numpy.array(wt)

    def give_synapses(self):
        return self.inputs, self.input_weights


def activation(inputs, weights):
    act = inputs*weights
    act = sum(x for x in act)
    if act > 0:
        return 1
    else:
        return 0


def reset_weight(act, pred, weight, inp):
    err = act - pred
    learning = 0.1
    new_wt = weight + err*inp*learning
    return new_wt


def neural_net():

    X = [[1, 1],
         [1, 0],
         [0, 1],
         [0, 0]]

    Y = [1, 1, 1, 0]
    new_wts = []

    while True:
        for index, elem in enumerate(X):
            input_layer = Synapse(elem)
            if new_wts:
                input_layer.assign_input_weights(new_wts)
            input_1, weight_1 = input_layer.give_synapses()
            act_1 = activation(input_1, weight_1)
            pd_1 = reset_weight(Y[index], act_1, weight_1[0], input_1[0])
            pd_2 = reset_weight(Y[index], act_1, weight_1[1], input_1[1])
            pd_3 = reset_weight(Y[index], act_1, weight_1[-1], input_1[-1])
            new_wts = [pd_1, pd_2, pd_3]
            print(new_wts)



if __name__ == "__main__":
    neural_net()





