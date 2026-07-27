# Detecting Software Supply Chain Attacks Using Machine Learning

## MSc Dissertation Project

### Author
Shivani burma

### University
The University of Roehampton

---

# Project Overview

This project presents a lightweight machine learning framework for detecting suspicious Python packages involved in software supply chain attacks before installation.

The proposed framework analyses package metadata and package name similarity instead of relying on source code analysis or runtime behaviour. The system is capable of identifying potential typosquatting attacks using supervised machine learning and provides predictions through a Streamlit web application.

---

# Project Objectives

- Detect suspicious Python packages before installation.
- Generate synthetic typosquatting package names.
- Extract metadata from the Python Package Index (PyPI).
- Engineer meaningful numerical features.
- Train and compare multiple machine learning models.
- Validate the trained model using real malicious packages from the OpenSSF repository.
- Deploy the best-performing model using Streamlit.

---

# Technologies Used

- Python 3.11
- Google Colab
- Visual Studio Code
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- RapidFuzz
- Matplotlib
- Seaborn
- Joblib
- Requests

---

# Machine Learning Models

The following supervised learning algorithms were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

The Decision Tree model was selected for deployment.

---

# Features Used

The machine learning models were trained using the following five features:

- SimilarityScore
- NameLength
- SummaryLength
- ReleaseCount
- PackageAgeDays

---

# Dataset

## Training Dataset

The training dataset contains:

- Legitimate Python packages collected from PyPI
- Synthetic typosquatting packages
- Engineered metadata features

Final dataset:

```
enhanced_final_detection_dataset.csv
```

---

## External Validation Dataset

External validation was performed using:

- OpenSSF Malicious Packages Repository

100 unseen malicious packages were used for evaluation.

---

# Project Structure

```
Supply-Chain-Attack-Detection/

│
├── app.py
├── requirements.txt
├── README.md
├── models/
│     └── best_supply_chain_model.pkl
├── data/
│     ├── enhanced_final_detection_dataset.csv
│     └── top100_packages.csv
├── pages/
├── plots/
├── notebooks/
│     └── Supply_Chain_Detection.ipynb
├── screenshots/
└── images/
└── models/
```

---

# How to Run the Google Colab Notebook

## Step 1

Open Google Colab.

https://colab.research.google.com

---

## Step 2

Upload the notebook:

```
Supply_Chain_Detection.ipynb
```

---

## Step 3

Run all notebook cells sequentially.

The notebook performs:

- Data collection
- Feature engineering
- Data preprocessing
- Model training
- Model evaluation
- External validation
- Model saving

The trained model will be saved as:

```
best_supply_chain_model.pkl
```

---

# How to Run the Streamlit Application (VS Code)

## Step 1

Clone the repository.

```bash
git clone https://github.com/shivani-burma/Supply-Chain-Attack-Detection.git
```

---

## Step 2

Open the project folder in Visual Studio Code.

---

## Step 3

Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

---

## Step 4

Install all dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 5

Run the Streamlit application.

```bash
streamlit run app.py
```

---

## Step 6

Open the browser.

Normally Streamlit opens automatically.

Otherwise visit:

```
http://localhost:8501
```

---

# Application Features

The Streamlit dashboard allows users to:

- Enter a package name
- View extracted package metadata
- Predict whether a package is legitimate or suspicious
- Display prediction confidence
- View feature importance
- Display evaluation results

---

# Results

## Internal Evaluation

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 100% |
| Decision Tree | 100% |
| Random Forest | 100% |

All three machine learning models achieved perfect classification performance on the internally constructed testing dataset. This is largely attributed to the highly separable nature of the engineered metadata features, particularly the SimilarityScore used during dataset construction. While these results demonstrate the effectiveness of the selected features on the training dataset, they should be interpreted alongside the external validation results, which provide a more realistic assessment of the framework's generalisation capability.

## External Validation

- Packages Tested: **100**
- Packages Detected as Suspicious: **78**
- Detection Rate: **78%**

The trained Decision Tree model was evaluated using 100 previously unseen malicious Python packages obtained from the OpenSSF Malicious Packages Repository. The model successfully detected 78 malicious packages, achieving a detection rate of 78%. This external validation demonstrates that the proposed framework can identify the majority of real-world malicious packages, while also highlighting that some attacks exhibit metadata characteristics different from those represented in the synthetic training dataset. These findings indicate that external validation provides a more realistic evaluation of model performance than the internal testing results.
# Repository

This repository contains:

- Source code
- Machine learning notebook
- Trained model
- Datasets
- Streamlit application
- Figures
- Documentation

---

# References

Dataset

- Python Package Index (PyPI)
- OpenSSF Malicious Packages Repository

---

# License

This project was developed for academic purposes as part of the MSc Computing dissertation at the University of Roehampton.
