# Matrix Multiplication Analysis

#matrix #linear_algebra

행렬의 곱셈은 선형대수에서 중요한 연산이며, 다양한 방식으로 해석할 수 있다.

## 1. Dot Product Interpretation

행렬 곱셈을 직관적으로 이해하는 방법중 하나는 **내적의 관점**이다. 행렬 $A$와 $B$의 곱 $C = AB$는 다음과 같이 정의된다:

$$
A = \begin{bmatrix}
\mathbf a_1^T \\
\mathbf a_2^T \\
\vdots \\
\mathbf a_m^T
\end{bmatrix}, \quad
B = \begin{bmatrix}
\mathbf b_1 & \mathbf b_2 & \cdots & \mathbf b_n
\end{bmatrix}
$$

$$
C = AB = \begin{bmatrix}
\mathbf a_1^T \cdot \mathbf b_1 & \mathbf a_1^T \cdot \mathbf b_2 & \cdots & \mathbf a_1^T \cdot \mathbf b_n \\
\mathbf a_2^T \cdot \mathbf b_1 & \mathbf a_2^T \cdot \mathbf b_2 & \cdots & \mathbf a_2^T \cdot \mathbf b_n \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf a_m^T \cdot \mathbf b_1 & \mathbf a_m^T \cdot \mathbf b_2 & \cdots & \mathbf a_m^T \cdot \mathbf b_n
\end{bmatrix}
$$

여기서 $\mathbf a_i$는 행렬 $A$의 $i$번째 행 벡터이고, $\mathbf b_j$는 행렬 $B$의 $j$번째 열 벡터이다. 즉, 행렬 곱셈은 각 행과 각 열의 내적을 계산하는 것이다.

## 2. Rank 1 Matrix Sum Interpretation
행렬 곱셈을 **랭크 1 행렬의 합**으로 해석할 수도 있다. $A$의 각 열 벡터와 $B$의 각 행 벡터간의 외적을 이용하여 행렬 곱을 표현할 수 이다.

$$
A = \begin{bmatrix}
\mathbf a_1 & \mathbf a_2 & \cdots & \mathbf a_m
\end{bmatrix}, \quad
B = \begin{bmatrix}
\mathbf b_1^T \\
\mathbf b_2^T \\
\vdots \\
\mathbf b_n^T
\end{bmatrix}
$$

$$
C = AB = \sum_{i=1}^{m} \mathbf a_i \mathbf b_i^T
$$

벡터의 외적을 이용하여 행렬 곱을 분해할 수 있다.

## 3. Column space Interpretation

행렬 곱셈을 **열 공간**의 관점에서 해석할 수 있다. 행렬 $C$는 $B$의 컬럼 스페이스를 $A$의 컬럼 스페이스로 변환하는 선형 변환을 나타낸다.

$$
C_j = AB_j
$$

여기서 $C_j$는 행렬 $C$의 $j$번째 열이고, $B_j$는 행렬 $B$의 $j$번째 열이다. 즉, 행렬 곱셈은 각 열 벡터를 변환하는 것이다.

## 4. Row space Interpretation

행렬 곱셈을 **행 공간**의 관점에서 해석할 수 있다. 행렬 $C$는 $A$의 로우 스페이스를 $B$의 로우 스페이스로 변환하는 선형 변환을 나타낸다.
$A$를 행 벡터의 집합으로 보면, 행렬 곱셈은 B를 A의 각 행벡터와 결합하여 새로운 행 벡터를 생성하는 과정이다.

$$
C_i = A_iB
$$
여기서 $C_i$는 행렬 $C$의 $i$번째 행이고, $A_i$는 행렬 $A$의 $i$번째 행이다. 즉, 행렬 곱셈은 각 행 벡터를 변환하는 것이다.

