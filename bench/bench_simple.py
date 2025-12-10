# bench/bench_simple.py
import time
import io
import csv
from parser import CSVParser
from writer import CSVWriter

def gen_text(n_rows=100_000):
    # a row with a quoted field that contains commas and quotes
    row = 'Alice,"long,field with comma and ""quote""",42\n'
    return row * n_rows

def time_custom_parser(text):
    s = io.StringIO(text)
    start = time.perf_counter()
    count = sum(1 for _ in CSVParser().read_rows(s))
    dt = time.perf_counter() - start
    return count, dt

def time_csv_module(text):
    s = io.StringIO(text)
    start = time.perf_counter()
    r = csv.reader(s)
    count = sum(1 for _ in r)
    dt = time.perf_counter() - start
    return count, dt

def run(n_rows=20000):
    print(f"Generating {n_rows} rows...")
    text = gen_text(n_rows)

    print("Warming up (small clean sample)...")
    # warm-up with a small number of complete rows to avoid slicing inside quotes
    small = gen_text(100)  # 100 complete rows for warm-up
    _ = time_custom_parser(small)
    _ = time_csv_module(small)

    print("Timing custom parser...")
    c1, dt1 = time_custom_parser(text)
    print("Timing csv.reader...")
    c2, dt2 = time_csv_module(text)

    mb = len(text) / (1024*1024)
    print()
    print(f"Rows: {n_rows}, Size: {mb:.2f} MB")
    print(f"custom parser: {c1} rows in {dt1:.3f}s -> {c1/dt1:.0f} rows/s, {mb/dt1:.2f} MB/s")
    print(f"csv.reader:     {c2} rows in {dt2:.3f}s -> {c2/dt2:.0f} rows/s, {mb/dt2:.2f} MB/s")

if __name__ == "__main__":
    # change the number here if 20k is too slow/fast for your machine
    run(20000)
