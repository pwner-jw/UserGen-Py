# UserGen-Py 🛡️

A fast, lightweight Python implementation of the classic `username-anarchy` tool. This script generates a wide variety of username permutations based on a user's first and last name—essential for Active Directory (AD) enumeration, Kerberoasting prep, and credential stuffing labs.

## 🚀 Features
* **Format Generation**: Automatically creates 16+ common enterprise username formats (e.g., `jdoe`, `john.doe`, `j.doe`).
* **Format Recognition**: Identify which format a target organization uses by providing a known username.
* **Bulk Processing**: Feed a list of names from a `.txt` file to generate a massive custom wordlist.
* **Smart Filtering**: Automatically handles case sensitivity and removes duplicate entries.

## 🛠️ Installation
No dependencies required. Just clone and run with Python 3.
```bash
git clone [https://github.com/pwner-jw/UserGen-Py.git](https://github.com/pwner-jw/UserGen-Py.git)
cd UserGen-Py
```

## 📖 Usage

### 1. Basic Generation
Generate all possible formats for a single name:
```bash
python3 usergen.py anna key
```

### 2. Use a Name List
Generate a wordlist from a file (one name per line, "First Last"):
```bash
python3 usergen.py --input-file names.txt > potential_usernames.txt
```

### 3. Select Specific Format
If you already know the target uses `first.last`, filter the output:
```bash
python3 usergen.py --input-file names.txt --select-format first.last
```

### 4. Recognize Format
If you found one valid username (e.g., `j.smith`) and want to know which format to use for the rest of the employees:
```bash
python3 usergen.py --recognise j.smith "john smith"
```

## 📋 Supported Formats
| Format Tag | Example (Raju Mohan) |
| :--- | :--- |
| `first.last` | raju.mohan |
| `first1last` | rmohan |
| `last1first` | mraju |
| `first4last4`| rajumoha |
| `first1last1`| rm |
| ...and many more | |

