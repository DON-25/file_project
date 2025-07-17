# File Organizer – Automatic File Sorting Tool

A Python tool that automatically organizes files in a directory based on their type (images, documents, archives, etc.).

---

## Features

- Supports customizable classification rules via config file
- Automatically sorts and moves files into categorized folders
- Supports a wide range of file extensions
- One-command execution from the termina

---

## Installation

Make sure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```

## Project Structure
```
file_project/
├── config.json          # Configuration file for classification rules
├── config.py            # Loads the configuration
├── rules.py             # File type matching logic
├── organizer.py         # Core file organizing logic
├── main.py              # Program entry point
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation

```

## Usage
Run the main script:
```
python main.py
```
The program will automatically scan all files in the current directory and move them into folders based on the configuration.

## Example Output
Before running:
```
file_project/
├── test.jpg
├── report.docx
├── archive.zip

```
运行后：
```
file_project/
├── images/
│   └── test.jpg
├── documents/
│   └── report.docx
├── archives/
│   └── archive.zip

```

## Unit Testing
This project uses pytest as the unit testing framework. The following core functionalities are covered by tests:
- config.py：configuration loading and error handling
- rules.py：extension-based file categorization
- organizer.py：file movement, exception handling, and unmatched scenarios

Test directory structure:
```
tests/
├── test_config.py       # Tests configuration loading
├── test_rules.py        # Tests file matching logic
├── test_organizer.py    # Tests file organizing behavior

```

How to Run Tests
1.Make sure pytest is installed: 
```
pip install pytest
```
2.Run all tests from the project root directory:
```
pytest tests
```
3.Example output on success:
```
================= test session starts =================
collected 9 items

tests/test_config.py ....                         [33%]
tests/test_rules.py ....                          [66%]
tests/test_organizer.py ...                       [100%]

================== 9 passed in 0.05s ==================
```

