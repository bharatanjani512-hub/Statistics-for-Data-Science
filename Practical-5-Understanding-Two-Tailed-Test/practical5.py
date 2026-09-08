import pandas as pd
import math
from pathlib import Path


# ============================================================
# PRACTICAL 5 - UNDERSTANDING TWO TAILED TEST
# Statistics for Data Science
# ============================================================


# ============================================================
# LOAD DATASET
# ============================================================

file_path = Path(__file__).parent / "data" / "teachingratings.csv"

ratings_df = pd.read_csv(file_path)

print("=" * 70)
print("PRACTICAL 5 - UNDERSTANDING TWO TAILED TEST")
print("=" * 70)

print("\nDataset loaded successfully.")
print("Dataset shape:", ratings_df.shape)


# ============================================================
# QUESTION 1
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1")
print("=" * 70)

total_observations = ratings_df["eval"].count()

greater_than_4_5 = (ratings_df["eval"] > 4.5).sum()

probability_q1 = greater_than_4_5 / total_observations

print("\nCalculation:")
print("P(Evaluation > 4.5) = Number of scores > 4.5 / Total scores")

print(
    f"P(Evaluation > 4.5) = {greater_than_4_5} / "
    f"{total_observations}"
)

print(f"P(Evaluation > 4.5) = {probability_q1:.4f}")

print(f"Probability = {probability_q1 * 100:.2f}%")


# ============================================================
# QUESTION 2
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2")
print("=" * 70)

between_3_5_and_4_2 = (
    (ratings_df["eval"] > 3.5) &
    (ratings_df["eval"] < 4.2)
).sum()

probability_q2 = between_3_5_and_4_2 / total_observations

print("\nCalculation:")
print(
    "P(3.5 < Evaluation < 4.2) = "
    "Number of scores between 3.5 and 4.2 / Total scores"
)

print(
    f"P(3.5 < Evaluation < 4.2) = "
    f"{between_3_5_and_4_2} / {total_observations}"
)

print(f"P(3.5 < Evaluation < 4.2) = {probability_q2:.4f}")

print(f"Probability = {probability_q2 * 100:.2f}%")


# ============================================================
# QUESTION 3
# TWO-TAILED Z-TEST
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 3")
print("=" * 70)


# ------------------------------------------------------------
# Given information
# ------------------------------------------------------------

historical_mean = 12
historical_std = 5.5
sample_size = 36
sample_mean = 10.7
alpha = 0.05

print("\nGiven Information:")
print("Historical mean (μ) = 12")
print("Historical standard deviation (σ) = 5.5")
print("Sample size (n) = 36")
print("Sample mean (x̄) = 10.7")
print("Significance level (α) = 0.05")


# ------------------------------------------------------------
# Hypotheses
# ------------------------------------------------------------

print("\nHypotheses:")

print("H₀: μ = 12")

print("H₁: μ ≠ 12")


# ------------------------------------------------------------
# Standard Error
# ------------------------------------------------------------

standard_error = historical_std / math.sqrt(sample_size)

print("\nStandard Error:")

print(
    f"SE = σ / √n = {historical_std} / √{sample_size}"
)

print(f"SE = {standard_error:.4f}")


# ------------------------------------------------------------
# Z-test statistic
# ------------------------------------------------------------

z_value = (sample_mean - historical_mean) / standard_error

print("\nZ-test Statistic:")

print(
    f"Z = (x̄ - μ) / SE"
)

print(
    f"Z = ({sample_mean} - {historical_mean}) / "
    f"{standard_error:.4f}"
)

print(f"Z = {z_value:.4f}")


# ------------------------------------------------------------
# Standard Normal CDF
# ------------------------------------------------------------

def normal_cdf(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


# ------------------------------------------------------------
# Two-tailed p-value
# ------------------------------------------------------------

p_value = 2 * (1 - normal_cdf(abs(z_value)))


# ------------------------------------------------------------
# Critical value
# ------------------------------------------------------------

critical_z = 1.96

print("\nCritical Values:")

print("For α = 0.05 in a two-tailed test:")

print("Critical Z-values = -1.96 and +1.96")


# ------------------------------------------------------------
# P-value
# ------------------------------------------------------------

print("\nP-value:")

print(f"Two-tailed p-value = {p_value:.4f}")


# ------------------------------------------------------------
# Decision
# ------------------------------------------------------------

print("\nDecision:")

if abs(z_value) > critical_z:

    print("Since |Z| > 1.96, reject H₀.")

    print(
        "There is sufficient evidence that the mean score "
        "is different from 12."
    )

else:

    print("Since |Z| < 1.96, fail to reject H₀.")

    print(
        "There is not sufficient evidence that the mean score "
        "is different from 12."
    )


# ============================================================
# END OF PRACTICAL
# ============================================================

print("\n" + "=" * 70)
print("END OF PRACTICAL 5")
print("=" * 70)