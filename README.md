<img width="98" height="28" alt="image" src="https://github.com/user-attachments/assets/6339b4d4-bb14-46af-811c-0b4313c3e32d" />

# Data Cleaning Pipeline

A simple Python project for cleaning CSV/tabular datasets using Pandas and NumPy.

This script helps automate common data cleaning tasks like:

- fixing column names
- handling missing values
- removing duplicates
- detecting outliers
- normalizing numeric data

It is beginner-friendly and easy to modify for any dataset.

---

# Features

✔ Load CSV files  
✔ Clean and standardize column names  
✔ Fix date and text formats  
✔ Handle missing values automatically  
✔ Remove duplicate rows  
✔ Detect and treat outliers using IQR  
✔ Normalize or standardize numeric columns  
✔ Save cleaned dataset as a new CSV file  

---

# Technologies Used

- Python
- Pandas
- NumPy

---

# Installation

Clone the project or download the script.

Then install required libraries:

```bash
pip install pandas numpy
```

---

# Project Structure

```bash
project/
│
├── clean_data.py
├── indian_bikes_dataset_1000.csv
├── cleaned_data.csv
└── README.md
```

---

# How to Run

## Default Run

```bash
python clean_data.py
```

This will read:

```bash
indian_bikes_dataset_1000.csv
```

and create:

```bash
cleaned_data.csv
```

---

## Run With Custom Files

```bash
python clean_data.py --input data.csv --output output.csv
```

---

# Normalization Options

## Min-Max Scaling (default)

```bash
python clean_data.py --norm minmax
```

Scales values between 0 and 1.

---

## Z-Score Standardization

```bash
python clean_data.py --norm zscore
```

Converts data to mean = 0 and standard deviation = 1.

---

# Cleaning Steps Performed

## 1. Load Dataset
Reads the CSV file using Pandas.

## 2. Clean Column Names
- converts to lowercase
- removes extra spaces
- replaces spaces with underscores

Example:

```python
Customer Name -> customer_name
```

---

## 3. Fix Data Types
- converts date columns to datetime
- formats names properly
- lowercases emails

---

## 4. Handle Missing Values
- numeric columns → filled with median
- categorical columns → filled with mode

---

## 5. Remove Duplicates
Drops duplicate rows from the dataset.

---

## 6. Handle Outliers
Uses the IQR method to detect outliers and clips extreme values.

---

## 7. Normalize Data
Applies:
- Min-Max Scaling OR
- Z-Score Standardization

---

## 8. Save Cleaned Data
Exports the final cleaned dataset to CSV.

---

# Example Output

```bash
========== DATA CLEANING PIPELINE ==========

Loading data...

Rows    : 1000
Columns : 8

Cleaning column names...

Handling missing values...

Removing duplicates...

Saving cleaned data...

Pipeline completed successfully!
```

---

