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

### Milestone 1 — Data Selection & Exploration
- Dataset selection and justification
- Exploratory data analysis (EDA)
- Missing value and outlier analysis
- Initial preprocessing and feature engineering
- **Notebook:** `notebooks/01_data_exploration.ipynb`

### Milestone 2 — Model Selection, Training & Evaluation
- MLP (Deep Neural Network) model design and justification
- Ablation study: Dummy Baseline vs Small MLP vs Final MLP
- Full classification metrics: accuracy, F1, AUROC
- Efficiency metrics: latency, throughput, model size, FLOPs
- Deployment design and system-level trade-offs
- **Notebook:** `notebooks/02_model_training.ipynb`

### Milestone 3 — Robustness, Monitoring & Adaptation
- Failure mode analysis and risk mitigation (17 failure modes)
- Stress tests: Gaussian noise, feature masking, OOD, class rarity
- Adversarial evaluation: FGSM at 6 epsilon levels, white/grey/black-box adversaries
- Robustness methods: feature jittering augmentation + temperature scaling + confidence abstention
- Production monitoring dashboard: PSI, Wasserstein, JS divergence, rolling F1
- Drift simulation across 4 monitoring windows with alerting runbook
- Adaptation experiment: drift retrain with before/after comparison
- Model versioning: v1.0 baseline, v1.1 jittered, v1.2 retrained
- **Notebook:** `notebooks/03_robustness.ipynb`

---

## Model Performance

### Milestone 2 — Baseline MLP
| Metric | Value |
|---|---|
| Test Accuracy | 0.9992 |
| Macro F1-Score | 0.9992 |
| AUROC (macro OvR) | 1.0000 |
| Inference Latency p50 | 0.033 ms |
| Inference Latency p90 | 0.037 ms |
| Throughput (batch=32) | 565,936 samples/sec |
| Model Size | 0.071 MB |
| Parameters | 17,157 |

### Milestone 3 — Robustness Results
| Test | Macro F1 |
|---|---|
| Clean baseline | 0.9992 |
| Gaussian noise σ=0.5 | 0.9938 |
| Gaussian noise σ=1.0 | 0.9436 |
| Feature masking 50% | 0.9931 |
| FGSM ε=0.20 | 0.9907 |
| FGSM ε=0.30 | 0.9572 |
| After drift retrain | 0.9992 |

---

## Model Versions
| Version | File | Description |
|---|---|---|
| v1.0 | `outputs/mlp_final_v2.pt` | Baseline MLP — Milestone 2 |
| v1.1 | `outputs/mlp_jittered.pt` | Jitter augmentation — Milestone 3 |
| v1.2 | `outputs/mlp_retrained_v1.pt` | Post-drift retrain — Milestone 3 |

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

5 balanced classes, 51 numeric features, no missing values.

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
│   ├── 02_model_training.ipynb
│   └── 03_robustness.ipynb
├── src/
│   ├── preprocessing.py
│   └── model.py
└── outputs/
    ├── mlp_final_v2.pt
    ├── mlp_jittered.pt
    ├── mlp_retrained_v1.pt
    └── figures/
        ├── section1_stress_tests.png
        ├── section2_robustness.png
        ├── section2_confidence_histograms.png
        ├── section3_monitoring_dashboard.png
        └── section4_adaptation.png
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

**Milestone 3 — Robustness, Monitoring & Adaptation:**
```
jupyter notebook notebooks/03_robustness.ipynb
```

Run all cells in order. The notebook will train the jittered model, run FGSM evaluation, temperature scaling, monitoring dashboard, and adaptation experiment automatically.

---

## Citation
```
McMahan, H. B., Moore, E., Ramage, D., Hampson, S., & Aguera y Arcas, B. (2017).
Communication-Efficient Learning of Deep Networks from Decentralized Data.
International Conference on Artificial Intelligence and Statistics,
1273–1282. http://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf

Dalamagkas, C., Radoglou-Grammatikis, P., Bouzinis, P., Papadopoulos, I., Lagkas, T.,
Argyriou, V., Goudos, S., Margounakis, D., Fountoukidis, E., & Sarigiannidis, P. (2025).
Federated Detection of Open Charge Point Protocol 1.6 Cyberattacks. arXiv:2502.01569.

Szakály, M., Köhler, T., & Martinovic, I. (2025). Current Affairs: 
A Security Measurement Study of CCS EV Charging Deployments.
34th USENIX Security Symposium. USENIX Association
```