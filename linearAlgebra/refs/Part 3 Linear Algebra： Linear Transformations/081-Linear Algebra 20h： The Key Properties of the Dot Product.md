# Essential Properties of the Dot Product

## 1. Introduction
- The video discusses fundamental properties of the dot product.
- While these properties may not seem crucial now, they will become more important in future discussions of linear algebra.
- The presentation begins with a derivation of the **Law of Cosines** as a way to explore the dot product.

---

## 2. Law of Cosines Derivation
### Definition:
In a triangle:
- Pythagorean theorem applies for right angles: $c^2 = a^2 + b^2$.
- When the angle $\gamma$ is not $90^\circ$, the **Law of Cosines** adds an extra term.

### Scenario:
Suppose:
- The triangle has sides represented by vectors $\mathbf{A}$ and $\mathbf{B}$.
- The third side is denoted as $\mathbf{C}$, forming an angle $\gamma$.

### Vector Relationships:
The side $\mathbf{C}$ satisfies:

$$
\mathbf{C} = \mathbf{A} - \mathbf{B}
$$

Take the dot product of both sides with themselves:

$$
\mathbf{C} \cdot \mathbf{C} = (\mathbf{A} - \mathbf{B}) \cdot (\mathbf{A} - \mathbf{B})
$$

Expand using distributivity:

$$
\mathbf{A} \cdot \mathbf{A} - 2 (\mathbf{A} \cdot \mathbf{B}) + \mathbf{B} \cdot \mathbf{B} = \mathbf{C} \cdot \mathbf{C}
$$

Using the dot product definition:

$$
||\mathbf{C}||^2 = ||\mathbf{A}||^2 + ||\mathbf{B}||^2 - 2 ||\mathbf{A}|| ||\mathbf{B}|| \cos \gamma
$$

Thus, the **Law of Cosines** is derived.

---

## 3. Observations and Flaws in the Argument
### Derivation flaw:
- The distributive property of the dot product was used:
  $$
  \mathbf{A} \cdot (\mathbf{B} + \mathbf{C}) = \mathbf{A} \cdot \mathbf{B} + \mathbf{A} \cdot \mathbf{C}
  $$
- This property needs to be formally established before using it.

---

## 4. Properties of the Dot Product
### **Commutativity**:
For any vectors $\mathbf{A}$ and $\mathbf{B}$:
$$
\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}
$$

Reason:
- The dot product is defined as $||\mathbf{A}|| ||\mathbf{B}|| \cos \gamma$, where $\cos(-\gamma) = \cos(\gamma)$, ensuring symmetry.

---

### **Associativity**:
Associativity **does not apply** to the dot product.

Reason:
- $\mathbf{A} \cdot (\mathbf{B} \cdot \mathbf{C})$ does not make sense, as $\mathbf{B} \cdot \mathbf{C}$ is a scalar, and scalars cannot be dotted with vectors.

---

### **Distributivity**:
Given three vectors $\mathbf{A}$, $\mathbf{B}$, and $\mathbf{C}$:
$$
\mathbf{A} \cdot (\mathbf{B} + \mathbf{C}) = \mathbf{A} \cdot \mathbf{B} + \mathbf{A} \cdot \mathbf{C}
$$

#### Proof:
1. Expand the geometric interpretation:
   - $\mathbf{A} \cdot (\mathbf{B} + \mathbf{C})$ computes the projection of $\mathbf{B} + \mathbf{C}$ onto $\mathbf{A}$.
   - This is equivalent to the sum of the projections of $\mathbf{B}$ and $\mathbf{C}$ onto $\mathbf{A}$.

2. Projection is a linear operation:
   - Adding projections of individual vectors $\mathbf{B}$ and $\mathbf{C}$ first, or projecting their sum, results in the same value.

---

## 5. Representation in Cartesian Coordinates
The dot product can be expressed in component spaces:
- Given vectors $\mathbf{A} = [a_1, a_2, ... , a_n]$ and $\mathbf{B} = [b_1, b_2, ... , b_n]$:
$$
\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} a_i b_i
$$

This representation highlights its computational simplicity in Cartesian systems.

---

## Conclusion
- The dot product possesses **commutativity**, **distributivity**, but not **associativity**.
- The geometric and algebraic interpretations provide a bridge between vector algebra and geometry.
