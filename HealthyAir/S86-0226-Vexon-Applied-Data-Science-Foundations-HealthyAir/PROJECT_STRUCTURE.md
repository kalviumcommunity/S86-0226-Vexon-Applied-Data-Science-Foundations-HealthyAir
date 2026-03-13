# Project Structure

This project uses a standard, minimal Data Science folder layout to keep files organized and reproducible.

Root layout:

- data/
  - raw/          # Original raw data (read-only)
  - processed/    # Cleaned or transformed data
- notebooks/      # Jupyter notebooks for exploration and reporting
- src/            # Reusable Python modules and helper functions
- scripts/        # Small runnable scripts (one-off or utility)
- outputs/
  - figures/      # Generated plots and images
  - tables/       # Exported tables and CSVs
- models/         # Trained model artifacts
- docs/           # Documentation and notes
- references/     # External references and resources
- tests/          # Unit or integration tests

Guidelines:

- Keep `data/raw` unchanged; place transformed files in `data/processed`.
- Notebooks should read from `data/processed` and write outputs to `outputs/`.
- Put reusable code into `src/` and import from notebooks using a relative import.
- Use `models/` to store versioned model files; do not check large binary model files into git.

Recording suggestion:
- Create a ~2-minute screen recording showing the root folder and each subfolder, and briefly explain the purpose of each.
