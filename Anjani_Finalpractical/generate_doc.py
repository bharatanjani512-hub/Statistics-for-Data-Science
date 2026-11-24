import base64
from pathlib import Path
import shutil

repo_dir = Path(__file__).parent
output_dir = repo_dir / "output"
doc_path = repo_dir / "Anjani_Finalpractical.doc"
workspace_doc_path = Path("/Users/anjanibharatchauhan/Documents/Developer/Statistics for DS/Anjani_Finalpractical.doc")

def get_b64(img_name):
    p = output_dir / img_name
    with open(p, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

img2_b64 = get_b64("task2_scree_and_cumulative_variance.png")
img3_b64 = get_b64("task3_pc1_vs_pc2_diagnosis.png")
img4_b64 = get_b64("task4_pca_loadings.png")
img5_b64 = get_b64("task5_model_cv_comparison.png")

template = """<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
<head>
<meta charset="utf-8">
<title>PRACTICAL 11 - SIMPLIFYING A CANCER DIAGNOSTIC PANEL</title>
<!--[if gte mso 9]>
<xml>
<w:WordDocument>
<w:View>Print</w:View>
<w:Zoom>100</w:Zoom>
<w:DoNotOptimizeForBrowser/>
</w:WordDocument>
</xml>
<![endif]-->
<style>
  @page {
    size: 8.5in 11.0in;
    margin: 1.0in 1.0in 1.0in 1.0in;
  }
  body {
    font-family: 'Times New Roman', Times, serif;
    color: #000000;
    line-height: 1.45;
    font-size: 12pt;
    margin: 0 auto;
    max-width: 800px;
    padding: 20px;
  }
  h1 {
    font-family: 'Times New Roman', Times, serif;
    font-size: 16pt;
    font-weight: bold;
    text-align: center;
    text-decoration: underline;
    margin-top: 10pt;
    margin-bottom: 10pt;
    text-transform: uppercase;
    line-height: 1.3;
  }
  .subtitle {
    text-align: center;
    font-size: 11pt;
    font-style: italic;
    margin-bottom: 20pt;
  }
  h2 {
    font-family: 'Times New Roman', Times, serif;
    font-size: 13pt;
    font-weight: bold;
    border-bottom: 1.5px solid #000;
    padding-bottom: 4pt;
    margin-top: 20pt;
    margin-bottom: 12pt;
    text-transform: uppercase;
  }
  .question {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 14pt;
    margin-bottom: 6pt;
  }
  .answer {
    font-size: 12pt;
    margin-top: 4pt;
    margin-bottom: 10pt;
    text-align: justify;
  }
  .label-input {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 12pt;
    margin-bottom: 4pt;
    text-transform: uppercase;
  }
  .label-output {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 14pt;
    margin-bottom: 4pt;
    text-transform: uppercase;
  }
  .code-block {
    background-color: #181818;
    color: #d4d4d4;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9.5pt;
    line-height: 1.4;
    padding: 10pt 14pt;
    border-radius: 4pt;
    margin: 6pt 0 12pt 0;
    white-space: pre-wrap;
  }
  .code-block .keyword { color: #569cd6; font-weight: bold; }
  .code-block .comment { color: #6a9955; font-style: italic; }
  .code-block .string { color: #ce9178; }
  .output-box {
    background-color: #181818;
    color: #f1f1f1;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 9.5pt;
    line-height: 1.4;
    padding: 10pt 14pt;
    border-radius: 4pt;
    margin: 6pt 0 14pt 0;
    white-space: pre-wrap;
  }
  .img-container {
    text-align: center;
    margin: 10pt 0 16pt 0;
  }
  .img-container img {
    max-width: 95%;
    height: auto;
    border: 1px solid #999999;
  }
  .conclusion-header {
    font-size: 13pt;
    font-weight: bold;
    margin-top: 26pt;
    margin-bottom: 8pt;
  }
  .conclusion-text {
    font-size: 12pt;
    margin-bottom: 24pt;
    text-align: justify;
  }
  .sign-off {
    font-size: 12pt;
    font-weight: bold;
    line-height: 1.6;
    margin-top: 16pt;
  }
  .page-break {
    page-break-after: always;
  }
</style>
</head>
<body>

<h1>PRACTICAL EXAM: SIMPLIFYING A CANCER<br>DIAGNOSTIC PANEL</h1>
<div class="subtitle">MSc Data Science | Shoolini University | Student: Anjani Bharat (Reg. No: PGD202563026)</div>

<h2>SECTION 1: EXAM SUBMISSION REQUIREMENTS & ANSWERS</h2>

<div class="question">
Q.1) You are required to submit the prompt you used to write the code and find out the result.
</div>
<div class="answer">
<strong>Ans.</strong> Below is the exact prompt I formulated and utilized to generate the analytical code, pipeline, and findings for this practical examination:
</div>
<div class="code-block">
<span class="comment">&quot;&quot;&quot;</span>
<span class="string">PROMPT USED:
Act as an expert data scientist and biostatistician. Write an end-to-end Python script using the Breast Cancer Wisconsin Diagnostic dataset from scikit-learn to simplify a diagnostic panel with PCA:
1. Standardise the 30 cell nucleus biopsy features using StandardScaler and fit full 30-component PCA.
2. Plot a scree plot and cumulative variance curve; report components needed for >= 90% and >= 95% variance.
3. Project samples onto PC1 vs PC2 and scatter plot colored by tumor diagnosis (Malignant vs Benign).
4. Identify and visualize the top 5 features with the largest absolute loadings on PC1 and PC2.
5. Build an sklearn Pipeline (StandardScaler + PCA(k=7) + LogisticRegression) with 5-fold cross-validation accuracy to compare against the full 30-feature baseline without data leakage.
6. Address analytical questions on why standardisation changes variance distribution, and evaluate clinical recommendations for adopting the reduced panel in a diagnostic hospital laboratory.
Save all plots at 300 DPI in output/ directory.</span>
<span class="comment">&quot;&quot;&quot;</span>
</div>

<div class="question">
Q.2) Provide the link of the Github where you have publish your code.
</div>
<div class="answer">
<strong>Ans.</strong> I have published the complete code, documentation, and outputs in my GitHub repository:<br>
• <strong>Main Repository:</strong> <a href="https://github.com/bharatanjani512-hub/Statistics-for-Data-Science">https://github.com/bharatanjani512-hub/Statistics-for-Data-Science</a><br>
• <strong>Practical 11 Directory:</strong> <a href="https://github.com/bharatanjani512-hub/Statistics-for-Data-Science/tree/main/Anjani_Finalpractical">https://github.com/bharatanjani512-hub/Statistics-for-Data-Science/tree/main/Anjani_Finalpractical</a><br>
• <strong>Execution Script:</strong> <code>practical11.py</code>
</div>

<div class="question">
Q.3) Provide the screenshots of the outputs.
</div>
<div class="answer">
<strong>Ans.</strong> All visual output plots generated by <code>practical11.py</code> have been rendered at 300 DPI and embedded directly within this report:<br>
1. <strong>Scree Plot & Cumulative Explained Variance Plot</strong> &rarr; Embedded in Step 2 (Section 2)<br>
2. <strong>2D Scatter Projection of Biopsies on PC1 vs PC2</strong> &rarr; Embedded in Step 3 (Section 2)<br>
3. <strong>Top 5 Absolute Feature Loadings on PC1 & PC2 Bar Chart</strong> &rarr; Embedded in Step 4 (Section 2)<br>
4. <strong>5-Fold Cross-Validation Accuracy Comparison Bar Chart</strong> &rarr; Embedded in Step 5 (Section 2)<br>
5. <strong>Numerical Console Outputs & Execution Logs</strong> &rarr; Embedded in each respective step below.
</div>

<div class="question">
Q.4) Please provide the explaination of each step done.
</div>
<div class="answer">
<strong>Ans.</strong> In Section 2 of this report, I have provided a detailed first-person explanation of each step completed, including mathematical principles, preprocessing rationale, dimensionality reduction analysis, cross-validation setup, and answers to the follow-up analytical questions.
</div>

<div class="page-break"></div>

<h2>SECTION 2: STEP-BY-STEP PRACTICAL EXECUTION & ANALYSIS</h2>

<div class="question">
Step 1: Standardise the 30 features of cell nuclei from breast-tissue biopsies and fit PCA with all components.
</div>
<div class="answer">
<strong>Ans.</strong> The 30 cell nucleus features operate on drastically different physical units (e.g., mean area in hundreds of square micrometers vs. fractal dimension &lt; 0.1). Using <code>StandardScaler</code>, I standardized each feature to zero mean (&mu; = 0) and unit variance (&sigma; = 1). I then fitted a full 30-component PCA model to capture the complete orthogonal variance structure of the dataset.
</div>

<div class="label-input">INPUT</div>
<div class="code-block">
<span class="comment"># ============================================================</span>
<span class="comment"># STEP 1: STANDARDISE 30 FEATURES & FIT FULL PCA</span>
<span class="comment"># ============================================================</span>
<span class="keyword">from</span> sklearn.datasets <span class="keyword">import</span> load_breast_cancer
<span class="keyword">from</span> sklearn.preprocessing <span class="keyword">import</span> StandardScaler
<span class="keyword">from</span> sklearn.decomposition <span class="keyword">import</span> PCA

data = load_breast_cancer(as_frame=<span class="keyword">True</span>)
X, y = data.data, data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=X.shape[<span class="string">1</span>], random_state=<span class="string">42</span>)
X_pca = pca.fit_transform(X_scaled)

print(<span class="string">"Total biopsy samples:"</span>, X.shape[<span class="string">0</span>])
print(<span class="string">"Total cell nuclei features:"</span>, X.shape[<span class="string">1</span>])
print(<span class="string">"Standardisation complete: Mean = 0.0, Standard Deviation = 1.0."</span>)
print(<span class="string">"PCA fitted successfully with all 30 components."</span>)
print(<span class="string">"Transformed coordinates matrix shape:"</span>, X_pca.shape)
</div>

<div class="label-output">OUTPUT</div>
<div class="output-box">
Total biopsy samples: 569
Total cell nuclei features: 30
Standardisation complete: Mean = 0.0, Standard Deviation = 1.0.
PCA fitted successfully with all 30 components.
Transformed coordinates matrix shape: (569, 30)
</div>

<div class="page-break"></div>

<div class="question">
Step 2: Draw a scree plot and a cumulative explained-variance plot. Report how many components explain at least 90% and 95% of the variance.
</div>
<div class="answer">
<strong>Ans.</strong> In my variance decomposition, PC1 explains <strong>44.27%</strong> of the total variance, and PC2 explains <strong>18.97%</strong> (63.24% combined).<br>
• To explain at least <strong>90% of the variance</strong>, I found that <strong>k = 7 components</strong> are required (explaining <strong>91.01%</strong>).<br>
• To explain at least <strong>95% of the variance</strong>, I found that <strong>k = 10 components</strong> are required (explaining <strong>95.16%</strong>).
</div>

<div class="label-input">INPUT</div>
<div class="code-block">
<span class="comment"># ============================================================</span>
<span class="comment"># STEP 2: SCREE PLOT & CUMULATIVE EXPLAINED VARIANCE</span>
<span class="comment"># ============================================================</span>
<span class="keyword">import</span> numpy <span class="keyword">as</span> np
<span class="keyword">import</span> matplotlib.pyplot <span class="keyword">as</span> plt

explained_var_ratio = pca.explained_variance_ratio_
cumulative_var_ratio = np.cumsum(explained_var_ratio)

k_90 = int(np.argmax(cumulative_var_ratio >= <span class="string">0.90</span>) + <span class="string">1</span>)
k_95 = int(np.argmax(cumulative_var_ratio >= <span class="string">0.95</span>) + <span class="string">1</span>)

print(f<span class="string">"k for >= 90% variance: {k_90} ({cumulative_var_ratio[k_90-1]*100:.2f}%)"</span>)
print(f<span class="string">"k for >= 95% variance: {k_95} ({cumulative_var_ratio[k_95-1]*100:.2f}%)"</span>)
</div>

<div class="label-output">OUTPUT</div>
<div class="img-container">
  <img src="data:image/png;base64,__IMG2_B64__" alt="Scree and Cumulative Variance Plot">
</div>

<div class="page-break"></div>

<div class="question">
Step 3: Plot the samples on PC1 vs PC2, coloured by diagnosis.
</div>
<div class="answer">
<strong>Ans.</strong> When I projected the 569 biopsy samples onto the first two principal component axes, I observed a clear separation between malignant and benign tumors along PC1. Malignant biopsies concentrate heavily on positive PC1 scores (higher nuclear size, severe concavity, irregularity), while benign biopsies cluster on negative PC1 scores.
</div>

<div class="label-input">INPUT</div>
<div class="code-block">
<span class="comment"># ============================================================</span>
<span class="comment"># STEP 3: 2D PROJECTION ON PC1 VS PC2</span>
<span class="comment"># ============================================================</span>
plt.figure(figsize=(<span class="string">9</span>, <span class="string">7</span>))
mask_malignant = (y == <span class="string">0</span>)
mask_benign = (y == <span class="string">1</span>)

plt.scatter(X_pca[mask_malignant, <span class="string">0</span>], X_pca[mask_malignant, <span class="string">1</span>],
            c=<span class="string">"#d62728"</span>, marker=<span class="string">"x"</span>, s=<span class="string">65</span>, label=<span class="string">"Malignant (y=0)"</span>)
plt.scatter(X_pca[mask_benign, <span class="string">0</span>], X_pca[mask_benign, <span class="string">1</span>],
            c=<span class="string">"#1f77b4"</span>, marker=<span class="string">"o"</span>, s=<span class="string">55</span>, label=<span class="string">"Benign (y=1)"</span>)

plt.title(<span class="string">"Biopsy Samples on PC1 vs PC2"</span>)
plt.xlabel(<span class="string">"Principal Component 1 (44.27% Variance)"</span>)
plt.ylabel(<span class="string">"Principal Component 2 (18.97% Variance)"</span>)
plt.legend()
plt.tight_layout()
plt.savefig(<span class="string">"output/task3_pc1_vs_pc2_diagnosis.png"</span>)
</div>

<div class="label-output">OUTPUT</div>
<div class="img-container">
  <img src="data:image/png;base64,__IMG3_B64__" alt="PC1 vs PC2 Diagnosis Scatter Plot">
</div>

<div class="page-break"></div>

<div class="question">
Step 4: Print the five features with the largest absolute loadings on PC1 and on PC2.
</div>
<div class="answer">
<strong>Ans.</strong> In my loading analysis, PC1 is primarily driven by cell shape concavity and boundary irregularity, while PC2 is driven by fractal dimension and fine texture variation.<br><br>
<strong>Top 5 Features on PC1:</strong><br>
1. <code>mean concave points</code> (+0.2609) | 2. <code>mean concavity</code> (+0.2584) | 3. <code>worst concave points</code> (+0.2509)<br>
4. <code>mean compactness</code> (+0.2393) | 5. <code>worst perimeter</code> (+0.2366)<br><br>
<strong>Top 5 Features on PC2:</strong><br>
1. <code>mean fractal dimension</code> (+0.3666) | 2. <code>fractal dimension error</code> (+0.2801) | 3. <code>worst fractal dimension</code> (+0.2753)<br>
4. <code>mean radius</code> (-0.2339) | 5. <code>compactness error</code> (+0.2327)
</div>

<div class="label-input">INPUT</div>
<div class="code-block">
<span class="comment"># ============================================================</span>
<span class="comment"># STEP 4: TOP 5 ABSOLUTE LOADINGS ON PC1 AND PC2</span>
<span class="comment"># ============================================================</span>
<span class="keyword">import</span> pandas <span class="keyword">as</span> pd

loadings = pd.DataFrame(
    pca.components_.T,
    index=X.columns,
    columns=[f<span class="string">"PC{i+1}"</span> <span class="keyword">for</span> i <span class="keyword">in</span> range(pca.n_components_)]
)

pc1_top5 = loadings[<span class="string">"PC1"</span>].abs().sort_values(ascending=<span class="keyword">False</span>).head(<span class="string">5</span>)
pc2_top5 = loadings[<span class="string">"PC2"</span>].abs().sort_values(ascending=<span class="keyword">False</span>).head(<span class="string">5</span>)
</div>

<div class="label-output">OUTPUT</div>
<div class="img-container">
  <img src="data:image/png;base64,__IMG4_B64__" alt="PCA Loadings Bar Chart">
</div>

<div class="page-break"></div>

<div class="question">
Step 5: Train a logistic regression (5-fold CV accuracy) on (a) all 30 standardised features and (b) only the first k components, where k gives 90% variance. Fit the scaler and PCA inside a Pipeline so there is no leakage.
</div>
<div class="answer">
<strong>Ans.</strong> To prevent data leakage, I encapsulated both <code>StandardScaler</code> and <code>PCA</code> within <code>sklearn.pipeline.Pipeline</code>, fitting them strictly on the training partition of each fold:<br>
• <strong>Model (a) All 30 Standardised Features:</strong> <strong>97.37%</strong> (&plusmn; 1.66%)<br>
• <strong>Model (b) Reduced PCA Panel (First 7 Components):</strong> <strong>96.14%</strong> (&plusmn; 1.53%)<br>
• <strong>Performance Delta:</strong> I observed only a minor accuracy reduction of <strong>1.23%</strong>, while successfully reducing data dimensionality by <strong>76.7%</strong> (from 30 down to 7 features).
</div>

<div class="label-input">INPUT</div>
<div class="code-block">
<span class="comment"># ============================================================</span>
<span class="comment"># STEP 5: LOGISTIC REGRESSION 5-FOLD CV PIPELINE</span>
<span class="comment"># ============================================================</span>
<span class="keyword">from</span> sklearn.pipeline <span class="keyword">import</span> Pipeline
<span class="keyword">from</span> sklearn.linear_model <span class="keyword">import</span> LogisticRegression
<span class="keyword">from</span> sklearn.model_selection <span class="keyword">import</span> StratifiedKFold, cross_val_score

cv = StratifiedKFold(n_splits=<span class="string">5</span>, shuffle=<span class="keyword">True</span>, random_state=<span class="string">42</span>)

pipeline_all = Pipeline([
    (<span class="string">"scaler"</span>, StandardScaler()),
    (<span class="string">"classifier"</span>, LogisticRegression(max_iter=<span class="string">1000</span>, random_state=<span class="string">42</span>))
])
cv_all = cross_val_score(pipeline_all, X, y, cv=cv, scoring=<span class="string">"accuracy"</span>)

pipeline_pca = Pipeline([
    (<span class="string">"scaler"</span>, StandardScaler()),
    (<span class="string">"pca"</span>, PCA(n_components=k_90, random_state=<span class="string">42</span>)),
    (<span class="string">"classifier"</span>, LogisticRegression(max_iter=<span class="string">1000</span>, random_state=<span class="string">42</span>))
])
cv_pca = cross_val_score(pipeline_pca, X, y, cv=cv, scoring=<span class="string">"accuracy"</span>)

print(f"Model (a) All 30 Features Mean Accuracy: {cv_all.mean()*100:.2f}% (+/- {cv_all.std()*100:.2f}%)")
print(f"Model (b) Reduced Panel (k=7) Mean Accuracy: {cv_pca.mean()*100:.2f}% (+/- {cv_pca.std()*100:.2f}%)")
print(f"Accuracy Difference: {(cv_all.mean() - cv_pca.mean())*100:.2f}%")
</div>

<div class="label-output">OUTPUT</div>
<div class="img-container">
  <img src="data:image/png;base64,__IMG5_B64__" alt="Model Comparison Plot">
</div>

<div class="page-break"></div>

<div class="question">
Follow-up Question 1: What share of variance does PC1 now explain, and which feature dominates it? Explain why standardisation changes the result so much.
</div>
<div class="answer">
<strong>Ans.</strong><br>
<strong>1. Share of Variance & Dominant Feature (Standardised):</strong><br>
After standardising the dataset, I found that <strong>PC1 explains 44.27% of the total variance</strong>. The feature with the highest loading on PC1 is <code>mean concave points</code> (+0.2609), followed closely by <code>mean concavity</code> (+0.2584) and <code>worst concave points</code> (+0.2509). I noticed that no single feature overwhelmingly dominates PC1; multiple contour irregularity metrics contribute balanced weights (0.23 to 0.26).<br><br>
<strong>2. Contrast with Unstandardised PCA:</strong><br>
When I evaluated unstandardised PCA, PC1 accounted for <strong>98.20%</strong> of the variance and was overwhelmingly dominated by <code>worst area</code> (0.8521) and <code>mean area</code> (0.5168), while the other 28 features received loadings close to 0.00.<br><br>
<strong>3. Why Standardisation Changes the Result So Much:</strong><br>
PCA seeks orthogonal axes that maximize sample variance: Var(w<sup>T</sup>X) = w<sup>T</sup>&Sigma;w. Without standardisation, features with large physical measurement scales naturally exhibit enormous numerical variances (in this dataset, <code>worst area</code> variance is &approx; 324,165, whereas <code>concavity</code> variance is only &approx; 0.006). Because <code>area</code> has a variance millions of times larger than <code>concavity</code>, an unstandardised PCA aligns almost entirely with cell area simply due to units of measurement (&mu;m<sup>2</sup> vs. dimensionless ratios). By applying standardisation (z-score scaling), I scaled all feature variances to 1.0, enabling PCA to discover true biological covariation across all 30 indicators rather than measurement unit artifacts.
</div>

<div class="question">
Follow-up Question 2: Would you recommend the reduced panel to the lab? Give one statistical and one practical reason, and say what you lose in interpretability.
</div>
<div class="answer">
<strong>Ans.</strong> Yes, I would recommend the reduced panel (k = 7) to the hospital laboratory.<br><br>
<strong>1. Statistical Reason:</strong><br>
In my cross-validation experiments, the reduced panel with k = 7 components retains <strong>91.01% of the total informational variance</strong> across all 30 features, while achieving a <strong>96.14% 5-fold cross-validation accuracy</strong>—nearly identical to the full 30-feature baseline of 97.37% (a negligible drop of just 1.23%). Furthermore, I observed lower standard deviation across folds (&plusmn;1.53% vs &plusmn;1.66%), demonstrating that eliminating high multicollinearity stabilizes model performance and reduces the risk of overfitting.<br><br>
<strong>2. Practical Reason:</strong><br>
From a practical laboratory operations perspective, measuring, imaging, and performing quality control on 30 separate nuclear morphology assays for every biopsy is costly, computationally demanding, and increases the risk of measurement noise or assay failure. In my assessment, reducing the panel to 7 combined indicators significantly lowers test expenses, streamlines diagnostic workflows, and accelerates turnaround times for patients awaiting critical biopsy results.<br><br>
<strong>3. What You Lose in Interpretability:</strong><br>
What I lose in this reduction is direct clinical interpretability. Pathologists make clinical decisions using tangible physical measurements (such as <em>"mean cell radius exceeds 18 &mu;m"</em>). Because principal components are mathematical linear combinations (weighted sums) of all 30 features:
<br><br>
PC1 = 0.261(concave points) + 0.258(concavity) + ... + 0.237(perimeter)
<br><br>
A transformed coordinate such as PC1 = +2.48 has no direct histological meaning under a microscope, making it harder for clinicians to explain specific diagnostic reasoning to patients.
</div>

<div class="conclusion-header">Conclusion</div>
<div class="conclusion-text">
Principal Component Analysis successfully simplified the 30-feature breast cancer diagnostic panel into 7 orthogonal components while retaining 91.01% of total variance and 96.14% cross-validation accuracy. Standardisation was proven critical to avoid artificial dominance by cell area. The reduced panel is statistically robust and practically advantageous for high-throughput laboratory diagnosis.
</div>

<div class="sign-off">
Submitted by: Anjani Bharat<br>
Registration Number: PGD202563026<br>
Degree: MSc Data Science | Shoolini University
</div>

</body>
</html>
"""

html_out = (template
            .replace("__IMG2_B64__", img2_b64)
            .replace("__IMG3_B64__", img3_b64)
            .replace("__IMG4_B64__", img4_b64)
            .replace("__IMG5_B64__", img5_b64))

with open(doc_path, "w", encoding="utf-8") as f:
    f.write(html_out)

shutil.copy2(doc_path, workspace_doc_path)
print("Successfully written Practical 5 styled document to:", doc_path)
print("Copied to workspace root:", workspace_doc_path)
