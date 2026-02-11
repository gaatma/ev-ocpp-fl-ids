# A Federated Learning Based Intrusion Detection System for Privacy-Preserving and Robust Monitoring of Electric Vehicle Charging Infrastructure 
**INSE 6450 – Milestone 1**

---

## Project Overview
This project focuses on detecting cyberattacks targeting Open Charge Point Protocol (OCPP) 1.6 in smart EV charging environments using machine learning techniques.

The dataset used is the **Federated OCPP 1.6 Intrusion Detection Dataset (2025)**, which includes labeled network flow statistics extracted from OCPP and TCP/IP traffic.

This milestone covers:
- Data selection justification  
- Exploratory data analysis  
- Risk assessment  
- Initial preprocessing and feature engineering  
- Reproducible code pipeline  

---

## Dataset

**Dataset Name:** Federated OCPP 1.6 Intrusion Detection Dataset  
**Version:** v1 (February 2025)  
**Source:** [arXiv](https://doi.org/10.21227/v1f0-9t13) (Dalamagkas et al., 2025)  
**License:** Research use (Horizon Europe DYNABIC Project)  

I use:

```
Balanced_OCPP16_APP_Layer
```

Specifically:

```
data/ocpp_app_layer/Combined/Train.csv
data/ocpp_app_layer/Combined/Test.csv
```

The dataset contains:
- 3020 training samples  
- 1295 testing samples  
- 55 columns  
- 5 classes (4 attacks + normal)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/gaatma/ev-ocpp-fl-ids.git
cd ev-ocpp-fl-ids
```

### 2️⃣ Create virtual environment (Mac)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Code

Run Jupyter:

```bash
jupyter notebook
```

Open:

```
notebooks/01_data_exploration.ipynb
```

The notebook:
- Loads raw CSV files  
- Performs EDA  
- Encodes labels  
- Scales features  
- Saves output figures  

---

## Output Artifacts

Saved figures:

```
outputs/figures/class_distribution.png
outputs/figures/correlation_heatmap.png
```

---

## Feature Engineering (Milestone 1 Plan)

- Removal of identifiers (`flow_id`, IP addresses)  
- Label encoding for categorical target  
- Standardization of numeric features  
- Correlation analysis for feature redundancy  
- Future work: temporal aggregation and anomaly score features  

---

## 👩🏽‍💻 Author

**Gifty Acquah**  
INSE 6450 – Winter 2026  
PhD, Concordia University  

---
