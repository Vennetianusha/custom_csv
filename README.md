# Custom CSV Parser & Writer  
**Author:** Anusha Pavani Venneti

This project implements a **custom CSV reader and writer** completely from scratch in Python.  
It handles real-world CSV challenges such as:  
- Quoted fields  
- Escaped quotes (`""`)  
- Fields containing commas  
- Embedded newlines inside quoted fields  
- Correct CSV writing with proper quoting rules

The goal is to understand **low-level CSV parsing**, state-machine design, file I/O, and to compare performance with Python’s built-in `csv` module.

---

## 📁 Project Structure

custom_csv/
│ parser.py # CSVParser implementation
│ writer.py # CSVWriter implementation
│ README.md # Documentation (this file)
│ requirements.txt # Dependencies
│ .gitignore
│
├── tests/ # Complete pytest suite
│ test_*.py
│
├── bench/
│ bench_simple.py # Benchmark script
│
└── examples/
small.csv

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Create and activate virtual environment (recommended)

#### Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
macOS / Linux
bash
Copy code
python -m venv .venv
source .venv/bin/activate
2️⃣ Install dependencies
bash
Copy code
python -m pip install -r requirements.txt
This installs:

nginx
Copy code
pytest
🧪 Running Tests
Run the full test suite:

bash
Copy code
python -m pytest -q
Expected output:

css
Copy code
14 passed in X.XXs
📘 Usage Examples
✔️ Reading CSV rows (streaming)
python
Copy code
from parser import CSVParser

parser = CSVParser()

with open("examples/small.csv", "r", encoding="utf-8") as f:
    for row in parser.read_rows(f):
        print(row)
✔️ Writing rows to a CSV file
python
Copy code
from writer import CSVWriter

writer = CSVWriter()

with open("output.csv", "w", encoding="utf-8") as f:
    writer.write_row(f, ["name", "bio"])
    writer.write_row(f, ["Anusha", 'Loves, "Python" and testing'])
Output example:

pgsql
Copy code
name,bio
Anusha,"Loves, ""Python"" and testing"
🚀 Benchmarking
Run benchmark:

bash
Copy code
python -m bench.bench_simple
My benchmark results (your machine):
pgsql
Copy code
Rows: 20000, Size: 0.90 MB
custom parser: 20000 rows in 0.258s -> 77,662 rows/s, 3.48 MB/s
csv.reader:     20000 rows in 0.014s -> 1,455,000 rows/s, 65.22 MB/s
📊 Benchmark Analysis
The built-in csv.reader is much faster because it is implemented in C.

The custom parser runs entirely in Python, so per-character looping is slower.

However, the custom implementation correctly handles:
✔ embedded newlines
✔ escaped quotes
✔ custom delimiter rules

This project focuses on correctness, understanding, and flexibility, not outperforming csv.reader.

🧠 What I Learned
How CSV quoting rules work internally

Designing a state machine parser

Handling tricky cases: "abc","hello\nworld"

Implementing a writer that escapes quotes properly

Benchmarking Python code and analyzing performance differences

📝 Requirements
nginx
Copy code
pytest
✔️ Submission Ready
This repository includes:

Custom CSV reader (parser.py)

Custom CSV writer (writer.py)

Full test suite (tests/)

Benchmark script (bench/bench_simple.py)

This README with usage + analysis

Requirements file

Everything is ready for review.

📄 License
You may include any license you prefer or leave it unlicensed for private submission.