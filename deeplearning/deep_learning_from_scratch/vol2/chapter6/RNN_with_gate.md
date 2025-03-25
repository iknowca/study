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
```
Before clipping:
[[0.17580423 6.68174327 4.26460264]
 [2.50172378 5.96060279 7.51967006]
 [8.69938026 9.60995087 5.35574616]]
[[3.00875859 1.97693958 6.19630767]
 [8.89188166 6.44056629 0.24312801]
 [9.07131188 1.72330739 1.46642435]]
After clipping:
[[0.03538002 1.3446789  0.85823728]
 [0.5034637  1.19955175 1.51330892]
 [1.75072172 1.93397107 1.07782634]]
[[0.60550279 0.3978526  1.24698658]
 [1.789462   1.29614283 0.04892871]
 [1.82557174 0.34680996 0.29511309]]
```

## LSTM

기울기 소실을 해결하기 위해서는 RNN계층의 아키텍쳐를 변경해야 한다.
게이트가 추가된 RNN은 여러 종류가 제안되었지만, 그 중에서도 LSTM과 GRU가 가장 많이 사용된다.

### 인터페이스

![](./img/fig%206-11.png)

LSTM 계층에서는 $\mathbf{c}$라는 경로가 추가된다. 이를 memory cell이라고 하며, LSTM 전용의 기억 메커니즘이다.

memory cell의 특징은 데이터를 LSTM 내부에서만 주고 받는 것이다. LSTM안에서 완결되고, 다른 계층으로는 출력하지 않는다. 반면, 은닉상태 $\mathbf h$는 다른 계층으로 출력된다.

그렇기 때문에 LSTM의 출력을 받는 쪽에서는 memory cell에 대해 생각할 필요가 없다.

### 구조

그림에서 보이다 싶이 LSTM에는 메모리 셀 $\mathbf{c_t}$가 $t$시각의 LSTM의 기억이 저장되어 있다.
출력 $\mathbf{h_t}$는 메모리 셀 $\mathbf{c_t}$의 값에 $\tanh$를 취한 값이다.

![](./img/fig%206-12.png)

메모리 셀 $\mathbf{c_t}$는 3개의 입력 $(\mathbf{x_t}, \mathbf{h_{t-1}}, \mathbf{c_{t-1}})$을 받아서 계산된다.
중요한 점은 갱신된 $\mathbf{c_t}$를 사용해 $\mathbf{h_t}$를 계산한다는 점이다.

### 게이트

게이트란 입력과 출력을 조절하는 역할을 한다.
0또는 1뿐만 아니라, 0과 1사이의 값을 가질 수 있다.
중요한 것은 '게이트를 얼마나 열지'도 데이터로 부터 학습한다는 것이다.

### output 게이트

은닉상태 $\mathbf{h_t}$는 메모리 셀 $\mathbf{c_t}$의 값을 $\tanh$로 변환한 값이다.
이 계산에 어떤 게이트를 사용하는데, 그 의미는 '그것이 다음 시각의 은닉상태($\mathbf{h_t}$)로 얼마나 중요한지'에 대한 것이다.

output 게이트의 열림상태는 입력 $\mathbf{x_t}$와 은닉상태 $\mathbf{h_{t-1}}$에 의해 결정된다.
$$
\mathbf{o} = \sigma(\mathbf{x_t} \mathbf{W_{x}^o} + \mathbf{h}_{t-1} \mathbf{W_{h}^o} + b^o)
$$
위에서 계산한 $\mathbf{o}$는 $\mathbf{c_t}$와 곱해져서 $\mathbf{h_t}$를 계산한다.

![](./img/fig%206-15.png)

다만 위에서 계산하는 '곱'은 행렬곱이 아니라, 원소별 곱으로 Hadamard product라고 한다.

$$
\mathbf{h_t} = \mathbf{o} \odot \tanh(\mathbf{c_t})
$$

### forget 게이트

망각은 더 나은 전진을 낳는다. -니체

$\mathbf{c_{t-1}}$의 기억중에서 불필요한 기억을 잊게 해주는 게이트를 추가하여 잊는 것을 가능하게 한다.

![](./img/fig%206-16.png)

