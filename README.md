# Selenium Python Automation Framework

A scalable and maintainable Selenium Automation Framework built with **Python**, **Pytest**, and the **Page Object Model (POM)** design pattern.

This project demonstrates industry-standard automation testing practices, including data-driven testing, logging, reporting, screenshots, and cross-browser execution.

---

# Features

- Selenium WebDriver
- Python + Pytest
- Page Object Model (POM)
- Base Page Architecture
- Driver Factory Pattern
- Explicit Waits
- Cross Browser Testing
  - Chrome
  - Edge
  - Firefox
- Configuration Management (JSON)
- Screenshot Capture on Test Failure
- Logging
- HTML Test Reports
- Pytest Markers
- Parametrized Tests
- Data-Driven Testing
  - JSON
  - Excel (.xlsx)
  - CSV

---

# Project Structure

```
selenium-python-framework/
│
├── logs/
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── reports/
├── screenshots/
│
├── testdata/
│   ├── login_data.json
│   ├── login_data.xlsx
│   └── login_data.csv
│
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   ├── test_markers.py
│   ├── test_parametrize.py
│   ├── test_excel_reader.py
│   └── test_csv_reader.py
│
├── utils/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── driver_factory.py
│   ├── excel_reader.py
│   ├── json_reader.py
│   ├── logger.py
│   └── screenshot.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python 3.12
- Selenium
- Pytest
- OpenPyXL
- pytest-html
- Git
- GitHub

---

# Installation

Clone the repository

```bash
git clone https://github.com/F-A-Sweet/selenium-python-framework.git
```

Go to the project directory

```bash
cd selenium-python-framework
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run all tests

```bash
pytest -v
```

Run Chrome

```bash
pytest -v --browser chrome
```

Run Edge

```bash
pytest -v --browser edge
```

Run Smoke Tests

```bash
pytest -v -m smoke
```

Run Regression Tests

```bash
pytest -v -m regression
```

Run HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

# Test Data Sources

The framework supports multiple data sources.

- JSON
- Excel (.xlsx)
- CSV

Example login data:

| Username | Password | Expected |
|----------|----------|----------|
| Admin | admin123 | True |
| Admin | wrong123 | False |
| WrongUser | admin123 | False |

---

# Reports

The framework generates:

- HTML Reports
- Screenshots on Failure
- Automation Logs

Generated folders:

```
reports/
screenshots/
logs/
```

---

# Framework Highlights

- Clean Page Object Model architecture
- Reusable Base Page methods
- Centralized Driver Factory
- Externalized test data
- Easy browser switching
- Easy maintenance
- Scalable project structure

---

# Current Learning Progress

Completed

- Git & GitHub
- Selenium WebDriver
- Pytest
- Page Object Model
- Base Page
- Driver Factory
- Config Reader
- JSON Reader
- Excel Reader
- CSV Reader
- Logging
- Screenshot Utility
- HTML Reports
- Cross Browser Testing
- Data-Driven Testing
- Pytest Markers
- Parametrized Tests

---

# Planned Improvements

- API Testing
- Database Testing
- Parallel Execution (pytest-xdist)
- Allure Reports
- Jenkins CI/CD
- GitHub Actions
- Docker
- Selenium Grid

---

# Author

**Ferdous Ahmmed**

QA Automation Engineer

GitHub:
https://github.com/F-A-Sweet

---

# License

This project is created for learning and portfolio purposes.