import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Load the dataset
# ---------------------------------------------------------

ratings_df = pd.read_csv("data/teachingratings.csv")

print("Dataset shape:")
print(ratings_df.shape)

print("\nFirst five rows:")
print(ratings_df.head())


# ---------------------------------------------------------
# Question 1
# Calculate the percentage of visible minorities who are
# tenure professors.
# ---------------------------------------------------------

tenure_minority = (
    ratings_df[ratings_df["tenure"] == "yes"]
    .groupby("minority")
    .size()
    .reset_index(name="count")
)

tenure_minority["percentage"] = (
    100 * tenure_minority["count"] / tenure_minority["count"].sum()
)

print("\nQuestion 1: Percentage of tenured professors by minority status")
print(tenure_minority)


# To understand whether tenure status differs by minority status,
# calculate the percentage of tenured professors within each
# minority group.

minority_tenure_status = (
    ratings_df.groupby(["minority", "tenure"])
    .size()
    .unstack(fill_value=0)
)

minority_tenure_status["tenure_percentage"] = (
    100
    * minority_tenure_status["yes"]
    / minority_tenure_status.sum(axis=1)
)

print("\nTenure status within each minority group:")
print(minority_tenure_status)


# ---------------------------------------------------------
# Question 2
# Does average age differ by tenure?
# Produce mean and standard deviation for both groups.
# ---------------------------------------------------------

age_by_tenure = ratings_df.groupby("tenure")["age"].agg(
    ["mean", "std"]
)

print("\nQuestion 2: Mean and standard deviation of age by tenure")
print(age_by_tenure)

# ---------------------------------------------------------
# Checking the age values before plotting
# ---------------------------------------------------------

print("\nAge values in the dataset:")
print(sorted(ratings_df["age"].dropna().unique()))

print("\nNumber of professors in each age:")
print(ratings_df["age"].value_counts().sort_index())

# ---------------------------------------------------------
# Question 3
# Which graph works better for the age variable?
# A histogram is appropriate because age is numerical.
# ---------------------------------------------------------

plt.figure(figsize=(9, 5))

age_bins = [28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76]

plt.hist(
    ratings_df["age"].dropna(),
    bins=age_bins,
    edgecolor="black"
)

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Professor Age")

plt.xticks(range(28, 77, 4))

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Question 4
# Difference between plt.bar() and plt.barh()
# Plot the graph for gender variable
# ---------------------------------------------------------

gender_counts = ratings_df["gender"].value_counts()

plt.figure(figsize=(7, 5))

plt.bar(
    gender_counts.index,
    gender_counts.values,
    edgecolor="black"
)

plt.xlabel("Gender")
plt.ylabel("Number of Professors")
plt.title("Distribution of Professors by Gender")

plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Question 5
# Median evaluation score for tenured professors
# ---------------------------------------------------------

median_eval_tenured = ratings_df[ratings_df["tenure"] == "yes"]["eval"].median()

print("\nQuestion 5: Median evaluation score for tenured professors")
print(median_eval_tenured)