forget 게이트에서도 입력 $\mathbf{x_t}$와 은닉상태 $\mathbf{h_{t-1}}$를 사용한다.

$$
\mathbf{f} = \sigma(\mathbf{x_t} \mathbf{W_{x}^f} + \mathbf{h}_{t-1} \mathbf{W_{h}^f} + b^f)
$$

구한 $\mathbf{f}$는 $\mathbf{c_{t-1}}$와 곱해져서 $\mathbf{c_t}$를 계산한다.
$$
\mathbf{c_t} = \mathbf{f} \odot \mathbf{c_{t-1}}
$$

### 새로운 메모리 셀

forget 게이트를 사용하면, 이전 시각의 기억을 잊는 것이 가능하지만,
그렇다고 해서 새로운 기억을 추가하지 않으면, 기억이 계속 줄어들게 된다.
그렇기 때문에 새로운 기억을 추가하는 셀을 추가한다.

![](./img/fig%206-17.png)

새로운 기억을 추가하는 셀은 $\mathbf{g}$라고 하며, $\tanh$를 사용하여 새로운 기억을 추가한다.
$$
\mathbf{g} = \tanh(\mathbf{x_t} \mathbf{W_{x}^g} + \mathbf{h}_{t-1} \mathbf{W_{h}^g} + b^g)
$$
$\mathbf{g}$는 $\mathbf{c_t}$에 더해져서 새로운 기억을 추가한다.

### input 게이트

input 게이트는 새로운 기억을 얼마나 추가할지를 결정한다.
$\mathbf{g}$를 무조건 수용하는 것이 아니라, 적절히 취사 선택하는 역할을 담당한다.

![](./img/fig%206-18.png)
$$
\mathbf{i} = \sigma(\mathbf{x_t} \mathbf{W_{x}^i} + \mathbf{h}_{t-1} \mathbf{W_{h}^i} + b^i)
$$
$\mathbf{i}$는 $\mathbf{g}$와 곱해져서 $\mathbf{c_t}$에 더해진다.

### 기울기 소실 제거

![](./img/fig%206-19.png)

메모리셀의 역전파에서는 '+'와 '$\times$'연산만 수행하게 된다. '+' 연산은 상류의 기울기를 그대로 흘려보내기 때문에 기울기 변화가 없다.

'$\times$'에서는 'matmul'이 아닌 'Hadamard product'를 사용하는데, 매 $t$마다 다른 게이트 값을 사용하기 때문에, 곱셈의 효과가 누적되지 않아 기울기 소실이 발생하기 힘든 구조가 된다.

'$\times$'는 forget 게이트가 제어하는데, forget 게이트가 '잊어야한다'라고 판단한 원소의 경우에는 기울기가 작아지지만, '잊어서는 안된다'라고 판단한 원소에 대해서는 그 기울기가 약화되지 않은 상태로 과거로 전파된다.

### LSTM 구현

LSTM을 구현하기 위해서는 다음과 같은 4개의 게이트를 구현해야 한다.

- forget 게이트
  $$ \mathbf{f} = \sigma(\mathbf{x_t} \mathbf{W_{x}^f} + \mathbf{h}_{t-1} \mathbf{W_{h}^f} + b^f) $$
- new memory cell
  $$ \mathbf{g} = \tanh(\mathbf{x_t} \mathbf{W_{x}^g} + \mathbf{h}_{t-1} \mathbf{W_{h}^g} + b^g) $$
- input 게이트
  $$ \mathbf{i} = \sigma(\mathbf{x_t} \mathbf{W_{x}^i} + \mathbf{h}_{t-1} \mathbf{W_{h}^i} + b^i) $$
- output 게이트
  $$ \mathbf{o} = \sigma(\mathbf{x_t} \mathbf{W_{x}^o} + \mathbf{h}_{t-1} \mathbf{W_{h}^o} + b^o) $$

메모리 셀은 다음과 같은 식을 통해 구할 수 있다.
$$
\mathbf{c_t} = \mathbf{f} \odot \mathbf{c_{t-1}} + \mathbf{i} \odot \mathbf{g}
$$
그리고 은닉상태는 다음과 같이 구할 수 있다.
$$
\mathbf{h_t} = \mathbf{o} \odot \tanh(\mathbf{c_t})
$$

