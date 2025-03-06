# word2vec

## 통계 기반 기법의 문제점.

통계 기반 기법에서는 주변 단어의 빈도를 기초로 단어를 표현했다.

구체적으로는 동시발생 행렬을 만들고, 그 행렬에 SVD를 적용하여 밀집벡터(단어의 분산 표현)를 얻었다.

하지만 실제 현업에서 다루는 corpus의 어휘수는 100만개 이상이며, 이는 동시발생 행렬의 shape이 100만 X 100만이 되어야 한다.

이런 거대한 행렬에 SVD를 적용하는것은 현실적이지 않다.
> SVD 기법은 O(n^3)의 시간복잡도를 가지기 때문이다.

## 추론 기반 기법

추론 기반 기법에서는 추론이 주된 작업이다. 추론이란 주변 `context`가 주어졌을 때 무슨 단어가 들어가는지 추측하는 작업이다.

$$
\text{you ??? goodbye and I asy hello.}
$$

## 신경망의 단어처리

신경망은 "you", "say"같은 단어를 직접 처리할 수 없기 때문에 단어를 '고정 길이의 벡터'로 변환해야 한다.
이때 사용하는 대표적인 방법은 원핫 벡터로 변환하는 것이다. 원핫 표현이란 벡터의 원소 중 하나만 1이고 나머지는 모두 0인 벡터를 말한다.

![](./img/fig%203-5.png)

이제 단어를 벡터로 나타낼 수 있고, 신경망 계층들은 벡터를 처리할 수 있다. 즉, 단어를 신경망으로 처리할수 있게 되었다.

![](./img/fig%203-7.png)

```python
# onehot.ipynb
c = np.array([[1, 0, 0, 0, 0, 0, 0]])
W = np.random.randn(7, 3)
h = np.matmul(c, W)
print(h)
print(W)
# [[ 0.53049115  0.80939883 -0.06515422]]

# [[-1.28467208 -0.31236871  0.00881346]
#  [ 0.8517237   0.80260893  0.35117362]
#  [-1.77088339  0.73824633 -2.64538116]
#  [ 1.1128839   0.58763038  0.79380275]
#  [ 0.01287326 -0.14879395  0.33680531]
#  [-0.48498518 -0.4472975  -0.14260649]
#  [ 0.54463527  0.59979248 -0.32314239]]
```

c는 원핫 인코딩 되어 있으므로, c와 W의 행렬곱은 W의 행벡터 중 하나를 '뽑아낸'것과 같다.

![](./img/fig%203-8.png)

## CBOW 모델 (Continuous Bag of Words)

CBOW 모델은 context로부터 target을 추측하는 용도로 사용된다.

CBOW모델의 입력은 context이고, context는 "you", "goodbye", "and", "say"와 같이 단어들의 목록으로 구성되어 있다.

![](./img/fig%203-9.png)

입력층이 2개 있고, 은닉층을 거져 출력층에 도달한다.
입력층이 2개인 이유는 context의 단어 수가 2개이기 때문이다.
context의 단어 수가 N개라면 입력층도 N개가 된다.

은닉충의 뉴런은 입력층의 완전연결계층에 의해 반환된 값이 되는데, 입력층이 여러개인 경우, 전체를 평균한 벡터가 된다.
출력층에서는 뉴런 하나하나가 단어에 대응한다. 또한 출력층 뉴런은 단어의 점수를 의미하며, 값이 높을수록 대응 단어의 출현 확률도 높아진다.

![](./img/fig%203-11.png)

가장 앞단에 MatMul 계층이 2개 있고, 이 두 계층의 출력의 평균이 은닉층 뉴런이 된다. 다음으로, 은닉층에서 출력층으로 가는 MatMul 계층이 존재한다.

```python
# 샘플 context 데이터
c0 = np.array([[1, 0, 0, 0, 0, 0, 0]])
c1 = np.array([[0, 0, 1, 0, 0, 0, 0]])

# 가중치 초기화
W_in = np.random.randn(7, 3)
W_out = np.random.randn(3, 7)

# 계층 생성
in_layer0 = MatMul(W_in)
in_layer1 = MatMul(W_in)
out_layer = MatMul(W_out)

# 순전파
h0 = in_layer0.forward(c0)
h1 = in_layer1.forward(c1)
h = 0.5 * (h0 + h1)
s = out_layer.forward(h)

print(s)
#[[ 0.23718179 -0.15794509  0.1398977   0.06502093 -0.08007988 -0.07046796
#    0.06012722]]
```

입력층을 처리하는 MatMult 계층은 context 수만큼 생성하고, 출력층 계층은 하나만 생성한다.
이때, 입력층 측의 MatMul 계층은 가중치를 공유한다.

