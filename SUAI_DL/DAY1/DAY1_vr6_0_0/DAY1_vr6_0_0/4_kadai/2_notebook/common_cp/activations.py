import numpy as np
import cupy as cp

def sigmoid(x):
    return 1 / (1+ cp.exp(-x))

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - cp.max(x, axis=0)
        y = cp.exp(x) / cp.sum(cp.exp(x), axis=0)
        return y.T 

    x = x - cp.max(x) # オーバーフロー対策
    return cp.exp(x) / cp.sum(cp.exp(x))

def relu(x):
    return cp.maximum(0, x)

def tanh(x):
    return cp.tanh(x)