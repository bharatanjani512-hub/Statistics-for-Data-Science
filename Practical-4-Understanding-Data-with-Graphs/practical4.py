import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PRACTICAL 4 - UNDERSTANDING DATA WITH GRAPHS
# Dataset: TeachingRatings
# ============================================================

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------

ratings_df = pd.read_csv("data/teachingratings.csv")

print("=" * 70)
print("PRACTICAL 4 - UNDERSTANDING DATA WITH GRAPHS")
print("=" * 70)

print("\nDataset Shape:")
print(ratings_df.shape)

print("\nFirst Five Rows:")
print(ratings_df.head())


# ============================================================
# QUESTION 1
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1")
print("=" * 70)

# Identify duplicate cases using professor ID
duplicate_cases = ratings_df[
    ratings_df.duplicated(subset=["prof"], keep=False)
].sort_values("prof")

print("\nDuplicate cases based on professor ID:")
print(duplicate_cases[["prof", "age", "gender", "eval", "tenure"]])

# Number of observations and unique professors
total_observations = len(ratings_df)
unique_professors = ratings_df["prof"].nunique()

print("\nTotal observations:", total_observations)
print("Number of unique professors:", unique_professors)

# Age statistics using all observations
all_mean_age = ratings_df["age"].mean()
all_std_age = ratings_df["age"].std()

print("\nUsing all observations:")
print("Mean age:", round(all_mean_age, 4))
print("Standard deviation of age:", round(all_std_age, 4))

# Keep only one observation for each professor
one_per_professor = ratings_df.drop_duplicates(
    subset=["prof"],
    keep="first"
)

filtered_mean_age = one_per_professor["age"].mean()
filtered_std_age = one_per_professor["age"].std()

print("\nAfter keeping one observation per professor:")
print("Number of observations:", len(one_per_professor))
print("Mean age:", round(filtered_mean_age, 4))
print("Standard deviation of age:", round(filtered_std_age, 4))


# ============================================================
# QUESTION 2
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2")
print("=" * 70)

# Calculate average evaluation for each division
division_evaluation = (
    ratings_df
    .groupby("division")["eval"]
    .mean()
)

print("\nAverage evaluation by course division:")
print(division_evaluation.round(4))

# Create bar chart
plt.figure(figsize=(8, 5))

division_evaluation.plot(
    kind="bar",
    edgecolor="black"
)

plt.xlabel("Course Division")
plt.ylabel("Average Teaching Evaluation")
plt.title("Average Teaching Evaluation by Course Division")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "output/q2_average_evaluation_by_division.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# QUESTION 3
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 3")
print("=" * 70)

print("\nPlotting age against teaching evaluation scores...")

plt.figure(figsize=(8, 5))

plt.scatter(
    ratings_df["age"],
    ratings_df["eval"],
    alpha=0.7
)

plt.xlabel("Age")
plt.ylabel("Teaching Evaluation Score")
plt.title("Age vs Teaching Evaluation Score")

plt.tight_layout()

plt.savefig(
    "output/q3_age_vs_evaluation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# QUESTION 4
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 4")
print("=" * 70)

print("\nPlotting age against evaluation by gender...")

plt.figure(figsize=(8, 5))

for gender in sorted(ratings_df["gender"].dropna().unique()):

    gender_data = ratings_df[
        ratings_df["gender"] == gender
    ]

    plt.scatter(
        gender_data["age"],
        gender_data["eval"],
        alpha=0.7,
        label=gender
    )

plt.xlabel("Age")
plt.ylabel("Teaching Evaluation Score")
plt.title("Age vs Teaching Evaluation by Gender")
plt.legend(title="Gender")

plt.tight_layout()

plt.savefig(
    "output/q4_age_vs_evaluation_by_gender.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# QUESTION 5
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 5")
print("=" * 70)

print("\nPlotting age against evaluation by gender and tenure...")

plt.figure(figsize=(9, 6))

for gender in sorted(ratings_df["gender"].dropna().unique()):

    for tenure in sorted(ratings_df["tenure"].dropna().unique()):

        group_data = ratings_df[
            (ratings_df["gender"] == gender) &
            (ratings_df["tenure"] == tenure)
        ]

        if len(group_data) > 0:

            plt.scatter(
                group_data["age"],
                group_data["eval"],
                alpha=0.7,
                label=f"{gender}, tenure={tenure}"
            )

plt.xlabel("Age")
plt.ylabel("Teaching Evaluation Score")
plt.title("Age vs Teaching Evaluation by Gender and Tenure")
plt.legend(title="Group")

plt.tight_layout()

plt.savefig(
    "output/q5_age_vs_evaluation_gender_tenure.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 70)
print("PRACTICAL 4 COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nAll graphs have been saved in the 'output' folder.")