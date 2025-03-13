# Notes on Repeated Eigenvalues and Geometric Multiplicity

## 1. Introduction to Repeated Eigenvalues
- **Definition**: Situations where a single eigenvalue counts more than once in the eigenvalue spectrum.
- **Approaches**: There are two perspectives to understand repeated eigenvalues:
  1. **Geometric Approach** (focus of this video).
  2. **Algebraic Approach**.
  
---

## 2. Geometric View of Repeated Eigenvalues
### Example 1: Reflection in 3D
In three dimensions, we encounter two kinds of reflections:
1. **Reflection with Respect to a Plane**.
2. **Reflection with Respect to a Straight Line**.
   
Both scenarios illustrate eigenvalue behavior in transformations involving reflections.

### Reflection with Respect to a Plane
1. **What It Does**:
   - A reflection with respect to a plane mirrors vectors perpendicular to the plane and keeps vectors in the plane unchanged.
   - For a vector $v$, the reflection creates an "image" vector $v'$.

2. **Eigenvalues and Eigenvectors**:
   - Eigenvector corresponding to the eigenvalue $-1$: Any vector **perpendicular to the plane**. Reflection flips its direction:
     $$
     T(v) = -1 \cdot v
     $$
   - Eigenvectors corresponding to the eigenvalue $1$: Vectors that lie **within the plane**, as their direction remains unchanged:
     $$
     T(v) = 1 \cdot v
     $$
   - Summary:
     - Eigenvalue $-1$: One eigenvector (1D space).
     - Eigenvalue $1$: Any vector within the plane (2D space).
     - Total eigenvalues: $\{-1, 1\}$ with **geometric multiplicity** of:
       - $-1$: One-dimensional eigenspace.
       - $1$: Two-dimensional eigenspace.

### Reflection with Respect to a Straight Line
1. **What It Does**:
   - Vectors on the reflection line remain unchanged.
   - Vectors in the plane orthogonal to the line flip their direction under reflection.

2. **Eigenstructure**:
   - Eigenvector corresponding to eigenvalue $1$: The reflection line itself.
   - Eigenvectors corresponding to eigenvalue $-1$: Vectors in the plane orthogonal to the line.
   - Summary:
     - Eigenvalue $1$: One-dimensional eigenspace.
     - Eigenvalue $-1$: Two-dimensional eigenspace.
     - Total eigenvalues: $\{1, -1, -1\}$ with **geometric multiplicity** of:
       - $1$: One-dimensional.
       - $-1$: Two-dimensional.

---

## 3. Geometric Multiplicity
- **Definition**: Geometric multiplicity is the **dimension of the eigenspace** corresponding to a specific eigenvalue.
- **Key Observations**:
  1. Eigenvalue $-1$ appears **once** with a **geometric multiplicity of 1** if it corresponds to one vector.
  2. Eigenvalue $1$ is **repeated** with a **geometric multiplicity of 2**, indicating different independent vectors in its eigenspace.
  3. Geometric multiplicity = the number of **linearly independent eigenvectors** spanning the eigenspace.

---

## 4. Conclusion
### Example Summarization
1. **Reflection with Respect to a Plane**:
   - Eigenvalues: $-1$ (simple), $1$ (repeated).
   - Total eigenvalues: $\{-1, 1, 1\}$.
   
2. **Reflection with Respect to a Straight Line**:
   - Eigenvalues: $1$ (simple), $-1$ (repeated).
   - Total eigenvalues: $\{1, -1, -1\}$.
   
### Concepts Recap
- Geometric multiplicity helps clarify why certain eigenvalues **count more than once**.
- Linear independence of the eigenvectors is key to fully describing the eigenspaces.

Next, we will tackle **Algebraic Multiplicity** and its distinction from **Geometric Multiplicity**.