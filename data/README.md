# Data Organization Structure

This project follows best practices for data management by separating data into three distinct stages:

## 1. Raw Data
- **Location:** data/raw/
- **Purpose:** Stores original, untouched data as received.
- **Guidelines:** Never modify raw data. Treat as read-only. Preserve integrity.

## 2. Processed Data
- **Location:** data/processed/
- **Purpose:** Contains cleaned, transformed, or derived datasets.
- **Guidelines:** Always recreate processed data from raw. Use clear filenames indicating processing stage.

## 3. Output Artifacts
- **Location:** data/output/
- **Purpose:** Stores final results such as plots, reports, tables, or models.
- **Guidelines:** Outputs are never mixed with input data. Use descriptive names for clarity.

---

**Rationale:**
- Prevents accidental overwrites and data contamination
- Supports reproducibility and auditability
- Maintains clear, trustworthy workflows

**Tip:**
- Always keep raw data immutable
- Document processing steps
- Separate outputs for easy review

For a walkthrough, see the video submission accompanying this milestone.