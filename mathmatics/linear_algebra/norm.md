# Norm
#norm #linear_algebra

선형대수에서 **norm**은 벡터의 크기를 측정하는 함수다. 직관적으로는 유클리드 공간에서의 벡터의 **길이**를 나타내며, 다양한 norm이 존재한다. 

## Norm의 정의

벡터 공간 $V$에서 정의된 norm은 다음과 같은 성질을 만족하는 함수 $\|\cdot\|: V \to \mathbb{R}$이다.
1. **Non-negativity**: $\|x\| \geq 0$ for all $x \in V$, and $\|x\| = 0$ if and only if $x = 0$.
2. **Definiteness**: $\|x\| = 0$ if and only if $x = 0$.
3. **Homogeneity**: $\|\alpha x\| = |\alpha| \|x\|$ for all $x \in V$ and all scalars $\alpha$.
4. **Triangle inequality**: $\|x + y\| \leq \|x\| + \|y\|$ for all $x, y \in V$.

## Norm의 종류

### 1. Euclidean norm (L2 norm)

$\|x\|_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}$

일반적으로 "거리"개념, 피타고라스 정리를 적용한 거리.

### 2. Manhattan norm (L1 norm) (Taxicab geometry)

$\|x\|_1 = |x_1| + |x_2| + \cdots + |x_n|$
각 성분의 절대값을 더한 것.

### 3. p-norm  (Lp norm)
$\|x\|_p = \left( |x_1|^p + |x_2|^p + \cdots + |x_n|^p \right)^{1/p}$

$p$가 커질수록, $p$-norm은 더 큰 성분에 더 많은 가중치를 부여한다.

### 4. Maximum norm (L∞ norm)
$\|x\|_\infty = \max(|x_1|, |x_2|, \ldots, |x_n|)$

## Norm의 활용

- **거리 측정**: 두 벡터 간의 거리를 측정하는 데 사용된다.
- **최적화**: 최적화 문제에서 목적 함수나 제약 조건을 정의하는 데 사용된다.
- **머신러닝**: 모델의 성능을 평가하거나 정규화하는 데 사용된다.

등등 다양한 분야에서 활용된다.

