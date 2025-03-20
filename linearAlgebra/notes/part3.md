## 1. What makes a Transformation Linear?

Result is the same irrespective of the order of operations:
- Whether you add first, and then do the transformation or do the transformation first and then add.
- Whether you multiply by a scalar first, and then do the transformation or do the transformation first and then multiply by the scalar.

$$
\begin{cases}
\operatorname{T}(\mathbf{u} + \mathbf{v}) &= \operatorname{T}(\mathbf{u}) + \operatorname{T}(\mathbf{v})\\
\operatorname{T}(\alpha\mathbf{u}) &= \alpha\operatorname{T}(\mathbf{u})
\end{cases}
$$

or, in a single equation:

$$
\operatorname{T}(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha\operatorname{T}(\mathbf{u}) + \beta\operatorname{T}(\mathbf{v})
$$

---

## 2. The reflection transformation and intro to eigenvalues

A transformation is written as $\mathbf{R}$. When $\mathbf{R}$ is applied to a vector $\mathbf{u}$, the result is written as $\mathbf{R}\mathbf{u}$, inspired by the matrix notation, and not function notation.

- Given any transformation, we have to first check if it is linear.
- Once we have identified it is linear, we are asked the question: Are there any vectors, which after transformation (i.e., the __image__ of a vector), remain parallel to the __pre-image__?
  + Each vector is called __eigenvector__.
  + The scalar factor making the image parallel to the pre-image is called the __eigenvalue__.
- The maths notation is:
  + $\mathbf{R}\mathbf{v} = \lambda\mathbf{v}$.
  + $\mathbf{v}$ is the eigenvector.
  + $\lambda$ is the eigenvalue.

> _Eigen is a german word meaning "own" or "self"._

- For the reflection transformation, we have two cases:
  + Vectors on the line of reflection remain unchanged.
  + Vectors orthogonal to the line of reflection become their opposite.
- We have two sets of vectors, each set is called an __eigenspace__.
- Hence, for reflection, we have two eigenvalues:
  - $\mathbf{R}\mathbf{v_{parallel}} = \mathbf{v_{parallel}}$
  - $\mathbf{R}\mathbf{v_{orthogonal}} = -\mathbf{v_{orthogonal}}$

Another intriguing question is this:
- When we apply R twice, we get the identity transformation. And the roots of the equation $x^2 = 1$ are $\pm 1$.
- What is this connection between the eigenvalues and the roots of the equation? 🤓 We'll discover later.

---

## 3. The Projection Transformation

- The projection transformation is denoted by $\mathbf{P}$.
- There are 2 cases:
  + Vectors on the line of projection remain unchanged. ($\lambda = 1$)
  + Vectors orthogonal to the line of projection become the zero vector. ($\lambda = 0$)

$\lambda = 0$ (i.e., eigenvalue = 0 is perfectly legitimate).
However, $\mathbf{v} = 0$ should not be considered as an eigenvector. Because, $\mathbf{T}\vec{0} = \vec{0}$ for any linear transformation $\mathbf{T}$.

$R^2 = R$ for projection transformation. Roots are $\lambda = 0, 1$.

---

## 4. The Rotation Transformation

- Rotation by an angle $\alpha$ is denoted by $\mathbf{R}_\alpha$.
- It's a linear transformation (You can imagine the whole space is rotated by the given angle). So, addition and scalar multiplication are preserved.
- There are no eigenvectors for general values of $\alpha$.
- However, for some special values of $\alpha$, there are eigenvectors.
  + For $\alpha = 2k\pi$, where $k$ is an integer, all vectors are eigenvectors with eigenvalue 1.
  + For $\alpha = (2k + 1)\pi$, where $k$ is an integer, all vectors are eigenvectors with eigenvalue -1.

---

## 5. The Translation Transformation

- Translation by a vector $\vec{a}$ is denoted by $\mathbf{T}_{\vec{a}}$.
- This is not a linear transformation. It does not pass the addition or the scalar multiplication test.
- Also, we observe $\mathbf{T}{\vec{0}} \ne \vec{0}$, which is at the core of the definition of a linear transformation.

---

## 6. Geometric Transformation in Space

- Reflection:
  + On a plane
    - There is a plane of eigenvalue 1, the plane of rotation itself.
    + There is line of eigenvalue -1, the line perpendicular to the plane of reflection.
    + Eigenvalues: $\lambda = {1, 1, -1}$
  + On a line
    - There is a line of eigenvalue 1, the line of reflection itself.
    - There is a plane of eigenvalue -1, the plane perpendicular to the line of reflection.
    - Eigenvalues: $\lambda = {1, -1, -1}$
- Projection:
  + On a plane
    - There is a plane of eigenvalue 1, the plane of projection itself.
    - There is a line of eigenvalue 0, the line perpendicular to the plane of projection.
    - Eigenvalues: $\lambda = {1, 1, 0}$
  + On a line
    - There is a line of eigenvalue 1, the line of projection itself.
    - There is a plane of eigenvalue 0, the plane perpendicular to the line of projection.
    - Eigenvalues: $\lambda = {1, 0, 0}$
- Rotation (along an axis):
  - There is a single eigenvalue - The axis of rotation itself.
  - __In some exceptional cases like this, the number of eigenvalues is not equal to the dimension of the space.__ $\lambda = {1}$
  - We'll learn more about rotation later.

---

## 7. The Derivative as a Linear Transformation

- $\mathbf{D}$ is the first derivative operator
- $\mathbf{D}^2$ is the second derivative operator

Consider the following:

$$
\begin{align*}
\mathbf{D}&(x^2 + x) &= 2x + 1\\
\mathbf{D}&^2(x^4-3x^3) &= 12x^2 - 18x\\
\mathbf{D}&^2{e^{2x}} &= 4e^{2x}\\
\mathbf{D}&^2{sin 5x} &= -25sin 5x
\end{align*}
$$

Are they linear transformations?

All of these are linear because as per calculus:

$$
\begin{align*}
(f+g)' &= f' + g'\\
(cf)' &= cf'\\
(f+g)'' &= f'' + g''\\
(cf)'' &= cf''\\
\end{align*}
$$

- __Eigenfunctions__ for polynomials:
  + For $\mathbf{D}$:
    - eigenvector is the constant function $\mathbf{D}c = 0c$
    - eigenvalue is 0
  + For $\mathbf{D}^2$:
    - eigenvector is the linear function $\mathbf{D}^2(ax + b) = 0(ax + b)$, hece it's 2 dimensional.
    - eigenvalue is 0
  + $\mathbf{D}^n$ will have $n$-dimensional eigenspace.

- Exponential $\mathbf{D}e^{px} = pe^{px}$
  + For any $p$, $e^{px}$ is an eigenvector with eigenvalue $p$.
  + So, in the space of exponential functions, there are infinitely many eigenvectors. (__needs more clarity, didn't get it fully__)
- Exponential $\mathbf{D}^{2}e^{px} = p^{2}e^{px}$
  + For a particular eigenvalue $p^2$, now there are 2 eigenvectors: $e^{px}$ and $e^{-px}$: the eigenspace is 2-dimensional.
  + All the eigenvalues are positive numbers.
- Sines and cosines double derivatives:
  + $\mathbf{D}^{2}\sin px = -p^{2}\sin px$
  + $\mathbf{D}^{2}\cos px = -p^{2}\cos px$
  + The eigenspace is 2-dimensional. (__Will need to be proven later__)

---

## 8. Dilation as a Linear Transformation

- Dilation was thoroughly researched by Gilbert Strang.
- Dilation invites us to do a substitution, plug in some other expression of x instead of x.
- Example: $\mathbf{D}f(x) = f(2x - 1)$

$$
\begin{align*}
\mathbf{D}x^2 &= (2x - 1)^2 = 4x^2 - 4x + 1\\
\mathbf{D}(x-1) &= (2x-1) - 1 = 2x - 2\\
\mathbf{D}(x^2 + x - 1) &= (2x-1)^2 + (2x-1) - 1\\
&= 4x^2 - 4x + 1 + 2x - 1 - 1\\
&= 4x^2 - 2x - 1
\end{align*}
$$

- Finding all eigenvalues and eigenfunctions (the name for eigenvectors in this context) is a bit tricky.
- Computers might help here.