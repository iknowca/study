# 게이트가 추가된 RNN

이전에 구현한 RNN은 구조가 단순하고, 구현도 간단하지만, 성능이 좋지 않다.
그 원인으로는 시계열 데이터에서 시간적으로 먼, 장기 의존관계(long-term dependency)를 학습하기 어렵기 때문이다.

그래서 요즘에는 단순한 RNN 대시 LSTM, GRU와 같은 계층이 주로 사용된다. 일반적으로 RNN이라고 하면 LSTM을 의미하는 경우도 많다. 오히려 RNN을 *기본 RNN*이라고 부르기도 한다.

## RNN의 한계

RNN은 앞서 언급했다싶이, 장기 의존관계를 학습하기 어려운데, 그 이유는 BPTT에서 기울기 소실 혹은 폭발이 일어나기 때문이다.

### 기울기 소실 혹은 폭발

예문 "Tom was watching TV inhis room. Mary came into the room. Mary said hi to ???"
를 사용하여 기울기 소실을 확인하자

RNNLM 학습의 관점에서 정답 레이블 "Tom"이라는 단어가 주어졌을때, "Tom"이라는 정답레이블이 주어진 시점으로부터 가거 방향으로 기울기를 전달하게 된다.

![](./img/fig%206-4.png)
RNN계층은 '의미있는 기울기'를 과거 방향으로 전달함으로써 시간 방향의 의존 관계를 학습할 수 있다.
기울기는 학습해야 할 의미가 있는 정보가 포함되고, 그걸 과거로 전달함으로써 장기 의존 관계를 학습할 수있다.

하지만, 기울기가 거의 사라지거나(소실), 의미없이 매우 커지면(폭발) 장기 의존 관계를 학습 할 수 없게 된다.
안타깝지만, 단순한 RNN계층에서는 대부분 이런 현상이 발생한다.

### 기울기 소실과 폭발의 원인

길이가 T인 시계열데이터에 대해 생각해보자, 역전파로 전해지는 시간방향 기울기는 차례로 'tanh', '+', 'MatMul'연산을 통과한다.

'+'역전파는 상류의 기울기를 그대로 흘려보내지만,

'tanh'의 경우 $y = \tanh(x)$의 미분은 $\frac{\partial y}{\partial x} = 1 - y^2$이다.

![](./img/fig%206-6.png)

미분값은 1보다 작고 x가 0에서 멀어질수록 작아진다. 그 의미는 기울기가 tanh를 통과할때마다 그 값이 지속적으로 작아진다는 의미이다.

'MatMul'의 경우 상류로부터 $\mathbf{dh}$를 받아서 $\mathbf{dhW_h^T}$를 계산한다.이 행렬 곱셈에서는 매번 똑같은 가중치 $\mathbf{W_h}$를 사용한다.

'MatMul'의 역전파는 실제 코드를 통해 확인해보자.
```python
import numpy as np
import matplotlib.pyplot as plt

N = 2 # 배치 크기
H = 3 # 은닉층의 벡터 차원 수
T = 20 # 시계열 데이터의 길이

dh = np.ones((N, H)) # 상류로부터의 기울기
Wh = np.random.randn(H, H)

norm_list = []
for t in range(T):
    dh = np.matmul(dh, Wh.T)
    norm = np.sqrt(np.sum(dh**2)) / N
    norm_list.append(norm)
```

위 코드를 실행해 얻은 결과는 다음과 같다.

![](./img/fig%206-8.png)
![](./img/fig%206-9.png)

기울기의 크기가 지수적으로 증가하거나 감소하는 것을 확인할 수 있는데, 이유는 $Wh$를 $T$번 곱했기 때문이다. 행렬이 아니라 스칼라라고 생각해보면, $Wh$의 값에 따라 $Wh^T$로 변화하게 된다.

### 폭발 대책

기울기 폭발을 막기위해서는 기울기 클리핑 (gradient clipping)이라는 방법을 사용한다.
수식으로는 다음과 같이 나타낼 수 있다.
$$
\begin{align*}
\text{if } ||\hat g|| \ge \text{threshold: } \\
\hat g = \frac{\text{threshold}}{||\hat g||}\hat g
\end{align*}
$$

기울기의 L2 노름이 threshold보다 크면 기울기를 threshold를 사용해 수정한다.

기울기 클리핑은 다음과 같이 구현할 수 있다.
```python
dW1 = np.random.rand(3, 3) * 10
dW2 = np.random.rand(3, 3) * 10
grads = [dW1, dW2]
max_norm = 5.0

def clip_grads(grads, max_norm):
    total_norm = 0
    for grad in grads:
        total_norm += np.sum(grad ** 2)
    total_norm = np.sqrt(total_norm)

    rate = max_norm / (total_norm + 1e-65)
    if rate < 1:
        for grad in grads:
            grad *= rate
```