여기서 중요한 부분은 아핀변환이다.

($\mathbf{f, g, i, o}$)는 아핀변환으로 하나의 식으로 정리해 계산할 수 있다.

$$
\begin{align*}
\mathbf{x_t} \mathbf{W_{x}^f} &+ \mathbf{h}_{t-1} \mathbf{W_{h}^f} &+ b^f \\
\mathbf{x_t} \mathbf{W_{x}^g} &+ \mathbf{h}_{t-1} \mathbf{W_{h}^g} &+ b^g \\
\mathbf{x_t} \mathbf{W_{x}^i} &+ \mathbf{h}_{t-1} \mathbf{W_{h}^i} &+ b^i \\
\mathbf{x_t} \mathbf{W_{x}^o} &+ \mathbf{h}_{t-1} \mathbf{W_{h}^o} &+ b^o
\end{align*}
$$
$$
\Downarrow
$$
$$
\mathbf x_t \begin{bmatrix}
\mathbf W_{x}^f & \mathbf W_{x}^g & \mathbf W_{x}^i & \mathbf W_{x}^o \end{bmatrix} + \mathbf h_{t-1} \begin{bmatrix} \mathbf W_{h}^f & \mathbf W_{h}^g & \mathbf W_{h}^i & \mathbf W_{h}^o \end{bmatrix} +
\begin{bmatrix}
b^f & b^g & b^i & b^o
\end{bmatrix}
$$
$$
\Downarrow
$$
$$
\mathbf x_t \mathbf W_x + \mathbf h_{t-1} \mathbf W_h + b
$$

이렇게 아핀변환을 수행하므로써 4개의 가중치를 하나로 모으고, 개별적으로 수행하던 아핀변환을 한번에 수행할 수 있다.

알다싶이 수치 계산에서는 행렬곱을 한번에 수행하는 것이 훨씬 빠르다.

이제 $\mathbf W_x$, $\mathbf W_h$, $\mathbf b$에 4개의 가중치가 포함되어 있다고 생각하고 LSTM을 나타내면 다음과 같다.

![](./img/fig%206-21.png)

코드로 구현하면 다음과 같다.
```python
class LSTM:
  def __init__(self, Wx, Wh, b):
    self.params = [Wx, Wh, b]
    self.grads = [np.zeros_like(Wx), np.zeros_like(Wh), np.zeros_like(b)]
    self.cache = None
```

```python
def forward(self, x, h_prev, c_prev):
  Wx, Wh, b = self.params
  N, H = h_prev.shape

  A = np.matmul(x, Wx) + np.matmul(h_prev, Wh) + b

  #slice
  f = A[:, :H]
  g = A[:, H:2*H]
  i = A[:, 2*H:3*H]
  o = A[:, 3*H:]

  f = sigmoid(f)
  g = np.tanh(g)
  i = sigmoid(i)
  o = sigmoid(o)

  c_next = f * c_prev + g * i
  h_next = o * np.tanh(c_next)
  self.cache = (x, h_prev, c_prev, i, f, g, o, c_next)
  return h_next, c_next
```

```python
def backward(self, dh_next, dc_next):
    Wx, Wh, b = self.params
    x, h_prev, c_prev, i, f, g, o, c_next = self.cache

    tanh_c_next = np.tanh(c_next)

    ds = dc_next + (dh_next * o) * (1 - tanh_c_next ** 2)

    dc_prev = ds * f

    di = ds * g
    df = ds * c_prev
    do = dh_next * tanh_c_next
    dg = ds * i

    di *= i * (1 - i)
    df *= f * (1 - f)
    do *= o * (1 - o)
    dg *= (1 - g ** 2)

    dA = np.hstack((df, dg, di, do))

    dWh = np.dot(h_prev.T, dA)
    dWx = np.dot(x.T, dA)
    db = dA.sum(axis=0)

    self.grads[0][...] = dWx
    self.grads[1][...] = dWh
    self.grads[2][...] = db

    dx = np.dot(dA, Wx.T)
    dh_prev = np.dot(dA, Wh.T)

    return dx, dh_prev, dc_prev
```
순전파에서 slice노드는 행렬을 네조각으로 나눴으니, 역전파에서는 4개의 기울기를 결합해야한다.
![](./img/fig%206-23.png)

