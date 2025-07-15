# polars_stats.py

import polars as pl
import time

# Path to your dataset
DATA_PATH = "data/US_Accidents_March23.csv"

# Columns to analyze
NUMERIC_COLUMNS = ["Severity", "Temperature(F)", "Humidity(%)", "Visibility(mi)"]
CATEGORICAL_COLUMNS = ["State", "City", "Weather_Condition"]

start_time = time.time()

# Load dataset with polars
df = pl.read_csv(DATA_PATH)

# === Descriptive Stats for Numeric Columns ===
print("\n===== Descriptive Stats for Numeric Columns =====")
print(df.select([
    pl.col(col).mean().alias(f"{col}_mean") for col in NUMERIC_COLUMNS
] + [
    pl.col(col).min().alias(f"{col}_min") for col in NUMERIC_COLUMNS
] + [
    pl.col(col).max().alias(f"{col}_max") for col in NUMERIC_COLUMNS
] + [
    pl.col(col).std().alias(f"{col}_std") for col in NUMERIC_COLUMNS
]))

# === Descriptive Stats for Categorical Columns ===
print("\n===== Descriptive Stats for Categorical Columns =====")
for col in CATEGORICAL_COLUMNS:
    print(f"\nColumn: {col}")
    unique_count = df.select(pl.col(col).n_unique()).item()
    print(f"Unique Values: {unique_count}")
    print("Most Common:")
    top_common = df.group_by(col).agg(pl.count().alias("count")).sort("count", descending=True).limit(5)
    print(top_common)

# === Grouped Stats by State ===
print("\n===== Grouped Numeric Stats by State =====")
grouped_state = df.group_by("State").agg([
    pl.col(col).mean().alias(f"{col}_mean") for col in NUMERIC_COLUMNS
] + [
    pl.col(col).min().alias(f"{col}_min") for col in NUMERIC_COLUMNS
] + [
    pl.col(col).max().alias(f"{col}_max") for col in NUMERIC_COLUMNS
])
print(grouped_state.head(10))

# === Grouped Stats by State + City ===
print("\n===== Grouped Numeric Stats by State + City =====")
grouped_state_city = df.group_by(["State", "City"]).agg([
    pl.col(col).mean().alias(f"{col}_mean") for col in NUMERIC_COLUMNS
] + [
    pl.col(col).min().alias(f"{col}_min") for col in NUMERIC_COLUMNS
] + [
    pl.col(col).max().alias(f"{col}_max") for col in NUMERIC_COLUMNS
])
print(grouped_state_city.head(10))

end_time = time.time()
print(f"\nExecution Time: {end_time - start_time:.2f} seconds")
