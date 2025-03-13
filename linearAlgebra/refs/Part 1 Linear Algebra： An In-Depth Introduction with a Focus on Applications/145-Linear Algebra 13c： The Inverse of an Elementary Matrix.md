# Structured Notes on Elementary Matrices

## Elementary Matrices and Their Inverses

- Elementary matrices are easy to invert.
- Inversion can use either:
  - A robust algorithm that requires a few steps.
  - A simpler conceptual method: **treat them as actions** and reverse those actions.

### Conceptual Example: Reverse an Operation

- Consider the elementary matrix that **subtracts 7 times the second column from the first**:
  - To reverse, **add 7 times the second column to the first**.
  
  This boils down to simply encoding that action in a matrix.

### Using Column Perspective

1. Example:
    - An action: Start with the identity matrix, subtract 7 of column 2 from column 1.
    - Reverse action:
        - **Add 7 of column 2 to column 1.**
        - Encode the reverse action in the matrix to get its inverse.

---

## Multiplying Columns for Reversal

- Example described with an elementary matrix:
  - Action:
    1. **Multiply column 2 by 2**.
    2. **Add 4 times column 3 to column 2**.
  - Reverse Action:
    1. Subtract 4 times column 3 from column 2.
    2. Divide column 2 by 2.

### Two Approaches:
1. Use the identity matrix and apply reverse operations:
    $$
    \text{Subtract 4 of column 3 from column 2 and divide column 2 by 2.}
    $$

2. Alternative column perspective:
    - Reverse actions but remember **to apply them in reverse order**.

---

## Using Row Perspective

- Example with an elementary matrix:
  - Action from a row perspective:
    1. Multiply row 2 by 2.
    2. Add 2 times row 2 (now scaled as per step 1) to row 3.
  - Reverse Action:
    1. Subtract 2 times row 2 from row 3.
    2. Divide row 2 by 2.

---

### General Observations

- The perspective (column or row) does not change results **if the operations are correctly reversed**.
- Simpler conceptual approaches, such as viewing elementary matrices as actions, avoid fractions unless necessary. These actions often involve integers.

---

## Simplified Method for Finding an Inverse

- To find the inverse:
  1. Start from the given matrix.
  2. Determine the steps necessary to transform it into the identity matrix.
  3. Apply those steps in reverse to the identity matrix to get the inverse.

### Example:
- If the action involves:
  - Subtracting 4 of column 3 from column 2.
  - Dividing column 2 by 2.
- Reverse these steps:
  - Add 4 of column 3 to column 2.
  - Multiply column 2 by 2.

---

## Key Takeaways

- Elementary matrices provide a clear, intuitive way to conceptualize matrix inversion.
- Reversing matrix operations involves reversing structural actions:
  - For addition, perform subtraction and vice versa.
  - For division, perform multiplication and vice versa.
- Perspective (row vs. column) does not impact the final inverse matrix.

---

### Practice and Exercises

- Future exercises will focus on reinforcing this way of thinking with **over 30 elementary matrix examples**.