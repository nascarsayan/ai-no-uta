# Transformation of Vectors in $\mathbb{R}^n$

## Overview
- **Previous discussions**: Transformation settings for geometric vectors and functions (e.g., polynomials).
- **Current topic**: Transformation of vectors in $\mathbb{R}^n$, dealing with an entirely different vector space.
    - Sets of $n$ numbers, particularly focusing on $\mathbb{R}^3$ (triplets of numbers).
    - Questions to explore:
        - Is the transformation **linear**?
        - **Eigenvalues** and **eigenvectors** of the transformation.

---

## Specifying a Transformation
1. **Entry-wise Specification**:
    - Transformation rules indicate how each entry of a vector is manipulated. 
    - Example: Transform $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \to \begin{bmatrix} 2 \\ 1 \\ 6 \end{bmatrix}$.
        - Switch the first two entries.
        - Multiply the last entry by 2.
    - Example Transformation:
        $$
        \begin{bmatrix} a \\ b \\ c \end{bmatrix} \to \begin{bmatrix} b \\ a \\ 2c \end{bmatrix}
        $$

---

## Linear Nature of the Transformation
### Test for Linearity:
1. **Scalar Multiplication**:
    - If scalar $k$ is applied, does $\begin{bmatrix} ka \\ kb \\ kc \end{bmatrix}$ transform as expected under the rule?  
    - Switching entries and scaling are commutative:
        - Example: Multiply first $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ by 2, then transform:
            $$
            \text{Result: }  \begin{bmatrix} 4 \\ 2 \\ 12 \end{bmatrix} \to \begin{bmatrix} 2 \\ 4 \\ 24 \end{bmatrix}
            $$  
        - Transform first, then scale:
            $$
            \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \to \begin{bmatrix} 2 \\ 1 \\ 6 \end{bmatrix}, \text{then scale to } \begin{bmatrix} 4 \\ 2 \\ 12 \end{bmatrix}
            $$  
        - Both cases are equivalent.

2. **Addition**:
    - Adding vectors before or after applying the transformation yields the same result:
        $$
        \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} + \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix} \to
        \begin{bmatrix} 7 \\ 7 \\ 9 \end{bmatrix}
        \quad \text{(transform after addition)} 
        $$  
        $$
        \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \to \begin{bmatrix} 2 \\ 1 \\ 6 \end{bmatrix}, 
        \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix} \to \begin{bmatrix} 5 \\ 4 \\ 12 \end{bmatrix}.
        \quad \text{(transform first, then add)}
        $$
        Result: $\begin{bmatrix} 7 \\ 7 \\ 18 \end{bmatrix}$ is consistent.

3. **Conclusion**: This transformation is **linear**. 

---

## Finding Eigenvalues and Eigenvectors

### Definition:
- A vector is an **eigenvector** of a linear transformation if multiplying the vector by the transformation results in a scalar multiple of the original vector. The scalar is called the **eigenvalue**.

### Examples:
#### Eigenvector 1: $\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$
- Transformation:
    $$
    \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \to 
    \begin{bmatrix} 0 \\ 0 \\ 2 \end{bmatrix}.
    $$
- The output is a multiple of the input ($2 \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$).
- **Eigenvalue**: $2$.

#### Eigenvector 2: $\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$
- Transformation:
    $$
    \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} \to 
    \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}.
    $$
- The output is unchanged ($1 \cdot \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$).
- **Eigenvalue**: $1$.

#### Eigenvector 3: $\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$
- Transformation:
    $$
    \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix} \to 
    \begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}.
    $$
- The output is $-1$ times the input ($-1 \cdot \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$).
- **Eigenvalue**: $-1$.

---

## Discussion and Generalization
- **Number of Eigenvalues/Eigenvectors**:
    - Related to the dimension of the space. For real numbers, $\mathbb{R}^n$, there can be at most $n$ eigenvalues/eigenvectors.
    - For complex numbers, there are **exactly $n$ eigenvalues** (future topic).

- **Linear Algebra's Power**:
    - Linear transformations, eigenvalues, and eigenvectors carry across diverse vector spaces (geometric vectors, functions, sets of numbers).
    - As long as objects can be treated as vectors, the same principles apply.

--- 

Continue exploring transformations and identifying patterns for more generalizations.