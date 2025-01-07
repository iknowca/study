---
marp: true
theme: beam
paginate: true
math: katex
footer: '**Perceptron and Simple Nueral Network**
         **2025. 01. 08**'
---

<!-- _class: title -->
# Perceptron and Simple Nueral Network

연구원 김원기

Raresoft
기업부설 연구소

-2025. 01. 08

---

    
<!-- _class: title -->
# Perceptron


---
# What is perceptron?

![perceptron width:400px](./img/perceptron.svg)

퍼셉트론은 다수의 신호를 받아 하나의 신호를 출력한다.

---

퍼셉트론은 위와 같이 표현할 수 있으며, $x_1$, $x_2$는 입력 신호, $y$는 출력 신호, $w_1$, $w_2$는 가중치이다.
그림에서 원은 뉴런 혹은 노드라고 부른다.
입력 신호가 뉴런에 도달하면 가중치와 곱해져 합산된다.
합이 어떤 임계값을 넘으면 뉴런이 활성화되어 신호를 출력한다.

수식으로는 다음과 같다.

> $$
f(x) = \begin{cases}
    0 & \text{if } w_1x_1 + w_2x_2 \leq \theta \\
    1 & \text{if } w_1x_1 + w_2x_2 > \theta
\end{cases} $$

퍼셉트론은 다수의 입력 신호 각각에 가중치를 부여하며, 가중치는 각 신호의 영향력을 제어하는 요소이다. 따라서 가중치는 신호의 중요도를 나타낸다.

---
# Basic logic gates
### AND gate

AND 게이트는 두 개의 입력과 하나의 출력을 가진다.
AND 게이트는 두 입력이 모두 1일 때만 1을 출력하고, 그 외에는 0을 출력한다.

|$x_1$|$x_2$|$y$|
|---|---|---|
|0|0|0|
|1|0|0|
|0|1|0|
|1|1|1|

---

# Basic logic gates
### NAND gate

NAND 게이트는 AND 게이트의 반대이다. 두 입력이 모두 1일 때만 0을 출력하고, 그 외에는 1을 출력한다.

|$x_1$|$x_2$|$y$|
|---|---|---|
|0|0|1|
|1|0|1|
|0|1|1|
|1|1|0|

---
# Basic logic gates

### OR gate

OR 게이트는 두 입력 중 하나라도 1이면 1을 출력하고, 그 외에는 0을 출력한다.
|$x_1$|$x_2$|$y$|
|---|---|---|
|0|0|0|
|1|0|1|
|0|1|1|
|1|1|1|

---

# A simple perceptron
```python
# AND gates implemented in Python.
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    else:
        return 1
```
$w_1, w_2$와 $\theta$는 각각 가중치와 임계값이며 함수 내에서 초기화되며, 입력의 가중합이 입력의 총합보다 크거나 같으면 1을 반환하고, 그렇지 않으면 0을 반환한다.

---
# Weight and bias

임계값 $\theta$는 편향 $b = -\theta$로 다시 쓸 수 있다. 편향은 뉴런을 활성화하는 것이 얼마나 쉬운지를 결정하는 값이다. 편향이 크면 뉴런이 쉽게 활성화되고, 작으면 뉴런이 활성화되기 어렵다.
가중치는 입력 신호의 중요도를 결정하는 값이다. 가중치가 클수록 신호가 중요하다.

> $$
y = \begin{cases}
    0 & \text{if } b + w_1x_1 + w_2x_2 \leq 0 \\
    1 & \text{if } b + w_1x_1 + w_2x_2 > 0
\end{cases}$$

---
# Weight and bias

```python
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
```

---

# limits of perceptron

## XOR gate

XOR 게이트는 입력이 1인 개수가 홀수이면 1을 출력하고, 짝수이면 0을 출력하는 게이트이다.

|$x_1$|$x_2$|$y$|
|---|---|---|
|0|0|0|
|1|0|1|
|0|1|1|
|1|1|0|


