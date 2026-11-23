# Practical 11: Anjani_Finalpractical - Simplifying a Cancer Diagnostic Panel (PCA & Clinical Feature Reduction)

## Objective
To evaluate whether a reduced Principal Component Analysis (PCA) panel can replace a full 30-feature cell nucleus biopsy panel without sacrificing the hospital lab's ability to differentiate malignant from benign breast tumors.

---

## Dataset Description
- **Source:** Breast Cancer Wisconsin (Diagnostic) Dataset (`sklearn.datasets.load_breast_cancer`)
- **Total Samples:** 569 patient biopsies
- **Target Variable ($y$):** Diagnosis
  - `0` = Malignant (212 samples, 37.3%)
  - `1` = Benign (357 samples, 62.7%)
- **Predictor Features ($X$):** 30 continuous morphological features extracted from digitized images of Fine Needle Aspirates (FNA) of breast masses (describing characteristics of cell nuclei such as radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension across mean, standard error, and "worst"/largest measurements).

---

## Practical Tasks & Results

### Task 1: Standardisation & Full PCA Fit
- The 30 features have vastly different physical units (e.g., cell area in hundreds/thousands of $\mu m^2$ vs. fractal dimension $< 0.1$).
- Using `StandardScaler()`, each feature is standardized to zero mean ($\mu = 0$) and unit variance ($\sigma = 1$).
- Full PCA with 30 components is fitted to capture the complete orthogonal variance structure.

### Task 2: Scree Plot & Cumulative Explained Variance
- **PC1 Variance Explained:** **44.27%**
- **PC2 Variance Explained:** **18.97%**
- **First 2 Components Combined:** **63.24%** of total variance.
- **Threshold Analysis:**
  - $\ge 90\%$ variance threshold: achieved at **$k = 7$ components** (explaining **91.01%** variance).
  - $\ge 95\%$ variance threshold: achieved at **$k = 10$ components** (explaining **95.16%** variance).
- **Generated Plot:** `output/task2_scree_and_cumulative_variance.png`

### Task 3: 2D Projection (PC1 vs. PC2 by Diagnosis)
- Biopsy samples are projected onto the first two principal component axes.
- Malignant and benign tumors show clean visual separation along **PC1**:
  - Malignant biopsies concentrate heavily on positive PC1 scores (higher nuclear size, severe concavity, irregularity).
  - Benign biopsies cluster on negative PC1 scores.
- **Generated Plot:** `output/task3_pc1_vs_pc2_diagnosis.png`

### Task 4: Top 5 Absolute Loadings on PC1 and PC2

#### Top 5 Features on PC1 (Primary Tumor Severity / Shape Irregularity Axis)
| Rank | Feature | Loading Value | Absolute Loading | Direction / Interpretation |
|:---:|:---|:---:|:---:|:---|
| 1 | `mean concave points` | +0.2609 | 0.2609 | High number of concave contour portions |
| 2 | `mean concavity` | +0.2584 | 0.2584 | Severity of concave contour portions |
| 3 | `worst concave points` | +0.2509 | 0.2509 | Extreme concave portions in biopsy |
| 4 | `mean compactness` | +0.2393 | 0.2393 | High perimeter$^2$ / area ratio |
| 5 | `worst perimeter` | +0.2366 | 0.2366 | Extreme nuclear boundary length |

#### Top 5 Features on PC2 (Texture & Fractal Complexity Axis)
| Rank | Feature | Loading Value | Absolute Loading | Direction / Interpretation |
|:---:|:---|:---:|:---:|:---|
| 1 | `mean fractal dimension` | +0.3666 | 0.3666 | Higher boundary self-similarity/roughness |
| 2 | `fractal dimension error` | +0.2801 | 0.2801 | Higher variance in boundary roughness |
| 3 | `worst fractal dimension` | +0.2753 | 0.2753 | Peak irregular boundary dimension |
| 4 | `mean radius` | -0.2339 | 0.2339 | Smaller mean nuclear radius |
| 5 | `compactness error` | +0.2327 | 0.2327 | Variance in cell compactness |

- **Generated Plot:** `output/task4_pca_loadings.png`

### Task 5: Logistic Regression with 5-Fold Cross-Validation Pipeline
To prevent data leakage, both `StandardScaler` and `PCA` are fitted strictly within the training folds of a 5-fold Stratified CV:

| Model | Dimensionality | Mean 5-Fold CV Accuracy | Std Dev ($\pm$) | Accuracy Range Across Folds |
|:---|:---:|:---:|:---:|:---:|
| **(a) Full Panel (All 30 Features)** | 30 features | **97.37%** | $\pm 1.66\%$ | 94.74% – 99.12% |
| **(b) Reduced PCA Panel ($k=7$)** | 7 components | **96.14%** | $\pm 1.53\%$ | 93.86% – 98.23% |

- **Performance Delta:** The 7-component panel experiences a minor accuracy reduction of only **1.23%**, while reducing data dimensionality by **76.7%** (from 30 down to 7).
- **Generated Plot:** `output/task5_model_cv_comparison.png`

