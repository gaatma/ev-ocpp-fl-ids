# A Federated Learning Based Intrusion Detection System for Privacy-Preserving and Robust Monitoring of Electric Vehicle Charging Infrastructure

**INSE 6450 – Winter 2026**
**Gifty Acquah | Student ID: 40358162 | PhD, Concordia University**
**GitHub:** https://github.com/gaatma/ev-ocpp-fl-ids

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
- MLP (128-64-32) model design and justification
- Ablation study: Dummy Baseline vs Small MLP vs Final MLP
- Full classification metrics: accuracy, F1, AUROC
- Efficiency metrics: latency, throughput, model size
- **Notebook:** `notebooks/02_model_training.ipynb`

### Milestone 3 — Robustness, Monitoring & Adaptation
- Failure mode analysis (17 failure modes, Table 1)
- Stress tests: Gaussian noise, feature masking, OOD, class rarity
- FGSM adversarial evaluation at 6 epsilon levels
- Jitter augmentation + temperature scaling + confidence abstention
- PSI/Wasserstein/JS drift monitoring dashboard (4 windows)
- Drift simulation and adaptation experiment
- Model versioning: v1.0 → v1.1 → v1.2
- **Notebook:** `notebooks/03_robustness.ipynb`

### Milestone 4 — Continual Learning & Human-in-the-Loop
- Experience Replay continual learning (buffer=500, stratified)
- 5-episode drift simulation with before/after metrics
- Hybrid active learning (Entropy + Margin, n=50 per cycle)
- Human-in-the-loop simulation (5% annotation noise)
- Dynamic INT8 quantization (66.7% size reduction)
- ONNX export for edge deployment
- Full system diagram (Milestones 1–4)
- **Notebook:** `notebooks/04_continual_learning.ipynb`
- **Demo:** `notebooks/05_demo.ipynb`

---

## Quick Start — End-to-End Demo
```bash
jupyter notebook notebooks/05_demo.ipynb
```

Run all cells. The demo covers the full pipeline in 5 steps:

| Step | Action | Key Result |
|---|---|---|
| 1 | Train MLP with jitter | F1=0.9992 in ~4s |
| 2 | Infer with abstention | p50=0.0545ms latency |
| 3 | Detect drift (PSI) | Alert if PSI > 0.20 |
| 4 | AL query + human annotation | 75% labelling burden reduction |
| 5 | Continual update (Experience Replay) | F1 maintained ≥ 0.97 |

---

## Model Performance Summary

### Milestone 2 — Baseline
| Metric | Value |
|---|---|
| Test Accuracy | 0.9992 |
| Macro F1 | 0.9992 |
| AUROC | 1.0000 |
| Inference p50 | 0.033 ms |
| Inference p90 | 0.037 ms |
| Throughput | 565,936 samples/sec |
| Model size | 0.071 MB |
| Parameters | 17,157 |

### Milestone 3 — Robustness
| Condition | Macro F1 |
|---|---|
| Clean baseline | 0.9992 |
| Gaussian noise σ=0.5 | 0.9938 |
| Feature masking 50% | 0.9931 |
| FGSM ε=0.20 | 0.9907 |
| FGSM ε=0.30 | 0.9572 |
| Post drift retrain | 0.9992 |

### Milestone 4 — Continual Learning
| Condition | Macro F1 |
|---|---|
| CL Episode 1 (clean) | 0.9938 |
| CL Episode 5 (clean) | 0.9961 |
| AL Cycle 1 (clean) | 0.9946 |
| AL Cycle 5 (clean) | 0.9915 |
| Quantized model | 0.9977 |

---

## Model Version Registry
| Version | File | Description |
|---|---|---|
| v1.0 | `outputs/mlp_final_v2.pt` | Baseline MLP — Milestone 2 |
| v1.1 | `outputs/mlp_jittered.pt` | Jitter augmentation — Milestone 3 |
| v1.2 | `outputs/mlp_retrained_v1.pt` | Post-drift retrain — Milestone 3 |
| v1.3 | `outputs/mlp_quantized.pt` | Dynamic INT8 quantization — Milestone 4 |
| demo | `outputs/demo_model.pt` | Demo baseline |
| demo | `outputs/demo_model_updated.pt` | Demo after CL update |
| onnx | `outputs/mlp_model.onnx` | ONNX export for edge deployment |

---

## Dataset

