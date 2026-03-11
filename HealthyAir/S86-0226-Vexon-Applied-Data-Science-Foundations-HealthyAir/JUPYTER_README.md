# Jupyter Launch & Video Checklist

This file contains the steps to complete the orientation milestone.

1) Activate the correct Conda environment (if you use Conda).

- Example (replace `myenv` with your environment name):

```
conda activate myenv
```

2) Launch Jupyter Notebook from the project folder. Two safe options:

- Change directory, then launch:

```powershell
cd "C:\Users\Ashritha\OneDrive\Desktop\Air_pollution\S86-0226-Vexon-Applied-Data-Science-Foundations-HealthyAir"
jupyter notebook
```

- Or launch with explicit notebook-dir:

```powershell
jupyter notebook --notebook-dir="C:\Users\Ashritha\OneDrive\Desktop\Air_pollution\S86-0226-Vexon-Applied-Data-Science-Foundations-HealthyAir"
```

3) What to check in the Jupyter Home interface:
- File listing area: where folders/files appear.
- Breadcrumbs: path shown at top to confirm current folder.
- "New" button: create a new notebook (choose Python 3 or correct kernel).
- File-type icons: notebook, folder, text files.

4) Verify the notebook runs:
- Open `Starter_Notebook.ipynb` from the Home interface.
- Confirm the kernel shown at the top-right (e.g., Python 3).
- Run the code cell; it should print `Hello, Jupyter!`.

5) Notebook file management basics:
- Rename: click checkbox next to notebook → Rename, or open notebook → File → Rename.
- Save: `File → Save and Checkpoint` or press `Ctrl+S`.
- Close: `File → Close and Halt` from inside notebook or close the browser tab and stop the kernel from the `Running` tab.
- Reopen: find the file in Home and click it.

6) Short screen-capture video (~2 minutes) checklist (what to record):
- Open terminal and show environment activation (if applicable).
- Launch `jupyter notebook` from the project folder.
- Show the Jupyter Home interface and breadcrumbs.
- Navigate into and out of a folder in the Home UI.
- Open `Starter_Notebook.ipynb`, run the single code cell, and show its output.
- Rename the notebook briefly, save, and reopen to show persistence.

7) Submission notes:
- Save the video and upload/submit per your assignment instructions.
- If you need a Pull Request, create one with the video link and mention this README and the starter notebook.

If you want, I can also open and run the notebook here (if you want me to run commands), or help craft the 2-minute narration script for the video.