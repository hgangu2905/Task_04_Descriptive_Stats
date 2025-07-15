# pure_python_stats.py

import csv
import statistics
from collections import defaultdict, Counter
import time

# Path to your dataset (change if needed)
DATA_PATH = "data/US_Accidents_March23.csv"


# Columns to analyze
NUMERIC_COLUMNS = ["Severity", "Temperature(F)", "Humidity(%)", "Visibility(mi)"]
CATEGORICAL_COLUMNS = ["State", "City", "Weather_Condition"]

# Initial EDA to understand the structure
print("===== Initial Dataset Exploration =====")
with open(DATA_PATH, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    print(f"Total Columns: {len(headers)}")
    print("First 10 Columns:")
    for col in headers[:10]:
        print(f"  - {col}")
    print("\nSample Record:")
    sample_row = next(reader)
    for h, v in zip(headers[:10], sample_row[:10]):
        print(f"  {h}: {v}")

# Storage for column-wise data
numeric_data = defaultdict(list)
categorical_data = defaultdict(list)

# Grouped data storage
grouped_by_state = defaultdict(lambda: defaultdict(list))
grouped_by_state_city = defaultdict(lambda: defaultdict(list))

start_time = time.time()

# Read CSV data
with open(DATA_PATH, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        state = row.get("State")
        city = row.get("City")

        for col in NUMERIC_COLUMNS:
            try:
                val = float(row[col])
                numeric_data[col].append(val)
                if state:
                    grouped_by_state[state][col].append(val)
                if state and city:
                    key = f"{state}|{city}"
                    grouped_by_state_city[key][col].append(val)
            except (ValueError, KeyError):
                continue

        for col in CATEGORICAL_COLUMNS:
            val = row.get(col, None)
            if val:
                categorical_data[col].append(val)

print("\n===== Descriptive Stats for Numeric Columns =====")
for col, values in numeric_data.items():
    print(f"\nColumn: {col}")
    print(f"Count: {len(values)}")
    print(f"Mean: {statistics.mean(values):.2f}")
    print(f"Min: {min(values):.2f}")
    print(f"Max: {max(values):.2f}")
    if len(values) > 1:
        print(f"Standard Deviation: {statistics.stdev(values):.2f}")

print("\n===== Descriptive Stats for Categorical Columns =====")
for col, values in categorical_data.items():
    print(f"\nColumn: {col}")
    count = Counter(values)
    print(f"Unique Values: {len(count)}")
    print("Most Common:")
    for item, freq in count.most_common(5):
        print(f"  {item}: {freq}")

# Grouping by State
print("\n===== Grouped Numeric Stats by State =====")
for state, cols in list(grouped_by_state.items())[:10]:  # Limit to top 10 states for brevity
    print(f"\nState: {state}")
    for col, values in cols.items():
        if values:
            print(f"  {col} -> Count: {len(values)}, Mean: {statistics.mean(values):.2f}, Min: {min(values):.2f}, Max: {max(values):.2f}")

# Grouping by State and City
print("\n===== Grouped Numeric Stats by State + City =====")
for key, cols in list(grouped_by_state_city.items())[:10]:  # Limit to top 10 state+city
    print(f"\nLocation: {key}")
    for col, values in cols.items():
        if values:
            print(f"  {col} -> Count: {len(values)}, Mean: {statistics.mean(values):.2f}, Min: {min(values):.2f}, Max: {max(values):.2f}")

end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.2f} seconds")