**Name:** Federated OCPP 1.6 Intrusion Detection Dataset
**Version:** v1 (February 2025)
**Source:** [arXiv](https://doi.org/10.48550/arXiv.2502.01569) — Dalamagkas et al., 2025
**License:** Research use (Horizon Europe DYNABIC Project)
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
│   ├── 03_robustness.ipynb
│   ├── 04_continual_learning.ipynb
│   └── 05_demo.ipynb
├── src/
│   ├── preprocessing.py
│   └── model.py
└── outputs/
    ├── mlp_final_v2.pt
    ├── mlp_jittered.pt
    ├── mlp_retrained_v1.pt
    ├── mlp_quantized.pt
    ├── mlp_model.onnx
    ├── demo_model.pt
    ├── demo_model_updated.pt
    └── figures/
        ├── section1_stress_tests.png
        ├── section2_robustness.png
        ├── section2_confidence_histograms.png
        ├── section3_monitoring_dashboard.png
        ├── section4_adaptation.png
        ├── section1_continual_learning.png
        ├── section2_hitl.png
        ├── section2_al_workflow.png
        ├── section3_system_diagram.png
        └── section3_summary.png
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/gaatma/ev-ocpp-fl-ids.git
cd ev-ocpp-fl-ids
```

### 2. Create virtual environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add the dataset
Download from the source above and place at:
```
data/ocpp_app_layer/Combined/Train.csv
data/ocpp_app_layer/Combined/Test.csv
```

---

## Running the Notebooks

Run notebooks in order for full reproducibility:
```bash
# Milestone 1
jupyter notebook notebooks/01_data_exploration.ipynb

# Milestone 2
jupyter notebook notebooks/02_model_training.ipynb

# Milestone 3
jupyter notebook notebooks/03_robustness.ipynb

# Milestone 4
jupyter notebook notebooks/04_continual_learning.ipynb

# End-to-end demo
jupyter notebook notebooks/05_demo.ipynb
```

Each notebook runs independently. Run all cells from top to bottom. All outputs are saved automatically to `outputs/` and `outputs/figures/`.

---

## Output Artifacts

| File | Description |
|---|---|
| `outputs/mlp_final_v2.pt` | Baseline model weights |
| `outputs/mlp_jittered.pt` | Jitter-augmented model |
| `outputs/mlp_retrained_v1.pt` | Post-drift retrained model |
| `outputs/mlp_quantized.pt` | INT8 quantized model |
| `outputs/mlp_model.onnx` | ONNX export |
| `outputs/figures/*.png` | All report figures |

---

## Citation
```
## Citation & References

McMahan, H. B., Moore, E., Ramage, D., Hampson, S., & Agüera y Arcas, B. (2017).
Communication-Efficient Learning of Deep Networks from Decentralized Data.
AISTATS, 1273–1282.
http://proceedings.mlr.press/v54/mcmahan17a/mcmahan17a.pdf

Dalamagkas, C., Radoglou-Grammatikis, P., Bouzinis, P., Papadopoulos, I.,
Lagkas, T., Argyriou, V., Goudos, S., Margounakis, D., Fountoukidis, E.,
& Sarigiannidis, P. (2025).
Federated Detection of Open Charge Point Protocol 1.6 Cyberattacks.
arXiv:2502.01569. https://doi.org/10.48550/arXiv.2502.01569

Szakály, M., Köhler, T., & Martinovic, I. (2025).
Current Affairs: A Security Measurement Study of CCS EV Charging Deployments.
34th USENIX Security Symposium.

Kirkpatrick, J., et al. (2017).
Overcoming Catastrophic Forgetting in Neural Networks.
Proceedings of the National Academy of Sciences, 114(13), 3521–3526.

Rolnick, D., Ahuja, A., Schwarz, J., Lillicrap, T., & Wayne, G. (2019).
Experience Replay for Continual Learning.
Advances in Neural Information Processing Systems (NeurIPS).

Settles, B. (2009).
Active Learning Literature Survey.
University of Wisconsin–Madison, Computer Sciences Technical Report 1648.

Gal, Y., & Ghahramani, Z. (2016).
Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning.
ICML, 1050–1059.

Goodfellow, I. J., Shlens, J., and Szegedy, C. (2014). 
Explaining and harnessing adversarial examples. 
In International Conference on Learning Representations (ICLR).

Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017).
On Calibration of Modern Neural Networks.
ICML, 1321–1330.

Vitter, J. S. (1985).
Random Sampling with a Reservoir.
ACM Transactions on Mathematical Software, 11(1), 37–57.
```