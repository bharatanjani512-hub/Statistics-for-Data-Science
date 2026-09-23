import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from pathlib import Path


# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------

file_path = Path(__file__).parent / "data" / "teachingratings.csv"
ratings_df = pd.read_csv(file_path)

print("=" * 70)
print("PRACTICAL 7 - UNDERSTANDING REGRESSION WITH T-TEST AND ANOVA")
print("=" * 70)

print("\nDataset loaded successfully.")
print("Dataset shape:", ratings_df.shape)


# =========================================================
# QUESTION 1 - REGRESSION WITH T-TEST
# =========================================================

print("\n" + "=" * 70)
print("QUESTION 1 - REGRESSION WITH T-TEST")
print("=" * 70)

print("\nQuestion:")
print("Using the teachers' rating data set, does gender affect")
print("teaching evaluation rates?")

# Convert gender into a binary variable.
# Male = 0 and Female = 1
ratings_df["female"] = (ratings_df["gender"] == "female").astype(int)

# OLS regression
model_q1 = ols("eval ~ female", data=ratings_df).fit()

print("\nOLS Regression Results:")
print(model_q1.summary())


# =========================================================
# QUESTION 2 - REGRESSION WITH ANOVA
# =========================================================

print("\n" + "=" * 70)
print("QUESTION 2 - REGRESSION WITH ANOVA")
print("=" * 70)

print("\nQuestion:")
print("Using the teachers' rating data set, does beauty score")
print("for instructors differ by age?")

# Create the age groups
def create_age_group(age):
    if age <= 40:
        return "40 and below"
    elif age < 57:
        return "Between 40 and 57"
    else:
        return "57 and above"


ratings_df["age_group"] = ratings_df["age"].apply(create_age_group)

# Regression model using age group as a categorical variable
model_q2 = ols(
    "beauty ~ C(age_group)",
    data=ratings_df
).fit()

# ANOVA table
anova_results = anova_lm(model_q2)

print("\nANOVA Results:")
print(anova_results)


# =========================================================
# QUESTION 3 - CORRELATION / REGRESSION
# =========================================================

print("\n" + "=" * 70)
print("QUESTION 3 - CORRELATION / REGRESSION")
print("=" * 70)

print("\nQuestion:")
print("Using the teachers' rating dataset, is teaching evaluation")
print("score correlated with beauty score?")

# OLS regression
model_q3 = ols("eval ~ beauty", data=ratings_df).fit()

print("\nOLS Regression Results:")
print(model_q3.summary())


print("\n" + "=" * 70)
print("END OF PRACTICAL 7")
print("=" * 70)