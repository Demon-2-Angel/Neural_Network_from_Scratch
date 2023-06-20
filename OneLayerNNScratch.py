inputs =[1,2,3,2.5]
weight1 = [0.2,0.8,-0.5,1]
weight2 = [0.5,-0.91,0.26, -0.5]
weight3 = [-0.26, -0.27, 0.17, 0.87]

bias1 =2
bias2 =3
bias3 =0.5

output =[
    #Neuron1
         inputs[0]*weight1[0]+
         inputs[1]*weight1[1]+
         inputs[2]*weight1[2]+ bias1,

    #Neuron2
         inputs[0]*weight2[0]+
         inputs[1]*weight2[1]+
         inputs[2]*weight2[2]+ bias2,

    #Neuron3
         inputs[0]*weight3[0]+
         inputs[1]*weight3[1]+
         inputs[2]*weight3[2]+ bias3,
]

print("Hardcode :",output)

#another method write

inputs =[1,2,3,2.5]

weights = [
        [0.2,0.8,-0.5,1],
        [0.5,-0.91,0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]
    ]
biases =[2,3,0.5]

#Whole Output layer
layered_output = []

#For each Neuron
for neuron_weights, neuron_bias in zip(weights,biases):
    #Zeroed Output of Given Neuron
    neuron_output =0
    for n_input, weight in zip(inputs,neuron_weights):
        neuron_output += n_input*weight
    #adding bias to whole neuron output
    neuron_output += neuron_bias

    #Put neuron's result to the layer's output list
    layered_output.append(neuron_output)

print("Looped neuron: ",layered_output)

import numpy as np

outputs = np.dot(weights, inputs) + biases

print("Numpy implimentation of a single layer: ",outputs)