---

## Follow-Up Questions (Detailed Responses)

### Q1. What share of variance does PC1 now explain, and which feature dominates it? Explain why standardisation changes the result so much.

1. **Variance Explained & Dominant Feature (Standardised):**
   - With standardisation, **PC1 explains 44.27% of the total variance**.
   - The feature with the highest loading on PC1 is **`mean concave points`** (loading = $+0.2609$), followed closely by `mean concavity` ($+0.2584$) and `worst concave points` ($+0.2509$).
   - Notice that no single feature overwhelmingly dominates PC1. Instead, multiple morphological features measuring nuclear concavity, contour irregularity, and size contribute balanced, moderate weights ($0.23$ to $0.26$).

2. **Contrast with Unstandardised PCA:**
   - Without standardisation, PC1 explains **98.20% of the total variance**, and is almost entirely dominated by **`worst area`** (absolute loading = $0.8521$) and **`mean area`** (loading = $0.5168$). All other 28 features (such as concavity, smoothness, and symmetry) receive loadings close to $0.00$.

3. **Why Standardisation Changes the Result So Drastically:**
   - PCA is an unsupervised technique that finds orthogonal linear combinations that maximize sample variance:
     $$\text{Var}(w^T X) = w^T \Sigma w$$
   - When features are unstandardised, features with inherently larger physical measurement scales have vastly larger raw numerical variances. In this dataset:
     - `worst area` variance is **$\approx 324,165$**
     - `mean area` variance is **$\approx 123,844$**
     - In contrast, `mean concavity` variance is **$\approx 0.006$** and `mean fractal dimension` is **$\approx 0.00005$**.
   - Because the variance of `area` is millions of times larger than that of `concavity`, an unstandardised PCA aligns the first principal axis almost entirely with cell area simply to maximize raw numerical spread.
   - **Standardisation ($z$-score scaling)** divides each feature by its standard deviation, setting all feature variances to exactly $1.0$. This places all 30 indicators on equal mathematical footing, allowing PCA to detect genuine biological correlations and multi-variable shape relationships rather than artifacts of measurement units ($\mu m^2$ vs dimensionless ratios).

---

### Q2. Would you recommend the reduced panel to the lab? Give one statistical and one practical reason, and say what you lose in interpretability.

**Recommendation:** **YES**, the reduced panel ($k=7$) is recommended for clinical laboratory diagnostic implementation (especially as a high-throughput primary diagnostic screen).

1. **Statistical Reason:**
   - **Dimensionality Reduction without Predictive Loss:** The full 30-feature panel contains high multicollinearity (e.g., radius, perimeter, and area are algebraically interdependent). Reducing 30 correlated features down to $k=7$ orthogonal components preserves **91.01% of total informational variance** while maintaining **96.14% cross-validation accuracy** (within $1.23\%$ of the 30-feature baseline). Moreover, the reduced model has a lower standard deviation across folds ($\pm 1.53\%$ vs $\pm 1.66\%$), demonstrating higher generalization stability and reduced risk of overfitting.

2. **Practical Reason:**
   - **Cost, Efficiency, and Operational Robustness:** In a hospital pathology workflow, measuring, imaging, segmenting, and conducting quality control for 30 distinct sub-nuclear markers takes significant computational time and increases laboratory turnaround latency. Each additional assay also carries a risk of measurement failure, noise, or missing values. A condensed diagnostic indicator system streamlines lab processing, decreases diagnostic turnaround time for patients, and cuts assay expenses.

3. **What You Lose in Interpretability:**
   - **Loss of Direct Biological/Clinical Meaning:**
     - In clinical oncology, pathologists and oncologists make treatment decisions based on direct, measurable physical observations (e.g., *"the mean cell radius exceeds $18\mu m$ and margins display irregular concavities"*).
     - Principal components are mathematical linear combinations:
       $$\text{PC}_1 = 0.261(\text{concave points}) + 0.258(\text{concavity}) + \dots + 0.237(\text{perimeter})$$
     - A transformed score such as $\text{PC}_1 = +2.48$ is an abstract mathematical coordinate. Clinicians cannot directly visualize or verify a "PC1 score" under a microscope, making it harder to explain specific tumor staging to patients or justify borderline decisions in medical-legal contexts.

---

## Files Included

- `practical11.py`: Full end-to-end Python script implementing Tasks 1–5, 5-fold cross-validation pipeline, and follow-up question analysis.
- `output/task2_scree_and_cumulative_variance.png`: Scree plot and cumulative variance plot.
- `output/task3_pc1_vs_pc2_diagnosis.png`: Scatter plot of biopsy samples on PC1 vs PC2 colored by diagnosis.
- `output/task4_pca_loadings.png`: Horizontal bar chart displaying the top 5 absolute loadings on PC1 and PC2.
- `output/task5_model_cv_comparison.png`: 5-fold CV accuracy comparison between full and reduced panels.

---

## How to Run

From the repository root:
```bash
python Anjani_Finalpractical/practical11.py
```
