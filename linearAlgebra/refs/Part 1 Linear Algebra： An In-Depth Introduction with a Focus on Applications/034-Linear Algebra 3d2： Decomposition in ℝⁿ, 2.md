## Bootstrapping in $\mathbb{R}^2$

### Introduction

Bootstrapping in $\mathbb{R}^2$ revolves around the careful selection of coefficients to represent a target vector as a linear combination of two given vectors. Key considerations include:
- **Order of deciding coefficients**: Start by determining the second coefficient to avoid interfering with the first entry calculations.
- **Matching entries sequentially**: First match the second entry, then use the result to match the first entry.

---

### Basic Example: Matching Entries in $\mathbb{R}^2$

#### Setup
Given two vectors:  
- $\mathbf{a} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$  
- $\mathbf{b} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$  

We want to bootstrap a target vector $\mathbf{t} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}$.

#### Step 1: Start with the **second coefficient**  
Match the second entry of $\mathbf{t}$ using $\mathbf{b}$.

$$
8 = x_2 \times 1 \implies x_2 = 8
$$

- Taking $8 \cdot \mathbf{b}$ contributes $16$ to the first entry:
  $$
  x_1 = 16
  $$

#### Step 2: Adjust the **first entry**  

Add **adjusting factor**