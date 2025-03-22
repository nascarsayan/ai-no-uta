## 1. What makes a Transformation Linear?

Result is the same irrespective of the order of operations:
- Whether you add first, and then do the transformation or do the transformation first and then add.
- Whether you multiply by a scalar first, and then do the transformation or do the transformation first and then multiply by the scalar.

$$
\begin{cases}
{T}(\mathbf{u} + \mathbf{v}) &= {T}(\mathbf{u}) + {T}(\mathbf{v})\\
{T}(\alpha\mathbf{u}) &= \alpha{T}(\mathbf{u})
\end{cases}
$$

or, in a single equation:

$$
{T}(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha{T}(\mathbf{u}) + \beta{T}(\mathbf{v})
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

---

## 9. Examples of Non-linear Transformations

$$
\begin{align*}
\mathbf{T_1}f(x) &= f^2(x)\\
\mathbf{T_2}f(x) &= f(x^2)\\
\mathbf{T_3}f(x) &= \sin(x)f(x)\\
\mathbf{T_4}f(x) &= f(x) + x
\end{align*}
$$

The second and the third are linear transformations, rest are not.

---

## 10. A Linear Transformation in $\mathbb{R}^N$

- Manipulating numbers is what transformation does here.

$$
\mathbf{T}
\begin{bmatrix}
a \\\ b \\\ c
\end{bmatrix} =
\begin{bmatrix}
b \\\ a \\\ 2c
\end{bmatrix}
$$

$$
\begin{align*}
\mathbf{v_1} &=
\begin{bmatrix}
0 \\\ 0 \\\ 1
\end{bmatrix} \quad &\lambda: 2\\
\mathbf{v_2} &=
\begin{bmatrix}
1 \\\ 1 \\\ 0
\end{bmatrix} \quad &\lambda: 1\\
\mathbf{v_3} &=
\begin{bmatrix}
1 \\\ -1 \\\ 0
\end{bmatrix} \quad &\lambda: -1
\end{align*}
$$

---

## 11. Another Linear Transformation in $\mathbb{R}^N$

$$
\mathbf{T}
\begin{bmatrix}
a \\\ b \\\ c
\end{bmatrix} =
\begin{bmatrix}
(a+b)/2 \\\ (a+b)/2 \\\ c
\end{bmatrix}
$$

$$
\begin{align*}
\mathbf{v_1} &=
\begin{bmatrix}
1 \\\ 1 \\\ 0
\end{bmatrix} \quad &\lambda: 1\\
\mathbf{v_2} &=
\begin{bmatrix}
1 \\\ -1 \\\ 0
\end{bmatrix} \quad &\lambda: 0\\
\mathbf{v_3} &=
\begin{bmatrix}
0 \\\ 0 \\\ 1
\end{bmatrix} \quad &\lambda: 1
\end{align*}
$$

---

## 12. All Transformations in $\mathbb{R}^N$ can be Represented by Matrix Products

$$
\begin{align*}
\mathbf{T_1}
\begin{bmatrix}
a \\\ b \\\ c
\end{bmatrix} &=
\begin{bmatrix}
b \\\ a \\\ 2c
\end{bmatrix} &=&
\begin{bmatrix}
0 & 1 & 0 \\\ 1 & 0 & 0 \\\ 0 & 0 & 2
\end{bmatrix}
\begin{bmatrix}
a \\\ b \\\ c
\end{bmatrix}\\
\mathbf{T_2}
\begin{bmatrix}
a \\\ b \\\ c
\end{bmatrix} &=
\begin{bmatrix}
(a+b)/2 \\\ (a+b)/2 \\\ c
\end{bmatrix} &=&
\begin{bmatrix}
1/2 & 1/2 & 0 \\\ 1/2 & 1/2 & 0 \\\ 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
a \\\ b \\\ c
\end{bmatrix}
\end{align*}
$$

A transformation is linear iff the transformation can be represented by a matrix product.

$$
\mathbf{T}
\begin{bmatrix}
a \\\ b \\\ c
\end{bmatrix} =
\begin{bmatrix}
a^2 \\\ abc \\\ b+1
\end{bmatrix}
$$

Above one isn't linear. (None of the entries are)

---

## 13. The Identity Crisis, I mean Transformation

$$
\mathbf{Iv} = \mathbf{v}
$$

- The only eigenvalue is 1.
- All vectors are eigenvectors.
  + If the space is n-dimensional, there are n representative eigenvectors.

---

## 14. Why Eigenvalues and Eigenvectors are so Important?

Suppose we can write $\mathbf{v}$ as a linear combination of some linearly independent vectors (__basis vectors__) $\mathbf{v_1}, \mathbf{v_2}, \ldots, \mathbf{v_n}$:

$$
\mathbf{v} = \alpha_1\mathbf{v_1} + \alpha_2\mathbf{v_2} + \ldots + \alpha_n\mathbf{v_n}
$$

Then, any transformation $\mathbf{T}$ applied to $\mathbf{v}$ can be written as:

$$
\mathbf{Tv} = \alpha_1\mathbf{Tv_1} + \alpha_2\mathbf{Tv_2} + \ldots + \alpha_n\mathbf{Tv_n}
$$

This is because of the linearity property of the transformation.

In words:

> __If we know what happens to the basis vectors after transformation, then we know the entire tranformation.__

Now, let's talk about the special case, where the basis vectors are chosen as the eigenvectors of the transformation.

$$
\begin{align*}
\mathbf{Tv} &= \alpha_1\mathbf{Te_1} + \alpha_2\mathbf{Te_2} + \ldots + \alpha_n\mathbf{Te_n}\\
&= \alpha_1\lambda_1\mathbf{e_1} + \alpha_2\lambda_2\mathbf{e_2} + \ldots + \alpha_n\lambda_n\mathbf{e_n}
\end{align*}
$$

> [!IMPORTANT]
>
> So, if the pre-image had the coefficients $\alpha_1, \alpha_2, \ldots, \alpha_n$, then the image will have the coefficients $\alpha_1\lambda_1, \alpha_2\lambda_2, \ldots, \alpha_n\lambda_n$.

---

## 15. The Null Space of a Linear Transformation

- The null space of a transformation is the set of all vectors whose image is the zero vector.
- The null space is closed under addition and scalar multiplication (hence the name __space__).
- The null space can also be considered as the eigenspace corresponding to the eigenvalue $\lambda = 0$.

The null space of the transformation is the null space of the matrix representing the transformation. Simple!

---

## 16. The Inverse of a Linear Transformation

The inverse of a tranformation is defined as:

$$
\begin{align*}
\mathbf{T}^{-1}\mathbf{Tv} &= \mathbf{v}, \quad or\\
\mathbf{T}^{-1}\mathbf{T} &= \mathbf{I}
\end{align*}
$$

- Reflection is its own inverse: $R^{-1} = R$
- If we have a non-trivial null space, then we can't have an inverse. Because, __in the inverse transformation where will you send back the null vector back to?__

- Projection does not have inverse

- Rotation has inverse: ${R_\alpha}^{-1} = R_{-\alpha}$

- Translation is not linear, but still we can talk about its inverse. $T_{\vec{a}}^{-1} = T_{-\vec{a}}$

For the differential transformation in polynomials:
- $\mathbf{Dc} = 0$
  + The constant function is in the null space
  + Inverse does not exist, as all candiates for the inverse will differ by a constant function.
- $\mathbf{D}(ax + b) = c$
  + Any linear function is in the null space.
  + Inverse does not exist, as all candiates for the inverse will differ by a linear function.

$$
\text{Non-trivial } \mathbf{N} \iff \text{No Inverse}
$$

$$
\begin{align*}
\mathbf{T u_1} &= \mathbf{v}\\
\mathbf{T u_2} &= \mathbf{v}\\
\hline
\mathbf{T(u_1 - u_2)} &= \mathbf{0}
\end{align*}
$$

The pre-images differ by a vector in the null space.

---

## 17. The Eigenvalue Algorithm

__How did we arrive to the algorithm? This video shows the full intuition by taking an example__

We need to find the eigenvalues for a particular linear tranformation, represented as a matrix. In words this is:

$$
\begin{bmatrix}
2 & 1 \\
1 & 2
\end{bmatrix}
\begin{bmatrix}
x \\\ y
\end{bmatrix} =
\lambda
\begin{bmatrix}
x \\\ y
\end{bmatrix}
$$

There are 2 equations and 3 unknowns. So, how to slove this? Maybe if we break it down into 2 equations, we might have some intuition.

$$
\begin{cases}
2x + y &= \lambda x\\
x + 2y &= \lambda y
\end{cases}
$$

Now, we can rewrite this as:

$$
\begin{cases}
(2 - \lambda)x + y &= 0\\
x + (2 - \lambda)y &= 0
\end{cases}
$$

In matrix form:

$$
\begin{bmatrix}
2 - \lambda & 1 \\
1 & 2 - \lambda
\end{bmatrix}
\begin{bmatrix}
x \\\ y
\end{bmatrix} =
\begin{bmatrix}
0 \\\ 0
\end{bmatrix}
$$

But still, this isn't linear right? Yes, $\lambda$ is the variable. We are essentially looking for those magical values of $\lambda$ that will make the columns linearly dependent.

Determinants to the rescue! We want to know when the matrix is singlular $\iff$ determinant is 0.

$$
\begin{align*}
\begin{vmatrix}
2 - \lambda & 1 \\
1 & 2 - \lambda
\end{vmatrix}
&= (2 - \lambda)^{2} - 1\\
&= \lambda^{2} - 4\lambda + 3 = 0\\
\end{align*}
$$

This polynomial is called the __characteristic polynomial__. When we equate to 0, it's called the __characteristic equation__. It's roots are the eigenvalues, also called the __characteristic values__.

$$
\lambda = 1, 3
$$

We now plug in each individual eigenvalue back into the original equation to find the null spaces for each eigenvalue.

$$
\begin{align*}
\lambda _1 = 1\\
\begin{bmatrix}
1 & 1 \\
1 & 1
\end{bmatrix}
\end{align*}\\
\mathbf{v_1} = \begin{bmatrix}
1 \\\ -1
\end{bmatrix}
$$

$$
\begin{align*}
\lambda _2 = 3\\
\begin{bmatrix}
-1 & 1 \\
1 & -1
\end{bmatrix}
\end{align*}\\
\mathbf{v_2} = \begin{bmatrix}
1 \\\ 1
\end{bmatrix}
$$

---

## 18. Algebraic Derivation of the Eigenvalue Algorithm

$$
\begin{align*}
\mathbf{Ax} &= \lambda\mathbf{x}\\
\mathbf{Ax} - \lambda\mathbf{x} &= \mathbf{0}\\
\mathbf{Ax} - \lambda\mathbf{I}\mathbf{x} &= \mathbf{0}\\
(\mathbf{A} - \lambda\mathbf{I})\mathbf{x} &= \mathbf{0}\\
|\mathbf{A} - \lambda\mathbf{I}| &= 0
\end{align*}
$$

The $\mathbf{I}$ was plugged in artificially to because matrix - scalar number does not make sense.

__Try to stick to matrices as whole indivisible objects, and use matrix algebra as far as possible.__

---

## 19. Determining Eigenvalues and Eigenvectors - A Detailed Example

> [!NOTE]
>
> 1. The trace of a matrix is the sum of the diagonal elements.
> 2. The sum of the eigenvalues is equal to the trace of the matrix.
> 3. The product of the eigenvalues is equal to the determinant of the matrix.

Find the eigenvalues of the matrix:

$$
\begin{bmatrix}
17 & -6 \\
45 & -16
\end{bmatrix}
$$

---

## 20. The Sum is the Trace and the Product is the Determinant

Algebraic proof:

$$
\begin{align*}
\mathbf{p}(\lambda) 
&= |\mathbf{A} - \lambda\mathbf{I}|\\
\quad\\
&= \begin{vmatrix}
a_11 - \lambda & \ldots & \ldots & \ldots \\
\ldots & a_22 - \lambda & \ldots & \ldots\\
\vdots & \vdots & \ddots & \vdots\\
\ldots & \ldots & \ldots & a_nn - \lambda
\end{vmatrix}\\
\quad\\
&= \pm \lambda^n \mp C_{n-1}\lambda^{n-1} \pm \ldots + C_0
\end{align*}
$$

- For the coefficient of $\lambda^{n-1}$, there is only one way to get it - take all the diagonal elements. Because if we miss a diagonal element, we will miss two during the permutation of the determinant term.

So, 

$$
\mp C_{n-1}\lambda^{n-1} \text{ will come from} \prod_{i=1}^{n}(a_{ii} - \lambda)
$$

To take all but one $\lambda$ from the product, there are $n$ ways to do it, and every time we get the coefficient as the constant from the term we missed taking $\lambda$ from.

So, the coefficient of the $\lambda^{n-1}$ term is the sum of the diagonal elements (also called __the trace of the matrix__).

$$
\mp C_{n-1} = \mp \sum_{i=1}^{n}a_{ii}
$$

The constant term can be evaluated by putting $\lambda = 0$ in $\mathbf{p}(\lambda)$.

$$
\mathbf{p}(0) = |A| = C_0
$$

Hence, the constant term is the determinant of the matrix.

TIll now, we haven't spoken about the eigenvalues. Once we have computed the roots of the characteristic polynomial, we'll have the eigenvalues. Then the same characteristic polynomial can be written as:

$$
\begin{align*}
&\pm \lambda^{n-1} \mp C_{n-1}\lambda^{n-1} + \ldots + C_0 \\ =& (\lambda _1 - \lambda)(\lambda _2 - \lambda)\ldots(\lambda _n - \lambda)
\end{align*}
$$

Now, again, the coefficient of $\lambda^{n-1}$ is the sum of the roots, and the constant term is the product of the roots.

$$
\begin{align*}
&(\lambda_1 - \lambda)(\lambda_2 - \lambda)\ldots(\lambda_n - \lambda) \\
=&\lambda^n - \sum_{i=1}^{n}\lambda^{n-1} + \ldots + (-1)^n\prod_{i=1}^{n}\lambda_i\\
=&\pm \lambda^n \mp \sum_{i=1}^{n}a_{ii}\lambda^{n-1} \pm \ldots + |A|
\end{align*}
$$

Hence, by term matching:

$$
\begin{align*}
\sum_{i=1}^{n}\lambda_i &= \sum_{i=1}^{n}a_{ii}\\
\prod_{i=1}^{n}\lambda_i &= |A|
\end{align*}
$$

---

## 21. $\mathbf{A}$ and $\mathbf{A}^{T}$ have the same eigenvalues

The characteristic polynomial of $\mathbf{A}$ is the same as the characteristic polynomial of $\mathbf{A}^{T}$.

$$
\begin{align*}
p_{\mathbf{A}}(\lambda) &= |\mathbf{A} - \lambda\mathbf{I}|\\
p_{\mathbf{A}^{T}}(\lambda) &= |\mathbf{A}^{T} - \lambda\mathbf{I}|\\
\quad\\
\because |\mathbf{A}^{T} - \lambda\mathbf{I}| &= |\mathbf{A}^{T} - \lambda\mathbf{I^T}|\\
\quad\\
\therefore p_{\mathbf{A}^{T}}(\lambda) &= |(\mathbf{A} - \lambda\mathbf{I})^T|\\
&= |\mathbf{A} - \lambda\mathbf{I}|\\
&= p_{\mathbf{A}}(\lambda)
\end{align*}
$$

Hence, the eigenvalues of $\mathbf{A}$ and $\mathbf{A}^{T}$ are the same (but not the eigenvectors).

---

## 22-25. Eigenvalues and Eigenvectors : Exercises

We solve some exercises on eigenvalues and eigenvectors.

---

## 26. Repeated Eigenvalues and the Geometric Multiplicity

- When the eigenspace is multi-dimensional, we need to pick some linearly independent arbitrary eigenvectors to represent the eigenspace.
- The geometric multiplicity of an eigenvalue is the dimension of the eigenspace corresponding to that eigenvalue.

---

## 27. Repeated Eigenvalues and the Algebraic Multiplicity

- The algebraic multiplicity of an eigenvalue is the number of times it appears as a root of the characteristic polynomial.

---

## 28. Algebraic Multiplicity Matches Geometric Multiplicity

Typically, the algebraic multiplicity of an eigenvalue is equal to the geometric multiplicity. (most cases).

---

## 29. Defective Matrices

- When the algebraic multiplicity is greater than the geometric multiplicity, the matrix is called defective.

$$
\begin{bmatrix}
3 & 2 \\
 & 3 \\
\end{bmatrix}\\
\quad\\
\begin{bmatrix}
3 & 2 & \\
& 3 & 4 \\
&  &  3
\end{bmatrix}
$$

Eigenvalue = $(3, 3)$, $(3, 3, 3)$ respectively.

Substitute $\lambda = 3$ in the matrix:

$$
\begin{bmatrix}
0 & 2 \\
0 & 0
\end{bmatrix}\\
\begin{bmatrix}
0 & 2 & 0\\
0 & 0 & 4\\
0 & 0 & 0
\end{bmatrix}
$$

We see, that the geometric multiplicity is 1 in both cases, but the algebraic multiplicity is 2 and 3 respectively.

A defective matrix need not be triangular.

$$
\begin{bmatrix}
4 & -1 \\
1 & 2
\end{bmatrix}
$$

Eigenvalue = $(3, 3)$
Eigenvector = $(1, 1)$

__The defect is the difference between the algebraic and the geometric multiplicity.__

Defect can be greater than 1 too.

__The defective property is fragile.__
- If you change some entry in the matrix by a very small amount, the matrix will become non-defective, and the changes in the eigenvalues is much greater than the change in the matrix.
  + Compared to this the changes in the eigenvalues in symmetric matrices is much more proportional to the changes in the matrix made to make it non-symmetric.
- The probability that you'll get a defective matrix in applications (in the real world) is 0.

---

## 30. Defective Transformations?

We observe that cubic polynomials have algebraic multiplicity 4, but geometric multiplicity 1.

---

## 31. Generalized Eigenvectors

We learn more about defects here, and how to find the remaining bases of the eigenspace.

- generalized vectors are the remaining vectors in the eigenspace.
- The generalized vectors are the solutions to the equation $(\mathbf{A} - \lambda\mathbf{I})\mathbf{v} = \mathbf{u}$, where $\mathbf{u}$ is the generalized vector.
- The generalized vectors are not eigenvectors, but they are in the eigenspace.
- If we have n eigenvectors then we have (dimension of the eigenspace - n) generalized vectors.
- All the generalized vectors are linearly independent.

$$
\begin{bmatrix}
6 & -2 & -1\\
3 & 1 & -1\\
2 & -1 & 2
\end{bmatrix}
$$

$$
p(\lambda) = (3 - \lambda)^3
\implies \lambda = 3, 3, 3
$$

$$
\begin{align*}
\begin{bmatrix}
3 & -2 & -1\\
3 & -2 & -1\\
2 & -1 & -1
\end{bmatrix}
\begin{bmatrix}
1 \\\ 1 \\\ 1
\end{bmatrix} &=
\begin{bmatrix}
0 \\\ 0 \\\ 0
\end{bmatrix}\\
\begin{bmatrix}
3 & -2 & -1\\
3 & -2 & -1\\
2 & -1 & -1
\end{bmatrix}
\begin{bmatrix}
0 \\\ 0 \\\ -1
\end{bmatrix} &=
\begin{bmatrix}
1 \\\ 1 \\\ 1
\end{bmatrix} \text{Generalized vector Rank 2}\\
\begin{bmatrix}
3 & -2 & -1\\
3 & -2 & -1\\
2 & -1 & -1
\end{bmatrix}
\begin{bmatrix}
0 \\\ -1 \\\ 2
\end{bmatrix} &=
\begin{bmatrix}
0 \\\ 0 \\\ -1
\end{bmatrix} \text{Generalized vector Rank 3}
\end{align*}
$$

---

## 32. Generalized Eigenvector Example

$$
\begin{bmatrix}
4 & 1 & 0\\
1 & 4 & 1\\
4 & -4 & 7
\end{bmatrix}
$$

---

## 33. Defective Transformations!

- Null space is also called the __kernel of the transformation__.

Defective transformations can be realised in transformations outside the $\mathbb{R}^n$ space too.
For example, in the polynomial space, the derivative operator in the cubic polynomial space is defective. The null space is the linear polynomials, and the algebraic multiplicity is 3. We can use the same method we used for the matrix to find the generalized eigenvectors.

$$
\frac{d}{dx} 1 = 0, \lambda = 0
$$

Since $\lambda = 0$, to find the rank 2 genereated eigenvector, $\frac{d}{dx} - 0I$ is still the same as $\frac{d}{dx}$.

$1$, the eigenvector, is also in the range of the transformation. Pre-image o $1$:

$$
\frac{d}{dx} x = 1
$$

$x$ is the generalized eigenvector of rank 2. It is also in the range of the transformation.

$$
\frac{d}{dx} 1/2 x^2 = x
$$

$1/2 x^2$ is the generalized eigenvector of rank 3. It is also in the range of the transformation.

$$
\frac{d}{dx} 1/6 x^3 = 1/2 x^2
$$

$1/6 x^3$ is the generalized eigenvector of rank 4. It is also in the range of the transformation.

The process stops here for cubic polynomials.

---

