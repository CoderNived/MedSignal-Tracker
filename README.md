# 🫀 MedSignal-Tracker

<div align="center">

![Build Status](https://img.shields.io/github/actions/workflow/status/CoderNived/MedSignal-Tracker/ci.yml?style=flat-square&label=build)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Repo Size](https://img.shields.io/github/repo-size/CoderNived/MedSignal-Tracker?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/CoderNived/MedSignal-Tracker?style=flat-square)
![Issues](https://img.shields.io/github/issues/CoderNived/MedSignal-Tracker?style=flat-square)
![Stars](https://img.shields.io/github/stars/CoderNived/MedSignal-Tracker?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Node](https://img.shields.io/badge/Node.js-18%2B-brightgreen?style=flat-square&logo=node.js)
![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green?style=flat-square&logo=mongodb)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=flat-square&logo=docker)

**A full-stack biomedical signal tracking and monitoring platform for real-time acquisition, processing, visualization, and analysis of medical signal data.**

[Overview](#overview) · [Architecture](#system-architecture) · [Features](#core-features) · [Installation](#installation) · [Usage](#usage) · [Contributing](#contributing)

</div>

---

## Overview

Monitoring physiological signals — heart rate, ECG waveforms, EEG patterns, blood oxygen levels — is foundational to both clinical care and medical research. Yet most systems that handle this data are either proprietary, inflexible, or too fragmented to integrate cleanly into modern software stacks.

**MedSignal-Tracker** is an open-source, full-stack platform designed to bridge that gap. It provides a complete pipeline from signal acquisition and processing through to storage, API delivery, and interactive dashboard visualization — all in a modular architecture that can be extended for clinical, research, or IoT contexts.

### The Problem

| Challenge | Consequence |
|---|---|
| Delayed detection of physiological anomalies | Missed clinical intervention windows |
| Siloed signal data with no unified interface | Difficult cross-patient or longitudinal analysis |
| No accessible open tooling for signal monitoring | Research teams build one-off, non-reproducible systems |
| Poor visualization of time-series medical data | Clinicians can't interpret trends efficiently |

### Real-World Applications

- **Remote Patient Monitoring (RPM)** — Track vitals from wearable sensors and flag threshold breaches in real time
- **Hospital Telemetry Systems** — Centralize multi-patient signal feeds into a single monitoring dashboard
- **Biomedical Research** — Log, query, and export structured signal datasets for analysis and publication
- **IoT Healthcare Devices** — Ingest data from embedded sensors via standard protocols (MQTT, REST)
- **Health Analytics Platforms** — Build longitudinal trend dashboards over patient cohorts

---

## Demo / Screenshots

> **Note:** Attach screenshots or an animated demo GIF after first deployment. Recommended sections:

```
[ Screenshot: Real-time ECG dashboard with live waveform rendering ]
[ Screenshot: Signal history view with time-range filtering ]
[ Screenshot: Patient profile with signal summary cards ]
[ Screenshot: Anomaly alert panel with threshold configuration ]
[ GIF: End-to-end flow — sensor data in → processed signal → dashboard update ]
```

To contribute demo assets, see the [Contributing](#contributing) section.

---

## System Architecture

MedSignal-Tracker is designed as a layered, decoupled system. Each layer has a well-defined interface with adjacent layers, making individual components replaceable without restructuring the whole platform.

```
┌──────────────────────────────────────────────────────────────────────┐
│                        MedSignal-Tracker                             │
└──────────────────────────────────────────────────────────────────────┘

  Medical Sensors / Data Sources
  (ECG devices, EEG headsets, wearables, simulation scripts)
           │
           ▼
  ┌─────────────────────────┐
  │  Signal Ingestion Layer  │  ← REST API / MQTT / WebSocket endpoints
  │  (server/routes/)        │    that accept raw signal payloads
  └───────────┬─────────────┘
              │
              ▼
  ┌──────────────────────────────┐
  │  Data Processing & Filtering │  ← Noise reduction, normalization,
  │  (scripts/ + server/services)│    band-pass filtering, resampling
  └───────────┬──────────────────┘
              │
              ▼
  ┌──────────────────────────┐
  │  Persistence Layer        │  ← MongoDB (time-series signal docs)
  │  (server/models/)         │    + optional PostgreSQL for patient data
  └───────────┬───────────────┘
              │
              ▼
  ┌──────────────────────────┐
  │  Backend API              │  ← Node.js / Express REST API
  │  (server/controllers/)    │    Handles auth, CRUD, analytics queries
  └───────────┬───────────────┘
              │
              ▼
  ┌──────────────────────────┐
  │  Frontend Dashboard       │  ← React + Chart.js / D3.js
  │  (client/)                │    Real-time signal rendering,
  └───────────┬───────────────┘    patient views, alert management
              │
              ▼
  ┌────────────────────────────────┐
  │  Signal Visualization &        │  ← Interactive waveform charts,
  │  Analytics                     │    anomaly markers, export tools
  └────────────────────────────────┘
```

### Design Principles

- **Separation of concerns** — signal ingestion, processing, and visualization are independent services
- **Stateless API** — backend is horizontally scalable; session state lives client-side or in a token store
- **Schema flexibility** — MongoDB document model accommodates heterogeneous signal types without schema migrations
- **Extensibility** — new signal types or processing algorithms are added by implementing defined interfaces

---

## Tech Stack

### Backend

| Technology | Version | Role |
|---|---|---|
| Node.js | 18 LTS | API server runtime |
| Express.js | 4.x | HTTP routing and middleware |
| Python | 3.10+ | Signal processing scripts |
| FastAPI | 0.100+ | Optional Python microservice for heavy DSP tasks |

### Frontend

| Technology | Version | Role |
|---|---|---|
| React | 18 | Component-based UI framework |
| Chart.js | 4.x | Real-time waveform and trend charts |
| D3.js | 7.x | Custom signal visualizations |
| Tailwind CSS | 3.x | Utility-first styling |

### Data Processing

| Library | Purpose |
|---|---|
| NumPy | Numerical signal operations, array manipulation |
| SciPy | Band-pass filters, FFT, spectral analysis |
| Pandas | Time-series structuring, resampling, export |

### Database

| Technology | Role |
|---|---|
| MongoDB 6.0 | Primary store for time-series signal documents |
| PostgreSQL (optional) | Relational patient and user data |
| Redis (optional) | Pub/sub for real-time signal streaming |

### DevOps & Tooling

| Tool | Purpose |
|---|---|
| Docker + Compose | Containerized, reproducible local and production deployment |
| GitHub Actions | CI pipeline (lint, test, build) |
| dotenv | Environment variable management |
| ESLint / Prettier | Code quality enforcement |
| pytest | Python processing module tests |
| Jest | JavaScript unit and integration tests |

---

## Core Features

### Real-Time Signal Tracking
Ingest live signal data via WebSocket or REST. The frontend dashboard updates without page refresh, rendering waveforms at configurable sample rates.

### Waveform Visualization
Interactive time-series charts with zoom, pan, and time-range selection. Supports ECG, EEG, PPG, and generic analog signal formats. Rendered via Chart.js for performance-critical streams and D3.js for custom overlays.

### Signal Processing Pipeline
Raw signals are passed through a configurable processing chain:
- **Noise reduction** — moving average or Savitzky-Golay smoothing
- **Band-pass filtering** — configurable frequency cutoffs (e.g., 0.5–40 Hz for ECG)
- **Normalization** — min-max or z-score scaling
- **Resampling** — standardize heterogeneous sample rates

### Data Logging and History
All ingested signals are persisted with full metadata (patient ID, signal type, device ID, timestamp). Query historical records with flexible time-range and patient filters.

### Threshold-Based Alerting
Define upper/lower bounds per signal type. The system evaluates incoming samples against thresholds and emits alerts to the dashboard and optionally to webhook endpoints.

### Patient Management
Manage patient profiles linked to signal records. Associate device assignments, review per-patient signal timelines, and generate summary reports.

### Data Export
Export raw or processed signal data as CSV or JSON for use in external tools, statistical packages, or research workflows.

### Secure Access Control
JWT-based authentication with role-differentiated access (Admin, Clinician, Researcher). All patient data endpoints require authenticated sessions.

---

## Project Structure

```
MedSignal-Tracker/
│
├── client/                          # React frontend application
│   ├── components/                  # Reusable UI components
│   │   ├── SignalChart.jsx           #   Waveform rendering component
│   │   ├── AlertPanel.jsx            #   Real-time alert display
│   │   └── PatientCard.jsx           #   Patient profile widget
│   ├── pages/                       # Route-level page components
│   │   ├── Dashboard.jsx             #   Main monitoring dashboard
│   │   ├── PatientView.jsx           #   Per-patient signal history
│   │   └── Settings.jsx              #   Threshold & device config
│   ├── hooks/                       # Custom React hooks (WebSocket, data fetch)
│   ├── styles/                      # Tailwind config and global CSS
│   └── package.json
│
├── server/                          # Node.js / Express API server
│   ├── controllers/                 # Route handler logic
│   │   ├── signalController.js       #   Signal CRUD and streaming
│   │   ├── patientController.js      #   Patient management
│   │   └── alertController.js        #   Alert creation and retrieval
│   ├── routes/                      # Express route definitions
│   │   ├── signalRoutes.js
│   │   ├── patientRoutes.js
│   │   └── authRoutes.js
│   ├── models/                      # Mongoose / DB schema definitions
│   │   ├── Signal.js                 #   Time-series signal document schema
│   │   ├── Patient.js                #   Patient profile schema
│   │   └── Alert.js                  #   Alert record schema
│   ├── services/                    # Business logic, third-party integrations
│   │   ├── signalProcessor.js        #   Calls Python DSP scripts
│   │   └── alertService.js           #   Threshold evaluation logic
│   ├── middleware/                  # Auth, error handling, validation
│   └── index.js                     # Server entry point
│
├── scripts/                         # Python signal processing modules
│   ├── processing/
│   │   ├── filter.py                 #   Band-pass and noise filtering
│   │   ├── normalize.py              #   Signal normalization
│   │   └── resample.py               #   Sample rate standardization
│   └── simulation/
│       └── generate_signal.py        #   Synthetic ECG/EEG data generator for testing
│
├── data/
│   ├── raw/                         # Unprocessed ingested signal files
│   └── processed/                   # Filter-applied, normalized outputs
│
├── docs/                            # Architecture diagrams, API reference
│
├── tests/
│   ├── server/                      # Jest API and service tests
│   └── scripts/                     # pytest for Python processing modules
│
├── .env.example                     # Environment variable template
├── docker-compose.yml               # Multi-service local development stack
├── Dockerfile                       # Production container image
├── package.json                     # Root-level scripts and dependencies
└── README.md
```

---

## Installation

### Prerequisites

| Requirement | Version |
|---|---|
| Node.js | 18 LTS or higher |
| Python | 3.10 or higher |
| MongoDB | 6.0 (local or Atlas) |
| Docker (optional) | 24.x |
| Git | Any recent version |

---

### Option A — Docker (Recommended)

The fastest way to get a working local environment.

```bash
git clone https://github.com/CoderNived/MedSignal-Tracker.git
cd MedSignal-Tracker

cp .env.example .env
# Edit .env with your MongoDB URI and JWT secret

docker-compose up --build
```

Services will be available at:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5000`
- MongoDB: `localhost:27017`

---

### Option B — Manual Setup

**1. Clone the repository**

```bash
git clone https://github.com/CoderNived/MedSignal-Tracker.git
cd MedSignal-Tracker
```

**2. Configure environment variables**

```bash
cp .env.example .env
```

Edit `.env`:

```env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/medsignal
JWT_SECRET=your_secret_key_here
JWT_EXPIRY=7d
ALERT_WEBHOOK_URL=          # Optional: POST target for alert notifications
```

**3. Install backend dependencies**

```bash
cd server
npm install
```

**4. Install frontend dependencies**

```bash
cd ../client
npm install
```

**5. Install Python processing dependencies**

```bash
cd ../scripts
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

**6. Start the development stack**

```bash
# Terminal 1 — Backend API
cd server && npm run dev

# Terminal 2 — Frontend
cd client && npm start

# Terminal 3 — MongoDB (if running locally)
mongod --dbpath /data/db
```

---

## Usage

### Ingest a Signal Record

```bash
curl -X POST http://localhost:5000/api/signals \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_jwt_token>" \
  -d '{
    "patientId": "PAT-00123",
    "signalType": "ECG",
    "deviceId": "DEV-ECG-7",
    "sampleRate": 500,
    "unit": "mV",
    "timestamp": "2025-09-01T10:32:00Z",
    "samples": [0.12, 0.15, 0.22, 0.89, 1.24, 0.91, 0.18, 0.11]
  }'
```

### Query Signal History

```bash
curl "http://localhost:5000/api/signals?patientId=PAT-00123&signalType=ECG&from=2025-09-01&to=2025-09-07" \
  -H "Authorization: Bearer <your_jwt_token>"
```

### Export Data as CSV

```bash
curl "http://localhost:5000/api/signals/export?patientId=PAT-00123&format=csv" \
  -H "Authorization: Bearer <your_jwt_token>" \
  -o patient_ecg_export.csv
```

### Run Signal Processing Manually

```bash
cd scripts
python processing/filter.py \
  --input ../data/raw/ecg_pat00123.json \
  --output ../data/processed/ecg_pat00123_filtered.json \
  --lowcut 0.5 \
  --highcut 40.0 \
  --samplerate 500
```

### Run Tests

```bash
# API tests
cd server && npm test

# Python processing tests
cd scripts && pytest tests/ -v
```

---

## Example Data Flow

### Input — Raw Ingested Signal

```json
{
  "patientId": "PAT-00123",
  "signalType": "ECG",
  "timestamp": "2025-09-01T10:32:00.000Z",
  "sampleRate": 500,
  "unit": "mV",
  "samples": [0.08, 0.09, 0.22, 0.95, 1.31, 0.88, 0.15, 0.09, 0.08]
}
```

### Processing Steps

```
1. Band-pass filter applied (0.5 Hz – 40 Hz) → baseline wander removed
2. Z-score normalization → signal scaled to zero mean, unit variance
3. QRS peak detection → R-R intervals extracted
4. Heart rate derived: 72 bpm
5. Threshold check: HR within bounds [50, 100] → no alert triggered
```

### Output — Processed Signal Document (MongoDB)

```json
{
  "_id": "64e2f3a1b4c9d12e8f001234",
  "patientId": "PAT-00123",
  "signalType": "ECG",
  "timestamp": "2025-09-01T10:32:00.000Z",
  "sampleRate": 500,
  "unit": "mV",
  "rawSamples": [...],
  "processedSamples": [...],
  "derivedMetrics": {
    "heartRate": 72,
    "rrIntervalMs": 833,
    "peakCount": 6
  },
  "anomalyDetected": false,
  "processingVersion": "1.4.2"
}
```

### Dashboard Output

- Live waveform rendered in the ECG panel
- Heart rate badge updated to **72 bpm**
- Signal quality score displayed: **Good**
- No alert triggered; alert history unchanged

---

## Security & Privacy Considerations

Medical signal data is among the most sensitive categories of personal information. The following controls are implemented or recommended for deployment.

### Authentication & Authorization

- All API endpoints require a valid JWT bearer token
- Tokens expire after a configurable window (default: 7 days)
- Role-based access control: `ADMIN`, `CLINICIAN`, `RESEARCHER` — each with scoped permissions
- Password hashing via bcrypt with configurable work factor

### Data Encryption

| Layer | Control |
|---|---|
| Data in transit | TLS 1.2+ enforced on all API endpoints (configure via reverse proxy in production) |
| Data at rest | MongoDB encryption-at-rest enabled in production deployments |
| Environment secrets | Managed via `.env` files; never committed to version control |

### Compliance Considerations

> **Disclaimer:** MedSignal-Tracker is an open-source tool and does not constitute a certified medical device or HIPAA-compliant platform out of the box. Organizations deploying this system in clinical contexts are responsible for their own compliance obligations.

Recommended practices for regulated environments:

- Deploy behind a HIPAA-eligible cloud infrastructure (e.g., AWS GovCloud, Azure for Healthcare)
- Implement audit logging for all data access events
- Apply data minimization — only store the signals required for the use case
- Establish a data retention and deletion policy aligned with applicable regulations
- Engage a qualified compliance officer before clinical deployment

---

## Future Improvements

| Feature | Description | Priority |
|---|---|---|
| ML-based anomaly detection | Train classifiers (LSTM, Isolation Forest) on historical signal data to flag anomalies beyond simple thresholds | High |
| Predictive health analytics | Forecast adverse events based on signal trends using time-series models | High |
| IoT sensor integration | Native MQTT broker support for direct device-to-platform data streams | Medium |
| Cloud deployment templates | Terraform modules for AWS / GCP / Azure one-click deployment | Medium |
| Mobile application | React Native companion app for clinician alert review and patient summaries | Medium |
| Multi-patient dashboard | Simultaneous monitoring of signal feeds across a patient cohort | High |
| HL7 / FHIR support | Standardized healthcare data interchange format for EHR integration | Low |
| Signal annotation tools | Allow clinicians to mark regions of interest directly on waveforms | Low |

---

## Contributing

Contributions from engineers, clinicians, researchers, and domain experts are welcome. Please follow the workflow below to keep the codebase maintainable and reviewable.

### Workflow

1. **Fork** the repository on GitHub

2. **Create a feature branch** off `main`
   ```bash
   git checkout -b feature/ecg-peak-detection
   ```

3. **Write code and tests.** Every new module should include corresponding unit tests.

4. **Lint and test before pushing**
   ```bash
   # JavaScript
   npm run lint && npm test

   # Python
   flake8 scripts/ && pytest tests/
   ```

5. **Commit with a clear, conventional message**
   ```bash
   git commit -m "feat(processing): add QRS peak detection to ECG filter module"
   ```

6. **Open a Pull Request** against `main`. Include:
   - A description of the change and its motivation
   - Test results or screenshots
   - Any relevant issue numbers (`Closes #42`)

### Standards

- Follow [PEP 8](https://peps.python.org/pep-0008/) for Python and the project ESLint config for JavaScript
- All public functions must have docstrings (Python) or JSDoc comments (JavaScript)
- Do not commit `.env` files, secrets, or patient data — use `.gitignore`
- Data files larger than 1 MB should not be committed; use a data registry or object storage

### Reporting Issues

Open a [GitHub Issue](https://github.com/CoderNived/MedSignal-Tracker/issues) with:
- A clear title and description
- Steps to reproduce
- Expected vs. actual behavior
- Environment details (OS, Node/Python version, Docker version)

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for the full text.

> This software is provided for research and educational purposes. It is **not** a certified medical device. Clinical use requires independent validation and regulatory compliance review.

---

## Author

**Nived** — [@CoderNived](https://github.com/CoderNived)

If MedSignal-Tracker is useful to your work, consider starring the repository ⭐ — it helps others in the biomedical and engineering communities find the project.

---

<div align="center">

Built with precision for the intersection of software engineering and healthcare · [Report a Bug](https://github.com/CoderNived/MedSignal-Tracker/issues) · [Request a Feature](https://github.com/CoderNived/MedSignal-Tracker/issues)

</div>
