import pandas as pd
import math
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt


print("=" * 75)
print("PRACTICAL 8 - DECISION TREES AND ITS MAXDEPTH")
print("=" * 75)


# ---------------------------------------------------------
# 1. LOAD DATASET
# ---------------------------------------------------------

file_path = Path(__file__).parent / "data" / "diabetes.csv"

data = pd.read_csv(file_path)

print("\nDataset loaded successfully.")
print("Dataset shape:", data.shape)

print("\nDataset columns:")
print(list(data.columns))

print("\nFirst five rows:")
print(data.head())


# ---------------------------------------------------------
# 2. FEATURE SELECTION
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("FEATURE SELECTION")
print("=" * 75)

# Independent variables / features
X = data.drop("Outcome", axis=1)

# Dependent variable / target
y = data["Outcome"]

print("\nIndependent variables (Features):")
print(list(X.columns))

print("\nDependent variable (Target):")
print("Outcome")

print("\nFeature matrix shape:", X.shape)
print("Target shape:", y.shape)


# ---------------------------------------------------------
# 3. TRAIN-TEST SPLIT
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("TRAIN-TEST SPLIT")
print("=" * 75)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining data size:", X_train.shape)
print("Testing data size:", X_test.shape)

print("\nTraining target distribution:")
print(y_train.value_counts())


# ---------------------------------------------------------
# 4. ENTROPY FUNCTION
# ---------------------------------------------------------

def calculate_entropy(target):

    total = len(target)

    if total == 0:
        return 0

    counts = target.value_counts()

    entropy = 0

    for count in counts:

        probability = count / total

        if probability > 0:
            entropy -= probability * math.log2(probability)

    return entropy


# ---------------------------------------------------------
# 5. INFORMATION GAIN FUNCTION
# ---------------------------------------------------------

def calculate_information_gain(feature, target, threshold):

    parent_entropy = calculate_entropy(target)

    left = target[feature <= threshold]
    right = target[feature > threshold]

    if len(left) == 0 or len(right) == 0:
        return 0

    left_entropy = calculate_entropy(left)
    right_entropy = calculate_entropy(right)

    left_weight = len(left) / len(target)
    right_weight = len(right) / len(target)

    weighted_entropy = (
        left_weight * left_entropy
        + right_weight * right_entropy
    )

    information_gain = parent_entropy - weighted_entropy

    return information_gain


# ---------------------------------------------------------
# 6. GINI INDEX FUNCTION
# ---------------------------------------------------------

def calculate_gini(target):

    total = len(target)

    if total == 0:
        return 0

    counts = target.value_counts()

    gini = 1

    for count in counts:

        probability = count / total

        gini -= probability ** 2

    return gini


# ---------------------------------------------------------
# 6.0. ENTROPY, INFORMATION GAIN AND GINI INDEX
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("ENTROPY, INFORMATION GAIN AND GINI INDEX")
print("=" * 75)

parent_entropy = calculate_entropy(y_train)

print("\nEntropy of training target:")
print(f"Entropy = {parent_entropy:.6f}")


results = []

for feature_name in X_train.columns:

    feature_values = sorted(
        X_train[feature_name].unique()
    )

    if len(feature_values) < 2:
        continue

    thresholds = [
        (feature_values[i] + feature_values[i + 1]) / 2
        for i in range(len(feature_values) - 1)
    ]

    best_gain = -1
    best_threshold = None

    for threshold in thresholds:

        gain = calculate_information_gain(
            X_train[feature_name],
            y_train,
            threshold
        )

        if gain > best_gain:

            best_gain = gain
            best_threshold = threshold


    # Calculate Gini reduction at the same threshold
    left_target = y_train[
        X_train[feature_name] <= best_threshold
    ]

    right_target = y_train[
        X_train[feature_name] > best_threshold
    ]

    left_weight = len(left_target) / len(y_train)
    right_weight = len(right_target) / len(y_train)

    weighted_gini = (
        left_weight * calculate_gini(left_target)
        + right_weight * calculate_gini(right_target)
    )

    gini_reduction = (
        calculate_gini(y_train)
        - weighted_gini
    )

    results.append({
        "Feature": feature_name,
        "Best Threshold": best_threshold,
        "Information Gain": best_gain,
        "Gini Reduction": gini_reduction
    })


