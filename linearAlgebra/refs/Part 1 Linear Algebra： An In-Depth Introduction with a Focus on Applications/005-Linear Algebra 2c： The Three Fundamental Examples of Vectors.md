# Notes on Vectors from Transcript

## 1. Introduction to Vectors in Linear Algebra

- **Definition**: Linear algebra studies objects (vectors) that can be added and multiplied by scalars to produce new objects of the same type.
- **Importance**: Vectors are fundamental in linear algebra, and they come in various forms.
- **Examples Covered**:
  1. Geometric vectors
  2. Polynomials
  3. $\mathbb{R}^n$ (n-tuples of numbers)

---

## 2. Geometric Vectors

- **Definition**: Directed segments, visualized in 1D, 2D, or 3D spaces.
- **Characteristics**:
  - Simple and intuitive.
  - Inspired by geometry concepts such as lines, planes, and angles.
- **Operations**:
  - Scalar multiplication: Length is scaled while direction remains unchanged.
  - Addition: Combining vectors intuitively.
- **Connection to Linear Algebra**:
  - Many terms in linear algebra derive from geometry (e.g., space, subspace, angles, dot product).
- **Geometric Inspiration**: Helps build intuition; concepts like distance and direction make linear algebra more accessible.

---

## 3. Polynomials as Vectors

- **Properties**:
  - Polynomials satisfy the properties of addition and scalar multiplication.
  - Examples include functions (e.g., polynomials, sines, cosines, exponential functions).
- **Operations**:
  - Addition: Adding two polynomials produces another polynomial.
  - Scalar multiplication: A polynomial multiplied by a scalar remains a polynomial.

### **Polynomials and Functions**
- **Functional Spaces**: Polynomials are considered a subspace of the broader "space of functions."
- **Linear Algebra Connection**:
  - Polynomials and functions serve as vector spaces.
  - Subspace terminology applies naturally.

---

## 4. $\mathbb{R}^n$: Sets of Numbers as Vectors

- **Definition**:
  - Tuple of numbers, e.g., $\mathbb{R}^3$ (contains triplets of real numbers).
  - Written with square brackets: $[x_1, x_2, \ldots, x_n]$.
- **Operations**:
  - **Addition**: Performed component-wise.
    
    $$
    \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix} +
    \begin{bmatrix} 6 \\ 1 \\ 8 \end{bmatrix} =
    \begin{bmatrix} 8 \\ 4 \\ 12 \end{bmatrix}
    $$

  - **Scalar Multiplication**: Each component is scaled accordingly.
    
    $$
    -\frac{1}{2} \times 
    \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} = 
    \begin{bmatrix} -0.5 \\ -1 \\ -1.5 \end{bmatrix}
    $$

- **$\mathbb{R}^n$ Space**:
  - Abstract yet intuitive after familiarity.
  - Algorithmically robust due to computational simplicity (e.g., Gaussian elimination, eigenvalue calculations).

---

## 5. Why $\mathbb{R}^n$ is Critical

1. **Algorithms**: Core linear algebra algorithms are formulated in $\mathbb{R}^n$.
2. **Computational Applications**: Numerical manipulations (ideal for computers).
3. **Abstract Representation**: $\mathbb{R}^n$ connects all vector spaces—it simplifies studying other spaces through equivalence.

---

## 6. Summary

- **Three Examples of Vectors**:
  - Geometric vectors: Rooted in drawings and geometry.
  - Polynomials/Functions: Abstract mathematical objects.
  - $\mathbb{R}^n$: Numbers classified by tuples.
- **Linear Algebra's Focus**:
  - Finds commonality across diverse vector spaces.
  - Celebrates variations in representation while unifying core operations.

---

## Next Steps: Dive Deeper into Each Vector Type

- Subsequent content will explore geometric vectors, polynomials, and $\mathbb{R}^n$ in greater detail.