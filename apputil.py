import pandas as pd

# ==================================================
# Exercise 1
# Fibonacci using recursion
# ==================================================

def fibonacci(n):
    """
    Return the nth Fibonacci number using recursion.

    Fibonacci sequence:
    0, 1, 1, 2, 3, 5, 8, ...
    Each number is the sum of the two before it.
    """

    # input validation
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # base cases (stop the recursion)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)


# ==================================================
# Exercise 2
# Convert integer to binary using recursion
# ==================================================

def to_binary(n):
    """
    Convert a non-negative integer to a binary string
    using recursion (without using bin()).
    """

    # input validation
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    # base cases
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    # recursive step:
    # divide by 2 and append the remainder
    return to_binary(n // 2) + str(n % 2)


# ==================================================
# Exercise 3
# Bellevue Almshouse dataset
# ==================================================

def task_1():
    """
    Return a list of column names sorted by the number
    of missing values (from least missing to most missing).
    """

    df = df_bellevue.copy()

    # clean gender column if it exists
    if 'gender' in df.columns:
        df['gender'] = (
            df['gender']
            .astype(str)
            .str.strip()
            .str.lower()
            .replace({'nan': pd.NA, 'unknown': pd.NA, '': pd.NA})
        )

    # count missing values per column
    missing_counts = df.isna().sum()

    # sort columns by missing values
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns


def task_2():
    """
    Return a DataFrame with:
    - year
    - total number of admissions per year
    """

    if 'year' not in df_bellevue.columns:
        raise KeyError("Column 'year' not found in dataset")

    admissions_per_year = (
        df_bellevue
        .groupby('year')
        .size()
        .reset_index(name='total_admissions')
        .sort_values('year')
    )

    return admissions_per_year


def task_3():
    """
    Return a Series showing the average age by gender.
    """

    if 'gender' not in df_bellevue.columns or 'age' not in df_bellevue.columns:
        raise KeyError("Columns 'gender' and/or 'age' not found")

    # remove rows with missing gender or age
    clean_data = df_bellevue.dropna(subset=['gender', 'age'])

    avg_age_by_gender = clean_data.groupby('gender')['age'].mean()

    return avg_age_by_gender


def task_4():
    """
    Return a list of the 5 most common professions.
    """

    if 'profession' not in df_bellevue.columns:
        raise KeyError("Column 'profession' not found")

    # clean profession column
    professions = (
        df_bellevue['profession']
        .dropna()
        .astype(str)
        .str.strip()
    )

    top_5_professions = professions.value_counts().head(5).index.tolist()

    return top_5_professions
