"""
What this script does:
1. Loads CSV data
2. Cleans column names
3. Fixes data types
4. Handles missing values
5. Removes duplicates
6. Handles outliers
7. Normalizes numeric columns
8. Saves cleaned file
"""

import pandas as pd
import numpy as np
import argparse


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
def load_data(file_path):
    print("\nLoading data...")

    df = pd.read_csv(file_path)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

    return df


# ---------------------------------------------------
# CLEAN COLUMN NAMES
# ---------------------------------------------------
def clean_columns(df):
    print("\nCleaning column names...")

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Updated columns:")
    print(list(df.columns))

    return df


# ---------------------------------------------------
# FIX DATA TYPES
# ---------------------------------------------------
def fix_types(df):
    print("\nFixing data types...")

    # Convert date columns
    for col in df.columns:
        if "date" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")
            print(f"Converted '{col}' to datetime")

    # Clean text columns
    text_cols = ["name", "email", "department"]

    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    if "name" in df.columns:
        df["name"] = df["name"].str.title()

    if "email" in df.columns:
        df["email"] = df["email"].str.lower()

    return df


# ---------------------------------------------------
# HANDLE MISSING VALUES
# ---------------------------------------------------
def handle_missing_values(df):
    print("\nHandling missing values...")

    numeric_cols = df.select_dtypes(include=np.number).columns
    object_cols = df.select_dtypes(include="object").columns

    # Fill numeric columns with median
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            median = df[col].median()
            df[col].fillna(median, inplace=True)

            print(f"{col} -> filled with median")

    # Fill categorical columns with mode
    for col in object_cols:
        if df[col].isnull().sum() > 0:
            mode = df[col].mode()[0]
            df[col].fillna(mode, inplace=True)

            print(f"{col} -> filled with mode")

    return df


# ---------------------------------------------------
# REMOVE DUPLICATES
# ---------------------------------------------------
def remove_duplicates(df):
    print("\nRemoving duplicates...")

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"Removed {before - after} duplicate rows")

    return df


# ---------------------------------------------------
# HANDLE OUTLIERS
# ---------------------------------------------------
def handle_outliers(df):
    print("\nHandling outliers...")

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:

        # Skip ID columns
        if "id" in col:
            continue

        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = df[(df[col] < lower) | (df[col] > upper)]

        if len(outliers) > 0:
            print(f"{col} -> {len(outliers)} outliers found")

            # Clip values
            df[col] = df[col].clip(lower, upper)

    return df


# ---------------------------------------------------
# NORMALIZE DATA
# ---------------------------------------------------
def normalize_data(df, method="minmax"):
    print("\nNormalizing numeric columns...")

    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:

        if "id" in col:
            continue

        # Min-Max Scaling
        if method == "minmax":

            min_val = df[col].min()
            max_val = df[col].max()

            if max_val != min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)

        # Z-Score Standardization
        elif method == "zscore":

            mean = df[col].mean()
            std = df[col].std()

            if std != 0:
                df[col] = (df[col] - mean) / std

    return df


# ---------------------------------------------------
# SAVE FILE
# ---------------------------------------------------
def save_data(df, output_path):
    print("\nSaving cleaned data...")

    df.to_csv(output_path, index=False)

    print(f"Cleaned file saved as: {output_path}")


# ---------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------
def run_pipeline(input_file, output_file, norm_method):

    print("\n========== DATA CLEANING PIPELINE ==========")

    df = load_data(input_file)

    df = clean_columns(df)

    df = fix_types(df)

    df = handle_missing_values(df)

    df = remove_duplicates(df)

    df = handle_outliers(df)

    df = normalize_data(df, method=norm_method)

    save_data(df, output_file)

    print("\nPipeline completed successfully!")


# ---------------------------------------------------
# RUN SCRIPT
# ---------------------------------------------------
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="popular_people.csv",
        help="Input CSV file"
    )

    parser.add_argument(
        "--output",
        default="cleaned_data.csv",
        help="Output CSV file"
    )

    parser.add_argument(
        "--norm",
        default="minmax",
        choices=["minmax", "zscore"],
        help="Normalization method"
    )

    args = parser.parse_args()

    run_pipeline(args.input, args.output, args.norm)