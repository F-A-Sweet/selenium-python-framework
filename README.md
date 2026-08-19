# Selenium Python Automation Framework

A professional Selenium WebDriver automation framework built with **Python**, **Pytest**, and the **Page Object Model (POM)**.

The framework is designed with reusable page objects, centralized WebDriver management, fixture chaining, data-driven testing, configuration management, logging, failure screenshots, and cross-browser execution.

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
- JSON Reader Support
- Configuration Management
- Environment-based Test Credentials
- Explicit Waits
- Logging
- Screenshot Capture on Test Failure
- HTML Test Reports
- Cross-Browser Testing
- Smoke Test Execution
- Regression Test Execution

---

## Project Structure

```text
selenium-python-framework/
│
├── config/
│   └── config.json
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
│   ├── test_login_logout_flow.py
│   ├── test_csv_reader.py
│   └── test_excel_reader.py
│
├── testdata/
│   ├── login_data.json
│   ├── login_data.csv
│   └── login_data.xlsx
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
├── reports/
├── screenshots/
├── logs/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Framework Architecture

```text
                    Pytest
                       │
                       ▼
                  conftest.py
                       │
                       ▼
                 Driver Factory
                       │
                       ▼
                    WebDriver
                       │
                       ▼
                Homepage Fixture
                       │
                       ▼
                 LoginPage Fixture
                       │
                       ▼
                DashboardPage
                       │
                       ▼
                     Tests
```

---

## Page Object Model

The framework separates test logic from Selenium implementation.

### BasePage

Provides reusable browser operations such as:

- Click
- Type
- Wait for element
- Wait for clickable element
- Get text
- Check visibility
- URL validation
- Title validation
- Scrolling
- JavaScript interactions

### LoginPage

Handles:

- Username input
- Password input
- Login action
- Login error validation

### DashboardPage

Handles:

- Dashboard validation
- Profile menu
- Logout
- Page transition back to LoginPage

---

## Fixture Chaining

Pytest fixtures are chained to create the required page objects.

```text
driver
  │
  ▼
homepage
  │
  ▼
login_page
  │
  ▼
dashboard_page
```

This keeps test cases clean and avoids repeating browser setup and login logic.

---

## Page Transition Pattern

Page actions return the next Page Object when appropriate.

Example:

```python
dashboard_page = login_page.login(
    username,
    password
)
```

After logout:

```python
login_page = dashboard_page.logout()
```

This allows tests to work with page objects instead of directly managing WebDriver navigation.

---

## Data-Driven Testing

Login testing uses Pytest parametrization with external test data.

Current login test data is loaded from CSV:

```text
testdata/login_data.csv
        │
        ▼
    CSVReader
        │
        ▼
@pytest.mark.parametrize
        │
        ▼
     test_login
```

Example:

```python
@pytest.mark.parametrize("data", test_data)
def test_login(login_page, data):
    ...
```

The framework also includes readers for:

- CSV
- Excel
- JSON

---

## Configuration Management

Framework configuration is stored in:

```text
config/config.json
```

Example configuration:

```json
{
    "base_url": "https://opensource-demo.orangehrmlive.com/",
    "browser": "chrome",
    "implicit_wait": 10
}
```

Configuration values are accessed through `ConfigReader`.

---

## Environment Variables

Test credentials are loaded from environment variables rather than being stored directly in the test code.

Example:

```text
TEST_USERNAME
TEST_PASSWORD
```

The `.env` file is excluded from Git through `.gitignore`.

This prevents sensitive test credentials from being committed to the repository.

---

## Cross-Browser Testing

The framework supports:

- Chrome
- Firefox
- Edge

Browser selection is handled through the Pytest command-line option.

---

## Test Execution

## CI Verification

GitHub Actions CI pipeline runs the Pytest suite and uploads HTML reports, screenshots, and logs as artifacts.

## Continuous Integration

This framework uses GitHub Actions to automatically execute the Pytest test suite on every push and pull request to the `main` branch.

The CI pipeline:

- Installs Python dependencies
- Runs Pytest tests
- Generates a self-contained HTML test report
- Captures screenshots for failed tests
- Stores test reports, screenshots, and logs as GitHub Actions artifacts

### Run all tests

```bash
pytest -v
```

### Run smoke tests

```bash
pytest -v -m smoke
```

### Run regression tests

```bash
pytest -v -m regression
```

### Run login tests

```bash
pytest -v tests/test_login.py
```

### Run with Chrome

```bash
pytest -v --browser chrome
```

### Run with Edge

```bash
pytest -v --browser edge
```

### Run with Firefox

```bash
pytest -v --browser firefox
```

### Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Logging

The framework uses Python's built-in `logging` module.

Logs are stored in:

```text
logs/Automation.log
```

Example log format:

```text
2026-01-01 12:00:00 | INFO | Entering username
2026-01-01 12:00:01 | INFO | Entering password
2026-01-01 12:00:02 | INFO | Clicking login
```

---

## Screenshot on Failure

When a test fails, the Pytest reporting hook captures a screenshot automatically.

Screenshots are stored in:

```text
screenshots/
```

The filename contains the test name and timestamp.

---

## Current Test Coverage

The current suite covers:

- Homepage validation
- Successful login
- Invalid login credentials
- Dashboard validation
- Logout
- Login → Dashboard → Logout flow
- CSV reader validation
- Excel reader validation

Latest full-suite verification:

```text
9 passed
```

---

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- OpenPyXL
- python-dotenv
- CSV
- JSON
- Python Logging
- pytest-html

---

## Design Patterns and Practices

- Page Object Model
- Base Page Pattern
- Driver Factory Pattern
- Fixture Chaining
- Page Transition Pattern
- Data-Driven Testing
- Explicit Waits
- Configuration Management
- Environment Variables
- Failure Screenshot Capture
- Centralized Logging

---

## Author

**Ferdous Ahmmed**

QA Automation Engineer

**Skills:** Python | Selenium | Pytest | Test Automation