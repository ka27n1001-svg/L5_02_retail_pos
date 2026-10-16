# Lab 5 Reflection
**Student:** Pratham P Shetty  
**SRN:** PES2UG24CS370

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
Style issues such as unused imports, f-string formatting, and function naming were the easiest because they required small, localized edits. The hardest issue was replacing `eval()` because promo codes still needed to support useful arithmetic while preventing arbitrary code execution. Input validation also needed care so valid checkouts continued to work.

### 2. Did the static analysis tools report any false positives? If so, describe one example.
No actual tool runs were available in this environment, so I cannot honestly claim a specific false positive from Pylint, Bandit, or Flake8. A possible warning that needs human review is a style or complexity warning on a small helper function: it may be technically correct according to a rule but not necessarily indicate a runtime defect. Any such finding should be checked against the code and requirements.

### 3. How would you integrate static analysis tools into your actual software development workflow?
I would install Pylint, Bandit, and Flake8 in the project's development environment, run them before committing, and configure a CI workflow to run them on every pull request. Security findings from Bandit and correctness-related warnings would be prioritized, while style rules would be kept consistent through project configuration. I would also rerun tests after applying fixes.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
The revised code rejects unknown products and invalid quantities instead of silently producing misleading totals. It no longer evaluates promo text as arbitrary Python, validates tax and stock inputs, closes receipt files reliably, and uses clearer logging and naming. These changes make failures easier to diagnose and reduce the risk of incorrect bills.
