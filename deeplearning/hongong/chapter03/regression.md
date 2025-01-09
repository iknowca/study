# regression

A supervised learning algorithm can be divided into classification and regression. Classification is a problem of classifying a sample into one of several classes, and regression is a problem of predicting an arbitrary value.

## K-Nearest Neighbors Regression

The K-Nearest Neighbors algorithm selects the k closest samples to the sample to be predicted, and calculates the average of the targets of these samples.


In scikit-learn, the K-Nearest Neighbors regression algorithm is provided as KNeighborsRegressor. This class makes it very easy to use KNN regression.
```python
from sklearn.neighbors import KNeighborsRegressor
knr = KNeighborsRegressor()
knr.fit(train_input, train_target)
# 0.992809406101064
```

In classification, the ratio of the number of samples in the test set that are correctly classified is given as accuracy. In regression, the score is evaluated using the coefficient of determination. This is also called $R^2$.

$$
R^2 = 1- { \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 \over \sum_{i=1}^{n} (y_i - \bar{y})^2 }
$$

The coefficient of determination can be calculated using the above formula. It is the sum of the squares of the differences between the target and the predicted value of each sample, divided by the sum of the squares of the differences between the target and the target mean. If the prediction is close to the target, the coefficient of determination is close to 1, and if the prediction is about the target mean, it is close to 0.

<!-- ## 과대적합과 과소적합 -->
## Overfitting and Underfitting

<!-- 모델을 훈련 세트로 훈련한다는 것은 모델이 훈련 세트에 최대한 잘 맞도록 학습 하는 것을 의미한다. 이렇게 훈련시킨 모델을 훈련세트와 테스트 세트에서 각각 평가하면 어떻게 될까? 일반적으로는 훈련 세트의 점수가 조금 더 높게 나온다. -->

Training a model with a training set means that the model learns to fit the training set as well as possible. What happens if you evaluate this trained model on the training set and the test set? Generally, the score of the training set is slightly higher.

<!-- 만약 훈련 세트에서 점수가 매우 좋지만, 테스트 세트에서는 점수가 나쁜경우 모델이 과대적합 되었다고 말한다. 훈련세트에만 잘 맞는 모델이기 때문에 테스트 세트나, 새로운 샘플에 대해 추론할 때 잘 동작하지 않을것이다. -->
If the score is very good on the training set, but poor on the test set, the model is said to be **overfit**. Since it is a model that fits only the training set well, it will not work well when inferring the test set or new samples.

<!-- 반대로 훈련세트보다 테스트 세트의 점수가 높거나, 두 점수가 모두 너무 낮은경우에는 모델이 과소적합되었다고 하고, 이런 경우는 충분히 훈련되지 않은 경우나, 훈련세트와 테스트 세트의 크기가 매우 작은경우 나타날 수 있다. -->
Conversely, if the score on the test set is higher than the training set, or if both scores are too low, the model is said to be **underfit**, and this can occur when the model is not sufficiently trained or when the size of the training set and test set is very small.

