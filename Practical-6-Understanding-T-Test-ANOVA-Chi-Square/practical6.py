import pandas as pd
import math
from pathlib import Path
from scipy import stats

# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------

file_path = Path(__file__).parent / "data" / "teachingratings.csv"
ratings_df = pd.read_csv(file_path)

print("=" * 70)
print("PRACTICAL 6 - UNDERSTANDING T-TEST, ANOVA, CHI-SQUARE")
print("=" * 70)

print("\nDataset loaded successfully.")
print("Dataset shape:", ratings_df.shape)

# =========================================================
# QUESTION 1 - T-TEST
# =========================================================

print("\n" + "=" * 70)
print("QUESTION 1 - T-TEST")
print("=" * 70)

print("\nQuestion:")
print("Does gender affect teaching evaluation rates?")

male_eval = ratings_df[ratings_df["gender"] == "male"]["eval"]
female_eval = ratings_df[ratings_df["gender"] == "female"]["eval"]

print("\nGroup Information:")
print("Male instructors:", len(male_eval))
print("Female instructors:", len(female_eval))

print("\nMean Evaluation Scores:")
print(f"Male mean = {male_eval.mean():.4f}")
print(f"Female mean = {female_eval.mean():.4f}")

print("\nHypotheses:")
print("H₀: There is no significant difference in evaluation scores")
print("    between male and female instructors.")
print("H₁: There is a significant difference in evaluation scores")
print("    between male and female instructors.")

t_statistic, p_value_ttest = stats.ttest_ind(
    male_eval,
    female_eval,
    equal_var=True
)

print("\nT-Test Result:")
print(f"t-statistic = {t_statistic:.4f}")
print(f"p-value = {p_value_ttest:.6f}")

alpha = 0.05

print("\nDecision:")
if p_value_ttest < alpha:
    print("Since p-value < 0.05, reject H₀.")
    print("There is a statistically significant difference in")
    print("teaching evaluation scores between genders.")
else:
    print("Since p-value >= 0.05, fail to reject H₀.")
    print("There is not sufficient evidence of a significant")
    print("difference in teaching evaluation scores between genders.")


# =========================================================
# QUESTION 2 - ANOVA
# =========================================================

print("\n" + "=" * 70)
print("QUESTION 2 - ANOVA")
print("=" * 70)

print("\nQuestion:")
print("Does beauty score for instructors differ by age?")

# Create age groups
def create_age_group(age):
    if age <= 40:
        return "40 and below"
    elif age < 57:
        return "Between 40 and 57"
    else:
        return "57 and above"


ratings_df["age_group"] = ratings_df["age"].apply(create_age_group)

group_1 = ratings_df[
    ratings_df["age_group"] == "40 and below"
]["beauty"]

group_2 = ratings_df[
    ratings_df["age_group"] == "Between 40 and 57"
]["beauty"]

group_3 = ratings_df[
    ratings_df["age_group"] == "57 and above"
]["beauty"]

print("\nAge Groups:")
print("Group 1: 40 years and below")
print("Group 2: Between 40 and 57 years")
print("Group 3: 57 years and above")

print("\nNumber of instructors:")
print("40 and below:", len(group_1))
print("Between 40 and 57:", len(group_2))
print("57 and above:", len(group_3))

print("\nMean Beauty Scores:")
print(f"40 and below = {group_1.mean():.4f}")
print(f"Between 40 and 57 = {group_2.mean():.4f}")
print(f"57 and above = {group_3.mean():.4f}")

print("\nHypotheses:")
print("H₀: The mean beauty scores are equal across all age groups.")
print("H₁: At least one age group has a different mean beauty score.")

f_statistic, p_value_anova = stats.f_oneway(
    group_1,
    group_2,
    group_3
)

print("\nANOVA Result:")
print(f"F-statistic = {f_statistic:.4f}")
print(f"p-value = {p_value_anova:.10f}")

print("\nDecision:")
if p_value_anova < alpha:
    print("Since p-value < 0.05, reject H₀.")
    print("There is a statistically significant difference")
    print("in beauty scores across the age groups.")
else:
    print("Since p-value >= 0.05, fail to reject H₀.")
    print("There is not sufficient evidence of a significant")
    print("difference in beauty scores across the age groups.")


# =========================================================
# QUESTION 3 - CHI-SQUARE TEST
# =========================================================

print("\n" + "=" * 70)
print("QUESTION 3 - CHI-SQUARE TEST")
print("=" * 70)

print("\nQuestion:")
print("Is there an association between tenure and gender?")

contingency_table = pd.crosstab(
    ratings_df["tenure"],
    ratings_df["gender"]
)

print("\nContingency Table:")
print(contingency_table)

print("\nHypotheses:")
print("H₀: There is no association between tenure and gender.")
print("H₁: There is an association between tenure and gender.")

chi2_statistic, p_value_chi, degrees_of_freedom, expected = stats.chi2_contingency(
    contingency_table
)

print("\nChi-Square Test Result:")
print(f"Chi-square statistic = {chi2_statistic:.4f}")
print(f"Degrees of freedom = {degrees_of_freedom}")
print(f"p-value = {p_value_chi:.6f}")

print("\nDecision:")
if p_value_chi < alpha:
    print("Since p-value < 0.05, reject H₀.")
    print("There is a statistically significant association")
    print("between tenure and gender.")
else:
    print("Since p-value >= 0.05, fail to reject H₀.")
    print("There is not sufficient evidence of an association")
    print("between tenure and gender.")


# =========================================================
# QUESTION 4 - CORRELATION
# =========================================================

print("\n" + "=" * 70)
print("QUESTION 4 - CORRELATION")
print("=" * 70)

print("\nQuestion:")
print("Is teaching evaluation score correlated with beauty score?")

evaluation = ratings_df["eval"]
beauty = ratings_df["beauty"]

print("\nHypotheses:")
print("H₀: There is no significant correlation between evaluation")
print("    score and beauty score.")
print("H₁: There is a significant correlation between evaluation")
print("    score and beauty score.")

correlation, p_value_corr = stats.pearsonr(
    evaluation,
    beauty
)

print("\nPearson Correlation Result:")
print(f"Correlation coefficient (r) = {correlation:.4f}")
print(f"p-value = {p_value_corr:.10f}")

print("\nDecision:")
if p_value_corr < alpha:
    print("Since p-value < 0.05, reject H₀.")
    print("There is a statistically significant correlation")
    print("between teaching evaluation score and beauty score.")
else:
    print("Since p-value >= 0.05, fail to reject H₀.")
    print("There is not sufficient evidence of a significant")
    print("correlation between teaching evaluation score and beauty score.")

print("\n" + "=" * 70)
print("END OF PRACTICAL 6")
print("=" * 70)