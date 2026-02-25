## 🧠 Learning Milestone 3: Running, Restarting, and Interrupting Jupyter Kernels  

This milestone focuses on understanding how **Jupyter kernels work** and how to control them effectively. Many notebook issues occur not because of coding errors, but due to hidden kernel state such as variables stored in memory, incorrect execution order, or long-running processes.

This milestone helps in building strong debugging, reproducibility, and workflow management skills during the Data Science sprint.

---

### ✅ 1️⃣ Understanding the Jupyter Kernel  

The Jupyter kernel is the engine that executes code inside a notebook and stores variables in memory.  
It remembers all executed cells until it is restarted.

Key learnings:
- What a kernel is and why it is important  
- How kernel state affects notebook outputs  
- Why results sometimes change unexpectedly  
- How hidden state can cause confusion  

This builds awareness of how notebooks function internally.

---

### ✅ 2️⃣ Running Cells and Execution Order  

We practiced running cells one by one in a structured manner.

Key observations:
- Outputs depend on execution order  
- Variables remain stored until the kernel restarts  
- Running cells randomly may cause errors  
- Hidden dependencies can lead to unpredictable results  

This improves clarity and control while working with notebooks.

---

### ✅ 3️⃣ Restarting the Kernel  

Restarting the kernel clears all memory and variables, creating a clean and fresh notebook environment.

We practiced:
- Restarting the kernel from Jupyter options  
- Observing that variables and outputs are removed  
- Rerunning cells from the beginning  
- Ensuring reproducibility and consistency  

This is essential before sharing or submitting notebooks.

---

### ✅ 4️⃣ Interrupting Execution  

Sometimes cells run for a long time or get stuck. Interrupting helps stop execution safely without restarting the entire notebook.

We learned:
- How to interrupt running cells  
- How to stop infinite loops and long computations  
- How to keep the notebook responsive  
- How to avoid freezing and wasting time  

This improves productivity during analysis.

---

### ✅ 5️⃣ Restart vs Interrupt: Decision Making  

We understood when to interrupt and when to restart.

| Action | Use Case |
|------|------|
| Interrupt | Stop a long or stuck execution |
| Restart | Reset the entire notebook state |

We also learned:
- Interrupting is useful for temporary issues  
- Restarting is safer when variables are corrupted or unclear  
- Choosing the correct action improves debugging efficiency  

---

### 🚀 Importance of This Milestone  

This milestone ensures:
- Consistent and predictable notebook behavior  
- Easier debugging and error identification  
- Reproducible results  
- Better collaboration and review  
- Clean and organized workflows  

Kernel control is essential for professional data science work.

---

### 📌 Key Takeaways  

After completing this milestone, we are able to:
- Identify kernel states such as running, idle, and stuck  
- Restart kernels intentionally  
- Interrupt long-running operations  
- Maintain a clean notebook environment  
- Ensure reliable and reproducible workflows   