import numpy as np

def unitstep(v):
    if v >= 0:
        return 1
    else:
        return 0
    
def perceptron(x, w, b):
    v = np.dot(w, x) + b
    y = unitstep(v)
    return y

# logic function
def NOTlogic(x):
    w = -1
    b = 0.5
    return perceptron(x, w, b)
    
    
# testing
test1 = np.array(1)
test2 = np.array(0)

print("NOT({}) = {}".format(1, NOTlogic(test1))) 
print("NOT({}) = {}".format(0, NOTlogic(test2)))