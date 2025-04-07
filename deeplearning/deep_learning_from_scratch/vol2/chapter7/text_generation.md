# RNN을 사용한 문장 생성

## LM을 사용한 문장생성

### 문장 생성의 순서

LSTM을 이용한 언어 모델의 신경망 구성은 다음과 같다.
![](./img/fig%207-1.png)

이 학습된 언어 모델에 "I"라는 단어를 입력으로 주면 다음과 같은 확률분포를 출력한다.
![](./img/fig%207-2.png)

이 결과로 다음 단어를 생성하는 방법은 다음과 같다.

1. 확률이 가장 높은 단어를 선택한다.
확률이 가장 높은 단어를 선택하는 방법은 결과가 일정하게 정해지는 결정론적인 방법이다.
2. 확률적으로 단어를 선택한다.
이 방법에서는 선택되는 단어가 매번 달라질 수 있다.

여기서는 확률적으로 단어를 선택하는 방법을 사용한다.
확률분포로부터 샘플링을 수행한 결과로 "say"가 선택되었다고 가정하자.
(확률분포에서 "say"의 확률이 가장 높기 때문에 "say"가 샘플링될 확률이 가장 높지만, 결정적인 것이 아니라, 확률적으로 선택된다.)

다음 단어를 샘플링 하는 방법은 앞에서 한 작업을 반복하는 것이다.

"say"를 언어 모델에 입력으로 하여 다음 단어의 확률 분포를 얻는 것이다.
![](./img/fig%207-4.png)

이 작업을 원하는 원하는 만큼 혹은 `<eos>`같은 종결기호가 나타날때 까지 반복한다.

이렇게 생성된 문장은 훈련 데이터에는 존재하지 않는, 말 그대로 새로 생성된 문장이다.
언어모델은 훈련데이터를 암기하는 것이 아니라, 훈련 데이터에서 사용된 단어의 정렬 패턴은 학습하고, 올바르게 학습되었다면, 생성된 문장은 문법적으로도 맞고, 의미적으로도 자연스러운 문장이 된다.

### 문장 생성 구현

```python
class RnnlmGen(Rnnlm):
    def generate(self, start_id, skip_ids=None, sample_size=100):
        word_ids = [start_id]

        x = start_id
        while len(word_ids) < sample_size:
            x = np.array(x).reshape(1, 1)
            score = self.predict(x)
            p = softmax(score.flatten())
            sampled = np.random.choice(len(p), size=1, p=p)
            if (skip_ids is None) or (sampled not in skip_ids):
                x = sampled
                word_ids.append(int(x))
        
        return word_ids
```
```python
corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
corpus_size = len(corpus)

model = RnnlmGen()

start_word = 'you'
start_id = word_to_id[start_word]
skip_words = ['N', '<unk>', '$']
skip_ids = [word_to_id[w] for w in skip_words]

word_ids = model.generate(start_id, skip_ids)
txt = ' '.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos', '.\n')
print(txt)
```
```
<!-- 학습 전 데이터(무작위 매개변수) -->
you setback best raised fill steelworkers montgomery kohlberg told beam worthy allied ban swedish aichi mather promptly ramada explicit leslie bets discovery considering campaigns bottom pertrie warm large-scale frequent temple grumman bennnett ...
```
```
<!-- 학습 된 데이터 -->
you 'll include one of them a good problems.
moreover so if not gene's corr experience with the heat of bridges a new deficits model is non-viloent what it 's a rule must exploit it.
there 's no tires industry could occur.
beyound my hours where he is n't going home says and japanese letter
knight transplants d.c. turmoil with one-third of voters.
the justice department...
```

### 더 좋은 언어 모델
```
<!-- BetterRnnlm사용 -->
you 've seen two families and the women and two other women of students.
the principles of investors that prompted a bipartisan rule of which had a withdrawn target of black men or legislators interfere with the number of plants can doto carry it together.
the appeal was to deny steady increases in the operation of dna and educational damage inthe 1950s.
```
## seq2seq
seq2seq는 2개의 RNN을 사용하여 시계열 데이터를 다른 시계열 데이터로 변환하는 모델이다.

