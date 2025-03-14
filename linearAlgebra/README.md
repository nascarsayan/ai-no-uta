# Linear Algebra

Learning linear Algebra. The plan is to take notes and write sample code in python while learning.

To convert drawings to Latex, use the website [webdemo.myscript.com](https://webdemo.myscript.com/views/math/index.html)

- Encouraged to follow exercises from the website: [https://www.lem.ma/](https://www.lem.ma/)
- You can also download videos from the [first youtube Playlist](https://www.youtube.com/watch?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv) to follow offline.
- [Youtube Channel](https://www.youtube.com/@MathTheBeautiful).
- The Professor is [Pavel GrinFeld](https://grinfeld.org/index.html).

List of playlists:
- [Part 1: Intro and Applications](https://www.youtube.com/playlist?list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv)
- [Part 2: Intro and Applications](https://www.youtube.com/playlist?list=PLlXfTHzgMRULWJYthculb2QWEiZOkwTSU)
- [Part 3: Linear Transformations](https://www.youtube.com/watch?list=PLlXfTHzgMRUIqYrutsFXCOmiqKUgOgGJ5)
- [Part 4: Inner Products](https://www.youtube.com/watch?v=Ww_aQqWZhz8&list=PLlXfTHzgMRULZfrNCrrJ7xDcTjGr633mm)

```bash
# brew install yt-dlp
playlistIds=(
    PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv
    PLlXfTHzgMRULWJYthculb2QWEiZOkwTSU
    PLlXfTHzgMRUIqYrutsFXCOmiqKUgOgGJ5
    PLlXfTHzgMRULZfrNCrrJ7xDcTjGr633mm
)
for playlistId in ${playlistIds[@]}; do
    yt-dlp -f bestvideo+bestaudio --merge-output-format mp4 -o "%(playlist)s/%(playlist_index)s-%(title)s.%(ext)s" --write-thumbnail --write-auto-sub --embed-subs --embed-metadata --embed-thumbnail "https://www.youtube.com/playlist?list=$playlistId"
done
```

---

## 1. Intro :  Eye vs Ear

- How our eyes perceive light vs how our ears perceive sound.
- Eye is very complex. Retina has 120 million rods and 6 million cones. The brain has to process all this information. Resolution of the eye is 576 megapixels, while the best monitors have 33 megapixels.
- Ear has a single sensor. Ear takes in the sum of all the sound waves. The brain processes this information. The ear has a resolution of 4000 bits per second, while the best microphones have 1000 bits per second.

---

## 2. Showcase : Approximating functions using Guassian Quadrature

**Approximating area under a curve**

Area under a curve can be approximated using rectangles, trapezoids, or Guassian Quadrature.

**Guassian Quadrature**

- Guassian Quadrature is a method for numerical integration. It is based on the idea that the integral of a function can be approximated by a weighted sum of the function at certain points. The weights and points are chosen in such a way that the approximation is extremely accurate.

This is related to linear algebra somehow 😅

---

## 3. Linear Addition of Sounds

- If a sound is simply an array of numbers, then adding two sounds is simply adding two arrays.
- If we add two sounds, we get a new sound that is the sum of the two sounds.

```py
bach + mlk # adding Bach and LMK speech
0.5*bach + mlk # adding half amplitude of Bach with LMK speech
```

---

## 4. Linear Decomposition

- Decomposition is not possible, in these examples:
  + I have some 5 rupee coins, some 10 rupee coins. Total is 100 rupees. How many 5 rupee coins and 10 rupee coins do I have? -> This has some finite number of solutions.
  + If count can be negative, then there are infinite solutions.
- For sound it is possible to decompose. We can decompose a sound into a sum of other sounds.
- In a situation, can we decompose? Classifications:
  + Decomposition is possible in a unique way.
  + Decomposition is not unique - infinite ways to decompose.
  + Decomposition is not possible - can't be decomposed.

---

## 5. The Three Fundamental Examples of Vectors

> Vectors are the kinds of objects that can be:
>   + Added together
>   + Multiplied by a number
>   
> To create an object of the same kind.

**Geometric Vectors**

- A geometric vector is a directed segment.
- Least abstract objects - since they are drawings.
- Much of inspiration and intuition in the world of linear algebra comes from geometric vectors.

**Polynomials**

- Polynomials are vectors.
- We can throw in sines, cosines, exponentials too. We can add two functions, and multiply a function by a number.
- Functions are vectors too!
- Polynomials is **a vector sub-space** of functions.

- Space of vectors is very useful to physicists.
- Mathematicians and physicists have a healthy obsession with exact mathemical expressions. They like to capture phenomena in the world with exact mathematical expressions.

**$\mathbb{R}^n$**

- $\mathbb{R}^n$ is the set of all n-tuples of real numbers.
- As abstract as it gets. When in everydya life do we encounter n-tuples of real numbers?

They are very important kinds of vectors:
1. The algorithms of linear algebra are stated, formulated, explored in $\mathbb{R}^n$.
2. Computers are particularly helpful if yyou can restate your problem in terms of sets of numbers.
3. All spaces look like $\mathbb{R}^n$.

By studying $\mathbb{R}^n$, we are studying all other kinds of vector spaces.

---

## 6. Geometric Vectors: Addition

> Typically, in introductory courses, we add a coordinate-system, and geometric vectors are defined as tip of the coordinates. Prof. Pavel (will refer to him as simply "Pavel", hereafter ☺️) encourages to give up the coordinate system, and just think of geometric vectors as directed segments floating in space.

- Suppose you want to go from a village O to a village R. The following pieces of information are not enough alone:
  + The distance from O to R. This reduces to a circle of possible locations.
  + The direction from O to R. This reduces to a ray of possible locations.

The displacement is captured by this directed segment. This is a geometric vector.

- We can add geometric vectors to denote the displacement from O to R, and then from R to S. This is the same as going from O to S.
- We can multiply a geometric vector by a number. Positive number means same direction, negative number means opposite direction. The magnitude of the vector is scaled by the number.
- When we add 2 vectors, the sum of the vectors lies in the same plane containing the 2 vectors.

---

## 7. Commutativity, Associativity, Distributivity for Geometric Vectors

$$
\begin{align*}
\text{Commutativity:} & \quad \vec{a} + \vec{b} = \vec{b} + \vec{a} \\
\text{Associativity:} & \quad (\vec{a} + \vec{b}) + \vec{c} = \vec{a} + (\vec{b} + \vec{c}) \\
\text{Distributivity:} & \quad \alpha(\vec{a} + \vec{b}) = \alpha\vec{a} + \alpha\vec{b}
\end{align*}
$$

- Associativity is a much more fundamental property than commutativity. Matrices are not commutative, but they are associative.
- 😅 Every operation that Pavel uses in his research are associative! That's how common associative properties are!
- How fundamental are these properties? (First is the more fundamental)
  + Associativity (most fundamental)
  + Commutativity
  + Distributivity (least fundamental)

All of them are about the order of operations not mattering:
- Commutativity: Order of the terms doesn't matter.
- Associativity: Order of the two addition operations doesn't matter.
- Distributivity: Order of the multiplation operation and the addition operation doesn't matter.

![Fundamental Laws](./assets/01_fundamental_laws.svg)

---

## 8. The Origin in the Plane and the Parallelogram Rule

Suppose, vectors all over the place:
- Some start at origin
- Some start at the tip of another vector
- Some seem to float in the plane wherever they want.

This is perfectly legitimate approach - vectors can be drawn anywhere as long as the length and direction of the vector is kept the same. However, linear algrebra takes a much cleaner approach for aesthetics and simplicity.

In linear algebra:
- We will choose a point that will be called the origin.
- We will only consider vectors that start at the origin.
- We might have to draw temporary constructions tosolve the problems, but once we find the answer, we will have to bring it back to the origin, because those are the only vectors which are part of the game.

Hence, the parallelogram rule which states that the sum of two vectors is the diagonal of the parallelogram formed by the two vectors.

- The parallelogram rule fails to be intuitively applicable in one dimentional geometric vectors! 😂 We cannot complete a parallelogram where the two vectors intersect.

---

## 9,10. Subtraction of Geometric Vectors

Two ways to do $\vec{a} - \vec{b}$:
1. $\vec{a} + (-\vec{b})$ : We can use the addition operation that we already know with $-\vec{b}$.
2. $\vec{a} - \vec{b}$ is such a vector that when added to $\vec{b}$ gives $\vec{a}$.

![Subtraction of Geometric Vectors](./assets/02_subtraction_of_vectors.svg)

Subtraction is a piece of cake when vectors originate from the same point (origin) - Just draw from one tip to another tip.

However, addition results can have larger error because additional construction is involved.

![Subtraction is easier](./assets/03_sub_is_easier.svg)

---

## 11. What else works like Geometric Vectors?

We've used displacements or relative locations between points as our intuition for what Geometric Vectors represent. What else can be used as Geometric Vectors?

1. Displacements
2. Velocities
3. Accelerations
4. Forces

- The actions need not be sequential. They can be concurrent. Example:
  + A train is moving 60 miles per hour in the north direction.
  + A ladybug inside the train is moving 60 inches per hour (with respect to the train) in the east direction. <br/>
  Then, the two displacement vectors can be added to get the displacement of the ladybug with respect to the ground. <br/>
  Similar addition can be done for velocities and accelerations, and it can be derived algebraically from the displacement vectors.
- Force is different. For force vector, we have to believe in Newton's law $\vec{F} = m\vec{a}$. There is no way we can derive addition of forces without Newton's law. Possible explanations:
  + Since $\vec{a}$ is a vector, multiplication of mass (scalar) and acceleration, $m\vec{a}$, gives the force vector $\vec{F}$.
  + Why do forces add up to the parallelogram rule? Because Newton said so, and we don't know why! 🙏'
  + [Check discussions in the comment section.](https://www.youtube.com/watch?v=SPdqsGIAcXM&list=PLlXfTHzgMRUKXD88IdzS14F4NxAZudSmv&index=11)

---

## 12. Polynomials or Functions as Vectors

- Useful in numerical analysis.
- Complex phenomena or problems can be represented as polynomial functions.
- Now, while talking about polynomials, do two quadratic polynomials add up to a quadratic polynomial? No necessarily - the higher degree terms might cancel out. Even, we can multiply by 0 to get the zero polynomial. <br/>
  Hence, **terminology needs to fixed**: we cannot say n-degree polynomials, rather **polynomials upto degree n.**

Similar to how the linear combination of two geometric vectors are stuck in the plane containing the two vectors, the linear combination of two polynomials having a root as K will also have K as a root.

---

## 13. Is one polynomial a multiple of another?

$$
\begin{align*}
p(x) &= x + 1 \\
q(x) &= x^2 + x \\
\end{align*}
$$

Is $p(x)$ a multiple of $q(x)$? IIf we are not looking into the vector aspect, then yes. However, when we are considering polynomial as vectors, then only scalar multiples are allowed, we cannot multiply by `x`, which is not a scalar value (number).

---

## 14. $\mathbb{R}^n$ as Vectors

Addition:

$$
\begin{bmatrix} 1 \\\ 2 \\\ 3 \end{bmatrix} +
\begin{bmatrix} -2 \\\ 7 \\\ -6 \end{bmatrix} =
\begin{bmatrix} -1 \\\ 9 \\\ -3 \end{bmatrix}
$$

Scalar multiplication:

$$
7 \times \begin{bmatrix} 4 \\\ 0 \\\ 12 \end{bmatrix} =
\begin{bmatrix} 28 \\\ 0 \\\ 84 \end{bmatrix}
$$

Stuck in a plane:
- In each of the vectors in LHS, the third entry is 3 times the first entry. By any linear combination (multiplication by a scalar or addition), we will always be stuck with vectors having the same property.
- By goemetric analogy, this is called a subspace of $\mathbb{R}^3$.

😅 There is no linkage between $\mathbb{R}^3$ and a plane, which is a term from geometry - other than both being vectors.

---

## 15. Linear Combinations

- We have two vectors $\vec{a}$ and $\vec{b}$.
- We can multiply by different numbers and add them: $\alpha\vec{a} + \beta\vec{b}$. $\alpha$ and $\beta$ are called coefficients of the linear combination.
- That stuck terminology can be conveniently said: **You are stuck in this plane under linear combinations**.

---

## 16. Examples of Linear Combinations

- For each of the types of vectors (geometric, polynomial, $\mathbb{R}^n$), we can take linear combinations.
- For polynomials, intriguing question:
  + $a(x) = x^2 + 1$, $b(x) = 3x^2 - 3x - 6$. For any $\alpha$ and $\beta$, does $c(x) = \alpha a(x) + \beta b(x)$ have the same property that $x = 2$ is a solution?
  + Is another property $f(2) = 1$ preserved under linear combinations?
- For matrices, similar questions can be asked:
  + Given matrices $a$ and $b$, , does $c = \alpha a + \beta b$ have the same property that $c_3 = 0$ or the property $c_3 = 1$?
  + $c_3 = -c_1$ -> will this be preserved?

$$
a = \begin{bmatrix} 1 \\\ 2 \\\ 0 \end{bmatrix}, \quad
b = \begin{bmatrix} -2 \\\ 4 \\\ 0 \end{bmatrix}
$$

Personal Thought: The 0 values always look to be honoured; so $c_3 = 0$ should preserved in the linear combination of $a$ and $b$. Similarly, the roots of the equation should be preserved. But some property like $f(2) = 1$ or $c_3 = 1$ should not be preserved under every linear combination. <br/>
Properties like $c_3 = -c_1$ should also be preserved too under linear combination - because the proportion is maintained.

---

## 17. The Zero Vector

The zero vector:
- Geometric vector: A vector with 0 length, denoted using a dot, with an arrow pointing anywhere : $\vec{\mathbf{0}}$.
- Polynomial: The zero polynomial. The 0 can be made bold: $\mathbf{0}$.
- $\mathbb{R}^n$: The vector with all entries as 0: In $\mathbb{R}^3$ it is the below matrix, also denoted as $\mathbf{0}$.

$$\begin{bmatrix} 0 \\\ 0 \\\ 0 \end{bmatrix}$$


---

## 18. Span the Man

- The set of all possible linear combinations of a set of vectors is called the span of the set of vectors.
- Example, $span(a, b) = \{ \alpha a + \beta b ; \alpha, \beta \in \mathbb{R} \}$.
- The span of a set of vectors is a subspace of the space containing the vectors.

__Question__: Is the span of the vectors $a$ and $b$ all of $\mathbb{R}^3$, or a proper subspace of $\mathbb{R}^3$? 

$$
a = \begin{bmatrix} 1 \\\ 0 \\\ 2 \end{bmatrix}, \quad
b = \begin{bmatrix} 7 \\\ 0 \\\ 15 \end{bmatrix}
$$

__Answer__: We can see middle entry is always 0. So, the span of these vectors cannot have any vector with non-zero middle entry. Hence, it is a proper subspace of $\mathbb{R}^3$.

---

## 19. Spanning Sets

A spanning set is a set of vectors whose span is the entire space.

$$
\begin{aligned}
a(x) &= 3x^2 + 5x - 8 \\
b(x) &= -x^2 + 3x - 2
\end{aligned}
$$

- Does $a(x)$ and $b(x)$ span all polynomials of degree 2?

  Nopes, because 1 is root of both $a(x)$ and $b(x)$, but some polynomials of degree 2 might not have 1 as root.
- Does $a(x)$ and $b(x)$ span all polynomials having root 1?
  We'll need to investigate this.

---

## 20. Linear Subspaces of the Plane

- We go through some examples of sets of vectors, and answer if those sets form the spanning set for the defined space.

---

## 21. An interesting exercise of Linear Combination

Consider, two vectors $\vec{a}$ and $\vec{b}$. We do linear combination, $\alpha\vec{a} + \beta\vec{b}$, with the constraint that $\alpha + \beta = 1$. What is the span of the set of vectors?

- By construction of locus from sample points, we observe that it is the line passing through the tip of the two vectors.
- Formally, using algebra: $\beta = 1 - \alpha$, so $\alpha\vec{a} + \beta\vec{b} = \alpha\vec{a} + (1 - \alpha)\vec{b} = \vec{b} + \alpha(\vec{a} - \vec{b})$.<br/>
  This tell us we always start at the tip of $\vec{b}$ and slide along the line connecting the tips of $\vec{a}$ and $\vec{b}$.

---

## 22. Equation of a straight line

![Equation of a straight line](./assets/04_straight_line_quation.svg)

---

## 23. Passionate Appeal - Treat all objects on their own terms.

- Don't intermix the world of geometric vectors with the world of polynomials or $\mathbb{R}^n$.

---

## 24. Summary of terms encountered so far

1. Vector
2. Linear Combination
3. Decomposition
4. Vector space and Linear space -> Closure

---

## 29. Decomposition

![decomposition](./assets/05_decompose_1.svg)

---

## 30. Decomposition wrt arbitrary vectors

![general decomposition](./assets/06_generic_decomposition.png)

- This looks like a skewed cartesian coordinate system. It's called __Affine grid__.

[chatgpt conversation](https://chatgpt.com/share/67d2a5c8-61cc-8009-979a-53f96dc1b353)

---

## 32. Decomposition with polynomials 2

$$
p_1(x) = 1, p_2(x) = x + 2, p_3(x) = x^2 + x - 3
$$

$$
x^2 + 7x + 5 = \alpha _1 p_1(x) + \beta _1 p_2(x) + \gamma _1 p_3(x) \\
x^2 - 7x = \alpha _2 p_1(x) + \beta _2 p_2(x) + \gamma _2 p_3(x)
$$

![Decompose Polynomial](./assets/07_decompose_polynomial.svg)

---

## 33. Decomposition with $\mathbb{R}^n$

Let:

$$
a = \begin{bmatrix} 1 \\\ 0 \\\ 0 \end{bmatrix}, \quad
b = \begin{bmatrix} 0 \\\ 1 \\\ 0 \end{bmatrix}, \quad
c = \begin{bmatrix} 0 \\\ 0 \\\ 1 \end{bmatrix}
$$

We have:

$$
\begin{bmatrix} 3 \\\ 5 \\\ 6 \end{bmatrix}
= 3a + 5b + 6c
$$

$$
\begin{bmatrix} 8 \\\ -11 \\\ 17 \end{bmatrix}
= 8 a + (-11) b + 17 c
$$

---

## 35. Decomposition with $\mathbb{R}^n$ 3

Let:

$$
a = \begin{bmatrix} 0 \\\ 0 \\\ 1 \end{bmatrix}, \quad
b = \begin{bmatrix} 0 \\\ 1 \\\ -1 \end{bmatrix}, \quad
c = \begin{bmatrix} 1 \\\ 2 \\\ 3 \end{bmatrix}
$$

We have:

$$
\begin{bmatrix} 3 \\\ 5 \\\ 6 \end{bmatrix}
= \rule{1em}{0.8pt} a + \rule{1em}{0.8pt} b + \rule{1em}{0.8pt} c
$$

$$
\begin{bmatrix} 8 \\\ -11 \\\ 17 \end{bmatrix}
= \rule{1em}{0.8pt} a + \rule{1em}{0.8pt} b + \rule{1em}{0.8pt} c
$$

---

## 36. Linear Systems are a Decomposition Problem

The system of equations:

$$
x + 2y + 3z + 3t = 12
$$

$$
4x + 5y + 6z + 3t = 45
$$

$$
7x + 8y + 9z + 3t = 78
$$

can be written in matrix form as:

$$
\begin{bmatrix} 12 \\\ 45 \\\ 78 \end{bmatrix} =
x \begin{bmatrix} 1 \\\ 4 \\\ 7 \end{bmatrix} +
y \begin{bmatrix} 2 \\\ 5 \\\ 8 \end{bmatrix} +
z \begin{bmatrix} 3 \\\ 6 \\\ 9 \end{bmatrix} +
t \begin{bmatrix} 3 \\\ 3 \\\ 3 \end{bmatrix}
$$

---

## 37. Impossible Decomposition

Wordings:

- The decomposition problem does not have a solution if the target vector does not lie in the subspace spanned by the decomposition vectors.
- The decomposition problem does not have a solution if the target vector is not within the span of the decomposition vectors.

---

## 38. Impossible Decomposition with Polynomials

The given equations are:

$$
X^2 + 1 = \rule{1em}{0.8pt} (X^2 + X) + \rule{1em}{0.8pt} (3X^2 - 11X) + \rule{1em}{0.8pt} (7X^2 - X)
$$

$$
X^2 + 1 = \rule{1em}{0.8pt} (X - 1) + \rule{1em}{0.8pt} (X^2 - 1) + \rule{1em}{0.8pt} (X^2 - 2X + 1)
$$

$$
X^2 + 1 = \rule{1em}{0.8pt} (X^2 - 4) + \rule{1em}{0.8pt} (3X - 6) + \rule{1em}{0.8pt} (X^2 - 4X + 4)
$$

1. RHS in the first equation does not have any polynomial with constant terms, so we can't get constant in LHS.
2. RHS in the second equation have all polynomials having coefficients adding up to 0 (i.e., 1 is a root). But the polynomial in LHS does not have 1 as a root.
3. RHS in the third equation have 2 as a root, but the polynomial in LHS does not have 2 as a root.

Thus, the polynomial in LHS is not in the subspace of the polynomials spanned by the decomposition polynomials / vectors.

---

## 39. Impossible Decomposition in $\mathbb{R}^n$

The given vector equations are:

$$
\begin{bmatrix} 3 \\\ 4 \\\ 7 \end{bmatrix} = \rule{1em}{0.8pt} \begin{bmatrix} 1 \\\ 0 \\\ 2 \end{bmatrix} + \rule{1em}{0.8pt} \begin{bmatrix} -7 \\\ 0 \\\ 5 \end{bmatrix} + \rule{1em}{0.8pt} \begin{bmatrix} 4 \\\ 0 \\\ 11 \end{bmatrix}
$$

$$
\begin{bmatrix} 3 \\\ 4 \\\ 7 \end{bmatrix} = \rule{1em}{0.8pt} \begin{bmatrix} 3 \\\ 15 \\\ 7 \end{bmatrix} + \rule{1em}{0.8pt} \begin{bmatrix} -4 \\\ -20 \\\ 3 \end{bmatrix} + \rule{1em}{0.8pt} \begin{bmatrix} 1 \\\ 5 \\\ 17 \end{bmatrix}
$$

$$
\begin{bmatrix} 3 \\\ 4 \\\ 7 \end{bmatrix} = \rule{1em}{0.8pt} \begin{bmatrix} 1 \\\ 2 \\\ 3 \end{bmatrix} + \rule{1em}{0.8pt} \begin{bmatrix} 4 \\\ 5 \\\ 6 \end{bmatrix} + \rule{1em}{0.8pt} \begin{bmatrix} 7 \\\ 8 \\\ 9 \end{bmatrix}
$$

1. Second entry cannot be made non-zero by a linear combination of the given vectors.
2. Second entry is 5 times first entry in all the decomposition vectors, but the target vector does not have this property.
3. Second entry is average of first and third entry in all the decomposition vectors, but the target vector does not have this property.

The properties which we identified remain preserved under addition and scalar multiplication - you can try out a few examples to verify this.

---

## 40. What is a Linear Property and Why it is Synonymous with Subspaces

__Linear property is synonymous with the noun subspace.__

A __subspace__ is a subset of a vector space that is a vector space in its own right. In other words, a subspace is a subset of a vector space that is closed under linear combination.

---

## 41. A property Irrelevant to Linear Combinations

Some properties are irrelevant to linear combinations. For example:
- divisible by 2, 3 or any number
- some value is constant (not equal to 0).

These properties are not linear properties because they are not preserved under linear combinations.

---

## 42. Linear Subspaces in $\mathbb{R}^n$

$$
\begin{bmatrix} 1 \\\ 0 \\\ 2 \end{bmatrix} \quad
\begin{bmatrix} -7 \\\ 0 \\\ 5 \end{bmatrix} \quad
\begin{bmatrix} 4 \\\ 0 \\\ 11 \end{bmatrix}
$$

$$
\begin{bmatrix} 3 \\\ 15 \\\ 7 \end{bmatrix} \quad
\begin{bmatrix} -4 \\\ -20 \\\ 3 \end{bmatrix} \quad
\begin{bmatrix} 1 \\\ 5 \\\ 17 \end{bmatrix}
$$

$$
\begin{bmatrix} 1 \\\ 2 \\\ 3  \end{bmatrix} \quad
\begin{bmatrix} 4 \\\ 5 \\\ 6 \end{bmatrix} \quad
\begin{bmatrix} 7 \\\ 8 \\\ 9 \end{bmatrix}
$$

If the vector entries are named as following:

$$
\begin{bmatrix} a \\\ b \\\ c \end{bmatrix}
$$

Then, the algebraic expression corresponding to the properties of the vectors are:
1. $b = 0$
2. $b = 5a$
3. $b = \frac{a + c}{2}$

Or, equivalently:
1. $b = 0$
2. $5a - b = 0$
3. $a - 2b + c = 0$

These algebraic expressions all follow the same template: __A linear combination of the coefficients of the entries of the vectors = 0.__

__Any subspace can be characterized by just a triplet of coefficients.__

1. $(0, 1, 0)$ - The subspace of vectors with second entry 0.
2. $(5, -1, 0)$ - The subspace of vectors with second entry 5 times the first entry.
3. $(1, -2, 1)$ - The subspace of vectors with second entry being the average of the first and third entry.

__This is exactly the requirement for linear properties. Any characteristic that cannot be written down in this format is not a linear property.__

$$
\begin{bmatrix} 1 \\\ 0 \\\ 3 \end{bmatrix} \quad
\begin{bmatrix} -7 \\\ 0 \\\ -21 \end{bmatrix} \quad
\begin{bmatrix} 4 \\\ 0 \\\ 12 \end{bmatrix}
$$

$$
\begin{cases}b=0\\ 3a-c=0\end{cases}
$$

---

## 43. Linear Subspaces of Polynomials

$$
\begin{aligned}
f(1) =0 \\
\int^{1}_{0} f(x) dx=0 \\
3f''(x) -f'(x) =0
\end{aligned}
$$

---

$$
\begin{aligned}
f_{c}(x) =f_{1}(x) +f_{2}(x) \\
f_{1}(1) =0;\quad f_{2}(1) =0 \\
f_{c}(1) =f_{1}(1) +f_{2}(1) =0
\end{aligned}
$$

---

$$
\begin{aligned}
\int_0^1 f_c(x) d x & =\int_0^1\left(f_1(x)+f_2(x)\right) d x \\
& =\int_0^1 f_1(x) d x+\int_0^1 f_2(x) d x \\
& =0
\end{aligned}
$$

---

$$
\begin{aligned} &
3 f_c^{\prime \prime}(x)-f_c^{\prime}(x) \\
= & 3(f_1(x)+f_2(x))^{\prime \prime}-(f_1(x)+f_2(x))^{\prime} \\
= & 3 f_1^{\prime \prime}(x)+3 f_2^{\prime \prime}(x)-f_1^{\prime}(x)+f_2^{\prime}(x) \\
= & (3 f_1^{\prime \prime}(x)-f_1^{\prime}(x))+(3 f_2^{\prime \prime}(x)-f_2^{\prime}(x)) \\
= & 0
\end{aligned}
$$

---

If we take $f(x)=a x^{2}+b x+c$, then, these are the conditions:

---

$$
\begin{aligned}
& f(1)=0 \\
\Rightarrow & a+b+c=0
\end{aligned}
$$

---

$$
\begin{aligned}
& \int_0^1 f(x) d x=0 \\
\Rightarrow & \int_0^1\left(a x^2+b x+c\right) d x=0 \\
\Rightarrow & {\left[\frac{a x^3}{3}+\frac{b x^2}{2}+c x\right]_0^1=0 } \\
\Rightarrow & \frac{a}{3}+\frac{b}{2}+c=0
\end{aligned}
$$

---

$$
\begin{aligned}
& 3 f^{\prime \prime}(x)-f^{\prime}(x)=0 \\
\Rightarrow & 3(2 a)-(2 a x+b)=0 \\
\Rightarrow & (6 a-b)-2 a x=0 \\
\end{aligned}
$$

In order for the polynomial to satisfy this property, $(6a-b)-2ax$ must vanish identically. Hence each coefficient must vanish:

$$
\begin{aligned}
\begin{cases}
6a - b = 0 \\
2a = 0
\end{cases}
\end{aligned}
$$

---

## 44. A good way to express linear subspaces in $\mathbb{R}^n$

- Use new variables for every independent value
- Use constants for every constant value (mostly 0)
- Use existing variables for any dependent value

Examples for the following statements:
1. $b = 0$
2. $5a - b = 0$
3. $a - 2b + c = 0$
4. $b = 0, c - 3a = 0$


$$
\begin{bmatrix} \alpha \\\ 0 \\\ \beta \end{bmatrix}, \quad
\begin{bmatrix} \alpha \\\ 5 \alpha \\\ \beta \end{bmatrix}, \quad
\begin{bmatrix} \alpha \\\ \frac{\alpha+\beta}{2} \\\ \beta \end{bmatrix}, \quad
\begin{bmatrix} \alpha \\\ 0 \\\ 3 \alpha \end{bmatrix}
$$

---

## 45. Unions and Intersections of Subspaces

- Union of two subspaces is not a subspace.
- Intersection of two subspaces is a subspace.

Why union is not (necessarily) a subspace?

Let's take two subspaces, $S_1$ and $S_2$. Let $v_1$ and $v_2$ be vectors in $ S_1 \setminus S_2$ and $S_2 \setminus S_1$ respectively. Then, $v_1 + v_2$ is not in either $S_1$ or $S_2$.

In some trivial case, when one subspace is a subset of another, then the union is a subspace.

Why intersection is a subspace?

Let $v_1$ and $v_2$ be vectors, both of them in $S1 \cap S2$. Then, $v_1 + v_2$ is in:
- $S1$, because $v_1$ and $v_2$ are in $S1$, and $S1$ is a subspace.
- $S2$, because $v_1$ and $v_2$ are in $S2$, and $S2$ is a subspace.

Hence, $v_1 + v_2$ is in $S1 \cap S2$.

Multiplication by a scalar is also preserved in the intersection in similar argument.

A linear dependency we'd discussed earlier can also be be thought as an intersection of two subspaces:

$$
\begin{aligned}
\begin{cases}
b = 0 \\
3a - c = 0
\end{cases}
\end{aligned}
$$

can be written as:

$$
\begin{bmatrix} \alpha \\\ 0 \\\ 3 \alpha \end{bmatrix} =
\begin{bmatrix} \alpha _1 \\\ 0 \\\ \beta _1 \end{bmatrix} \cap
\begin{bmatrix} \alpha _2 \\\ \beta _2 \\\ 3 \alpha _2 \end{bmatrix}
$$

---

## 46. Linear Independence

![Multiple Decomposition](./assets/08_multiple_decomposition.svg)

$$
\begin{aligned}
\vec{d} &= 2\vec{a} &+ 1\vec{b} &+ 0\vec{c}\\
     &= 1\vec{a} &+ 0\vec{b} &+ 1\vec{c}\\
     &= 0\vec{a} &+ (-1)\vec{b} &+ 2\vec{c}\\
     &= \ldots\\
\end{aligned}
$$

This is because there is a linear dependency between the vectors $\vec{a}$, $\vec{b}$, and $\vec{c}$: $\vec{c} = \vec{a} + \vec{b}$.

> [!NOTE]
> A set of vectors is __linearly dependent__ if __at least__ one of the vectors is a linear combination of the rest.

> [!NOTE]
> A set of vectors is __linearly independent__ if __none__ of the vectors is a linear combination of the rest.

---

## 47-48. Alternative definition of Linear Independence

$$
\begin{aligned}
\vec{d} &= 2\vec{a} + 1\vec{b} + 0\vec{c}\\
        &= (2+\alpha)\vec{a} + (1+\alpha)\vec{b} - \alpha \vec{c}\\
        &= 2\vec{a} + \vec{b} + \alpha(\vec{a}+\vec{b}-\vec{c})
\end{aligned}
$$

$(\vec{a}+\vec{b}-\vec{c})$ is not a useless 0, but a fancy $\vec{0}$.

> Fancy Zero 😝:
> 
> Adding any propotion of the fancy 0 does not change the value of the expression, but the appearance of the expression itself.

Hence, alternative definition:

> [!NOTE]
> A set of vectors is __linearly dependent__ if there __exists__ a __non-trivial__ linear combination that equals zero.

> [!NOTE]
> A trivial linear combination is one where all coefficients are zero. A non-trivial linear combination is one where at least one coefficient is non-zero.

---

## 49. The Equivalence of the Two Definitions of Linear Independence

Let the vectors be linearly dependenct by the first definition.

$$
\begin{aligned}
\vec{a} &= \beta \vec{b} + \gamma \vec {c} + \delta \vec{d} \\
\implies 0 &= \beta \vec{b} + \gamma \vec{c} + \delta \vec{d} - \vec{a}
\end{aligned}
$$

Even if all of $\beta$, $\gamma$, and $\delta$ are zero, since the coefficient of $\vec{a}$ is $-1$, hence the linear combination is non-trivial.

---

Let the vectors be linearly independent by the second definition. In the non-trivial linear combination, let $\gamma \neq 0$.

$$
\begin{aligned}
0 &= \alpha \vec{a} + \beta \vec{b} + \gamma \vec{c} + \delta \vec{d} \\
\implies \vec{c} &= -\frac{\alpha}{\gamma} \vec{a} - \frac{\beta}{\gamma} \vec{b} - \frac{\delta}{\gamma} \vec{d}
\end{aligned}
$$

Since $\gamma$ is non-zero, we can divide the whole equation by it, and hence the vectors are linearly dependent by the first definition.

---

## 50. Linear Independence Implies Uniqueness

We are going to prove that if the decomposition vectors are linearly independent, then the decomposition is unique.

We'll prove this by contradiction. Let's assume that the decomposition is not unique. Then, there are two different decompositions, where not all of the coefficients are equal to each other.

The condition of the coefficients formally:

$$
\neg\left(\alpha_1=\alpha_2 \quad \wedge\quad \beta_1=\beta_2 \quad \wedge\quad \gamma_1=\gamma_2\right).
$$
which is equivalent to writing:
$$
(\alpha_1-\alpha_2,\;\beta_1-\beta_2,\;\gamma_1-\gamma_2) \neq (0,0,0)
$$

The two decompositions can be written as:

$$
\begin{aligned}
\alpha_1 \vec{a} + \beta_1 \vec{b} + \gamma_1 \vec{c} &= \vec{d}, \\
\alpha_2 \vec{a} + \beta_2 \vec{b} + \gamma_2 \vec{c} &= \vec{d}, \\
\text{Subtracting the second equation from the first:} \quad & \quad \\
(\alpha_1 - \alpha_2) \vec{a} + (\beta_1 - \beta_2) \vec{b} + (\gamma_1 - \gamma_2) \vec{c} &= \vec{0}.
\end{aligned}
$$

This is a non-trivial linear combination of the vectors that equals zero, which contradicts the linear independence of the vectors.
