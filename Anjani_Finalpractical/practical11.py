"""
Practical 11 / Practical Exam: Simplifying a Cancer Diagnostic Panel
Objective: Evaluate whether a reduced PCA panel can replace the full 30-feature
diagnostic panel without sacrificing malignant vs. benign classification performance.
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score, StratifiedKFold

# Configure styling
plt.rcParams["font.sans-serif"] = ["Helvetica", "Arial", "DejaVu Sans"]
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["axes.linewidth"] = 0.8

# Output directory setup
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(parents=True, exist_ok=True)

print("=" * 80)
print("PRACTICAL 11 / PRACTICAL EXAM: SIMPLIFYING A CANCER DIAGNOSTIC PANEL")
print("=" * 80)


# =============================================================================
# DATA LOADING & INITIAL EXPLORATION
# =============================================================================
print("\n" + "=" * 80)
print("STEP 0: LOAD BREAST CANCER DATASET")
print("=" * 80)

data = load_breast_cancer(as_frame=True)
X, y = data.data, data.target  # y: 0 = malignant, 1 = benign

target_names = {0: "Malignant", 1: "Benign"}
target_series = y.map(target_names)

print(f"Total biopsy samples: {X.shape[0]}")
print(f"Total cell nuclei features: {X.shape[1]}")
print(f"Diagnosis distribution:\n{target_series.value_counts()}")
print(f"\nFeature names (30 features):\n{list(X.columns)}")


# =============================================================================
# TASK 1: STANDARDISE THE 30 FEATURES AND FIT PCA WITH ALL COMPONENTS
# =============================================================================
print("\n" + "=" * 80)
print("TASK 1: STANDARDISE 30 FEATURES & FIT FULL PCA")
print("=" * 80)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=X.shape[1], random_state=42)
X_pca = pca.fit_transform(X_scaled)

print("Standardisation complete: Mean = 0.0, Standard Deviation = 1.0 for each feature.")
print(f"PCA fitted successfully with all {pca.n_components_} components.")
print(f"Transformed coordinates matrix shape: {X_pca.shape}")


# =============================================================================
# TASK 2: SCREE PLOT & CUMULATIVE EXPLAINED-VARIANCE PLOT
# =============================================================================
print("\n" + "=" * 80)
print("TASK 2: SCREE PLOT & CUMULATIVE EXPLAINED VARIANCE")
print("=" * 80)

explained_var_ratio = pca.explained_variance_ratio_
cumulative_var_ratio = np.cumsum(explained_var_ratio)

# Find minimum components for 90% and 95% variance
k_90 = int(np.argmax(cumulative_var_ratio >= 0.90) + 1)
k_95 = int(np.argmax(cumulative_var_ratio >= 0.95) + 1)

print(f"PC1 individual variance explained: {explained_var_ratio[0]*100:.2f}%")
print(f"PC2 individual variance explained: {explained_var_ratio[1]*100:.2f}%")
print(f"First 2 components explain: {cumulative_var_ratio[1]*100:.2f}% of total variance.")
print(f"\n-> Components required for >= 90% variance: k = {k_90} (explains {cumulative_var_ratio[k_90-1]*100:.2f}%)")
print(f"-> Components required for >= 95% variance: k = {k_95} (explains {cumulative_var_ratio[k_95-1]*100:.2f}%)")

# Visualization: Scree Plot & Cumulative Explained Variance
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# (a) Scree Plot
components_range = np.arange(1, len(explained_var_ratio) + 1)
ax1.plot(components_range, explained_var_ratio * 100, "o-", color="#1f77b4", linewidth=2, markersize=5)
ax1.bar(components_range, explained_var_ratio * 100, alpha=0.3, color="#1f77b4", edgecolor="#1f77b4")
ax1.set_title("Scree Plot (Individual Variance Explained)", fontsize=12, fontweight="bold")
ax1.set_xlabel("Principal Component Index", fontsize=11)
ax1.set_ylabel("Variance Explained (%)", fontsize=11)
ax1.set_xticks(range(1, 31, 2))
ax1.grid(True, linestyle="--", alpha=0.6)

# (b) Cumulative Variance Plot
ax2.plot(components_range, cumulative_var_ratio * 100, "s-", color="#2ca02c", linewidth=2, markersize=5)
ax2.axhline(90, color="#d62728", linestyle="--", linewidth=1.5, label="90% Variance Threshold")
ax2.axhline(95, color="#ff7f0e", linestyle="--", linewidth=1.5, label="95% Variance Threshold")
ax2.axvline(k_90, color="#d62728", linestyle=":", linewidth=1.5, label=f"k={k_90} (90% threshold: {cumulative_var_ratio[k_90-1]*100:.1f}%)")
ax2.axvline(k_95, color="#ff7f0e", linestyle=":", linewidth=1.5, label=f"k={k_95} (95% threshold: {cumulative_var_ratio[k_95-1]*100:.1f}%)")
ax2.set_title("Cumulative Explained Variance Plot", fontsize=12, fontweight="bold")
ax2.set_xlabel("Number of Principal Components", fontsize=11)
ax2.set_ylabel("Cumulative Variance (%)", fontsize=11)
ax2.set_xticks(range(1, 31, 2))
ax2.legend(loc="lower right", frameon=True)
ax2.grid(True, linestyle="--", alpha=0.6)

plt.suptitle("Breast Cancer PCA: Variance Decomposition", fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()

scree_plot_path = output_dir / "task2_scree_and_cumulative_variance.png"
plt.savefig(scree_plot_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Plot saved successfully to: {scree_plot_path.name}")


# =============================================================================
# TASK 3: PLOT SAMPLES ON PC1 VS PC2 COLOURED BY DIAGNOSIS
# =============================================================================
print("\n" + "=" * 80)
print("TASK 3: 2D PROJECTION ON PC1 VS PC2 COLOURED BY DIAGNOSIS")
print("=" * 80)

plt.figure(figsize=(9, 7))

# Separate points by diagnosis
mask_malignant = (y == 0)
mask_benign = (y == 1)

plt.scatter(
    X_pca[mask_malignant, 0],
    X_pca[mask_malignant, 1],
    c="#d62728",
    marker="x",
    s=65,
    label="Malignant (y=0)",
    alpha=0.85,
    linewidth=1.2
)

plt.scatter(
    X_pca[mask_benign, 0],
    X_pca[mask_benign, 1],
    c="#1f77b4",
    marker="o",
    s=55,
    label="Benign (y=1)",
    alpha=0.75,
    edgecolors="k",
    linewidth=0.5
)

plt.title(
    f"Breast Biopsy Samples Projected on PC1 vs PC2\n(Explains {cumulative_var_ratio[1]*100:.2f}% Total Variance)",
    fontsize=13,
    fontweight="bold"
)
plt.xlabel(f"PC1 ({explained_var_ratio[0]*100:.2f}% Variance Explained)", fontsize=11)
plt.ylabel(f"PC2 ({explained_var_ratio[1]*100:.2f}% Variance Explained)", fontsize=11)
plt.axhline(0, color="grey", linestyle="--", linewidth=0.8, alpha=0.7)
plt.axvline(0, color="grey", linestyle="--", linewidth=0.8, alpha=0.7)
plt.legend(title="Diagnosis", loc="upper right", frameon=True)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

pc_scatter_path = output_dir / "task3_pc1_vs_pc2_diagnosis.png"
plt.savefig(pc_scatter_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Plot saved successfully to: {pc_scatter_path.name}")


# =============================================================================
# TASK 4: FIVE FEATURES WITH LARGEST ABSOLUTE LOADINGS ON PC1 AND PC2
# =============================================================================
print("\n" + "=" * 80)
print("TASK 4: TOP 5 ABSOLUTE LOADINGS ON PC1 AND PC2")
print("=" * 80)

# components_ has shape (n_components, n_features) -> transpose to (features, components)
loadings = pd.DataFrame(
    pca.components_.T,
    index=X.columns,
    columns=[f"PC{i+1}" for i in range(pca.n_components_)]
)

# Top 5 absolute loadings on PC1
pc1_top5_idx = loadings["PC1"].abs().sort_values(ascending=False).head(5).index
pc1_top5 = loadings.loc[pc1_top5_idx, ["PC1"]].copy()
pc1_top5["Absolute_Loading"] = pc1_top5["PC1"].abs()

# Top 5 absolute loadings on PC2
pc2_top5_idx = loadings["PC2"].abs().sort_values(ascending=False).head(5).index
pc2_top5 = loadings.loc[pc2_top5_idx, ["PC2"]].copy()
pc2_top5["Absolute_Loading"] = pc2_top5["PC2"].abs()

print("\nTop 5 Features with Largest Absolute Loadings on PC1:")
print("-" * 65)
for rank, (feat, row) in enumerate(pc1_top5.iterrows(), 1):
    print(f" {rank}. {feat:<28} : Loading = {row['PC1']:+.4f} (Abs: {row['Absolute_Loading']:.4f})")

print("\nTop 5 Features with Largest Absolute Loadings on PC2:")
print("-" * 65)
for rank, (feat, row) in enumerate(pc2_top5.iterrows(), 1):
    print(f" {rank}. {feat:<28} : Loading = {row['PC2']:+.4f} (Abs: {row['Absolute_Loading']:.4f})")

# Visualization: Bar plots of top 5 loadings
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# PC1 top 5 barplot
colors_pc1 = ["#1f77b4" if v >= 0 else "#ff7f0e" for v in pc1_top5["PC1"]]
ax1.barh(pc1_top5.index[::-1], pc1_top5["PC1"][::-1], color=colors_pc1[::-1], edgecolor="black", alpha=0.85)
ax1.set_title("Top 5 Loadings on PC1 (Primary Shape/Concavity Factor)", fontsize=11, fontweight="bold")
ax1.set_xlabel("Loading Value", fontsize=10)
ax1.grid(True, linestyle="--", alpha=0.6)

# PC2 top 5 barplot
colors_pc2 = ["#1f77b4" if v >= 0 else "#ff7f0e" for v in pc2_top5["PC2"]]
ax2.barh(pc2_top5.index[::-1], pc2_top5["PC2"][::-1], color=colors_pc2[::-1], edgecolor="black", alpha=0.85)
ax2.set_title("Top 5 Loadings on PC2 (Fractal Dimension & Texture Factor)", fontsize=11, fontweight="bold")
ax2.set_xlabel("Loading Value", fontsize=10)
ax2.grid(True, linestyle="--", alpha=0.6)

plt.suptitle("Principal Component Loadings (Feature Contributions)", fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()

loadings_plot_path = output_dir / "task4_pca_loadings.png"
plt.savefig(loadings_plot_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Plot saved successfully to: {loadings_plot_path.name}")


# =============================================================================
# TASK 5: LOGISTIC REGRESSION WITH 5-FOLD CV PIPELINE
# =============================================================================
print("\n" + "=" * 80)
print("TASK 5: LOGISTIC REGRESSION WITH 5-FOLD CROSS-VALIDATION")
print("=" * 80)

# Stratified 5-Fold Cross-Validation ensures balanced class proportions
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Model (a): All 30 standardised features inside Pipeline
pipeline_all_features = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

cv_scores_all = cross_val_score(pipeline_all_features, X, y, cv=cv, scoring="accuracy")

# Model (b): Only first k components (k=7 for 90% variance) inside Pipeline
pipeline_pca_reduced = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=k_90, random_state=42)),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42))
])

cv_scores_pca = cross_val_score(pipeline_pca_reduced, X, y, cv=cv, scoring="accuracy")

print(f"\nModel (a) - All 30 Standardised Features:")
for fold_idx, score in enumerate(cv_scores_all, 1):
    print(f"  Fold {fold_idx}: Accuracy = {score*100:.2f}%")
print(f"  Mean Accuracy: {cv_scores_all.mean()*100:.2f}% (+/- {cv_scores_all.std()*100:.2f}%)")

print(f"\nModel (b) - Reduced Panel (First k={k_90} PCA Components - 91.01% Variance):")
for fold_idx, score in enumerate(cv_scores_pca, 1):
    print(f"  Fold {fold_idx}: Accuracy = {score*100:.2f}%")
print(f"  Mean Accuracy: {cv_scores_pca.mean()*100:.2f}% (+/- {cv_scores_pca.std()*100:.2f}%)")

acc_difference = (cv_scores_all.mean() - cv_scores_pca.mean()) * 100
print(f"\nPerformance Difference (All Features vs PCA): {acc_difference:.2f}%")
print("Note: Both pipelines fit scaler & PCA strictly within training folds, guaranteeing zero data leakage.")

# Visualization: Comparison Bar Chart
fig, ax = plt.subplots(figsize=(8, 5))
model_names = ["All 30 Features\n(Standardised)", f"Reduced Panel\n(First {k_90} PCA Components)"]
means = [cv_scores_all.mean() * 100, cv_scores_pca.mean() * 100]
stds = [cv_scores_all.std() * 100, cv_scores_pca.std() * 100]

bars = ax.bar(model_names, means, yerr=stds, capsize=8, color=["#1f77b4", "#2ca02c"], alpha=0.85, edgecolor="black", width=0.45)

for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2.0,
        height - 6,
        f"{height:.2f}%\n(±{stds[i]:.2f}%)",
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color="white"
    )

ax.set_ylim(80, 102)
ax.set_ylabel("5-Fold Cross-Validation Accuracy (%)", fontsize=11)
ax.set_title("Diagnostic Performance Comparison: Full vs. Reduced Panel", fontsize=12, fontweight="bold")
ax.grid(True, linestyle="--", alpha=0.6, axis="y")
plt.tight_layout()

model_comp_path = output_dir / "task5_model_cv_comparison.png"
plt.savefig(model_comp_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Plot saved successfully to: {model_comp_path.name}")


# =============================================================================
# FOLLOW-UP QUESTIONS (Q1 & Q2) ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("FOLLOW-UP QUESTIONS: ANSWERS & STATISTICAL EXPLANATIONS")
print("=" * 80)

# Comparison with Unstandardised PCA
pca_unscaled = PCA(random_state=42)
pca_unscaled.fit(X)
unscaled_pc1_var = pca_unscaled.explained_variance_ratio_[0] * 100
unscaled_pc1_loadings = pd.Series(pca_unscaled.components_[0], index=X.columns).abs().sort_values(ascending=False)

print("\n--- QUESTION 1: SHARE OF VARIANCE & STANDARDISATION EFFECT ---")
print(f"1. Standardised PC1 explains: {explained_var_ratio[0]*100:.2f}% of the total variance.")
print(f"   Top feature on standardised PC1: '{pc1_top5.index[0]}' with loading = {pc1_top5['PC1'].iloc[0]:.4f}.")
print(f"2. In contrast, UNSTANDARDISED PC1 explains: {unscaled_pc1_var:.2f}% of total variance.")
print(f"   Top feature on unstandardised PC1: '{unscaled_pc1_loadings.index[0]}' with absolute loading = {unscaled_pc1_loadings.iloc[0]:.4f}.")
print("3. Why standardisation changes the result so drastically:")
print("   - PCA seeks directions of maximal variance.")
print("   - Features with large numerical ranges (e.g. 'worst area' variance ~ 324,000) mechanically")
print("     dominate unstandardised PCA, rendering features with small units (e.g. 'concavity' ~ 0.005) invisible.")
print("   - Standardisation rescales all features to unit variance (sigma^2 = 1.0), forcing PCA to identify")
print("     true correlation and biological covariation rather than arbitrary measurement units.")

print("\n--- QUESTION 2: RECOMMENDATION TO THE LAB ---")
print("1. Recommendation: YES, the reduced panel is recommended for clinical implementation.")
print("2. One Statistical Reason:")
print(f"   - The reduced panel uses only 7 components (a 76.7% reduction in dimensions) while retaining")
print(f"     91.01% of all variance, achieving {cv_scores_pca.mean()*100:.2f}% CV accuracy compared to {cv_scores_all.mean()*100:.2f}%")
print(f"     on all 30 features (a negligible drop of just {acc_difference:.2f}%). This eliminates high multicollinearity")
print(f"     and reduces overfitting risk.")
print("3. One Practical Reason:")
print("   - Operational cost, lab throughput, and error reduction: Measuring and quality-controlling")
print("     30 individual nuclear morphology assays is expensive, computationally demanding, and prone to assay failure.")
print("     A condensed panel reduces biopsy processing turnaround time and clinical diagnostic cost.")
print("4. Loss in Interpretability:")
print("   - Principal components are mathematical linear combinations (weighted sums) of all original features.")
print("   - While pathologists understand direct biological measurements (e.g. 'cell radius = 18 um', 'severe concavity'),")
print("     a composite score like 'PC1 = +2.4' has no intuitive histological meaning, making clinical explanation to")
print("     oncologists and patients harder.")

print("\n" + "=" * 80)
print("PRACTICAL 11 EXECUTION COMPLETED SUCCESSFULLY!")
print("=" * 80)
