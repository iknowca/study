from mnist import load_mnist
import pickle
import numpy as np

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = x@W1 + b1
    z1 = sigmoid(a1)
    a2 = z1@W2 + b2
    z2 = sigmoid(a2)
    a3 = z2@W3 + b3
    y = softmax(a3)
    
    return y

if __name__ == "__main__":
    x, t = get_data()
    network = init_network()
    
    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)
        if p == t[i]:
            accuracy_cnt += 1
    
    print("Accuracy: " + str(float(accuracy_cnt)/len(x)))