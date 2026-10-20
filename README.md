# Mintaka Data Loader

Python application for extracting data from the Mintaka REST API, converting the data to CSV, and maintaining incremental data loads using state tracking.

## Features

- Incremental data loading
- State tracking by Product ID
- Configuration via YAML
- Credentials stored securely using Windows Credential Manager (Keyring)
- CSV output generation
- Windows Task Scheduler compatible

---

## Project Structure

```text
mintaka_loader/
│
├── config/
│   └── config.yaml.example
│
├── utils/
│   └── setup_credentials.py
│
├── src/
│   ├── config_loader.py
│   ├── json_response_processor.py
│   ├── niwa_mintaka_client.py
│   ├── orchestration_layer.py
│   └── state_manager.py
│
├── requirements.txt
├── README.md
├── run.py
└── .gitignore
```

---

## Prerequisites

- Python 3.11+
- Windows Server / Windows 10+
- Access to Mintaka API

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd NIWAMintakaDataDownload
```

### Create a virtual environment

```cmd
python -m venv .venv
```

### Activate

```cmd
.venv\Scripts\activate
```

### Install dependencies

```cmd
pip install -r requirements.txt
```

---

## Configuration

Copy the sample configuration file:

```cmd
copy config\config.yaml.example config\config.yaml
```

Edit:

```yaml
api:
  base_url: "https://mintaka.niwa.co.nz/rest/api"
  api_credential: "mintaka_api"

folders:
  raw: "output/raw"
  csv: "output/csv"

state:
  file: "state/last_run.json"

logging:
  file: "logs/NIWA_Mintaka_Climate.log"
  level: "INFO"

products:
  - product_id: 123456 
    enabled: true
    initial_start_date: "2021-01-01T00:00:00Z"

  - product_id: 456789
    enabled: true
    initial_start_date: "2021-01-01T00:00:00Z"

#  - product_id: 3116539
#    enabled: false
#    initial_start_date: "2021-01-01T00:00:00Z"
```

---

## Credentials

Credentials are stored in Windows Credential Manager using Keyring.

Run once:

```cmd
python utils\setup_credentials.py
```

Enter:

```text
Username
Password
```

The credentials will be securely stored in the Windows user profile.

---

## Running the Application

```cmd
python run.py
```

---

## Task Scheduler

Configure:

### Program/script

```text
D:\mintaka_loader\.venv\Scripts\python.exe
```

### Add arguments

```text
run.py
```

### Start in

```text
D:\mintaka_loader
```

Ensure the scheduled task runs under the same Windows account used to store the Keyring credentials.

---

## State Tracking

The application maintains a state file to track the last successful load date for each Product ID.

Example:

```json
{
    "123456": "2026-10-20T02:20:00Z",
    "456789": "2026-10-20T02:20:00Z"
}
```

---

## Updating Credentials

If the Mintaka password changes:

```cmd
python utils\setup_credentials.py
```

The existing credentials will be overwritten.

---

## Troubleshooting

### Keyring credentials not found

Verify:

- Credentials were stored using `setup_credentials.py`
- Task Scheduler runs under the same Windows account

### Configuration file missing

Ensure:

```text
config/config.yaml
```

exists and contains valid settings.

### Dependency issues

Reinstall:

```cmd
pip install -r requirements.txt
```

---

## Authors
Nandakumar Thachapilly | 
Environmental Data Analyst | 
Marlborough District Council

Emma Chibnall | 
Principal Environmental Systems & Data Analyst | 
Marlborough District Council