inputs =[1,2,3]
weights = [0.2,0.8,-0.5]
bias =2

output =(inputs[0]*weights[0]+
         inputs[1]*weights[1]+
         inputs[2]*weights[2]+ bias)

print(output)

import numpy as np
inputs =[1,2,3,2.5]
weights1 = [0.2,0.8,-0.5,1]
bias1 =2
outputs = np.dot(weights1, inputs) + bias1

print("Numpy Implimentation of SIngle Neuron: ",outputs)