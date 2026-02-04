import pandas as pd

# --------------------------------------------------
# Exercise 1
# Fibonacci using recursion
# --------------------------------------------------

def fibonacci(n):
    # Fibonacci numbers:
    # 0, 1, 1, 2, 3, 5, 8, ...
    # Each number is the sum of the two before it

    if n < 0:
        raise ValueError("n must be non-negative")

    # base cases (bottom of recursion)
    if n == 0:
        return 0
    if n == 1:
        return 1

    # recursive call
    return fibonacci(n - 1) + fibonacci(n - 2)


# --------------------------------------------------
# Exercise 2
# Convert integer to binary using recursion
# --------------------------------------------------

def to_binary(n):
    # converts an integer to binary without using bin()

    if n < 0:
        raise ValueError("n must be non-negative")

    # base cases
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    # divide by 2 and keep remainder
    return to_binary(n // 2) + str(n % 2)


# --------------------------------------------------
# Exercise 3
# Bellevue Almshouse dataset
# --------------------------------------------------

def task_1():
    """
    Return column names sorted by how many missing values they have
    (least missing to most missing)
    """
    global df_bellevue

    # gender column has messy values, so clean it first
    if 'gender' in df_bellevue.columns:
        print("Cleaning gender column due to inconsistent values.")
        df_bellevue['gender'] = (
            df_bellevue['gender']
            .astype(str)
            .str.strip()
            .str.lower()
            .replace({'nan': pd.NA, 'unknown': pd.NA, '': pd.NA})
        )

    missing_counts = df_bellevue.isna().sum()

    # sort columns by missing values
    sorted_columns = missing_counts.sort_values().index.tolist()

    return sorted_columns


def task_2():
    """
    Return a dataframe with:
    - year
    - total number of admissions per year
    """
    global df_bellevue

    if 'year' not in df_bellevue.columns:
        raise KeyError("year column not found")

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
    Return a series showing average age by gender
    """
    global df_bellevue

    if 'gender' not in df_bellevue.columns or 'age' not in df_bellevue.columns:
        raise KeyError("gender or age column missing")

    print("Removing rows with missing gender or age.")

    clean_data = df_bellevue.dropna(subset=['gender', 'age'])

    avg_age = clean_data.groupby('gender')['age'].mean()

    return avg_age


def task_4():
    """
    Return a list of the 5 most common professions
    """
    global df_bellevue

    if 'profession' not in df_bellevue.columns:
        raise KeyError("profession column not found")

    print("Cleaning profession data (dropping blanks and NaNs).")

    professions = (
        df_bellevue['profession']
        .dropna()
        .astype(str)
        .str.strip()
    )

    top_5_professions = professions.value_counts().head(5).index.tolist()

    return top_5_professions
