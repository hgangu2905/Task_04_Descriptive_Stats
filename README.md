# Task_04_Descriptive_Stats

This project focuses on descriptive statistics using three different approaches in Python:

1. Pure Python (no third-party libraries)
2. Pandas
3. Polars

The dataset used represents real-world accident data from the **US Accidents (2016–2023)** dataset available on [Kaggle](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents).

> ⚠️ **Note**: The dataset file is not included in this repository. Please download it manually from Kaggle and place it in the `data/` directory.

---

## 📁 Repository Structure

```
.
├── .gitignore
├── pure_python_stats.py
├── pandas_stats.py
├── polars_stats.py
├── README.md
└── data/
    └── US_Accidents_March23.csv  # ← Not committed
```

---

## 📌 How to Run

1. Clone the repository
2. Download the dataset from [Kaggle - US Accidents](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
3. Place the file as: `data/US_Accidents_March23.csv`
4. Run any script via Python:


python pure_python_stats.py
python pandas_stats.py
python polars_stats.py

---

## 🧪 Summary of Work

Each script performs:

- Count, Mean, Min, Max, and Standard Deviation for numeric columns
- Unique value counts and most frequent values for categorical columns
- Grouped stats by:
  - `State`
  - `State + City`
- Runtime performance measurement (timing)

---

## ⚙️ Requirements

You will need:

- Python 3.8+
- The following libraries :
  - `pandas`
  - `polars`

---

## 🧠 Key Insights

> Example (you can customize this based on your findings):

- California has the highest number of accidents.
- Average visibility during accidents is around 9.5 miles.
- Most accidents are categorized as Severity Level 2.
- Performance: Polars ran significantly faster than Pandas on grouped stats.

---

## 🕒 Execution Times (Approximate)

| Script              | Runtime |
|---------------------|---------|
| Pure Python         | 6.5 sec |
| Pandas              | 4.2 sec |
| Polars              | 1.9 sec |

---

## ✅ Dataset Source

**US Accidents (March 2023)**  
🔗 https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

