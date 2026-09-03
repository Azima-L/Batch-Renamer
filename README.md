# Batch Renamer

A lightweight **Python GUI desktop application** built with **PySide6** designed to simulate and preview batch renaming workflows. It provides a clean, modern dark-themed interface to manipulate a list of names with custom prefixes, suffixes, text replacement (find/replace rules), and automated numbering systems.

This project serves as my practical exploration of GUI programming in Python and foundational tool development for a **Pipeline / Tools Technical Artist** path.

---

## Features & Architecture (v0.5.0)

* **PySide6 (Qt) GUI Framework**: Built a standalone GUI utilizing `QVBoxLayout` and nested `QHBoxLayout` configurations for structured layout alignment. Implements a stylized dark-theme Qt Style Sheet (QSS) to maintain visual consistency with industry-standard DCC environments.
* **Rule-Based Text Processing**: Allows users to instantly add custom prefixes and suffixes or use a find-and-replace tool to modify entire lists of names at once.
* **Smart Auto-Numbering Modes**: Offers flexible numbering choices (None, Sequential numbering, or Per-name tracking) to help artists and TDs to apply their intended naming rules across project.
* **Real-Time Visual Validation**: Features a side-by-side dual list view that shows the new names directly next to the original names, allowing quick visual checks before saving.
* **Production Log Exporting**: Generates organized `.txt` reports via a native file saver dialog. It maps out `Old Name → New Name` relationships, which is useful for asset tracking and pipeline auditing.
* **Error Prevention**: Built-in validation checks and console warning logs prevent the application from crashing if users accidentally try to export data before creating a preview.

---

## Prerequisites

* Python 3.10+ installed on your machine.
* pip install PySide6

---

## System Architecture

```text
├── batch_renamer.py        # Primary PySide6 application containing everything (UI and validation logic)
├── README.md               # Project documentation and developer overview
├── LICENSE                 # MIT Licensing details
└── .gitignore              # Python .gitignore details
```

---

## How to Use

Simply launch the application script via your command line interface:

```bash
python asset_validator.py
```
1. Open `batch_renamer.py` file.
2. Run the program and the application window titled **Batch Renamer** will pop up.
3. Fill in your asset names inside the text input field that says `Add name`.
4. Remove any names that you don't want just by selecting it directly from the `Input names` box and click `Remove`.
5. Customize the names with `Prefix`, `Suffix`, `Find`, and `Replace`.
6. Select any of the options under `Auto-numbering` if needed.
7. Check for real-time validation by clicking the `Preview` button at the bottom.
8. Export a .txt file for the logging report by clicking `Export` for asset tracking or any pipeline auditing.

---

## License
Distributed under the MIT License. See `LICENSE` for details.