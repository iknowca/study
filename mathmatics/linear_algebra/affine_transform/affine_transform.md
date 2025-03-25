# Affine Transform

행렬은 하나의 선형 변환으로 표현할 수 있다.

## Affine Transform

행렬만으로는 평행이동을 표현할 수 없다. 그 이유는 일반적인 행렬의 곱만으로는 벡터간의 덧셈을 표현할 수 없기 때문이다.
평행이동은 다음과 같은 수식으로 표현된다.

$$
\begin{bmatrix}
x' \\
y'
\end{bmatrix}
=
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
+
\begin{bmatrix}
b_1 \\
b_2
\end{bmatrix}
$$

## 행렬 곱으로 평행이동 표현

행렬 곱으로 평행이동을 표현하기 위해서는 다음과 같은 방법을 사용한다.
1. 3차원으로 확장한다.
2. 행렬을 확장한다.
3. 행렬을 곱한다.
4. 결과를 다시 2차원으로 변환한다.

수식으로는 다음과 같이 작성할 수 있다.

$$
\begin{bmatrix}
x' \\
y' \\ 1
\end{bmatrix}
=
\begin{bmatrix}
a_{11} & a_{12} & b_1 \\
a_{21} & a_{22} & b_2 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
x \\ y \\ 1
\end{bmatrix}
$$

이런식으로 방향과 크기 뿐만아니라 위치를 함께 표현하는 변환을 아핀변환이라고 한다.
또한 기존의 N차원 공간을 N+1차원으로 확장하여 표현하는 방법을 동차좌표계(homogeneous coordinates)라고 한다.