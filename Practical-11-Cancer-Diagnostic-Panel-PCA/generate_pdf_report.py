"""
Script to generate the final, comprehensive Practical Exam Submission PDF.
Includes:
1. Prompt Used
2. GitHub Repository Link
3. Screenshots & Visual Outputs (Embedded High-Res Plots)
4. Step-by-Step Technical Explanations and Follow-up Questions (Q1 & Q2)
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib_cache"
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg

project_dir = Path(__file__).parent
output_dir = project_dir / "output"
pdf_path = project_dir / "Practical_Exam_Submission_Report.pdf"

print(f"Generating submission PDF at: {pdf_path}")

with PdfPages(pdf_path) as pdf:
    # -------------------------------------------------------------
    # PAGE 1: TITLE & COVER / OVERVIEW / PROMPT / GITHUB LINK
    # -------------------------------------------------------------
    fig = plt.figure(figsize=(8.5, 11), dpi=150)
    fig.patch.set_facecolor("#ffffff")
    
    # Title box
    plt.text(0.5, 0.94, "SHOOLINI UNIVERSITY", ha="center", va="center", fontsize=14, fontweight="bold", color="#1a365d")
    plt.text(0.5, 0.915, "MSc Data Science | Statistics for Data Science", ha="center", va="center", fontsize=11, color="#4a5568")
    plt.text(0.5, 0.88, "PRACTICAL EXAM SUBMISSION REPORT", ha="center", va="center", fontsize=16, fontweight="bold", color="#2b6cb0")
    plt.text(0.5, 0.85, "Simplifying a Cancer Diagnostic Panel (PCA & Clinical Dimension Reduction)", ha="center", va="center", fontsize=11, style="italic", color="#2d3748")
    
    # Meta box
    meta_box = (
        "Student Name: Anjani Bharat                     Date: November 2026\n"
        "Course: MSc Data Science                        Submission Type: Individual Assignment\n"
        "GitHub Link: https://github.com/bharatanjani512-hub/Statistics-for-Data-Science"
    )
    plt.text(0.08, 0.77, meta_box, fontsize=9.5, family="monospace", bbox=dict(boxstyle="round,pad=0.6", facecolor="#edf2f7", edgecolor="#cbd5e0", alpha=0.9))
    
    # Section 1: Prompt
    plt.text(0.08, 0.71, "1. PROMPT USED FOR IMPLEMENTATION", fontsize=12, fontweight="bold", color="#1a365d")
    prompt_text = (
        "\"A hospital lab measures 30 features of cell nuclei from breast-tissue biopsies.\n"
        "The lab wants to know whether a few combined indicators can replace the full panel without\n"
        "losing the ability to tell malignant from benign tumours.\n\n"
        "Dataset: sklearn.datasets.load_breast_cancer(as_frame=True); X, y = data.data, data.target\n"
        "Tasks:\n"
        " 1. Standardise the 30 features and fit PCA with all components.\n"
        " 2. Draw a scree plot and a cumulative explained-variance plot. Report how many components\n"
        "    explain at least 90% and 95% of the variance.\n"
        " 3. Plot the samples on PC1 vs PC2, coloured by diagnosis.\n"
        " 4. Print the five features with the largest absolute loadings on PC1 and on PC2.\n"
        " 5. Train a logistic regression (5-fold CV accuracy) on (a) all 30 standardised features\n"
        "    and (b) only the first k components, where k gives 90% variance. Fit the scaler and\n"
        "    PCA inside a Pipeline so there is no leakage.\n"
        " Follow-up Questions:\n"
        "  Q1: What share of variance does PC1 now explain, and which feature dominates it?\n"
        "      Explain why standardisation changes the result so much.\n"
        "  Q2: Would you recommend the reduced panel to the lab? Give one statistical and one\n"
        "      practical reason, and say what you lose in interpretability.\""
    )
    plt.text(0.08, 0.47, prompt_text, fontsize=8.5, family="monospace", va="top", bbox=dict(boxstyle="round,pad=0.6", facecolor="#f7fafc", edgecolor="#e2e8f0"))
    
    # Section 2: GitHub Repository Link
    plt.text(0.08, 0.44, "2. GITHUB REPOSITORY LINK", fontsize=12, fontweight="bold", color="#1a365d")
    git_text = (
        "Repository URL: https://github.com/bharatanjani512-hub/Statistics-for-Data-Science\n"
        "Practical Folder: /Practical-11-Cancer-Diagnostic-Panel-PCA\n"
        "Main Script: practical11.py\n"
        "Documentation: README.md (Comprehensive report and visual outputs)"
    )
    plt.text(0.08, 0.35, git_text, fontsize=9.5, family="monospace", va="top", bbox=dict(boxstyle="round,pad=0.6", facecolor="#edf2f7", edgecolor="#cbd5e0"))
    
    # Section 3: Summary of Numerical Findings
    plt.text(0.08, 0.31, "3. SUMMARY OF KEY EXPERIMENTAL FINDINGS", fontsize=12, fontweight="bold", color="#1a365d")
    summary_text = (
        "• Total Biopsy Samples: 569 (212 Malignant, 357 Benign) across 30 morphological features.\n"
        "• Standardised PC1 explains 44.27% variance; PC2 explains 18.97% variance (Total 63.24%).\n"
        "• 90% Variance Threshold: Requires k = 7 components (explains 91.01% of variance).\n"
        "• 95% Variance Threshold: Requires k = 10 components (explains 95.16% of variance).\n"
        "• Model (a) Full 30 Standardised Features 5-Fold CV Accuracy: 97.37% (±1.66%)\n"
        "• Model (b) Reduced k=7 PCA Panel 5-Fold CV Accuracy:         96.14% (±1.53%)\n"
        "• Accuracy Difference: Only 1.23% drop despite reducing dimensionality by 76.7%!"
    )
    plt.text(0.08, 0.16, summary_text, fontsize=9, va="top", bbox=dict(boxstyle="round,pad=0.6", facecolor="#f0fff4", edgecolor="#9ae6b4"))
    
    plt.text(0.5, 0.04, "Page 1 of 4", ha="center", fontsize=9, color="#718096")
    plt.axis("off")
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------
    # PAGE 2: VISUAL OUTPUTS (TASKS 2 & 3)
    # -------------------------------------------------------------
    fig = plt.figure(figsize=(8.5, 11), dpi=150)
    plt.text(0.5, 0.96, "3. VISUAL OUTPUTS & PLOTS (PART 1)", ha="center", fontsize=14, fontweight="bold", color="#1a365d")
    
    # Task 2 plot
    plt.text(0.08, 0.92, "Task 2: Scree Plot & Cumulative Explained Variance Plot", fontsize=11, fontweight="bold", color="#2b6cb0")
    img2 = mpimg.imread(output_dir / "task2_scree_and_cumulative_variance.png")
    ax2 = fig.add_axes([0.08, 0.54, 0.84, 0.35])
    ax2.imshow(img2)
    ax2.axis("off")
    
    # Task 3 plot
    plt.text(0.08, 0.49, "Task 3: Biopsy Samples on PC1 vs PC2 Coloured by Diagnosis", fontsize=11, fontweight="bold", color="#2b6cb0")
    img3 = mpimg.imread(output_dir / "task3_pc1_vs_pc2_diagnosis.png")
    ax3 = fig.add_axes([0.15, 0.08, 0.70, 0.38])
    ax3.imshow(img3)
    ax3.axis("off")
    
    plt.text(0.5, 0.03, "Page 2 of 4", ha="center", fontsize=9, color="#718096")
    plt.axis("off")
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------
    # PAGE 3: VISUAL OUTPUTS (TASKS 4 & 5)
    # -------------------------------------------------------------
    fig = plt.figure(figsize=(8.5, 11), dpi=150)
    plt.text(0.5, 0.96, "3. VISUAL OUTPUTS & PLOTS (PART 2)", ha="center", fontsize=14, fontweight="bold", color="#1a365d")
    
    # Task 4 plot
    plt.text(0.08, 0.92, "Task 4: Five Features with Largest Absolute Loadings on PC1 & PC2", fontsize=11, fontweight="bold", color="#2b6cb0")
    img4 = mpimg.imread(output_dir / "task4_pca_loadings.png")
    ax4 = fig.add_axes([0.08, 0.54, 0.84, 0.35])
    ax4.imshow(img4)
    ax4.axis("off")
    
    # Task 5 plot
    plt.text(0.08, 0.49, "Task 5: 5-Fold Cross-Validation Accuracy Comparison (Full vs Reduced)", fontsize=11, fontweight="bold", color="#2b6cb0")
    img5 = mpimg.imread(output_dir / "task5_model_cv_comparison.png")
    ax5 = fig.add_axes([0.18, 0.08, 0.64, 0.38])
    ax5.imshow(img5)
    ax5.axis("off")
    
    plt.text(0.5, 0.03, "Page 3 of 4", ha="center", fontsize=9, color="#718096")
    plt.axis("off")
    pdf.savefig(fig)
    plt.close()

    # -------------------------------------------------------------
    # PAGE 4: DETAILED STEP-BY-STEP EXPLANATION & FOLLOW-UP QUESTIONS
    # -------------------------------------------------------------
    fig = plt.figure(figsize=(8.5, 11), dpi=150)
    plt.text(0.5, 0.96, "4. DETAILED STEP-BY-STEP EXPLANATIONS & FOLLOW-UP QUESTIONS", ha="center", fontsize=13, fontweight="bold", color="#1a365d")
    
    # Task Explanations
    tasks_exp = (
        "STEP-BY-STEP METHODOLOGY:\n"
        "• Task 1 (Standardisation): The 30 features measure different physical properties (area in 1000s of um^2 vs.\n"
        "  concavity < 0.1). StandardScaler transforms all features to mu=0, sigma=1, ensuring scale invariance.\n"
        "• Task 2 (Variance Analysis): Scree and cumulative plots identify the elbow and variance thresholds. While\n"
        "  PC1 explains 44.27% and PC2 explains 18.97%, k=7 components reach 91.01% (exceeding the 90% goal).\n"
        "• Task 3 (Diagnostic Separation): Biopsies plotted on PC1-PC2 reveal strong natural clustering. Malignant\n"
        "  cells cluster on high positive PC1 values (large, irregular nuclei), while benign cells occupy negative PC1.\n"
        "• Task 4 (Loadings Analysis): PC1 is primarily driven by nuclear shape concavity ('mean concave points' +0.2609,\n"
        "  'mean concavity' +0.2584). PC2 is driven by texture irregularity ('mean fractal dimension' +0.3666).\n"
        "• Task 5 (Leakage-Free Pipeline CV): Using sklearn.pipeline.Pipeline, both StandardScaler and PCA are fitted\n"
        "  exclusively on the training partition of each fold. Full 30 features achieve 97.37% accuracy, while the\n"
        "  reduced k=7 PCA panel achieves 96.14% accuracy (an insignificant 1.23% difference with lower variance)."
    )
    plt.text(0.08, 0.91, tasks_exp, fontsize=8.2, va="top", family="sans-serif", bbox=dict(boxstyle="round,pad=0.5", facecolor="#edf2f7", edgecolor="#cbd5e0"))
    
    # Follow-up Q1
    q1_text = (
        "RESPONSE TO FOLLOW-UP QUESTION 1:\n"
        "Q: What share of variance does PC1 now explain, and which feature dominates it?\n"
        "   Explain why standardisation changes the result so much.\n\n"
        "Answer:\n"
        "1. Standardised PC1 explains 44.27% of the total variance.\n"
        "2. The leading feature on PC1 is 'mean concave points' (+0.2609), followed closely by 'mean concavity'\n"
        "   (+0.2584) and 'worst concave points' (+0.2509). No single feature heavily dominates; instead,\n"
        "   multiple shape and contour irregularity metrics contribute balanced loadings (0.23 to 0.26).\n"
        "3. Standardisation Impact: In unstandardised PCA, PC1 explained 98.20% of the variance and was\n"
        "   overwhelmingly dominated by 'worst area' (0.8521) and 'mean area' (0.5168). This occurs because PCA\n"
        "   maximizes raw numerical variance: the variance of 'area' (~324,000) is millions of times larger than\n"
        "   'concavity' (~0.005). Standardisation equalizes variances to 1.0, enabling PCA to capture true biological\n"
        "   covariation and correlation patterns rather than arbitrary measurement units (um^2 vs ratios)."
    )
    plt.text(0.08, 0.65, q1_text, fontsize=8.2, va="top", family="sans-serif", bbox=dict(boxstyle="round,pad=0.5", facecolor="#ebf8ff", edgecolor="#bee3f8"))
    
    # Follow-up Q2
    q2_text = (
        "RESPONSE TO FOLLOW-UP QUESTION 2:\n"
        "Q: Would you recommend the reduced panel to the lab? Give one statistical and one\n"
        "   practical reason, and say what you lose in interpretability.\n\n"
        "Answer:\n"
        "Recommendation: YES, the reduced panel (k=7) is strongly recommended for diagnostic screening.\n\n"
        "1. Statistical Reason: The 7-component panel retains 91.01% of total informational variance across all 30\n"
        "   features while sustaining a 96.14% 5-fold cross-validation accuracy—nearly identical to the full panel's\n"
        "   97.37% (a minor 1.23% drop). Crucially, the reduced model shows lower variance across folds (±1.53% vs.\n"
        "   ±1.66%), eliminating collinearity and mitigating overfitting risks.\n\n"
        "2. Practical Reason: Measuring and performing quality control on 30 separate morphological features per\n"
        "   biopsy is time-consuming, expensive, and increases the likelihood of measurement noise or assay failure.\n"
        "   Consolidating down to 7 orthogonal indicators streamlines high-throughput processing, lowers laboratory\n"
        "   costs, and accelerates turnaround times for patients awaiting critical biopsy results.\n\n"
        "3. Loss in Interpretability: Principal components are linear combinations (weighted sums) of all 30 features.\n"
        "   Pathologists understand direct physical cytology metrics (e.g., 'cell radius exceeds 18 um'). In contrast,\n"
        "   a synthetic composite score like 'PC1 = +2.4' carries no direct intuitive histological meaning,\n"
        "   making it harder for clinicians to explain specific diagnostic reasoning to patients or in legal contexts."
    )
    plt.text(0.08, 0.35, q2_text, fontsize=8.2, va="top", family="sans-serif", bbox=dict(boxstyle="round,pad=0.5", facecolor="#fffaf0", edgecolor="#feebc8"))
    
    plt.text(0.5, 0.03, "Page 4 of 4", ha="center", fontsize=9, color="#718096")
    plt.axis("off")
    pdf.savefig(fig)
    plt.close()

print(f"Submission PDF successfully generated at: {pdf_path}")
