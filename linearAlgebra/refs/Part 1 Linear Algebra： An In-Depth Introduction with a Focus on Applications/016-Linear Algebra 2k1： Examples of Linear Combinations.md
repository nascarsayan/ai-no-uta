Here are the structured Markdown notes created from the provided transcript:

---

## 1. Linear Combinations: Geometric Vectors, Polynomials, and $\mathbb{R}^n$

### Key Points:
- Linear combinations are a fundamental concept applicable to various types of objects: geometric vectors, polynomials, and vectors in $\mathbb{R}^n$.
- There are only two operations involved:
  1. **Addition**
  2. **Multiplication by a scalar**

### Guiding Principles:
- Treat objects on their own terms:
  - For **geometric vectors**, consider properties like lengths and angles.
  - For **polynomials**, treat them as mathematical functions.
  - For **vectors in $\mathbb{R}^n$**, focus on their components.

---

## 2. Linear Combination of Geometric Vectors

### Example: Evaluate $2\mathbf{A} - 3\mathbf{B}$

#### Given:
- $\mathbf{A}$: Vector of length $\frac{3}{4}$.
- $\mathbf{B}$: Vector of length 1.
- Angle between $\mathbf{A}$ and $\mathbf{B}$: $\frac{\pi}{3}$.

#### Evaluation Process:
1. **Scale $\mathbf{A}$ and $\mathbf{B}$**:
   - $2\mathbf{A}$: A vector twice as long as $\mathbf{A}$, pointing in the same direction. 
     - Length: $2 \times \frac{3}{4} = \frac{3}{2}$.
   - $3\mathbf{B}$: A vector three times as long as $\mathbf{B}$, pointing in the same direction.
     - Length: $3$.

2. **Geometric Construction**:
   - Visualize $2\mathbf{A} - 3\mathbf{B}$ as connecting the tip of $-3\mathbf{B}$ with the tip of $2\mathbf{A}$.

3. **Properties of Resultant Vector**:
   - Orthogonal to $\mathbf{A}$.
   - Length: $\frac{3\sqrt{3}}{2}$ or $\frac{\sqrt{27}}{2}$.

4. **Purely Geometric Approach**:
   - Avoid reliance on Cartesian coordinates or components. Work with vector lengths, directions, and basic trigonometry.

---

## 3. Linear Combination of Polynomials

### Example: Evaluate $2P(x) - 3Q(x)$

#### Given:
- $P(x)$ and $Q(x)$ are two polynomials.
- Both polynomials have the property $P(2) = Q(2) = 0$ (i.e., $x = 2$ is a root for both).

#### Process:
1. **Compute Linear Combination**:
   - $2P(x)$: Multiply each coefficient of $P(x)$ by 2.
   - $-3Q(x)$: Multiply each coefficient of $Q(x)$ by -3.
   - Add the results to compute $2P(x) - 3Q(x)$.

2. **Preservation of Root Property**:
   - Resulting polynomial $2P(x) - 3Q(x)$ shares the same root property at $x = 2$.
   - **Question**: Is this particular property always preserved under linear combinations?

---

## 4. Linear Combination in $\mathbb{R}^n$

### Example: Evaluate $2\mathbf{A} - 3\mathbf{B}$ in $\mathbb{R}^3$

#### Given:
- $\mathbf{A}$ and $\mathbf{B}$ are vectors in $\mathbb{R}^3$.
- Both $\mathbf{A}$ and $\mathbf{B}$ satisfy $x_3 = 0$ (zero in the third component).

#### Process:
1. **Compute the Combination**:
   - $2\mathbf{A}$ and $-3\mathbf{B}$ are scaled versions of $\mathbf{A}$ and $\mathbf{B}$.
   - Sum them component-wise.

2. **Preservation of Properties**:
   - The property $x_3 = 0$ is preserved in the resulting vector.
   - **Question**: Is this preservation true for any property tied to individual components?

#### Follow-Up Question:
- Does the property $x_3 = 1$ (nonzero third component) also remain preserved under linear combinations?

---

## 5. Intriguing Questions

### General Property Preservation:
For all types of objects (vectors, polynomials, etc.), consider:
1. If two objects share a property (e.g., both evaluate to 0 at a specific point):
   - Does their linear combination also preserve that property?
   - Example for polynomials: If $P(2) = 0$ and $Q(2) = 0$, is $(2P(x) - 3Q(x))(2) = 0$?
   - Example for vectors: If $x_3 = 0$ for both $\mathbf{A}$ and $\mathbf{B}$, does $x_3 = 0$ for $2\mathbf{A} - 3\mathbf{B}$?

2. If a different property is given (e.g., evaluation to 1 rather than 0):
   - Is the property preserved under linear combinations?
   - Example for polynomials: $P(2) = 1$ and $Q(2) = 1$.

---

## 6. Additional Exercises and Exploration

1. Explore specific properties (orthogonality, scalar relationships, etc.) and their preservation under linear combinations.
2. Use the provided examples to analyze how structure differs between geometric vectors, polynomials, and vectors in $\mathbb{R}^n$.
3. Apply similar reasoning to your own mathematical models to identify when preservation of properties occurs.

---

