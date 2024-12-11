# pandas

 Pandas is an open-source Python library widely
 used for
  data manipulation,
  analysis,
  exploration.
  
  It provides 2 data structures  to
  handle structured data efficiently.

   1. Series
   2. DataFrame

 Key Features of Pandas:
  Data Handling:

- Supports structured data in tabular
     form (rows and columns).
  Data Cleaning:
- Tools for handling missing data,
     duplicates, and filtering.
  Data Transformation:
- Merging, reshaping, and aggregating datasets.
  Integration:
- Works seamlessly with other libraries like
     NumPy and Matplotlib.
  I/O Operations:
- Read/write from various file formats
     like CSV, Excel, SQL, JSON, etc.

## Core Data-Structures ( data-types ) in Pandas

### 1. `Series`

- A one-dimensional labeled array capable
  of holding data of any type
  (similar to a column in a spreadsheet).

```python
import pandas as pd

# Creating a Series
marks = pd.Series([90,80,67],index=["phy","che", "geo"])
print(marks)

# Accessing elements
print(data["phy"]) # 90
print(data["che"]) # 80
print(data["geo"]) # 67
```

### 2.`DataFrame:`

- A two-dimensional labeled data structure
    (like a table with rows and columns).
- Each column in a DataFrame is a Series.

```python
# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print(df)

# Accessing a column
print(df["Age"])

# Accessing a row
print(df.iloc[1])  # By index
```

## Common Pandas Operations

1. Reading and Writing Data:

```python
# Reading a CSV file
df = pd.read_csv("data.csv")

# Writing to a CSV file
df.to_csv("output.csv", index=False)
```

2. Inspecting Data:

```python
print(df.head())       # First 5 rows
print(df.tail())       # Last 5 rows
print(df.info())       # Summary of DataFrame
print(df.describe())   # Statistical summary
```

3. Filtering Data:

```python
# Filter rows where Age > 30
filtered_df = df[df["Age"] > 30]
print(filtered_df)
```

4. Handling missing data
5. Data aggregation

## Benefits of Using Pandas

- Simplifies data preprocessing.

- Handles large datasets efficiently.
- Easily integrates with data visualization
   libraries like Matplotlib and Seaborn.