in_layer0과 in_layer1의 forward()를 호출하여, 중간데이터를 계산하고 평균내어 out_layer를 통과시켜 단어의 점수를 구한다.

## CBOW 모델의 학습

앞서 제작한 CBOW 모델은 출력으로 단어의 점수를 출력했다. 이 점수에 소프트맥스 함수를 적용하여 확률을 얻을 수 있다. 이 확률이란 컨텍스트가 주어졌을때 어떤 단어가 출현할 확률을 의미한다.

![](./img/fig%203-12.png)

가중치가 적절히 설정되어 있다면, "you", "say"라는 컨텍스트가 주어졌을때 "goodbye"라는 단어가 높은 확률로 출력되어야 한다.

CBOW 모델에서는 당연하지만 신경망이 올바른 예측을 할 수 있도록 가중치를 조정하는 학습이 필요하다. 그 결과로 가중치 $W$에 단어의 출현 패턴을 파악한 벡터가 학습된다.

확률을 구하기 위해서 소프트맥스 함수를 사용했다면, 손실 함수로 크로스 엔트로피 오차를 사용하며, 구한 손실을 통해 가중치를 갱신한다.

![](./img/fig%203-13.png)

### word2vec의 가중치와 분산표현

$W_{in}, W_{out}$ 두 가중치가 있다. 

여기서 단어의 분산 표현은 $W_{in}$의 행벡터로 정의한다.
왜냐하면 $W_{in}$은 입력층과 연결되어 있고, 입력층은 단어를 원핫 벡터로 표현하기 때문이다.
즉, $W_{in}$의 행벡터는 원핫 벡터와 내적을 취했을때, 원핫 벡터에 해당하는 단어의 분산 표현이 된다.

## 학습 데이터

### 컨텍스트와 타깃

word2vec에서 입력은 `컨텍스트`고 정답은 컨텍스트에 둘러싸인 `타깃`이다.
이제 해야 할 일은 신경망에 `컨텍스트`를 입력했을 때, `타깃`이 출현할 확률을 높여야 한다.

그러므로 코퍼스로부터 학습할 데이터: `컨텍스트와` `타깃`을 준비해야 한다.
![](./img/fig%203-16.png)

`컨텍스트`의 각 행은 신경망으로 사용되고, 
`타깃`은 정답으로 사용된다.
또한 각 샘플 데이터에서 컨텍스트의 수는 여러개가 될 수 있지만, 타깃은 하나만 존재한다.

![](./img/fig%203-17.png)

```python
def create_contexts_target(corpus, window_size=1):
    target = corpus[window_size: -window_size]
    contexts = []

    for i in range(window_size, len(corpus) - window_size):
        contexts = []
        for t in range(- window_size, window_size + 1):
            if t == 0:
                continue
            contexts.append(corpus[i - t])
        contexts.append(corpus[i])
    return np.array(contexts), np.array(target)

contexts, target = create_contexts_target(corpus, window_size=1)
print(contexts)
# [[0 2]
#  [1 3]
#  [2 4]
#  [3 1]
#  [4 5]
#  [1 6]]
print(target)
# [1 2 3 4 1 5]
```

이렇게 만든 맥락과 타깃을 원핫 벡터로 변환하여야 한다.
![](./img/fig%203-18.png)

```python
def convert_one_hot(corpus, vocab_size):
    N = corpus.shape[0]

    if corpus.ndim == 1:
        one_hot = np.zeros((N, vocab_size), dtype=np.int32)
        for i, id in enumerate(corpus):
            one_hot[i, id] = 1
    
    elif corpus.ndim == 2:
        C = corpus.shape[1]
        one_hot = np.zeros((N, C, vocab_size), dtype=np.int32)
        for i, ids in enumerate(corpus):
            for j, id in enumerate(ids):
                one_hot[i, j, id] = 1
    return one_hot

text = "you say goodbye and I say hello."
corpus, word_to_id, id_to_word = preprocess(text)
contexts, target = create_contexts_target(corpus, window_size=1)
vocab_size = len(word_to_id)

target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)
```

##  CBOW 모델

