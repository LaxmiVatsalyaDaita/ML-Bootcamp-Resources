# Homework
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
# w1 = 1, w2 = 1, b = -0.5
def ORlogic(x):
    w = np.array([1, 1])
    b = -1.5
    return perceptron(x, w, b)
    
    
# testing
test1 = np.array([0,1])
test2 = np.array([1,1])
test3 = np.array([0,0])
test4 = np.array([1,0])

print("OR({}, {}) = {}".format(0 , 1, ORlogic(test1))) 
print("OR({}, {}) = {}".format(1, 1, ORlogic(test2)))
print("OR({}, {}) = {}".format(0, 0, ORlogic(test3))) 
print("OR({}, {}) = {}".format(1, 0, ORlogic(test4)))