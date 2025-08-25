# Binary to Decimal Converter

This repository contains two Python programs for converting binary numbers to decimal values:

- **Binary_To_Decimal.py** – A simple command-line based binary to decimal converter.
- **Binary_To_Decimal_GUI.py** – A graphical user interface (GUI) application built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for an interactive conversion experience.

---

## Features

- Input validation (only accepts binary digits `0` and `1`, with optional `-` for negatives).
- Handles empty input and invalid characters gracefully.
- CLI version for quick conversions.
- GUI version with a modern, user-friendly design.

---

## Requirements

- Python 3.8 or later
- CustomTkinter (for GUI version)

Install dependencies:
```bash
pip install customtkinter
```

---

## Usage

### 1. Run the CLI Converter
```bash
python Binary_To_Decimal.py
```
Follow the prompts and enter a binary number to get its decimal equivalent.

### 2. Run the GUI Converter
```bash
python Binary_To_Decimal_GUI.py
```
A window will open where you can enter a binary number and click **Convert** to see the decimal value.

---

## Examples

- Binary input: `1011`  
  Decimal output: `11`

- Binary input: `-1101`  
  Decimal output: `-13`

---

## File Structure
```
Binary-To-Decimal-Converter/
│
├── Binary_To_Decimal.py        # Command-line based converter
├── Binary_To_Decimal_GUI.py    # GUI based converter
└── README.md                   # Documentation
```
