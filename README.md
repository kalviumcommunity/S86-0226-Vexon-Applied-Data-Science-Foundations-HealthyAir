## 🧠 Learning Milestone 4: Working with Python Lists, Tuples, and Dictionaries

This milestone focuses on understanding Python's core collection data structures:
- **Lists**: Ordered and mutable collections
- **Tuples**: Ordered and immutable collections
- **Dictionaries**: Key-value pair collections

These structures allow you to store, organize, and manipulate multiple values efficiently, which is essential for handling real-world data.

This milestone ensures you can store and manage structured data confidently.

---

### ✅ 1️⃣ Working with Python Lists

Lists are **ordered** and **mutable** collections. In this section, we:
- Created lists with multiple values
- Accessed elements using indexes (0-based indexing)
- Modified elements using assignment
- Added elements with `append()`
- Removed elements with `remove()` and `pop()`
- Iterated over list items with for loops

Key insight: Lists are perfect for dynamic data that changes frequently.

---

### ✅ 2️⃣ Working with Python Tuples

Tuples are **ordered** and **immutable** collections. In this section, we:
- Created tuples with fixed values using parentheses
- Accessed elements using indexes (0-based indexing)
- Attempted to modify tuples to demonstrate immutability
- Observed that tuples raise `TypeError` when modified
- Iterated over tuple items with for loops

Key insight: Tuples protect data from accidental changes and are ideal for fixed configurations.

---

### ✅ 3️⃣ Working with Python Dictionaries

Dictionaries store data as **key-value pairs**. In this section, we:
- Created dictionaries with meaningful keys and values
- Accessed values using keys (not indexes)
- Modified existing values by key
- Added new key-value pairs
- Removed key-value pairs with `del`
- Iterated over dictionary items with `.items()`

Key insight: Dictionaries are perfect for modeling real-world entities with multiple attributes.

---

### ✅ 4️⃣ Choosing the Right Data Structure

We compared all three data structures across different scenarios:

| Aspect | List | Tuple | Dictionary |
|--------|------|-------|------------|
| **Ordered** | Yes | Yes | Yes (Python 3.7+) |
| **Mutable** | Yes | No | Yes |
| **Access Method** | Index | Index | Key |
| **Best For** | Dynamic data | Fixed data | Attributes & Relationships |
| **Example** | Shopping list | Color RGB | Student info |

**Decision Guide:**
- Choose **LIST** when you need ordered, changing data (shopping lists, grades, scores)
- Choose **TUPLE** when you need ordered, fixed data (coordinates, RGB colors, fixed constants)
- Choose **DICTIONARY** when you need key-based access (user profiles, configurations, attributes)

---

### 🚀 Importance of This Milestone

Mastering collections ensures:
- Your data is stored logically and appropriately
- Your code is easier to extend and maintain
- Errors related to data access are minimized
- You can model real-world data naturally
- You write clean, pythonic, professional code

Collections are foundational tools for all Python programming.

---

### 📁 Assignment Files

- **Collections_Milestone.ipynb**: Complete notebook with all examples and demonstrations
- **README.md**: This documentation file

After completing this milestone, we are able to:
- Identify kernel states such as running, idle, and stuck  
- Restart kernels intentionally  
- Interrupt long-running operations  
- Maintain a clean notebook environment  
- Ensure reliable and reproducible workflows   

---

## DataFrame Inspection & Shape/Type Milestone Notebooks

### How to Use
1. Open the following notebooks in VS Code or Jupyter:
   - `../HealthyAir/Inspecting_DataFrames_Inspection_Milestone.ipynb`
   - `../HealthyAir/Understanding_DataFrame_Shapes_and_Types.ipynb`
2. Run all cells in order. Read the markdown explanations and observe the code outputs.
3. For each notebook:
   - Review the code and explanations for inspecting DataFrame structure, types, and potential issues.
   - Use the code as a template for your own data analysis projects.

### Submission Guidelines
- Ensure all cells are executed and outputs are visible.
- Record a short screen-capture video (about 2 minutes) demonstrating:
  - Inspecting DataFrame shape and types
  - Explaining rows, columns, and why types matter
  - Using `.shape`, `.dtypes`, and `.info()`
- Submit the video link and the completed notebooks as instructed by your course.

### Tips
- Always check DataFrame shape and types before analysis.
- Never assume column types—inspect them!
- Use these notebooks as a reference for future data science work.