```python
class SimpleCBOW:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size

        W_in = 0.01 * np.random.randn(V, H).astype('f')
        W_out = 0.01 * np.random.randn(H, V).astype('f')

        self.in_layer0 = MatMul(W_in)
        self.in_layer1 = MatMul(W_in)
        self.out_layer = MatMul(W_out)
        self.loss_layer = SoftmaxWitLoss()

        layers = [self.in_layer0, self.in_layer1, self.out_layer]
        slef.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads

        self.word_vecs = W_in

    def forward(self, contexts, target):
        h0 = self.in_layer0.forward(contexts[:, 0])
        h1 = self.in_layer1.forward(contexts[:, 1])
        h = (h0 + h1) * 0.5
        score = self.out_layer.forward(h)
        loss = self.loss_layer.forward(score, target)
        return loss

    def backward(self, dout=1):
        ds = self.loss_layer.backward(dout)
        da = self.out_layer.backward(ds)
        da *= 0.5
        self.in_layer1.backward(da)
        self.in_layer0.backward(da)
        return None
```

![](./img/fig%203-20.png)

```python
window_size = 1
hidden_size = 5
batch_size = 3

max_epoch = 1000

text = "You say goodbye and I say hello."
corpus, word_to_id, id_to_word = preprocess(text)

vocab_size = len(word_to_id)
contexts, target = create_contexts_target(corpus, window_size)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()
```

![](./img/train.png)

학습을 거듭할수록 손실이 줄어드는 것을 확인할 수 있으므로, 학습이 순조롭다는 것을 알 수 있다.

학습이 끝난 후의 가중치 매개변수를 확인해보자.
```python
word_vecs = model.word_vecs
for word_id, word in id_to_word.items():
    print(word, word_vecs[word_id])
# you [ 0.91027445  0.9109697   0.9093714  -1.636414    1.1909498 ]
# say [-1.2520131  -0.42286974 -1.2547204  -0.18793075  1.159552  ]
# goodbye [1.1790615  1.019854   1.1555815  0.59903586 0.61650884]
# and [-0.96715873 -1.5677291  -0.981955   -1.466045    0.82372546]
# i [1.1416799  1.0131328  1.1480596  0.6092619  0.56708306]
# hello [ 0.92347044  0.91841936  0.91537136 -1.6677319   1.1769753 ]
# . [-1.1574557  1.5436673 -1.1581074  1.3639181  1.2297388]
```

이제 단어를 밀집벡터로 표현할 수 있으며, 이 밀집 벡터가 단어의 분산 표현이다.

## CBOW와 확률

### 확률

$A$라는 사건이 발생할 확률은 $P(A)$로 나타낸다. $A$, $B$ 두 사건이 동시에 발생할 확률은 $P(A, B)$로 나타낸다. $A$가 발생했을 때 $B$가 발생할 확률은 $P(B|A)$로 나타낸다. 이때 $P(B|A)$는 조건부 확률(사후 확률)이라고 한다.

### CBOW 모델에서의 확률

CBOW모델은 컨텍스트가 주어졌을때, 타깃이 출현할 확률을 구한다.
코퍼스를 $w_1, w_2, w_3, \cdots, w_T$라고 하자. 이때 CBOW 모델은 다음과 같은 확률을 구한다.
![](./img/fig%203-22.png)

$w_t-1, w_t+1$이 주어졌을때, 타깃이 $w_t$일 확률.
$$
P(w_t | w_{t-1}, w_{t+1})
$$

위 식을 사용하여, 손실함수를 간결하게 표현할 수도 있다.

사용한 손실함수 교차 엔트로피 오차는 다음과 같다.
$$
L = - \sum_k t_k \log y_k
$$

이때 $y_k$는 'k번째 해당하는 사건이 일어날 확률이다.'
그리고 $t_k$는 정답 레이블이며 원핫 벡터로 표현되기 때문에, 다음 식을 유도 할 수 있다.

$$
L = -log{P(w_t | w_{t-1}, w_{t+1})}
$$
위 식은 단순히 확률에 로그를 취하고 부호를 바꾼 것이다.
이 식을 음의 로그 우도(Negative Log Likelihood)라고 한다.
> 우도(Likelihood)란 어떤 사건이 발생할 확률을 의미하지만 해석과 활용이 확률과는 다르다.
> 확률 $P(x|\theta)$는 매개변수 $\theta$가 주어졌을때, 사건 $x$가 발생할 확률을 의미한다.
> 
>> 확률은 예측에 사용된다.
>> 만약 이 모델이 맞다면, 이런 데이터가 나올 확률은 얼마일까?
> 
> 반면 우도 $L(\theta|x)$는 사건 $x$가 발생했을때, 매개변수 $\theta$의 확률을 의미한다.
>
> > 우도는 매개변수 추정에 사용된다.
> > 만약 이 데이터가 맞다면, 어떤 $\theta$가 적합할까?

그렇다면 코퍼스 전체로 확장하면 다음과 같이 정리할 수 있다.

$$
L = - {1\over T}\sum_{t=1}^T log{P(w_t | w_{t-1}, w_{t+1})}
$$