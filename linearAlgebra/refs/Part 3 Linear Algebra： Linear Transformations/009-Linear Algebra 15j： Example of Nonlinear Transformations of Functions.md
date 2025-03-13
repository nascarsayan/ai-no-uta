# Linear and Nonlinear Transformations

### 1. Transformation: Squaring a Function
- **Input:** A function $f(x)$  
- **Output:** $f(x)^2$  

#### Why it's nonlinear:
1. **Dead giveaway**: Squaring a function violates linearity.  
   - Linear transformations cannot involve nonlinear operations like squaring.  

2. **Multiplication test**:
   - Multiply the input function $f(x)$ by 5 → $5f(x)$.  
   - Apply the transformation:  
     $S(5f(x)) = (5f(x))^2 = 25f^2(x)$.  
   - If we transform first, then multiply by 5:  
     $5(S(f(x))) = 5(f(x)^2) = 5f^2(x)$.  
   - Comparing:  
     $25f^2(x) \neq 5f^2(x)$, so the transformation is **nonlinear**.

3. **Addition test**:
   - Adding $f(x)$ and $g(x)$ first, then transforming:  
     $S(f(x) + g(x)) = (f(x) + g(x))^2 = f^2(x) + 2f(x)g(x) + g^2(x)$.  
   - Transforming individually, then adding:  
     $S(f(x)) + S(g(x)) = f^2(x) + g^2(x)$.  
   - Comparing:  
     $f^2(x) + 2f(x)g(x) + g^2(x) \neq f^2(x) + g^2(x)$, so the transformation fails the addition test.  

#### General intuition:
- Any operation other than multiplication by a constant or addition typically results in nonlinearity. Examples of nonlinear transformations:
  - $f^2(x)$, $\log(f(x))$, $1/f(x)$, $f(x)^n$ (for $n \neq 1$).

---

### 2. Transformation: Plugging into Another Function
- **Input:** A function $f(x)$  
- **Output:** $f(x^2)$  

#### Why it's linear:
1. Plugging into another function like $x^2$, $\sin(x)$, $\log(x)$ does not disrupt linearity.  

2. **Addition test**:  
   - Adding two functions $f(x)$ and $g(x)$ first:   
     $S(f(x) + g(x)) = (f + g)(x^2) = f(x^2) + g(x^2)$.  
   - Transforming individually, then adding:  
     $S(f(x)) + S(g(x)) = f(x^2) + g(x^2)$.  
   - Results match, so the addition test passes.  

3. **Multiplication by constant test**:  
   - Multiply $f(x)$ by 5:  
     $S(5f(x)) = 5f(x^2)$.  
   - Transform, then multiply:  
     $5S(f(x)) = 5f(x^2)$.  
   - Results match, so it passes the multiplication test.  

#### Conclusion:
- Plugging into another function is a **linear transformation**.  
- Behavior is analogous to dilation (scaling) studied earlier.  

---

### 3. Transformation: Multiplying by $\sin(x)$
- **Input:** A function $f(x)$  
- **Output:** $\sin(x)f(x)$  

#### Why it's linear:
1. **Distribution test**:  
   - Adding two functions $f(x)$ and $g(x)$ first:  
     $S(f(x) + g(x)) = \sin(x)(f(x) + g(x)) = \sin(x)f(x) + \sin(x)g(x)$.  
   - Transforming individually, then adding:  
     $S(f(x)) + S(g(x)) = \sin(x)f(x) + \sin(x)g(x)$.  

2. **Multiplication by constant test**:  
   - Multiply $f(x)$ by 5:  
     $S(5f(x)) = \sin(x)(5f(x)) = 5\sin(x)f(x)$.  
   - Transform first, then multiply by 5:  
     $5S(f(x)) = 5\sin(x)f(x)$.  

3. Even though $\sin(x)$ is itself nonlinear, multiplying by it does not introduce nonlinearity to the transformation.

#### Conclusion:
- Multiplying $f(x)$ by $\sin(x)$ is a **linear transformation**.

---

### 4. Transformation: Addition of $x$ to the Function
- **Input:** A function $f(x)$  
- **Output:** $f(x) + x$  

#### Why it's nonlinear:
1. **Addition of constant effects**:
   - Adding $x$ is analogous to translation in geometry, where a constant vector is added to the input.  

2. **Addition test**:
   - Adding $f(x)$ and $g(x)$ first, then transforming:  
     $S(f(x) + g(x)) = (f(x) + g(x)) + x = f(x) + g(x) + x$.  
   - Transforming individually, then adding:  
     $S(f(x)) + S(g(x)) = (f(x) + x) + (g(x) + x) = f(x) + g(x) + 2x$.  
   - Comparing:  
     $f(x) + g(x) + x \neq f(x) + g(x) + 2x$, so it fails the addition test.  

3. **Intuition**:
   - This is not dilation or scaling but a constant shift, which inherently breaks linearity.  

#### Conclusion:
- Adding $x$ to a function is a **nonlinear transformation**.

---

### Summary of Transformations:
| Transformation                   | Linear/Nonlinear |
|----------------------------------|------------------|
| $f(x) \to f(x)^2$                | Nonlinear        |
| $f(x) \to f(x^2)$                | Linear           |
| $f(x) \to \sin(x)f(x)$           | Linear           |
| $f(x) \to f(x) + x$              | Nonlinear        |

This completes the discussion on linear and nonlinear transformations. Next, the focus shifts to vectors in $\mathbb{R}^n$.  