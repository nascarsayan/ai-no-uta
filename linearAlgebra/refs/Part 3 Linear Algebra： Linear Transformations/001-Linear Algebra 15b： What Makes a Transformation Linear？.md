## Linear Transformations and Examples of Linearity

### 1. **Introduction to Linearity**
- The concept of linear transformations in mathematics appears simple but can initially seem confusing.
- A linear transformation exhibits two hallmark properties that define its behavior:
  1. **Addition**: Whether transformations are applied before or after adding, the result remains the same.
  2. **Scalar Multiplication**: Whether transformations are applied before or after scaling, the result remains the same.

---

### 2. **Illustration of Linearity: Currency Conversion Example**
- **Setup**: Imagine you're in Paris and the exchange rate is 1 euro = $1.50. Breakfast prices:
  - Eggs: €4
  - Coffee: €2.
  
#### **Addition Property**:
Let’s calculate the total cost of breakfast using two approaches:
1. **Approach 1**: Add in euros first, then transform the total:
    $$
    4 + 2 = 6 \, \text{euros} \quad \implies \quad 6 \times 1.5 = 9 \, \text{dollars}.
    $$
2. **Approach 2**: Transform each item individually to dollars, then add:
    $$
    4 \times 1.5 = 6 \, \text{dollars}, \quad 2 \times 1.5 = 3 \, \text{dollars}.
    \quad \implies \quad 6 + 3 = 9 \, \text{dollars}.
    $$

- **Result**: Both approaches yield the same result of $9.

#### **Scalar Multiplication Property**:
Let’s calculate the cost of multiple coffees using two methods:
1. **Approach 1**: Multiply quantity in euros first, then transform:
    $$
    2 \times 3 = 6 \, \text{euros} \quad \implies \quad 6 \times 1.5 = 9 \, \text{dollars}.
    $$
2. **Approach 2**: Transform the cost of a single coffee into dollars first, then scale:
    $$
    2 \times 1.5 = 3 \, \text{dollars}, \quad 3 \times 3 = 9 \, \text{dollars}.
    $$

- **Result**: Both methods yield the same final cost of $9.

---

### 3. **Defining Linearity**
Linear transformations exhibit two key properties:
1. **Additivity**:
    $$
    T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}).
    $$
    - Whether you add vectors first and then transform, or transform individual vectors first and then add, the result is the same.

2. **Scalar Multiplication**:
    $$
    T(c\mathbf{u}) = cT(\mathbf{u}).
    $$
    - Scaling by a constant before transforming or transforming before scaling yields the same result.

These properties can be combined into one equation that uses **linear combinations**:
$$
T(c_1 \mathbf{u} + c_2 \mathbf{v}) = c_1 T(\mathbf{u}) + c_2 T(\mathbf{v}),
$$
where:
- $c_1, c_2$ are scalars.
- $\mathbf{u}, \mathbf{v}$ are vectors.

---

### 4. **Explanation Through Currency Example**
- **Additive Property in Words**: It doesn’t matter whether you add the cost of coffee and eggs first and then convert to dollars, or convert each item to dollars first and then add their dollar amounts. Both methods yield the same result.
- **Scalar Multiplication in Words**: It doesn’t matter whether you multiply the cost of coffee (€2 each) by the number of coffees (e.g., 3) and then convert to dollars, or convert the euro value (€2 per coffee) to dollars first and then multiply by the quantity.

---

### 5. **Looking Ahead: Spaces and Linear Transformations**
- Linear transformations will be studied across three major spaces:
  1. **Geometric Vectors**
  2. **Polynomials or Functions**
  3. **$\mathbb{R}^n$, the space of column vectors**

- Each of these spaces will be treated fairly, considering their properties and definitions independently ("treating all objects on their own terms"). Along the way, related concepts will be introduced.