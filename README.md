# IBAB-Task01-chiranjeevi-sai-deva
# IBAB Task 01 — Bubble Sort

## Task Description  
This task is part of the BIOHACK training program.  
The goal is to learn essential developer skills that will be used in hackathons, research labs, and real companies:

- Setting up a Linux environment (WSL/Ubuntu)
- Creating and using SSH keys for GitHub authentication
- Cloning repositories using SSH
- Writing clean code
- Committing and pushing code using Git

This task ensures we build a strong foundation before moving to advanced bioinformatics workflows, ML pipelines, or tool development.

---

## Bubble Sort — Logic Explanation  
Bubble Sort is a simple comparison-based sorting algorithm.

This version uses a *reverse inner loop* (from right to left), matching my pseudocode.

### **How it works:**
1. Start from the *end of the list*.
2. Compare each pair of adjacent elements:  
   - If "A[j] < A[j - 1]", swap them.
3. Repeat this for every element until "i + 1".
4. After each pass, the **smallest element moves toward the front**.
5. If no swaps happen in an entire pass, the list is already sorted → **stop early**.

### **Why this works:**
- Adjacent swaps slowly move elements toward their correct position.
- Early stopping avoids unnecessary passes and makes the algorithm faster when the list is almost sorted.

---

## ▶️ How to Run (Python)

 you should be inside the project folder.

Run:

```bash
python3 bubble_sort.py