results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="Information Gain",
    ascending=False
)


print("\nFeature analysis:")

print(
    results_df.to_string(
        index=False,
        formatters={
            "Best Threshold": "{:.4f}".format,
            "Information Gain": "{:.6f}".format,
            "Gini Reduction": "{:.6f}".format
        }
    )
)


# ---------------------------------------------------------
# 7. BEST ROOT NODE
# ---------------------------------------------------------

best_feature = results_df.iloc[0]["Feature"]
best_threshold = results_df.iloc[0]["Best Threshold"]
best_gain = results_df.iloc[0]["Information Gain"]

print("\nBest root feature based on Information Gain:")

print("Feature:", best_feature)
print(f"Threshold: {best_threshold:.4f}")
print(f"Information Gain: {best_gain:.6f}")

print("\nOriginal training Gini Index:")

print(
    f"Gini = {calculate_gini(y_train):.6f}"
)


# ---------------------------------------------------------
# 8. DECISION TREE CLASSIFIER
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("DECISION TREE CLASSIFIER")
print("=" * 75)


max_depth_value = 3

decision_tree = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=max_depth_value,
    random_state=42
)

decision_tree.fit(
    X_train,
    y_train
)


y_pred = decision_tree.predict(X_test)


accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\nDecision Tree Settings:")

print("Criterion: entropy")
print("Maximum depth:", max_depth_value)


print("\nModel Accuracy:")

print(f"Accuracy = {accuracy:.4f}")
print(f"Accuracy = {accuracy * 100:.2f}%")


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "No Diabetes",
            "Diabetes"
        ]
    )
)


# ---------------------------------------------------------
# 9. MAXDEPTH COMPARISON
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("MAXDEPTH COMPARISON")
print("=" * 75)


depth_values = [
    1,
    2,
    3,
    4,
    5,
    None
]

depth_results = []


for depth in depth_values:

    tree = DecisionTreeClassifier(
        criterion="entropy",
        max_depth=depth,
        random_state=42
    )

    tree.fit(
        X_train,
        y_train
    )

    predictions = tree.predict(X_test)

    score = accuracy_score(
        y_test,
        predictions
    )

    depth_results.append({
        "Max Depth": depth,
        "Accuracy": score
    })


depth_df = pd.DataFrame(depth_results)


print("\nAccuracy for different max_depth values:")

print(
    depth_df.to_string(
        index=False,
        formatters={
            "Accuracy": "{:.4f}".format
        }
    )
)


# ---------------------------------------------------------
# 10. DECISION TREE VISUALIZATION
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("DECISION TREE VISUALIZATION")
print("=" * 75)


plt.figure(
    figsize=(22, 12)
)


plot_tree(
    decision_tree,
    feature_names=X.columns,
    class_names=[
        "No Diabetes",
        "Diabetes"
    ],
    filled=True,
    rounded=True,
    fontsize=9
)


plt.title(
    "Decision Tree Classifier - Pima Indians Diabetes Dataset"
)


plt.tight_layout()


output_path = (
    Path(__file__).parent
    / "decision_tree_visualization.png"
)


plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)


print("\nDecision tree visualization saved to:")

print(output_path)


plt.show()


# ---------------------------------------------------------
# 11. FINAL CONCLUSION
# ---------------------------------------------------------

print("\n" + "=" * 75)
print("FINAL CONCLUSION")
print("=" * 75)


print(
    "\nThe Pima Indians Diabetes dataset was successfully"
)

print(
    "used to build a Decision Tree classification model."
)


print(
    "\nThe dataset was divided into:"
)

print(
    "- Independent variables (features)"
)

print(
    "- Dependent variable (Outcome)"
)


print(
    "\nEntropy and Information Gain were calculated to"
)

print(
    "identify the best feature for the root node."
)


print(
    "\nThe Decision Tree was trained using the entropy criterion"
)

print(
    f"with max_depth = {max_depth_value}."
)


print(
    "\nThe model accuracy was:"
)

print(
    f"{accuracy * 100:.2f}%"
)


print(
    "\nThe decision tree visualization was generated successfully."
)


print("\n" + "=" * 75)
print("END OF PRACTICAL 8")
print("=" * 75)