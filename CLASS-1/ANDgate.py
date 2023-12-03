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
# w1 = 1, w2 = 1, b = -1.5
def ANDlogic(x):
    w = np.array([1, 1])
    b = -1.5
    return perceptron(x, w, b)
    
    
# testing
test1 = np.array([0,1])
test2 = np.array([1,1])
test3 = np.array([0,0])
test4 = np.array([1,0])

print("NOT({}) = {}".format(1, ANDlogic(test1))) 
print("NOT({}) = {}".format(0, ANDlogic(test2)))
print("NOT({}) = {}".format(1, ANDlogic(test3))) 
print("NOT({}) = {}".format(0, ANDlogic(test4)))