
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# ---------------------------------------------------------
# PRACTICAL 10 - WINE DATASET ANALYSIS AND PCA
# ---------------------------------------------------------

print("=" * 75)
print("PRACTICAL 10 - WINE DATASET ANALYSIS AND PCA")
print("=" * 75)

output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)


# ---------------------------------------------------------
# 1. LOAD DATASET AND DISPLAY BASIC STATISTICS
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 1 - BASIC STATISTICS")
print("=" * 75)

wine = load_wine()

data = pd.DataFrame(
    wine.data,
    columns=wine.feature_names
)

data["Class"] = wine.target

class_names = {
    index: name
    for index, name in enumerate(wine.target_names)
}

data["Class_Name"] = data["Class"].map(class_names)

print("\nDataset loaded successfully.")
print("Dataset shape:", data.shape)

print("\nFirst five rows:")
print(data.head())

print("\nBasic statistical description:")
print(data[wine.feature_names].describe().round(2))

print("\nNumber of samples in each class:")
print(data["Class_Name"].value_counts().sort_index())


# ---------------------------------------------------------
# 2. BOXPLOTS BY OUTPUT LABELS / CLASSES
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 2 - BOXPLOTS BY CLASS")
print("=" * 75)

selected_features = [
    "alcohol",
    "malic_acid",
    "color_intensity"
]

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

for ax, feature in zip(axes, selected_features):

    sns.boxplot(
        data=data,
        x="Class_Name",
        y=feature,
        ax=ax
    )

    ax.set_title(feature.replace("_", " ").title())
    ax.set_xlabel("Wine Class")
    ax.set_ylabel(feature.replace("_", " ").title())

plt.suptitle("Wine Feature Distributions by Class")
plt.tight_layout()

boxplot_path = output_dir / "boxplots_by_class.png"

plt.savefig(
    boxplot_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nBoxplots generated successfully.")
print("Features plotted:", selected_features)
print("Boxplot saved to:", boxplot_path)


# ---------------------------------------------------------
# 3. SCATTERPLOT USING TWO VARIABLES
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 3 - SCATTERPLOT")
print("=" * 75)

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=data,
    x="alcohol",
    y="color_intensity",
    hue="Class_Name",
    palette="Set1",
    s=70
)

plt.title("Alcohol vs Color Intensity by Wine Class")
plt.xlabel("Alcohol")
plt.ylabel("Color Intensity")
plt.legend(title="Wine Class")
plt.tight_layout()

scatter_path = output_dir / "scatterplot_two_variables.png"

plt.savefig(
    scatter_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nScatterplot generated successfully.")
print("X-axis: Alcohol")
print("Y-axis: Color Intensity")
print("Scatterplot saved to:", scatter_path)


# ---------------------------------------------------------
# 4. COVARIANCE MATRIX
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 4 - COVARIANCE MATRIX")
print("=" * 75)

features = data[wine.feature_names]

covariance_matrix = features.cov()

print("\nCovariance Matrix:")
print(covariance_matrix.round(2).to_string())

plt.figure(figsize=(14, 11))

sns.heatmap(
    covariance_matrix,
    cmap="coolwarm",
    center=0,
    annot=False
)

plt.title("Covariance Matrix of Wine Features")
plt.tight_layout()

covariance_path = output_dir / "covariance_matrix.png"

plt.savefig(
    covariance_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nCovariance matrix calculated successfully.")
print("Covariance heatmap saved to:", covariance_path)


# ---------------------------------------------------------
# 5. DATA SCALING
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 5 - DATA SCALING")
print("=" * 75)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(features)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=wine.feature_names
)

print("\nData scaling completed successfully.")

print("\nFirst five rows after scaling:")
print(scaled_df.head().round(3))

print("\nMean of scaled features (first five):")
print(scaled_df.mean().head().round(4))

print("\nStandard deviation of scaled features (first five):")
print(scaled_df.std(ddof=0).head().round(4))


# ---------------------------------------------------------
# 6. PCA FOR BETTER CLASS SEPARATION
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 6 - PRINCIPAL COMPONENT ANALYSIS (PCA)")
print("=" * 75)

pca = PCA(n_components=2)

principal_components = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(
    principal_components,
    columns=["Principal Component 1", "Principal Component 2"]
)

pca_df["Class_Name"] = data["Class_Name"].values

print("\nPCA completed successfully.")

print("\nExplained variance ratio:")
print("Principal Component 1:",
      f"{pca.explained_variance_ratio_[0]:.4f}")
print("Principal Component 2:",
      f"{pca.explained_variance_ratio_[1]:.4f}")

total_variance = pca.explained_variance_ratio_.sum()

print("Total variance explained by two components:",
      f"{total_variance:.4f}")
print("Total variance explained (%):",
      f"{total_variance * 100:.2f}%")

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=pca_df,
    x="Principal Component 1",
    y="Principal Component 2",
    hue="Class_Name",
    palette="Set1",
    s=70
)

plt.title("PCA - Wine Class Separation")
plt.xlabel(
    f"PC1 ({pca.explained_variance_ratio_[0] * 100:.2f}% variance)"
)
plt.ylabel(
    f"PC2 ({pca.explained_variance_ratio_[1] * 100:.2f}% variance)"
)
plt.legend(title="Wine Class")
plt.tight_layout()

pca_path = output_dir / "pca_class_separation.png"

plt.savefig(
    pca_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nPCA visualization saved to:", pca_path)


# ---------------------------------------------------------
# FINAL CONCLUSION
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("FINAL CONCLUSION")
print("=" * 75)

print("\nThe Wine dataset was analysed successfully.")
print("Basic statistics were displayed using describe().")
print("Boxplots were created to compare selected features by class.")
print("A scatterplot was created using two numerical variables.")
print("The covariance matrix was calculated and visualized.")
print("StandardScaler was used to scale the data.")
print("PCA reduced the 13 features to two principal components.")
print(f"Variance retained by two components: {total_variance * 100:.2f}%")
print("All visualizations were saved in the output folder.")

print("\n" + "=" * 75)
print("END OF PRACTICAL 10")
print("=" * 75)
