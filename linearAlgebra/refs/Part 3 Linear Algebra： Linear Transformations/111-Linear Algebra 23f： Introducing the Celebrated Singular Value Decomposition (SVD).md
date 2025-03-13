# Singular Value Decomposition (SVD)

## 1. Introduction to SVD

- The **Singular Value Decomposition (SVD)** is widely regarded as one of the most important decompositions in linear algebra. 
- Though all decompositions have their value, SVD is particularly impactful in applications such as Google searches, where it plays a key role in determining search results. 
- SVD's universality makes it more general and flexible compared to other decompositions, including the eigendecomposition.

---

## 2. Moving from Eigendecomposition to SVD

### Eigendecomposition of a Symmetric Matrix:
- Symmetric matrices always have full sets of eigenvalues.
- The eigenvalues of a symmetric matrix are **non-negative**.
- Eigenvectors are **orthogonal** and can be chosen to be **orthonormal**.
- If the eigenvectors form a matrix \(X\), \(X\) is orthogonal, meaning \(X^{-1} = X^\top\).

**Formula for Symmetric Matrix Decomposition**:

$$
S = X \Lambda X^\top
$$

Where:
- \( \Lambda \) is a diagonal matrix containing eigenvalues.
- \( X \) is the orthogonal matrix formed by eigenvectors.

**Geometric Interpretation**:
- Symmetric matrix decomposition represents **rotation**, followed by **scaling**, and then an **inverse rotation**.

---

### Transition to Singular Value Decomposition (SVD):

Using the eigendecomposition of the symmetric matrix \(S\), we can derive the SVD for a matrix \(A\):

**SVD Formula**:

$$
A = Q \Sigma X^\top
$$

Where:
- \( Q \) and \( X \) are **orthogonal matrices**.
- \( \Sigma \) is a diagonal matrix containing **singular values**.
  
---

## 3. Properties of SVD

1. **Universality**:
    - Unlike eigendecomposition, SVD exists for **any matrix** (square or rectangular).
    - It is not restricted to matrices with full sets of eigenvalues and avoids complex eigenvalues or defects.

2. **Orthogonality**:
    - Both \( Q \) and \( X \) in the SVD are orthogonal matrices.

3. **Geometric Interpretation**:
    - **SVD Interpretation**: Any matrix transformation can be described as:
        - A **rotation** (or reflection),
        - Followed by **scaling** along the coordinate axes,
        - Then another **rotation** into a different orientation.
    - For symmetric matrices: Rotate → Scale → Rotate Back.
    - For arbitrary matrices: Rotate → Scale → Rotate to a new configuration.

---

## 4. Singular Values and Matrix Components

- **Singular Values**:
    - Singular values are the **non-negative numbers** on the diagonal of the matrix \( \Sigma \).
    - Denoted by lowercase \( \sigma \).
    - Matrix \( \Sigma \) is typically represented as capital \( \Sigma \) in the SVD context.

- **Connection to Eigendecomposition**:
    - Singular values correspond to the square roots of eigenvalues of \( A^\top A \).

**Formula for Singular Values**:

$$
\sigma_i = \sqrt{\lambda_i}
$$

Where:
- \( \lambda_i \) are the eigenvalues of \( A^\top A \).

---

## 5. Geometry of SVD

### Transformation of Geometric Shapes:
- **Sphere → Ellipsoid**:
    - Under linear transformation:
        - A sphere becomes an **ellipsoid**.
        - In 3D:
            - First, rotate the sphere (it remains a sphere).
            - Scale it along the coordinate axes → becomes an ellipsoid.
            - Perform another rotation → the ellipsoid moves into a new configuration.

- **Circle → Ellipse**:
    - Similarly, a circle in 2D becomes an ellipse under transformation.

---

## 6. Algebra and Geometry in SVD

- Algebra provides a concise and straightforward way to derive geometric results for transformations.
- SVD demonstrates the power of combining algebra and geometry:
    - E.g., deducing that spheres transform into ellipsoids under any linear transformation.

---

## 7. Summary of SVD Components

The complete SVD is expressed as:

$$
A = Q \Sigma X^\top
$$

Where:
- \(Q, X \): Orthogonal matrices.
- \( \Sigma \): Diagonal matrix with singular values (\( \sigma_i \)).
  
**Singular Values**:
- Diagonal entries of \( \Sigma \), denoted by \( \sigma_i \).
- Computed from the eigenvalues of \( A^\top A \) as \( \sigma_i = \sqrt{\lambda_i} \).

In the next steps:
- We will prove properties of SVD, including equivalence of orthogonal matrices under specific decompositions.
- Later, we will revisit SVD in greater depth, focusing on its applications in the course.