### 원리
seq2seq를 Encoder-Decoder 구조라고도 한다. 2개의 모듈 Encoder, Decoder로 구성되어 있다.
Encoder는 입력 시퀀스를 고정 길이의 벡터로 변환하고, Decoder는 이 벡터를 기반으로 출력 시퀀스를 생성한다.

### Encoder

![](./img/fig%207-6.png )

Encoder는 RNN을 사용하여 시계열 데이터를 은닉상태 벡터 h로 변환한다.

### Decoder

![](./img/fig%207-8.png)

Decoder는 Encoder에서 생성된 은닉상태 벡터 h를 입력으로 받아 시퀀스를 생성한다.

### seq2seq

![](./img/fig%207-9.png)

## 더하기 모델

![](./img/fig%207-10.png)

인간에게는 매우 쉬문 문제이지만 seq2seq모델은 덧셈의 논리에 대해 모르기 때문에, 덧셈을 수행할 수 없다.
이 모델에서는 "57+5"가 입력될때, ['5', '7', '+', '5']로 변환되어 입력된다.

### 패딩
더하기 문제에서는 샘플마다 데이터의 시간 방향 크기다 다르기때문에 미니배치 처리가 불가능하다.
가변 길이 시계열 데이터를 미니배치로 학습하기 위한 가장 단순한 방법으로는 패딩을 사용할 수 있다.
원본 데이터에 의미 없는 데이터를 채워 모든 데이터의 길이를 균일하게 맞추는 기법이다.
![](./img/fig%207-11.png)

질문과 정답을 구분하기 위해 출력 앞에 구분자로 언더바(_)를 사용해 구분한다.

하지만 이렇게 되면 원래는 존재하지 않던 패딩용 문자까지 seq2seq가 처리해야 하므로 기존 seq2seq에 패딩 전용 처리를 추가해야 한다. 예를들어 Decoder에 입력된 데이터가 패딩일 경우 손실의 결과에 반영되지 않도록 한다.

### 더하기 데이터 셋
![](./img/fig%207-12.png)

```python
(x_train, t_tarin), (x_test, t_test) = sequence.load_data("addition.txt", seed=1984)
char_to_id, id_to_char = sequence.get_vocab()

print(x_train.shape, t_train.shape)
print(x_test.shape, t_test.shape)
#(45000, 7) (45000, 5)
#(5000, 7) (5000, 5)

print(x_train[0])
# [3 0 2 0 0 11 5]
# [6 0 11 7 5]

print(''.join([id_to_char[c] for c in x_train[0]]))
print(''.join([id_to_char[c] for c in t_train[0]]))
# 71+118
# _180
```

## seq2seq 구현

seq2seqsms encoder와 decoder 두개의 RNN을 사용하여 시퀀스를 변환하는 모델이다.

### Encoder
encoder 클래스는 문자열을 받아 벡터 h로 변환한다.

![](./img/fig%207-13.png)

이를 LSTM으로 구현하면 다음과 같다.

![](./img/fig%207-14.png)

시간방향을 한꺼번에 처리하는 TimeLSTM을 사용하여 더 간단하게 나타낼 수 있다.

![](./img/fig%207-15.png)

```python
class Encoder:
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        V, D, H = vocab_size, wordvec_size, hidden_size
        rn = np.random.randn

        embed_W = (rn(V, D) * 100).astype('f')
        lstm_Wx = (rn(D, 4*H) /np.sqrt(D)).astype('f')
        lstm_Wh = (rn(H, 4*H) /np.sqrt(H)).astype('f')
        lstm_b = np.zeros(4*H).astype('f')

        self.embed = TimeEmbedding(embed_W)
        self.lstm = TimeLSTM(lstm_Wx, lstm_Wh, lstm_b, stateful=False)
        self.params = self.embed.params + self.lstm.params
        self.grads = self.embed.grads + self.lstm.grads
        self.hs = None
```

```python
def forward(self, xs):
    xs = self.embed.forward(xs)
    hs = self.lstm.forward(xs)
    self.hs = hs
    return hs[:, -1, :]
```

```python
def backward(self, dh):
    dhs = np.zeros_like(self.hs)
    dhs[:, -1, :] = dh

    dout = self.lstm.backward(dhs)
    dout = self.embed.backward(dout)
    return dout
```

### Decoder
decoder클래스는 Encoder로부터 h를 받아 다른 문자열을 출력한다.
