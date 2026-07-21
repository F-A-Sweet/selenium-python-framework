# Selenium Python Automation Framework

A professional Selenium Automation Framework built with **Python**, **Pytest**, and **Page Object Model (POM)**. The framework follows industry best practices such as Driver Factory, Base Page, Fixture Chaining, Page Transition Pattern, Data-Driven Testing, Logging, HTML Reporting, and Screenshot Capture.

---

## Features

- Selenium WebDriver
- Python 3
- Pytest
- Page Object Model (POM)
- Base Page Pattern
- Driver Factory Pattern
- Fixture Chaining
- Page Transition Pattern
- Data-Driven Testing
- CSV Test Data
- Excel Test Data
- JSON Test Data
- Config Reader
- Explicit Waits
- Logging
- Screenshot on Failure
- HTML Test Reports
- Cross Browser Testing (Chrome, Edge, Firefox)
- Smoke & Regression Test Execution

---

## Project Structure

```text
selenium-python-framework/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
│
├── tests/
│   ├── test_homepage.py
│   ├── test_login.py
│   ├── test_dashboard.py
│   ├── test_logout.py
│   ├── test_csv_reader.py
│   ├── test_excel_reader.py
│   ├── test_markers.py
│   └── test_parametrize.py
│
├── utils/
│   ├── config_reader.py
│   ├── csv_reader.py
│   ├── excel_reader.py
│   ├── json_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── screenshot.py
│
├── testdata/
│   ├── login_data.json
│   ├── login_data.csv
│   └── login_data.xlsx
│
├── reports/
├── screenshots/
├── logs/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Framework Flow

```text
Driver
   │
Homepage Fixture
   │
Login Page Fixture
   │
Dashboard Page Fixture
   │
Tests
```

---

## Design Patterns Used

- Page Object Model (POM)
- Base Page Pattern
- Driver Factory Pattern
- Fixture Chaining
- Page Transition Pattern
- Data-Driven Testing

---

## Test Data Sources

- JSON
- Excel (.xlsx)
- CSV

---

## Test Execution

Run all tests

```bash
pytest -v
```

Run smoke tests

```bash
pytest -v -m smoke
```

Run regression tests

```bash
pytest -v -m regression
```

Run login tests

```bash
pytest -v tests/test_login.py
```

Run with Chrome

```bash
pytest --browser chrome
```

Run with Edge

```bash
pytest --browser edge
```

Run with Firefox

```bash
pytest --browser firefox
```

Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Reports & Logs

- HTML Test Report
- Screenshot Capture on Failure
- Automation Logs
- Pytest Console Report

---

## Technologies Used

- Python
- Selenium
- Pytest
- OpenPyXL
- CSV
- JSON
- Logging
- Pytest HTML

---

## Current Framework Capabilities

- Login Automation
- Dashboard Validation
- Logout Automation
- Homepage Validation
- CSV Data-Driven Testing
- Excel Data-Driven Testing
- JSON Data-Driven Testing
- Parameterized Tests
- Smoke Testing
- Regression Testing
- Cross Browser Execution
- HTML Reporting
- Screenshot Capture
- Logging
- Reusable Fixtures
- Page Object Model
- Page Transition Pattern

---

## Author

**Ferdous Ahmmed**

QA Automation Engineer | Python | Selenium | Pytest