# ==========================================================
# Practical 1 - Revisiting Pandas and NumPy
# MSc Data Science
# ==========================================================

# ----------------------------------------------------------
# Step 1 : Import Required Libraries
# ----------------------------------------------------------

import pandas as pd
import numpy as np

# ----------------------------------------------------------
# Step 2 : Creating Raw Student Data
# ----------------------------------------------------------

raw_student_data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],

    "Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Neha",
        "Karan",
        "Sneha",
        "Rohan",
        "Anjali",
        "Vikas",
        "Pooja"
    ],

    "Age": [
        22, 23, 21, 22, 24,
        23, 22, 21, 24, 23
    ],

    "Gender": [
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female"
    ],

    "City": [
        "Delhi",
        "Mumbai",
        "Shimla",
        "Delhi",
        "Chandigarh",
        "Mumbai",
        "Delhi",
        "Shimla",
        "Chandigarh",
        "Delhi"
    ],

    "Department": [
        "Data Science",
        "Data Science",
        "Artificial Intelligence",
        "Artificial Intelligence",
        "Cyber Security",
        "Cyber Security",
        "Data Science",
        "Artificial Intelligence",
        "Cyber Security",
        "Data Science"
    ],

    "Marks": [
        88,
        91,
        75,
        85,
        79,
        90,
        83,
        87,
        81,
        95
    ]
}

# ----------------------------------------------------------
# Step 3 : Convert Raw Data into Pandas DataFrame
# ----------------------------------------------------------

student_df = pd.DataFrame(raw_student_data)

# ----------------------------------------------------------
# Step 4 : Display the DataFrame
# ----------------------------------------------------------

print("=" * 70)
print("STUDENT DATAFRAME")
print("=" * 70)

print(student_df)

# ----------------------------------------------------------
# Basic Information about the DataFrame
# ----------------------------------------------------------

print("\nNumber of Rows and Columns:")
print(student_df.shape)

print("\nColumn Names:")
print(student_df.columns)

print("\nData Types:")
print(student_df.dtypes)

print("=" * 70)

# ==========================================================
# Step 5 : Creating NumPy Arrays
# ==========================================================

matrix_A = np.array([
    [2, 4],
    [6, 8]
])

matrix_B = np.array([
    [1, 3],
    [5, 7]
])

print("\n" + "=" * 70)
print("NUMPY MATRICES")
print("=" * 70)

print("\nMatrix A:")
print(matrix_A)

print("\nMatrix B:")
print(matrix_B)

# ==========================================================
# Step 6 : Shape, Size and Dimension
# ==========================================================

print("\n" + "=" * 70)
print("PROPERTIES OF MATRIX A")
print("=" * 70)

print("Shape      :", matrix_A.shape)
print("Size       :", matrix_A.size)
print("Dimension  :", matrix_A.ndim)

print("\n" + "=" * 70)
print("PROPERTIES OF MATRIX B")
print("=" * 70)

print("Shape      :", matrix_B.shape)
print("Size       :", matrix_B.size)
print("Dimension  :", matrix_B.ndim)

# ==========================================================
# Step 7 : Matrix Operations
# ==========================================================

print("\n" + "=" * 70)
print("MATRIX OPERATIONS")
print("=" * 70)

# Addition
print("\n1. Addition (A + B)")
addition = matrix_A + matrix_B
print(addition)

# Subtraction
print("\n2. Subtraction (A - B)")
subtraction = matrix_A - matrix_B
print(subtraction)

# Element-wise Multiplication
print("\n3. Element-wise Multiplication (A * B)")
multiplication = matrix_A * matrix_B
print(multiplication)

# Matrix Product
print("\n4. Matrix Product (A × B)")
matrix_product = np.dot(matrix_A, matrix_B)
print(matrix_product)

# Transpose
print("\n5. Transpose of Matrix A")
transpose = matrix_A.T
print(transpose)

# Inverse
print("\n6. Inverse of Matrix A")
inverse = np.linalg.inv(matrix_A)
print(inverse)


# ==========================================================
# Step 8 : One-Hot Encoding
# ==========================================================

print("\n" + "=" * 70)
print("ONE-HOT ENCODING")
print("=" * 70)

# Selecting categorical columns
categorical_columns = ["Gender", "City", "Department"]

# Performing One-Hot Encoding
encoded_df = pd.get_dummies(
    student_df,
    columns=categorical_columns,
    dtype=int
)

print("\nOriginal DataFrame:")
print(student_df)

print("\nDataFrame After One-Hot Encoding:")
print(encoded_df)