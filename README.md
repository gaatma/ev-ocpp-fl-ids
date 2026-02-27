# A Federated Learning Based Intrusion Detection System for Privacy-Preserving and Robust Monitoring of Electric Vehicle Charging Infrastructure

**INSE 6450 – Winter 2026**
**Gifty Acquah | Student ID: 40358162 | PhD, Concordia University**

---

## Project Overview

This project develops an AI-based Intrusion Detection System (IDS) for EV charging infrastructure using a Federated Learning (FL) framework. The system detects cyberattacks targeting the Open Charge Point Protocol (OCPP) 1.6 by analyzing flow-level network statistics at each charging station locally, without sharing raw traffic data.

The task is formulated as a **5-class classification problem**:
- `normal` — legitimate charging traffic
- `cyberattack_ocpp16_doc_idtag` — fake ID tag attack
- `cyberattack_ocpp16_dos_flooding_heartbeat` — DoS flooding attack
- `cyberattack_ocpp16_fdi_chargingprofile` — false data injection attack
- `cyberattack_ocpp16_unauthorized_access` — unauthorized access attack

---

## Milestones

### ✅ Milestone 1 — Data Selection & Exploration
- Dataset selection and justification
- Exploratory data analysis (EDA)
- Missing value and outlier analysis
- Initial preprocessing and feature engineering
- **Notebook:** `notebooks/01_data_exploration.ipynb`

### ✅ Milestone 2 — Model Selection, Training & Evaluation
- MLP (Deep Neural Network) model design and justification
- Ablation study: Dummy Baseline vs Small MLP vs Final MLP
- Full classification metrics: accuracy, F1, AUROC
- Efficiency metrics: latency, throughput, model size, FLOPs
- Deployment design and system-level trade-offs
- **Notebook:** `notebooks/02_model_training.ipynb`

---

## Model Performance (Milestone 2)

| Metric | Value |
|---|---|
| Test Accuracy | 0.9992 |
| Macro F1-Score | 0.9992 |
| AUROC (macro OvR) | 1.0000 |
| Inference Latency p50 | 0.033 ms |
| Inference Latency p90 | 0.037 ms |
| Throughput (batch=32) | 565,936 samples/sec |
| Model Size | 0.071 MB |
| Parameters | 16,901 |

---

## Dataset

**Name:** Federated OCPP 1.6 Intrusion Detection Dataset
**Version:** v1 (February 2025)
**Source:** [arXiv](https://doi.org/10.48550/arXiv.2502.01569) — Dalamagkas et al., 2025
**License:** Research use (Horizon Europe DYNABIC Project)

Subset used:
```
data/ocpp_app_layer/Combined/Train.csv   (3,020 samples)
data/ocpp_app_layer/Combined/Test.csv    (1,295 samples)
```

5 balanced classes, 55 columns, no missing values.

---

## Repository Structure
```
ev-ocpp-fl-ids/
├── README.md
├── requirements.txt
├── data/
│   └── ocpp_app_layer/
│       └── Combined/
│           ├── Train.csv
│           └── Test.csv
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_model_training.ipynb
├── src/
│   ├── preprocessing.py
│   └── model.py
└── outputs/
    └── figures/
        ├── class_distribution.png
        ├── correlation_heatmap.png
        ├── learning_curves.png
        ├── ablation_comparison.png
        └── confusion_matrix.png
```

---

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/gaatma/ev-ocpp-fl-ids.git
cd ev-ocpp-fl-ids
```

### 2. Create virtual environment (Windows)
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Add the dataset
Download the dataset from the source above and place the CSV files at:
```
data/ocpp_app_layer/Combined/Train.csv
data/ocpp_app_layer/Combined/Test.csv
```

---

## Running the Code

**Milestone 1 — Data Exploration:**
```
jupyter notebook notebooks/01_data_exploration.ipynb
```

**Milestone 2 — Model Training & Evaluation:**
```
jupyter notebook notebooks/02_model_training.ipynb
```

Run all cells. The notebook will:
- Train the MLP model with early stopping
- Run the ablation study
- Print all classification and efficiency metrics
- Save figures to `outputs/figures/`

---

## Output Figures

| Figure | Description |
|---|---|
| `class_distribution.png` | Class balance in training set |
| `correlation_heatmap.png` | Feature correlation heatmap |
| `learning_curves.png` | Loss and accuracy vs epoch |
| `ablation_comparison.png` | Baseline vs Small MLP vs Final MLP |
| `confusion_matrix.png` | Per-class predictions on test set |

---

## Citation
```
McMahan, H. B., Moore, E., Ramage, D., Hampson, S., & Aguera y Arcas, B. (2017).
Communication-Efficient Learning of Deep Networks from Decentralized Data.
International Conference on Artificial Intelligence and Statistics,
1273–1282. http://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf

Dalamagkas, C., Radoglou-Grammatikis, P., Bouzinis, P., Papadopoulos, I., Lagkas, T., Argyriou, V., Goudos, S., 
Margounakis, D., Fountoukidis, E., & Sarigiannidis, P. (2025). 
Federated Detection of Open Charge Point Protocol 1.6 Cyberattacks. arXiv:2502.01569.
```