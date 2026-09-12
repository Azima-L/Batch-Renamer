# Batch Data Transformer

A configurable tool for batch transformation of string-based data entries that supports prefix/suffix injection, find-replace operation, and auto-numbering (sequential or per-name) formatting and generation.

The tool is built using PySide6 GUI, with an understanding of UX design: easy navigation, straightforward rules, color-coded output, and custom dark-themed UI built using Qt Style Sheets (QSS).

#### Purpose of the tool:
Batch transformation is a common requirement when it comes to data preparation and ETL (Extract, Transform, Load) workflows. This tool lets you standardize identifiers, apply naming convention across different datasets, and previewing changes before saving and committing your configured, customized data names. Overall, it demonstrates configurable transformation logic, real-time preview, and audit reporting: core skills in pipeline and data quality engineering.

---

## Features & Architecture (v0.6.0)

* **PySide6 (Qt) GUI Framework**: Integrated an intuitive dual-column interface with real-time preview — shows original and transformed names side by side for validation before changes are committed. Implements a stylized Qt Style Sheets (QSS) to maintain friendly visual for the user to navigate the tool.
* **Rule-Based Text Processing**: Allows users to instantly add custom prefixes and suffixes or use a find-and-replace tool to modify entire lists of names at once.
* **Smart Auto-Numbering Modes**: Offers flexible numbering choices (None, Sequential numbering, or Per-name tracking) to apply consistent naming conventions across any dataset or project.
* **Production Log Exporting**: Generates organized `.txt` reports via a native file saver dialog. It maps out `Old Name → New Name` relationships, which is useful for asset tracking and pipeline auditing.
* **Error Prevention**: Built-in validation checks and console warning logs prevent the application from crashing if users accidentally try to export data before creating a preview.

---

## Prerequisites

* Python 3.10+ installed on your machine.
* pip install PySide6

---

## System Architecture

```text
├── batch_renamer.py        # Primary application containing the UI and transformation logic
├── core.py                 # Software-agnostic transformation logic
├── README.md               # Project documentation and developer overview
├── LICENSE                 # MIT Licensing details
└── .gitignore              # Python .gitignore details
```

---

## How to Use

Simply launch the application script via your command line interface:

```bash
python batch_renamer.py
```
1. Open `batch_renamer.py` file.
2. Run the program and the application window titled **Batch Data Transformer** will pop up.
3. Fill in your file names inside the text input field that says `Add name`.
4. Remove any names that you don't want just by selecting it directly from the `Input names` box and click `Remove`.
5. Customize the names with `Prefix`, `Suffix`, `Find`, and `Replace`.
6. Select any of the options under `Auto-numbering` if needed.
7. Check for real-time validation by clicking the `Preview` button at the bottom.
8. Export a .txt file for the logging report by clicking `Export` for asset tracking or any pipeline auditing.

---

## License
Distributed under the MIT License. See `LICENSE` for details.