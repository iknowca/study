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

## Overfitting and Underfitting


Training a model with a training set means that the model learns to fit the training set as well as possible. What happens if you evaluate this trained model on the training set and the test set? Generally, the score of the training set is slightly higher.

If the score is very good on the training set, but poor on the test set, the model is said to be **overfit**. Since it is a model that fits only the training set well, it will not work well when inferring the test set or new samples.

Conversely, if the score on the test set is higher than the training set, or if both scores are too low, the model is said to be **underfit**, and this can occur when the model is not sufficiently trained or when the size of the training set and test set is very small.


## Linear Regression

### Limitations of KNN Regression

![KNN Regression Limitation](./resources/limitaion_of_knn_regression.png)

k-nearest neighbors regression finds the closest samples and calculates the average of the targets. If the sample is located outside the range of the training set, it predicts the wrong value.

### Linear Regression

Linear regression is one of the first machine learning algorithms to learn because it is relatively simple and performs well. It is an algorithm that learns a straight line when there is one feature.


![Linear Regression](./resources/linear_regression.png)

However, if you check the $R^2$ score for the training set and the test set,
```python
print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))
#>>>0.9398463339976041
#>>>0.824750312331356
```


The score of the test set is significantly lower than that of the training set, and the score of the training set is not close to 1. This means that the model is underfit. Also, when you check the graph, the linear graph predicted by the data does not represent the data well because the length is close to 0.

### Polynomial Regression

To draw a graph of a second-degree equation, the length must be squared and added to the training set.
```python
train_poly = np.column_stack((train_input ** 2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))
```

![polynomial regression](./resources/poly_linear_regression.png)


But is this a linear regression even though it is a second-degree equation? This is linear regression. Linear regression is an algorithm that learns a linear equation for features. By squaring the features and adding new features, linear regression can learn a second-degree equation.


```python
print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))
#>>>0.9706807451768623
#>>>0.9775935108325122
```

## Feature Engineering and Regularization

A linear regression model that uses multiple features is called multiple regression. If you use one feature, the regression model learns a straight line, and if you use two features, it learns a plane.

In high dimensions with many features, linear regression can represent very complex models. Also, the process of extracting new features using existing features is called feature engineering.

However, if there are too many features, the model may be overfitted to the training set, so it may not fit well in the test set.

### Regularization

Regularization is a method of preventing the model from learning the training set excessively. In linear regression models, you can apply it by making the coefficients multiplied by the features small.

There are Ridge and Lasso models that add regularization to linear regression models. Ridge applies regularization based on the square of the coefficients, and Lasso applies regularization based on the absolute value of the coefficients. Generally, Ridge is preferred.

When using the Ridge and Lasso models, the regularization strength is called alpha and can be adjusted arbitrarily. If the alpha value is large, the regularization is strong, so the coefficients are reduced and underfitted.

One way to find the appropriate alpha value is to draw a graph of the $R^2$ value for the alpha value. You can see that the $R^2$ value decreases as the alpha value increases.

```python
train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    ridge = Ridge(alpha=alpha)
    ridge.fit(train_poly, train_target)
    train_score.append(ridge.score(train_poly, train_target))
    test_score.append(ridge.score(test_poly, test_target))
```

![find_alpha](./resources/ridge.png)
![find_alpha](./resources/lasso.png)

|type| alpha | train_score | test_score |
|---|-------|-------------|------------|
|Linear| - | 0.990 | 0.971|
|Ridge| 0.34 | 0.988| 0.987|
|Lasso| 0.534 | 0.987| 0.986|