# Structured Notes

## 1. Eye vs. Ear: Understanding Signals
- Visual Recap:
  - The eye receives approximately **100 million individual signals**.
  - The ear receives a **single combined signal** which is the **sum of all available sounds**.

- Key Takeaway:
  - The term "sum" in this context is **literal and mathematical**.
  - **Linear algebra** revolves around adding things together in various proportions.

---

## 2. Linear Algebra and Addition
- Fundamental Idea: 
  - **Linear algebra** involves adding objects of the **same kind** in a way that results in another object of the **same kind**.
  - Example: Adding **forces** or **audio signals** produces a new force or signal that retains the same nature.

- Precise Mathematical Nature:
  - Addition in linear algebra follows a **precise mathematical sense**, unlike colloquial uses like "adding a player to a team."

---

## 3. Representing Audio Signals as Numbers
- **Audio signals** are represented by large **arrays of numbers**:
  - Example: Each array contains approximately **1 million numbers**.
  - Visualization: Arrays are often plotted as **time series** for better understanding.

---

## 4. Demonstration: Adding Audio Signals

### Step 1: Listening to Individual Clips
- **First Clip**: A prelude by Bach.
- **Second Clip**: An excerpt from Martin Luther King's "I Have a Dream" speech.

### Step 2: Examining Raw Numbers
- Example: The first 10 numbers from each clip.
  - **Bach** Clip: `[x_1, x_2, ..., x_{10}]`
  - **MLK** Clip: `[y_1, y_2, ..., y_{10}]`

### Step 3: Addition
- Summing the numbers **component by component**:
  $$
  \text{Sum: } [x_1 + y_1, x_2 + y_2, ..., x_{10} + y_{10}]
  $$

---

## 5. Listening to the Summed Signals
- **Mathematical summation** of the two signals results in an audio clip that combines both sounds.
- Example:
  - Bach’s music and MLK’s speech played together as a single combined signal.

---

## 6. Changing Proportions with Scalar Multiplication
- To adjust the balance of the signals:
  - Multiply the Bach signal by **0.5** before adding it to the MLK signal:
    $$
    0.5 \cdot [x_1, x_2, ..., x_N] + [y_1, y_2, ..., y_N]
    $$
- Result:
  - The Bach signal becomes **half as loud**, while the MLK speech remains unchanged.

---

## 7. Observations About Audio Signals
- **Audio signals** are added together in a **literal mathematical sense**.
- These signals can also be **scaled** (multiplied by a constant) or combined in various proportions.

---

## 8. Definition of Vectors
- **Vectors** are defined as objects that:
  1. Can be **multiplied by numbers** (scalars).
  2. Can be **added together** in a precise mathematical sense.
- The result of these operations is another object of the **same kind**.

---

### Summary
- This demonstration highlights two fundamental operations in linear algebra: **addition** and **scalar multiplication**.
- The **literal mathematical handling** of signals allows them to be analyzed and manipulated using linear algebra principles.