XOR 게이트는 단일 퍼셉트론으로 구현할 수 없다. 이는 단일 퍼셉트론은 선형 함수만 구현할 수 있기 때문이다. XOR 게이트는 비선형 함수이기 때문이다.

---

# Linear and non-linear functions
>

![center](./img/OR_gate_visualization.png)
선형 함수는 직선으로 표현할 수 있는 함수이고, 비선형 함수는 직선으로 표현할 수 없는 함수이다.
OR 게이트는 위의 이미지에서 볼 수 있듯이 하나의 직선으로 영역을 나눈다. 이것은 선형 함수이다.

---

# Linear and non-linear functions
![center](./img/XOR_gate_visualization.png)
그러나 XOR 게이트는 하나의 직선으로 나눌 수 없다. 이것은 비선형 함수이다.

---
# Multi-layer perceptron
![height:400px center](img/multilayer_network/main_ManimCE_v0.18.1.gif)

다층 퍼셉트론은 여러 층을 가진 퍼셉트론이다. 여러 퍼셉트론을 결합하여 비선형 함수를 구현할 수 있다. XOR 게이트는 다층 퍼셉트론으로 구현할 수 있다.

---
<!-- _class: title -->
# Neural network 

---

# Neural network

![height:500px center](../chapter3/img/neural_network/main_ManimCE_v0.18.1.gif)

---

# activation function

퍼셉트론의 수식은 다음과 같다.
이때, 표현을 단순화하기 위해 조건 분기를 함수로 작성할 수 있다.

$$
y = \begin{cases}
0 & (b + w_1x_1 + w_2x_2 \leq 0) \\
1 & (b + w_1x_1 + w_2x_2 > 0)
\end{cases}$$
$$
h(x) = \begin{cases}
0 & (x \leq 0) \\
1 & (x > 0)
\end{cases}$$
$$
y = h(b + w_1x_1 + w_2x_2)$$

$h(x)$와 같은 함수를 계단 함수라고 한다. 계단 함수는 입력이 0을 넘으면 1을 출력하고, 그 외에는 0을 출력한다. 이제 계단 함수 대신 활성화 함수를 사용해보자.

---

# Logic gate and activation function
이제 활성화 함수를 사용하여 논리 게이트를 구현해보자.
먼저 입력은 $x_1$과 $x_2$로 하고, 가중치는 $w_1=0.5$과 $w_2=0.5$로 하자. 그리고 편향 $b=0.7$로 하자.
$$
y = h(0.7 + 0.5 x_1 + 0.5x_2)$$

---

# Sigmoid function

시그모이드 함수 는 신경망에서 자주 사용되며 출력을 0과 1 사이의 값으로 조정하여 연속적으로 신호를 보낼 수 있다.
![center height:300px](../chapter3/img/sigmoid_function/main_ManimCE_v0.18.1.gif)
$$
h(x) = \frac{1}{1 + \exp(-x)}$$
---
# Sigmoid Vs Step function
## Non-linear function
계단함수와 시그모이드 함수는 둘다 비선형 함수이다. 신경망에서는 비선형 함수를 사용하여 신경망의 깊은 층 효과를 얻을 수 있다. 비선형 함수를 사용하지 않는다면, 신경망이 깊어져도 단층 신경망과 같은 효과를 얻을 수 있다.
![center height:300px](../chapter3/img/sigmoid_vs_step/main_ManimCE_v0.18.1.gif)

---

# multi-layer neural network
이전보다 조금은 더 복잡한 3층 신경망을 구현해본다.
![center height:400px](../chapter3/img/3layer_neural_network/main_ManimCE_v0.18.1.gif)

---
# multi-layer neural network


```python
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network

def forward(network: dict, x:np.array):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = x@W1 + b1
    z1 = sigmoid(a1)
    a2 = z1@W2 + b2
    z2 = sigmoid(a2)
    a3 = z2@W3 + b3
    y = a3
    return y
    
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

---
```python
if __name__ == '__main__':
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward(network, x)
    print(y)

#>> [0.31682708 0.69627909]
```