코드에서는 np.hstack을 사용하여 4개의 기울기를 결합하였다.

### Time LSTM

Time LSTM은 Time RNN과 마찬가지로, 시계열 데이터를 한꺼번에 처리하는 계층이다.
![](./img/fig%206-24.png)

그런데 Truncated BPTT를 사용하기 때문에, 역전파는 끊어서 수행하지만, 순전파는 그대로 유지해야하므로 은닉상태와 메모리 셀을 인스턴스 변수로 저장해야한다.

![](./img/fig%206-25.png)

## RNNLM with LSTM

### 아키텍쳐

![](./img/fig%206-26.png)

### 훈련

![](./img/Screenshot%202025-03-25%20at%208.59.08 PM.png)

첫번째 퍼플렉시티 값이 10000정도 인이유는 다음에 나올 수 있는 후보가 10000개 정도라는 의미이다. 사실 데이터 셋의 어휘가 10000개이므로 아무것도 학습하지 않은 상태를 의미한다.
![](./img/image.png)
퍼플렉시티 추이를 보면 100정도 되는 것을 확인할 수 있다.

아직 개선할 여지가 많기 때문에 조금 더 개선해본다.

## Better RNNLM with LSTM

### LSTM 다층화

![](./img/fig%206-29.png)

LSTM을 여러 층 쌓으면 모델의 정확도가 향상될것이라고 기대할 수 있다.
쌓는 층은 하이퍼파라미터이기 때문에, 정답은 없지만, PTB 데이터셋에서는 2~4층이 적당하다고 한다.

### Dropout

![](./img/fig%206-30.png)

LSTM을 다층화하면 복잡한 의존관계를 학습할 수 있지만, 그만큼 과적합의 위험이 높아진다.
특히 RNN은 피드포워드 신경망보다 과적합하기 쉽다고 알려져있다.
그래서 dropout을 사용하여 과적합을 방지한다.

근데 RNN에는 어느 부분에 dropout을 적용해야할까?

1. 시계열방향으로 삽입
   ![](./img/fig%206-32.png)
2. 깊이방향으로 삽입
    ![](./img/fig%206-33.png)

3. 시계열과 깊이 방향으로 삽입
  ![](./img/fig%206-34.png)

1은 시간이 흐름에 따라 정보가 사라질 수 있다. 시간이 흐를수록 드롭아웃에 의한 노이즈가 축적되므로 시간축으로의 드롭아웃은 피해야 한다.
2처럼 깊이 방향으로 드롭아웃을 구성하면, 아무리 진행해도 정보를 잃지 않기때문에 효과적으로 드롭아웃을 사용할 수 있다.

그러나 3같은 경우 variational Dropout이라고 하며 시간방향으로도 효과적으로 드롭아웃을 사용할 수 있다.

### weight tying

![](./img/fig%206-36.png)

두 계층의 가중치를 공유하여 모델의 크기를 줄이는 방법이다.
가중치를 공유하면, 매개변수의 수가 줄어들기 때문에 과적합을 방지할 수 있다.
또한, 매개변수의 수가 줄어들기 때문에 학습 속도가 빨라진다.

### 학습
여전히 학습을 함에 따라 퍼플렉시티가 낮아지는 것을 확인할 수 있으며 최종 퍼플렉시티는 70~80정도이다.
이전 LSTM보다 50%정도 낮아진 것을 확인 할 수 있다.

LSTM의 다층화로 표현력을 높이고, 드롭아웃으로 범용성을 확장시키며, 가중치 공유로 가중치를 효율적으로 사용하여 모델을 개선하였다.

## SUMMARY

- RNN에서는 기울기 소실과 폭발이 발생한다.
- LSTM은 기울기 소실/폭발을 해결하기 위해 메모리 셀을 도입한 RNN이다.
- LSTM은 forget 게이트, input 게이트, output 게이트를 사용하여 메모리 셀을 제어한다.
-언어모델 개선에는 LSTM의 다층화, 드롭아웃, 가중치 공유등을 사용할 수 있다.