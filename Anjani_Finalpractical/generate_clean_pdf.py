"""
Generates an 8-page clean, perfectly spaced PDF formatted in Times New Roman following Practical 5:
- Page 1: Mandatory Exam Instructions & Answers (Q1: Prompt, Q2: GitHub Link, Q3: Output Screenshots, Q4: Step Explanation Overview)
- Page 2: Step 1: Standardise 30 Features & Fit Full PCA (Input & Output)
- Page 3: Step 2: Scree Plot & Cumulative Explained Variance (+ Plot)
- Page 4: Step 3: Biopsy Samples on PC1 vs PC2 (+ Plot)
- Page 5: Step 4: Top 5 Absolute Loadings on PC1 and PC2 (+ Plot)
- Page 6: Step 5: 5-Fold Cross-Validation Logistic Regression Pipeline (+ Plot)
- Page 7: Follow-up Question 1: Variance Share, Dominance & Standardisation Impact
- Page 8: Follow-up Question 2: Lab Recommendation, Interpretability, Conclusion & Sign-Off
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"
from pathlib import Path
import shutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg

project_dir = Path(__file__).parent
output_dir = project_dir / "output"
pdf_path = project_dir / "Anjani_Finalpractical.pdf"
workspace_pdf_path = Path("/Users/anjanibharatchauhan/Documents/Developer/Statistics for DS/Anjani_Finalpractical.pdf")

print(f"Generating clean PDF at: {pdf_path}")

plt.rcParams["font.family"] = "serif"

def draw_header(ax, title_text, subtitle=None):
    ax.text(0.5, 0.96, title_text, ha="center", va="top", fontsize=14, fontweight="bold")
    if subtitle:
        ax.text(0.5, 0.925, subtitle, ha="center", va="top", fontsize=9.5, style="italic")
        ax.plot([0.08, 0.92], [0.90, 0.90], color="#222222", lw=1.2)
    else:
        ax.plot([0.15, 0.85], [0.91, 0.91], color="#222222", lw=1.2)

def draw_code_box(ax, y_top, label, code_str, height=0.30, font_size=8):
    ax.text(0.08, y_top, label, fontsize=10.5, fontweight="bold")
    box_y = y_top - height - 0.015
    rect = plt.Rectangle((0.08, box_y), 0.84, height, facecolor="#181818", edgecolor="#333333", zorder=2)
    ax.add_patch(rect)
    ax.text(0.10, y_top - 0.035, code_str, fontsize=font_size, family="monospace", color="#d4d4d4", va="top", zorder=3)
    return box_y

with PdfPages(pdf_path) as pdf:
    # -------------------------------------------------------------------------
    # PAGE 1: Exam Submission Instructions & Direct Answers (Q1 to Q4)
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    draw_header(ax, "PRACTICAL EXAM: SIMPLIFYING A CANCER DIAGNOSTIC PANEL", 
                "MSc Data Science | Shoolini University | Student: Anjani Bharat (Reg. No: PGD202563026)")
    
    sec1_title = "SECTION 1: EXAM SUBMISSION REQUIREMENTS & ANSWERS"
    ax.text(0.08, 0.87, sec1_title, fontsize=11, fontweight="bold")
    ax.plot([0.08, 0.92], [0.855, 0.855], color="#888888", lw=0.8)

    q1_text = (
        "Q.1) You are required to submit the prompt you used to write the code and find out the result.\n"
        "Ans. Below is the exact prompt I formulated and utilized to generate the analytical code and results:"
    )
    ax.text(0.08, 0.84, q1_text, fontsize=9.2, va="top", linespacing=1.25)

    prompt_str = (
        '"""\n'
        'PROMPT:\n'
        'Act as an expert data scientist and biostatistician. Write an end-to-end Python script using the\n'
        'Breast Cancer Wisconsin Diagnostic dataset from scikit-learn to simplify a diagnostic panel with PCA:\n'
        '1. Standardise the 30 cell nucleus biopsy features using StandardScaler and fit full 30-component PCA.\n'
        '2. Plot a scree plot and cumulative variance curve; report components needed for >= 90% and >= 95% variance.\n'
        '3. Project samples onto PC1 vs PC2 and scatter plot colored by tumor diagnosis (Malignant vs Benign).\n'
        '4. Identify and visualize the top 5 features with the largest absolute loadings on PC1 and PC2.\n'
        '5. Build an sklearn Pipeline (StandardScaler + PCA(k=7) + LogisticRegression) with 5-fold cross-validation\n'
        '   accuracy to compare against the full 30-feature baseline without data leakage.\n'
        '6. Address analytical questions on why standardisation changes variance distribution, and evaluate clinical\n'
        '   recommendations for adopting the reduced panel in a diagnostic hospital laboratory.\n'
        'Save all plots at 300 DPI in output/ directory.\n'
        '"""'
    )
    y_box1 = draw_code_box(ax, 0.77, "SUBMITTED PROMPT", prompt_str, height=0.18, font_size=7.2)

    q2_text = (
        "Q.2) Provide the link of the Github where you have publish your code.\n"
        "Ans. I have published the complete code, documentation, and outputs in my GitHub repository:\n"
        "   • Main Repository: https://github.com/bharatanjani512-hub/Statistics-for-Data-Science\n"
        "   • Practical 11 Directory: https://github.com/bharatanjani512-hub/Statistics-for-Data-Science/tree/main/Anjani_Finalpractical\n"
        "   • Execution Script: practical11.py"
    )
    ax.text(0.08, y_box1 - 0.02, q2_text, fontsize=9.2, va="top", linespacing=1.25)

    q3_text = (
        "Q.3) Provide the screenshots of the outputs.\n"
        "Ans. All visual output plots generated by practical11.py have been rendered at 300 DPI and embedded\n"
        "directly in this report:\n"
        "   1. Scree Plot & Cumulative Explained Variance Plot -> Embedded in Step 2 (Page 3)\n"
        "   2. 2D Scatter Projection of Biopsies on PC1 vs PC2 -> Embedded in Step 3 (Page 4)\n"
        "   3. Top 5 Absolute Feature Loadings on PC1 & PC2 Bar Chart -> Embedded in Step 4 (Page 5)\n"
        "   4. 5-Fold Cross-Validation Accuracy Comparison Bar Chart -> Embedded in Step 5 (Page 6)\n"
        "   5. Detailed numerical console outputs -> Embedded in each corresponding Step."
    )
    ax.text(0.08, y_box1 - 0.14, q3_text, fontsize=9.2, va="top", linespacing=1.25)

    q4_text = (
        "Q.4) Please provide the explaination of each step done.\n"
        "Ans. In Section 2 of this report (Pages 2–8), I have provided a comprehensive first-person explanation of\n"
        "each step done, including mathematical formulation, Python code inputs, terminal outputs, output screenshots,\n"
        "and detailed answers to the clinical and analytical follow-up questions."
    )
    ax.text(0.08, y_box1 - 0.28, q4_text, fontsize=9.2, va="top", linespacing=1.25)

    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------------------
    # PAGE 2: Step 1: Standardise 30 Features & Fit Full PCA
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    draw_header(ax, "SECTION 2: STEP-BY-STEP PRACTICAL EXECUTION & ANALYSIS")
    
    q1_text = (
        "Step 1: Standardise 30 Features of Cell Nuclei Biopsies & Fit Full PCA\n\n"
        "Ans. The 30 cell nucleus features operate on drastically different physical units (e.g.,\n"
        "mean area in hundreds of square micrometers vs. fractal dimension < 0.1). Using\n"
        "StandardScaler, I standardized each feature to zero mean (μ = 0) and unit variance\n"
        "(σ = 1). I then fitted a full 30-component PCA model to capture the complete orthogonal\n"
        "variance structure of the dataset."
    )
    ax.text(0.08, 0.85, q1_text, fontsize=10.5, va="top", linespacing=1.35)
    
    code1 = (
        "# ============================================================\n"
        "# STEP 1: STANDARDISE 30 FEATURES & FIT FULL PCA\n"
        "# ============================================================\n"
        "from sklearn.datasets import load_breast_cancer\n"
        "from sklearn.preprocessing import StandardScaler\n"
        "from sklearn.decomposition import PCA\n\n"
        "data = load_breast_cancer(as_frame=True)\n"
        "X, y = data.data, data.target\n\n"
        "scaler = StandardScaler()\n"
        "X_scaled = scaler.fit_transform(X)\n\n"
        "pca = PCA(n_components=X.shape[1], random_state=42)\n"
        "X_pca = pca.fit_transform(X_scaled)\n"
        "print('Transformed coordinates matrix shape:', X_pca.shape)"
    )
    y_after_code = draw_code_box(ax, 0.62, "INPUT", code1, height=0.28)
    
    out1 = (
        "Total biopsy samples: 569\n"
        "Total cell nuclei features: 30\n"
        "Standardisation complete: Mean = 0.0, Standard Deviation = 1.0.\n"
        "PCA fitted successfully with all 30 components.\n"
        "Transformed coordinates matrix shape: (569, 30)"
    )
    draw_code_box(ax, y_after_code - 0.03, "OUTPUT", out1, height=0.15)
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------------------
    # PAGE 3: Step 2: Scree Plot & Cumulative Explained Variance
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    q2_text = (
        "Step 2: Scree Plot & Cumulative Explained Variance Analysis\n\n"
        "Ans. In my variance decomposition, PC1 explains 44.27% of the total variance, and\n"
        "PC2 explains 18.97% (63.24% combined).\n"
        "• To explain at least 90% of the variance, I found that k = 7 components are required\n"
        "  (explaining 91.01%).\n"
        "• To explain at least 95% of the variance, I found that k = 10 components are required\n"
        "  (explaining 95.16%)."
    )
    ax.text(0.08, 0.95, q2_text, fontsize=10.5, va="top", linespacing=1.35)
    
    code2 = (
        "explained_var_ratio = pca.explained_variance_ratio_\n"
        "cumulative_var_ratio = np.cumsum(explained_var_ratio)\n"
        "k_90 = int(np.argmax(cumulative_var_ratio >= 0.90) + 1)\n"
        "k_95 = int(np.argmax(cumulative_var_ratio >= 0.95) + 1)\n"
        "print(f'k for >= 90% variance: {k_90} ({cumulative_var_ratio[k_90-1]*100:.2f}%)')\n"
        "print(f'k for >= 95% variance: {k_95} ({cumulative_var_ratio[k_95-1]*100:.2f}%)')"
    )
    y_after_code = draw_code_box(ax, 0.72, "INPUT", code2, height=0.15)
    
    ax.text(0.08, y_after_code - 0.03, "OUTPUT SCREENSHOT", fontsize=11, fontweight="bold")
    img2 = mpimg.imread(output_dir / "task2_scree_and_cumulative_variance.png")
    ax_img2 = fig.add_axes([0.08, 0.05, 0.84, 0.43])
    ax_img2.imshow(img2)
    ax_img2.axis("off")
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------------------
    # PAGE 4: Step 3: Biopsy Samples on PC1 vs PC2
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    q3_text = (
        "Step 3: 2D Biopsy Projection on PC1 vs PC2 (Coloured by Diagnosis)\n\n"
        "Ans. When I projected the 569 biopsy samples onto the first two principal component\n"
        "axes, I observed a clear separation between malignant and benign tumors along PC1.\n"
        "Malignant biopsies concentrate heavily on positive PC1 scores (higher nuclear size,\n"
        "severe concavity, irregularity), while benign biopsies cluster on negative PC1 scores."
    )
    ax.text(0.08, 0.95, q3_text, fontsize=10.5, va="top", linespacing=1.35)
    
    code3 = (
        "plt.figure(figsize=(9, 7))\n"
        "mask_malignant = (y == 0)\n"
        "mask_benign = (y == 1)\n"
        "plt.scatter(X_pca[mask_malignant, 0], X_pca[mask_malignant, 1],\n"
        "            c='#d62728', marker='x', s=65, label='Malignant (y=0)')\n"
        "plt.scatter(X_pca[mask_benign, 0], X_pca[mask_benign, 1],\n"
        "            c='#1f77b4', marker='o', s=55, label='Benign (y=1)')\n"
        "plt.title('Biopsy Samples on PC1 vs PC2')\n"
        "plt.savefig('output/task3_pc1_vs_pc2_diagnosis.png')"
    )
    y_after_code = draw_code_box(ax, 0.74, "INPUT", code3, height=0.19)
    
    ax.text(0.08, y_after_code - 0.03, "OUTPUT SCREENSHOT", fontsize=11, fontweight="bold")
    img3 = mpimg.imread(output_dir / "task3_pc1_vs_pc2_diagnosis.png")
    ax_img3 = fig.add_axes([0.15, 0.05, 0.70, 0.43])
    ax_img3.imshow(img3)
    ax_img3.axis("off")
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------------------
    # PAGE 5: Step 4: Top 5 Absolute Loadings on PC1 and PC2
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    q4_text = (
        "Step 4: Top 5 Features with Largest Absolute Loadings on PC1 and PC2\n\n"
        "Ans. In my loading analysis, PC1 is primarily driven by cell shape concavity and boundary\n"
        "irregularity, while PC2 is driven by fractal dimension and fine texture variation.\n\n"
        "Top 5 Features on PC1:\n"
        "  1. mean concave points (+0.2609)        4. mean compactness (+0.2393)\n"
        "  2. mean concavity (+0.2584)             5. worst perimeter (+0.2366)\n"
        "  3. worst concave points (+0.2509)\n\n"
        "Top 5 Features on PC2:\n"
        "  1. mean fractal dimension (+0.3666)     4. mean radius (-0.2339)\n"
        "  2. fractal dimension error (+0.2801)    5. compactness error (+0.2327)\n"
        "  3. worst fractal dimension (+0.2753)"
    )
    ax.text(0.08, 0.95, q4_text, fontsize=9.8, va="top", linespacing=1.28)
    
    code4 = (
        "loadings = pd.DataFrame(pca.components_.T, index=X.columns,\n"
        "                        columns=[f'PC{i+1}' for i in range(30)])\n"
        "pc1_top5 = loadings['PC1'].abs().sort_values(ascending=False).head(5)\n"
        "pc2_top5 = loadings['PC2'].abs().sort_values(ascending=False).head(5)"
    )
    y_after_code = draw_code_box(ax, 0.63, "INPUT", code4, height=0.13)
    
    ax.text(0.08, y_after_code - 0.03, "OUTPUT SCREENSHOT", fontsize=11, fontweight="bold")
    img4 = mpimg.imread(output_dir / "task4_pca_loadings.png")
    ax_img4 = fig.add_axes([0.08, 0.05, 0.84, 0.38])
    ax_img4.imshow(img4)
    ax_img4.axis("off")
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------------------
    # PAGE 6: Step 5: 5-Fold Cross-Validation Logistic Regression Pipeline
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    q5_text = (
        "Step 5: Logistic Regression Pipeline (5-Fold CV Accuracy Comparison)\n\n"
        "Ans. To prevent data leakage, I encapsulated both StandardScaler and PCA within\n"
        "sklearn.pipeline.Pipeline, fitting them strictly on the training partition of each fold:\n"
        "• Model (a) All 30 Standardised Features: 97.37% (± 1.66%)\n"
        "• Model (b) Reduced PCA Panel (First 7 Components): 96.14% (± 1.53%)\n"
        "• Performance Delta: I observed only a minor accuracy reduction of 1.23%, while\n"
        "  successfully reducing data dimensionality by 76.7% (from 30 down to 7 features)."
    )
    ax.text(0.08, 0.95, q5_text, fontsize=10, va="top", linespacing=1.35)
    
    code5 = (
        "pipeline_all = Pipeline([('scaler', StandardScaler()),\n"
        "                         ('classifier', LogisticRegression(max_iter=1000, random_state=42))])\n"
        "cv_all = cross_val_score(pipeline_all, X, y, cv=cv, scoring='accuracy')\n\n"
        "pipeline_pca = Pipeline([('scaler', StandardScaler()),\n"
        "                         ('pca', PCA(n_components=k_90, random_state=42)),\n"
        "                         ('classifier', LogisticRegression(max_iter=1000, random_state=42))])\n"
        "cv_pca = cross_val_score(pipeline_pca, X, y, cv=cv, scoring='accuracy')"
    )
    y_after_code = draw_code_box(ax, 0.69, "INPUT", code5, height=0.19)
    
    ax.text(0.08, y_after_code - 0.03, "OUTPUT SCREENSHOT", fontsize=11, fontweight="bold")
    img5 = mpimg.imread(output_dir / "task5_model_cv_comparison.png")
    ax_img5 = fig.add_axes([0.18, 0.05, 0.64, 0.38])
    ax_img5.imshow(img5)
    ax_img5.axis("off")
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------------------
    # PAGE 7: Follow-up Question 1
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    
    q6_text = (
        "Follow-up Question 1: What share of variance does PC1 now explain, and which\n"
        "feature dominates it? Explain why standardisation changes the result so much.\n\n"
        "Ans.\n"
        "1. Share of Variance & Dominant Feature (Standardised):\n"
        "   After standardising the dataset, I found that PC1 explains 44.27% of the total variance.\n"
        "   The feature with the highest loading on PC1 is mean concave points (+0.2609), followed\n"
        "   closely by mean concavity (+0.2584) and worst concave points (+0.2509). I noticed that no\n"
        "   single feature overwhelmingly dominates PC1; multiple contour irregularity metrics\n"
        "   contribute balanced weights (0.23 to 0.26).\n\n"
        "2. Contrast with Unstandardised PCA:\n"
        "   When I evaluated unstandardised PCA, PC1 accounted for 98.20% of the variance and was\n"
        "   overwhelmingly dominated by worst area (0.8521) and mean area (0.5168), while the other 28\n"
        "   features received loadings close to 0.00.\n\n"
        "3. Why Standardisation Changes the Result So Much:\n"
        "   PCA seeks orthogonal axes that maximize sample variance: Var(w^T X) = w^T Σ w. Without\n"
        "   standardisation, features with large physical measurement scales naturally exhibit enormous\n"
        "   numerical variances (in this dataset, worst area variance is ≈ 324,165, whereas concavity variance\n"
        "   is only ≈ 0.006). Because area has a variance millions of times larger than concavity, an\n"
        "   unstandardised PCA aligns almost entirely with cell area simply due to units of measurement\n"
        "   (μm² vs. dimensionless ratios). By applying standardisation (z-score scaling), I scaled all\n"
        "   feature variances to 1.0, enabling PCA to discover true biological covariation across all 30\n"
        "   indicators rather than measurement unit artifacts."
    )
    ax.text(0.08, 0.94, q6_text, fontsize=9.8, va="top", linespacing=1.35)
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------------------
    # PAGE 8: Follow-up Question 2, Conclusion & Sign-Off
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 11), dpi=150)
    ax.axis("off")
    
    q7_text = (
        "Follow-up Question 2: Would you recommend the reduced panel to the lab? Give\n"
        "one statistical and one practical reason, and say what you lose in interpretability.\n\n"
        "Ans. Yes, I would recommend the reduced panel (k = 7) to the hospital laboratory.\n\n"
        "1. Statistical Reason:\n"
        "   In my cross-validation experiments, the reduced panel with k = 7 components retains\n"
        "   91.01% of the total informational variance across all 30 features, while achieving a 96.14%\n"
        "   5-fold cross-validation accuracy—nearly identical to the full 30-feature baseline of 97.37%\n"
        "   (a negligible drop of just 1.23%). Furthermore, I observed lower standard deviation across\n"
        "   folds (±1.53% vs ±1.66%), demonstrating that eliminating high multicollinearity stabilizes\n"
        "   model performance and reduces the risk of overfitting.\n\n"
        "2. Practical Reason:\n"
        "   From a practical laboratory operations perspective, measuring, imaging, and performing\n"
        "   quality control on 30 separate nuclear morphology assays for every biopsy is costly,\n"
        "   computationally demanding, and increases the risk of measurement noise or assay failure.\n"
        "   In my assessment, reducing the panel to 7 combined indicators significantly lowers test\n"
        "   expenses, streamlines diagnostic workflows, and accelerates turnaround times for patients\n"
        "   awaiting critical biopsy results.\n\n"
        "3. What You Lose in Interpretability:\n"
        "   What I lose in this reduction is direct clinical interpretability. Pathologists make clinical\n"
        "   decisions using tangible physical measurements (such as 'mean cell radius exceeds 18 μm').\n"
        "   Because principal components are mathematical linear combinations (weighted sums) of all\n"
        "   30 features:\n"
        "       PC1 = 0.261(concave points) + 0.258(concavity) + ... + 0.237(perimeter)\n"
        "   A transformed coordinate such as PC1 = +2.48 has no direct histological meaning under a\n"
        "   microscope, making it harder for clinicians to explain specific diagnostic reasoning to patients."
    )
    ax.text(0.08, 0.94, q7_text, fontsize=9.8, va="top", linespacing=1.35)
    
    conc_text = (
        "Conclusion\n"
        "Principal Component Analysis successfully simplified the 30-feature breast cancer diagnostic\n"
        "panel into 7 orthogonal components while retaining 91.01% of total variance and 96.14% cross-\n"
        "validation accuracy. Standardisation was proven critical to avoid artificial dominance by cell\n"
        "area. The reduced panel is statistically robust and practically advantageous for high-throughput\n"
        "laboratory diagnosis."
    )
    ax.text(0.08, 0.30, conc_text, fontsize=10.2, va="top", linespacing=1.35)
    
    signoff = (
        "Submitted by: Anjani Bharat\n"
        "Registration Number: PGD202563026\n"
        "Degree: MSc Data Science | Shoolini University"
    )
    ax.text(0.08, 0.12, signoff, fontsize=11, va="top", linespacing=1.45, fontweight="bold")
    
    pdf.savefig(fig)
    plt.close()

# Copy to root workspace
shutil.copy2(pdf_path, workspace_pdf_path)
print(f"Generated clean Practical 5 styled PDF: {pdf_path}")
print(f"Copied to workspace root: {workspace_pdf_path}")
