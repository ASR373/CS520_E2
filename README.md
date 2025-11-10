# CS520 - Exercise 2

This project contains implementations of several Python functions along with unit tests and code coverage analysis using **pytest** and **coverage.py**.

## ✅ Contents
- `src/` — Python source code implementations
- `tests/` — Automated test cases for each function
- `htmlcov/` — Generated HTML coverage report
- `run_tests.py` (optional runner script)

## 🧪 Running Tests
To run all tests:

```bash
pytest
```
To run tests with coverage:
```
pytest --cov=src --cov-branch --cov-report=term --cov-report=html
```

After running coverage, open the HTML report:
```
open htmlcov/index.html
```
