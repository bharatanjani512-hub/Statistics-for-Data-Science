
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


# ---------------------------------------------------------
# PRACTICAL 9 - K NEAREST NEIGHBOURS (KNN)
# ---------------------------------------------------------

print("=" * 75)
print("PRACTICAL 9 - K NEAREST NEIGHBOURS (KNN)")
print("=" * 75)

output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)


# ---------------------------------------------------------
# 1. LOAD DATASET AND PERFORM EDA
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 1 - EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 75)

iris = load_iris()

iris_df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

iris_df["species"] = pd.Categorical.from_codes(
    iris.target,
    categories=iris.target_names
)

print("\nDataset loaded successfully.")
print("Dataset shape:", iris_df.shape)

print("\nFirst five rows:")
print(iris_df.head())

print("\nStatistical description:")
print(iris_df.describe().round(2))

print("\nSpecies-wise mean values:")
print(
    iris_df.groupby("species", observed=False)
    .mean(numeric_only=True)
    .round(2)
)

print("\nSpecies distribution:")
print(iris_df["species"].value_counts())


# ---------------------------------------------------------
# 2. FEATURE SELECTION AND TRAIN-TEST SPLIT
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 2 - FEATURE SELECTION AND TRAIN-TEST SPLIT")
print("=" * 75)

X = iris_df.drop("species", axis=1)
y = iris.target

print("\nIndependent variables:")
print(list(X.columns))

print("\nDependent variable:")
print("species")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)


# ---------------------------------------------------------
# 3. FEATURE SCALING
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 3 - FEATURE SCALING")
print("=" * 75)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed successfully.")
print("Scaled training data shape:", X_train_scaled.shape)
print("Scaled testing data shape:", X_test_scaled.shape)

print("\nFirst five scaled training rows:")
print(pd.DataFrame(
    X_train_scaled,
    columns=X.columns
).head().round(3))


# ---------------------------------------------------------
# 4. TRAIN THE KNN MODEL
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 4 - TRAINING THE KNN MODEL")
print("=" * 75)

k_value = 5

knn_model = KNeighborsClassifier(
    n_neighbors=k_value
)

knn_model.fit(X_train_scaled, y_train)

print("\nKNN model trained successfully.")
print("Number of neighbours (K):", k_value)


# ---------------------------------------------------------
# 5. PREDICTION AND CONFUSION MATRIX
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 5 - CONFUSION MATRIX AND PREDICTION")
print("=" * 75)

y_pred = knn_model.predict(X_test_scaled)

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=[0, 1, 2]
)

print("\nConfusion Matrix:")
print(cm)

print("\nFirst ten actual and predicted values:")

comparison = pd.DataFrame({
    "Actual Species": iris.target_names[y_test[:10]],
    "Predicted Species": iris.target_names[y_pred[:10]]
})

print(comparison.to_string(index=False))


# ---------------------------------------------------------
# 6. ACCURACY AND CLASSIFICATION REPORT
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 6 - ACCURACY AND CLASSIFICATION REPORT")
print("=" * 75)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy Score:")
print(f"Accuracy = {accuracy:.4f}")
print(f"Accuracy = {accuracy * 100:.2f}%")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names,
        zero_division=0
    )
)


# ---------------------------------------------------------
# 7. COMPARE ERROR RATES FOR DIFFERENT K VALUES
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 7 - ERROR RATE COMPARISON")
print("=" * 75)

k_values = list(range(1, 21))
error_rates = []

for k in k_values:

    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)

    error_rate = 1 - accuracy_score(y_test, predictions)

    error_rates.append(error_rate)

error_df = pd.DataFrame({
    "K Value": k_values,
    "Error Rate": error_rates
})

print("\nError rates for different K values:")

print(
    error_df.to_string(
        index=False,
        formatters={
            "Error Rate": "{:.4f}".format
        }
    )
)


# ---------------------------------------------------------
# 8. PLOT ERROR RATE AND FIND BEST K
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 8 - FINDING THE BEST K")
print("=" * 75)

best_index = error_rates.index(min(error_rates))
best_k = k_values[best_index]
best_error = error_rates[best_index]

print("\nBest K value:", best_k)
print(f"Lowest error rate: {best_error:.4f}")
print(f"Lowest error rate: {best_error * 100:.2f}%")

plt.figure(figsize=(10, 6))

plt.plot(
    k_values,
    error_rates,
    marker="o"
)

plt.xlabel("K Value")
plt.ylabel("Error Rate")
plt.title("Error Rate vs K Value")
plt.xticks(k_values)
plt.grid(True, alpha=0.3)
plt.tight_layout()

error_plot_path = output_dir / "error_rate_vs_k.png"

plt.savefig(
    error_plot_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nError-rate graph saved to:")
print(error_plot_path)


# ---------------------------------------------------------
# 9. VISUALIZE THE TEST RESULTS OF KNN
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("STEP 9 - VISUALIZING KNN TEST RESULTS")
print("=" * 75)

best_model = KNeighborsClassifier(
    n_neighbors=best_k
)

best_model.fit(X_train_scaled, y_train)

best_predictions = best_model.predict(X_test_scaled)

best_accuracy = accuracy_score(
    y_test,
    best_predictions
)

print("\nFinal KNN model trained using best K.")
print("Best K:", best_k)
print(f"Test accuracy: {best_accuracy * 100:.2f}%")


# Confusion matrix visualization

fig, ax = plt.subplots(figsize=(8, 6))

ConfusionMatrixDisplay.from_predictions(
    y_test,
    best_predictions,
    labels=[0, 1, 2],
    display_labels=iris.target_names,
    cmap="Blues",
    ax=ax
)

ax.set_title(f"KNN Confusion Matrix (Best K = {best_k})")

plt.tight_layout()

cm_plot_path = output_dir / "confusion_matrix.png"

plt.savefig(
    cm_plot_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# Actual versus predicted species visualization

sample_numbers = list(range(1, len(y_test) + 1))

plt.figure(figsize=(13, 6))

plt.plot(
    sample_numbers,
    y_test,
    marker="o",
    linestyle="",
    label="Actual Species"
)

plt.plot(
    sample_numbers,
    best_predictions,
    marker="x",
    linestyle="",
    label="Predicted Species"
)

plt.yticks(
    [0, 1, 2],
    iris.target_names
)

plt.xlabel("Test Sample Number")
plt.ylabel("Species")
plt.title(f"Actual vs Predicted Species (Best K = {best_k})")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

test_plot_path = output_dir / "test_results_visualization.png"

plt.savefig(
    test_plot_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nConfusion matrix graph saved to:")
print(cm_plot_path)

print("\nTest result visualization saved to:")
print(test_plot_path)


# ---------------------------------------------------------
# FINAL CONCLUSION
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("FINAL CONCLUSION")
print("=" * 75)

print("\nThe Iris dataset was loaded and analysed successfully.")
print("Feature scaling was applied before training the KNN model.")
print(f"The initial model used K = {k_value}.")
print(f"Initial model accuracy: {accuracy * 100:.2f}%")
print(f"Best K among tested values: {best_k}")
print(f"Best model accuracy: {best_accuracy * 100:.2f}%")
print("Error-rate and test-result visualizations were generated.")

print("\n" + "=" * 75)
print("END OF PRACTICAL 9")
print("=" * 75)
