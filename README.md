# Selenium Python Automation Framework

A professional Selenium Automation Framework built with Python and Pytest following industry-standard design patterns such as Page Object Model (POM), Driver Factory, Base Page, and Configuration Management.

---

## 🚀 Features

- Python + Selenium WebDriver
- Pytest Test Framework
- Page Object Model (POM)
- Base Page Design Pattern
- Driver Factory
- JSON Configuration Management
- Cross Browser Support
- Git & GitHub Integration

---

## 🛠 Tech Stack

- Python 3.12
- Selenium
- Pytest
- WebDriver Manager (Coming Soon)
- Git
- GitHub

---

## 📁 Project Structure

```text
selenium-python-framework/
│
├── config/
│   └── config.json
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── reports/
├── screenshots/
├── testdata/
│
├── tests/
│   ├── test_google.py
│   └── test_login.py
│
├── utils/
│   ├── config_reader.py
│   └── driver_factory.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/F-A-Sweet/selenium-python-framework.git
```

Go to project

```bash
cd selenium-python-framework
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Tests

Chrome

```bash
pytest --browser chrome
```

Edge

```bash
pytest --browser edge
```

Firefox

```bash
pytest --browser firefox
```

---

## 📌 Current Features

- Google Search Test
- OrangeHRM Login Test
- Driver Factory
- Base Page
- Page Object Model
- Config Reader

---

## 📅 Roadmap

- Explicit Waits
- Logging
- Screenshot on Failure
- HTML Reports
- Allure Reports
- Data Driven Testing
- Parallel Execution
- GitHub Actions
- Docker
- Jenkins

---

## 👨‍💻 Author

**Ferdous Ahmmed**

GitHub:
https://github.com/F-A-Sweet