# pandas_stats.py

import pandas as pd
import time

# Path to your dataset
DATA_PATH = "data/US_Accidents_March23.csv"

# Columns to analyze
NUMERIC_COLUMNS = ["Severity", "Temperature(F)", "Humidity(%)", "Visibility(mi)"]
CATEGORICAL_COLUMNS = ["State", "City", "Weather_Condition"]

start_time = time.time()

# Load dataset with pandas
df = pd.read_csv(DATA_PATH)

# === Descriptive Stats for Numeric Columns ===
print("\n===== Descriptive Stats for Numeric Columns =====")
print(df[NUMERIC_COLUMNS].describe())

# === Descriptive Stats for Categorical Columns ===
print("\n===== Descriptive Stats for Categorical Columns =====")
for col in CATEGORICAL_COLUMNS:
    print(f"\nColumn: {col}")
    print(f"Unique Values: {df[col].nunique()}")
    print("Most Common:")
    print(df[col].value_counts().head(5))

# === Grouped Stats by State ===
print("\n===== Grouped Numeric Stats by State =====")
grouped_state = df.groupby("State")[NUMERIC_COLUMNS].describe().round(2)
print(grouped_state.head(10))

# === Grouped Stats by State + City ===
print("\n===== Grouped Numeric Stats by State + City =====")
grouped_state_city = df.groupby(["State", "City"])[NUMERIC_COLUMNS].describe().round(2)
print(grouped_state_city.head(10))

end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.2f} seconds")
