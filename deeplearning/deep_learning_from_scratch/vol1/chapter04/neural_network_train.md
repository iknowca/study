# Neural network training


Training means automatically acquiring the optimal values of the weight parameters from the training data. In order for a neural network to learn, it must have a metric, which is called a **loss function**. In other words, training is finding the weight parameters that minimize the loss function.

## Learning from data

Neural networks learn from data. In other words, the values of the weight parameters are automatically determined by looking at the data. In the logic gate implemented with the perceptron, at most three parameters were used. However, in actual neural networks, tens of thousands to hundreds of billions of parameters are used. These parameters cannot be set manually by humans.


When solving a problem, especially when looking for a pattern, it is common for humans to think and find the answer. However, in machine learning, human intervention is minimized, and patterns are found from the collected data.

In the problem of recognizing numbers from images, humans want to extract **features** from the image and learn the pattern of the feature using machine learning techniques. A feature is a transformer designed to accurately extract essential data from input data. Features are usually represented as vectors. SVM, KNN, etc. are used to convert data into vectors using these features and learn using the transformed vectors.

> SVM(Support Vector Machine): Learns linear or non-linear decision boundaries to classify data

> KNN(K-Nearest Neighbors): Finds the K nearest neighbors to the given input vector and classifies them

In machine learning, machines find rules from data. Since it is more efficient to design algorithms from scratch, there is less burden on humans.

In neural networks, images are learned as they are. In machine learning, features are designed by humans, but in neural networks, machines learn features themselves. That's why deep learning is also called end-to-end machine learning.

## Loss function

In neural network learning, the current state is represented by a single metric, which is called a loss function. Learning is the process of finding weight parameters that minimize the loss function. Although various functions can be used as loss functions, mean squared error and cross-entropy error are mainly used.

> The loss function is a metric that indicates how bad the performance of the neural network is.

### Sum of squares for error, SSE
$$
E = \frac{1}{2} \sum_{k} (y_k - t_k)^2
$$
```python
def sum_of_squares_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)
```
The sum of squares is the most commonly used loss function. $y_k$ represents the output of the neural network, $t_k$ represents the correct label, and $k$ represents the dimension of the data.

### Cross-entropy error
$$
E = -\sum_{k} t_k \log y_k
$$
```python
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
```

$y_k$ is the output of the neural network, and $t_k$ is the one-hot encoded correct label. Therefore, the cross-entropy error function becomes a formula that calculates the natural logarithm of the estimate.

## mini-batch learning


In machine learning, learning is the process of finding parameters that reduce the value of the loss function for training data. However, to do this, the loss function must be calculated for all training data. The cross-entropy error function for N data is as follows:

$$
E = -\frac{1}{N} \sum_n \sum_k t_{nk} \log y_{nk}
$$


However, the problem is that if the sum of the loss function is calculated for all data, too much time and computational power are required. In this case, some data can be selected and used as an approximation of the whole. These are called **mini-batches**.

A source code for mini-batches can be found [here](./src/mini-batch.ipynb).

## Why use a loss function


Why should we use a loss function? Wouldn't it be more intuitive to use an accuracy function?


In neural network learning, the goal is to find the parameter values that **minimize the loss function** as much as possible. To do this, the **derivative** of the parameters is calculated during learning, and the parameter values are updated based on the derivative values.


Here, the derivative of the weight parameter means how the loss function changes when the weight parameter is changed slightly. If the derivative value is negative, changing the weight parameter in the positive direction can reduce the loss function. The same is true in the opposite case. However, if the derivative value is 0, the update of the weight parameter stops.


> **Why accuracy is not used as a metric**: Accuracy does not respond to slight changes in parameters. Even if there is a response, the value changes discontinuously.

