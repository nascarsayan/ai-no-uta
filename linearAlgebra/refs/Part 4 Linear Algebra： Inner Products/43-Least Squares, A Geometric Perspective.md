# Notes: Least Squares and Geometric Intuition

## 1. **Introduction**
- The goal is to derive the **least squares solution** to a linear system of equations.
  - This is particularly relevant when there are more equations than unknowns.
  - **Key Problem**: The column space of the matrix is not sufficient to represent all possible solutions (overdetermined systems).  
- Objective: Find the "best possible solution."

**Geometric Analogy**: 
1. Interpret solutions graphically in terms of lengths, angles, and geometric relationships.  
2. Translate geometric properties into algebraic expressions.

---

## 2. **Geometric Setup**
- **Given**:
    - A plane spanned by two non-orthogonal vectors $\mathbf{a}_1$ and $\mathbf{a}_2$.
    - A vector $\mathbf{b}$ that is **not in the plane**.
- **Objective**:
    - Find the vector in the plane (as a linear combination of $\mathbf{a}_1$ and $\mathbf{a}_2$) that is **closest to $\mathbf{b}$**.

### 2.1. Closest Vector
- The closest vector to $\mathbf{b}$ in the plane is determined **geometrically** by projecting $\mathbf{b}$ onto the plane:
    - This is the orthogonal projection of $\mathbf{b}$.  
    - The residual vector (the difference between $\mathbf{b}$ and its projection onto the plane) is **orthogonal to the plane**.

---

## 3. **Expressing Geometrically**
1. The vector we are looking for is:
   $$
   \mathbf{x} = \alpha_1 \mathbf{a}_1 + \alpha_2 \mathbf{a}_2
   $$
   where $\alpha_1$ and $\alpha_2$ are scalars.

2. **Orthogonality condition**:
   - The residual vector $\mathbf{b} - \mathbf{x}$ must be orthogonal to the plane. 
   - This means:
     - $\langle \mathbf{b} - \mathbf{x}, \mathbf{a}_1 \rangle = 0$
     - $\langle \mathbf{b} - \mathbf{x}, \mathbf{a}_2 \rangle = 0$

3. Substituting $\mathbf{x} = \alpha_1 \mathbf{a}_1 + \alpha_2 \mathbf{a}_2$, this becomes:
   $$
   \langle \mathbf{b} - (\alpha_1 \mathbf{a}_1 + \alpha_2 \mathbf{a}_2), \mathbf{a}_i \rangle = 0 \quad \text{for } i = 1, 2
   $$

4. Expanding:
   $$
   \langle \mathbf{b}, \mathbf{a}_i \rangle - \alpha_1 \langle \mathbf{a}_1, \mathbf{a}_i \rangle - \alpha_2 \langle \mathbf{a}_2, \mathbf{a}_i \rangle = 0
   $$

5. Writing this system in matrix form:
   $$
   \begin{bmatrix}
   \langle \mathbf{a}_1, \mathbf{a}_1 \rangle & \langle \mathbf{a}_2, \mathbf{a}_1 \rangle \\
   \langle \mathbf{a}_1, \mathbf{a}_2 \rangle & \langle \mathbf{a}_2, \mathbf{a}_2 \rangle
   \end{bmatrix}
   \begin{bmatrix}
   \alpha_1 \\
   \alpha_2
   \end{bmatrix}
   =
   \begin{bmatrix}
   \langle \mathbf{b}, \mathbf{a}_1 \rangle \\
   \langle \mathbf{b}, \mathbf{a}_2 \rangle
   \end{bmatrix}
   $$

---

## 4. **Connecting Geometry to Algebra**
- The matrix form described above is equivalent to:
  $$
  A^\top A \mathbf{x} = A^\top \mathbf{b}
  $$
  where:
  - $A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 \end{bmatrix}$
  - $\mathbf{x} = \begin{bmatrix} \alpha_1 \\ \alpha_2 \end{bmatrix}$

- **Key Insight**: The concept of orthogonality translates algebraically to the condition where the dot product is zero:
  - $\langle \mathbf{b} - \mathbf{x}, \mathbf{a}_i \rangle = 0$ aligns with $(\mathbf{b} - A \mathbf{x})^\top A = 0$, leading to $A^\top A \mathbf{x} = A^\top \mathbf{b}$.

---

## 5. **Matrix Interpretation**
1. **Matrix Components**:
   - Entries of $A^\top A$: $\langle \mathbf{a}_i, \mathbf{a}_j \rangle$ for all $i, j$.  
   - Entries of $A^\top \mathbf{b}$: $\langle \mathbf{b}, \mathbf{a}_i \rangle$ for all $i$.

2. The solution to $A^\top A \mathbf{x} = A^\top \mathbf{b}$ gives the coefficients $\alpha_1, \alpha_2$ that define the vector in the plane closest to $\mathbf{b}$.

---

## 6. **Key Takeaways**
1. The **least squares solution** is fundamentally rooted in the **geometric projection** of a vector onto a subspace.
2. The **orthogonality condition** bridges the geometric and algebraic representations:
    - The residual vector is orthogonal to the subspace spanned by $A$.
3. The matrix equation $A^\top A \mathbf{x} = A^\top \mathbf{b}$ emerges both from:
    - Intuitive geometric reasoning.
    - Rigorous linear algebra.

4. While the derivation provides **geometric intuition**, the formal proof relies on calculus and algebraic techniques.

---

## 7. **Further Notes**
- Projections and orthogonality are essential principles in understanding least squares.
- **Generalization**:
    - Applies to any dimension beyond three.
    - The concepts of dot product, span, and orthogonality extend seamlessly to higher-dimensional spaces.