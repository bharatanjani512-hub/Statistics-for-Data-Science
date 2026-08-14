# ==========================================================
# Practical 2 - Understanding Foundation of Stats
#              using Rating Dataset
# MSc Data Science
# ==========================================================

# ----------------------------------------------------------
# Step 1 : Import Required Libraries
# ----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ----------------------------------------------------------
# Step 2 : Locate and Load the Dataset
# ----------------------------------------------------------

project_folder = Path(__file__).parent

data_path = project_folder / "data" / "teachingratings.csv"

df = pd.read_csv(data_path)


# ----------------------------------------------------------
# Step 3 : Create Output Folder
# ----------------------------------------------------------

output_folder = project_folder / "output"

output_folder.mkdir(exist_ok=True)


# ----------------------------------------------------------
# Step 4 : Display the First Five Rows
# ----------------------------------------------------------

print("=" * 70)
print("FIRST FIVE ROWS OF THE DATASET")
print("=" * 70)

print(df.head())


# ----------------------------------------------------------
# Step 5 : Display Dataset Shape
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("DATASET SHAPE")
print("=" * 70)

print("Number of rows    :", df.shape[0])
print("Number of columns :", df.shape[1])


# ----------------------------------------------------------
# Step 6 : Display Column Names
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("COLUMN NAMES")
print("=" * 70)

print(df.columns.tolist())


# ----------------------------------------------------------
# Step 7 : Display Data Types
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)

print(df.dtypes)


# ----------------------------------------------------------
# Step 8 : Display Dataset Information
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("DATASET INFORMATION")
print("=" * 70)

df.info()


# ==========================================================
# QUESTION 1 : TYPE OF DATASET
# ==========================================================

print("\n" + "=" * 70)
print("QUESTION 1 : TYPE OF DATASET")
print("=" * 70)

print("The Teachers Rating dataset is cross-sectional data.")

print("\nReason:")

print(
    "The dataset contains observations of professors/course evaluations "
    "and does not contain a time or date variable."
)

print(
    "Therefore, the dataset represents cross-sectional observations "
    "rather than observations tracked over time."
)


# ==========================================================
# QUESTION 2 : MEAN, MEDIAN, MINIMUM AND MAXIMUM
# ==========================================================

print("\n" + "=" * 70)
print("QUESTION 2 : STUDENTS VARIABLE STATISTICS")
print("=" * 70)

# Select the students column
students = df["students"]

# Calculate descriptive statistics
mean_students = students.mean()
median_students = students.median()
minimum_students = students.min()
maximum_students = students.max()

# Display the results
print("Mean number of students   :", mean_students)
print("Median number of students :", median_students)
print("Minimum number of students:", minimum_students)
print("Maximum number of students:", maximum_students)


# ==========================================================
# QUESTION 3 : DESCRIPTIVE STATISTICS
# ==========================================================

print("\n" + "=" * 70)
print("QUESTION 3 : DESCRIPTIVE STATISTICS")
print("=" * 70)

# Select numerical variables
numerical_columns = df.select_dtypes(include="number").columns

# Generate descriptive statistics
descriptive_statistics = df[numerical_columns].describe()

# Display the descriptive statistics table
print(descriptive_statistics)


# ==========================================================
# QUESTION 4 : HISTOGRAM OF BEAUTY VARIABLE
# ==========================================================

print("\n" + "=" * 70)
print("QUESTION 4 : HISTOGRAM OF BEAUTY VARIABLE")
print("=" * 70)

# Create the histogram
plt.figure(figsize=(8, 5))

plt.hist(
    df["beauty"],
    bins=15,
    edgecolor="black"
)

plt.title("Distribution of Beauty Scores")
plt.xlabel("Beauty Score")
plt.ylabel("Frequency")

plt.tight_layout()

# Save the histogram
histogram_path = output_folder / "beauty_histogram.png"

plt.savefig(histogram_path, dpi=300)

# Display the histogram
plt.show()

print("\nHistogram saved to:")
print(histogram_path)

print("\nDistribution summary:")

print(
    "The beauty scores are centered approximately around zero "
    "and range from about -1.45 to 1.97."
)

print(
    "The distribution is fairly broad and somewhat irregular, "
    "with observations spread across both negative and positive "
    "beauty scores."
)


# ==========================================================
# QUESTION 5 : BEAUTY SCORE BY GENDER
# ==========================================================

print("\n" + "=" * 70)
print("QUESTION 5 : BEAUTY SCORE BY GENDER")
print("=" * 70)

# Calculate mean and standard deviation of beauty
# separately for male and female instructors
beauty_by_gender = df.groupby("gender")["beauty"].agg(
    mean="mean",
    standard_deviation="std"
)

print("\nMean and Standard Deviation of Beauty Scores by Gender:")
print(beauty_by_gender)


# Extract individual values for interpretation
female_mean_beauty = beauty_by_gender.loc["female", "mean"]
female_std_beauty = beauty_by_gender.loc["female", "standard_deviation"]

male_mean_beauty = beauty_by_gender.loc["male", "mean"]
male_std_beauty = beauty_by_gender.loc["male", "standard_deviation"]

print("\nFemale instructors:")
print("Mean beauty score              :", female_mean_beauty)
print("Standard deviation             :", female_std_beauty)

print("\nMale instructors:")
print("Mean beauty score              :", male_mean_beauty)
print("Standard deviation             :", male_std_beauty)

print("\nComparison:")

if female_mean_beauty > male_mean_beauty:
    print("Female instructors have a higher average beauty score.")
elif male_mean_beauty > female_mean_beauty:
    print("Male instructors have a higher average beauty score.")
else:
    print("Male and female instructors have the same average beauty score.")


# ==========================================================
# QUESTION 6 : TENURE STATUS BY GENDER
# ==========================================================

print("\n" + "=" * 70)
print("QUESTION 6 : TENURE STATUS BY GENDER")
print("=" * 70)

# Create a count table of gender and tenure status
tenure_counts = pd.crosstab(
    df["gender"],
    df["tenure"]
)

print("\nTenure Counts by Gender:")
print(tenure_counts)


# Calculate the total number of instructors in each gender
gender_totals = df["gender"].value_counts()

# Calculate number of tenured instructors in each gender
tenured_counts = df[df["tenure"] == "yes"]["gender"].value_counts()

# Calculate percentage of tenured instructors within each gender
tenure_percentage = (
    tenured_counts / gender_totals * 100
)

print("\nPercentage of Tenured Instructors by Gender:")

print(
    tenure_percentage.rename("Percentage Tenured").to_frame()
)


# Extract percentages for interpretation
female_tenure_percentage = tenure_percentage["female"]
male_tenure_percentage = tenure_percentage["male"]

print("\nFemale instructors:")
print(
    "Percentage tenured:",
    female_tenure_percentage,
    "%"
)

print("\nMale instructors:")
print(
    "Percentage tenured:",
    male_tenure_percentage,
    "%"
)


print("\nComparison:")

if female_tenure_percentage > male_tenure_percentage:
    print(
        "The percentage of tenured instructors is higher among females."
    )
elif male_tenure_percentage > female_tenure_percentage:
    print(
        "The percentage of tenured instructors is higher among males."
    )
else:
    print(
        "The percentage of tenured instructors is the same for males and females."
    )


# ----------------------------------------------------------
# End of Analysis
# ----------------------------------------------------------

print("\n" + "=" * 70)
print("ALL QUESTIONS ANALYZED SUCCESSFULLY")
print("=" * 70)