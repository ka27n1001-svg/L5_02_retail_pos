# SE Lab 5 Deliverables — Static Code Analysis
Student: Pratham P Shetty  
SRN: PES2UG24CS370

## Files
- `pos_system.py` — cleaned version of the starter POS program.
- `issues.md` — issue table and fix descriptions.
- `reflection.md` — answers to the four reflection questions.
- `static_analysis_tools_report.pdf` — commands and review findings for Pylint, Bandit, and Flake8.

## Run the tools locally
```bash
python -m pip install pylint bandit flake8
pylint pos_system.py > pylint_report.txt
bandit -r pos_system.py > bandit_report.txt
flake8 pos_system.py > flake8_report.txt
```
The three tools' authentic output files are not included because those tools could not be installed/run in the current environment. The PDF explicitly distinguishes code-review findings from actual tool output.

Repository: https://github.com/SETAPESU26/L5_02_retail_pos
