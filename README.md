# 🧩 Sudoku CSP Solver

This repository presents an efficient Sudoku solver implemented in Python, where the puzzle is modeled as a **Constraint Satisfaction Problem (CSP)**.

Instead of relying on brute-force techniques, the solver uses **constraint propagation** and **heuristic-based search** to significantly reduce the search space. As a result, Sudoku puzzles of varying difficulty levels are solved efficiently with minimal backtracking.

---

## 🚀 Features & Algorithms

### 🔹 Arc Consistency (AC-3)
Ensures consistency between variables by eliminating invalid values from domains based on constraints between neighboring cells (same row, column, or 3×3 grid).

### 🔹 Minimum Remaining Values (MRV)
A heuristic that selects the unassigned variable with the **fewest legal values**, helping to reduce branching and improve efficiency.

### 🔹 Forward Checking
Immediately updates and prunes the domains of neighboring variables after each assignment, preventing invalid paths early in the search.

### 🔹 Maintaining Arc Consistency (MAC)
Applies AC-3 dynamically during backtracking to maintain consistency throughout the solving process and detect conflicts early.

---

## ⚙️ Getting Started

### 📌 Prerequisites
- Python **3.x**
- No external libraries required

---

## ▶️ Running the Solver

Run the solver using the terminal:

```bash
python solver.py
