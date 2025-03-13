# Notes: Linear Transformations and Matrices in $\mathbb{R}^n$

## 1. Linear Transformations in $\mathbb{R}^n$

- We are considering a series of examples in $\mathbb{R}^n$ to explore:
  1. How the resulting matrix changes based on the choice of basis.
  2. How the same linear transformation behaves under different bases.

## 2. Example Transformation

Apply the linear transformation $T$ to the vector $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$:

**Given Transformation:**
$$
\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \to \begin{bmatrix} 3 \\ -1 \\ 9 \end{bmatrix}
$$

- Record results for reference in later steps.

## 3. Representing Linear Transformations with Matrices

### Matrix Representation of the Transformation:
Every linear transformation in $\mathbb{R}^n$ can be expressed as matrix multiplication. For our transformation $T$, the matrix is:

$$
T = \begin{bmatrix} 
1 & 0 & 0 \\ 
-1 & 0 & 0 \\ 
0 & 0 & 3 
\end{bmatrix}
$$

- This represents the transformation directly in the real-world space (not component space).

---

## 4. Representing $T$ in a New Basis

Choose a new basis:
$$
B = \left\{ 
\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix},
\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix},
\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}
\right\}.
$$

- **Strategy:**
  - Decompose $T(B_1)$, $T(B_2)$, and $T(B_3)$ in terms of the same new basis.
  - Place the coefficients of these decompositions into the columns of the new matrix $\mathbf{T}_B$.

### Applying Transformation $T$ to Basis Vectors:

1. **Compute $T(B_1)$:**
   $$
   B_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}
   $$
   $$
   T\left( \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} \right) = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}.
   $$
   Decompose $\begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}$ in terms of $B$:
   $$
   2 \cdot B_1 - 3 \cdot B_2 + 5 \cdot B_3.
   $$
   Coefficients: $\begin{bmatrix} 2 \\ -3 \\ 5 \end{bmatrix}$.

2. **Compute $T(B_2)$:**
   $$
   B_2 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}
   $$
   $$
   T\left( \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} \right) = \begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}.
   $$
   Decompose $\begin{bmatrix} 1 \\ 1 \\ 3 \end{bmatrix}$ in terms of $B$:
   $$
   0 \cdot B_1 + 1 \cdot B_2 + 1 \cdot B_3.
   $$
   Coefficients: $\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$.

3. **Compute $T(B_3)$:**
   $$
   B_3 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}
   $$
   $$
   T\left( \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} \right) = \begin{bmatrix} 1 \\ -1 \\ 3 \end{bmatrix}.
   $$
   Decompose $\begin{bmatrix} 1 \\ -1 \\ 3 \end{bmatrix}$ in terms of $B$:
   $$
   0 \cdot B_1 + 1 \cdot B_2 - 1 \cdot B_3.
   $$
   Coefficients: $\begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}$.

### New Matrix Representation:
In the new basis $B$, the transformation $T$ is represented by:
$$
\mathbf{T}_B = \begin{bmatrix} 
2 & 0 & 0 \\ 
-3 & 1 & 1 \\ 
5 & 1 & -1 
\end{bmatrix}.
$$

---

## 5. Comparing Matrix Representations

1. **Original Matrix** (real-world space):
   $$
   T = \begin{bmatrix} 
   1 & 0 & 0 \\ 
   -1 & 0 & 0 \\ 
   0 & 0 & 3 
   \end{bmatrix}.
   $$

2. **New Basis Matrix** (component space):
   $$
   \mathbf{T}_B = \begin{bmatrix} 
   2 & 0 & 0 \\ 
   -3 & 1 & 1 \\ 
   5 & 1 & -1 
   \end{bmatrix}.
   $$
   - The matrix changes with the basis.
   - Different bases yield different matrix representations.

---

## 6. Verifying the Transformation

Task: Decompose $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ in the new basis and verify the result through $T$.

1. Decompose $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$:
   $$
   \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
   = 3 B_1 - 1 B_2 + 0 B_3.
   $$
   Coefficients: $\begin{bmatrix} 3 \\ -1 \\ 0 \end{bmatrix}$.

2. Apply $\mathbf{T}_B$:
   $$
   \mathbf{T}_B \cdot \begin{bmatrix} 3 \\ -1 \\ 0 \end{bmatrix} 
   = \begin{bmatrix} 9 \\ -9 \\ -1 \end{bmatrix}.
   $$

3. Transform back to real-world space:
   $$
   9 \cdot B_1 - 9 \cdot B_2 + (-1) \cdot B_3.
   $$
   Verify:
   $$
   \begin{bmatrix} 3 \\ -1 \\ 9 \end{bmatrix}.
   $$
   - The transformation result matches the original in the real-world space.

---

## 7. Observations & Conclusion

1. **Key Insights:**
   - Different bases lead to different matrix representations.
   - The new matrix $\mathbf{T}_B$ represents the same transformation in a different "coordinate system."

2. **Verification Strategy:**
   - Decompose, transform, and reconstruct to ensure correctness.

3. **Next Steps:**
   - Explore the standard basis in $\mathbb{R}^3$:
     $$
     \left\{ \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix},  
     \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix},
     \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \right\}.
     $$

---  