# Static Code Analysis Issue Log
**Student:** Pratham P Shetty  
**SRN:** PES2UG24CS370  
**Repository:** https://github.com/SETAPESU26/L5_02_retail_pos

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Unsafe `eval()` | Security / High | 343 | Promo-code input was evaluated as arbitrary Python code. | Replaced with a restricted AST evaluator supporting only `total`, numeric constants, and basic arithmetic. |
| Broad bare `except` | Reliability | 325–327 | Any error was silently treated as a zero-priced item, hiding unknown products and type errors. | Validate product names and quantities and raise a clear `ValueError`. |
| Mutable default argument | Correctness | 313 | `receipts=[]` was shared across calls. | Changed default to `None` and initialize a fresh list inside the function. |
| File handle not closed | Reliability | 359–363 | Receipt log was opened without a context manager. | Used `Path.open()` in a `with` block and specified UTF-8 encoding. |
| Broad exception and `pass` | Reliability | 347–355 | Stock update swallowed all failures and did not validate item or quantity. | Validate item and non-zero integer quantity; report through logging. |
| Invalid checkout inputs | Correctness | 374–376 | Negative quantity and invalid tax rate could produce invalid bills. | Validate positive integer quantities and tax rate range. |
| Old-style formatting / naming | Style | 335, 365–367 | `%` formatting and `printSales` naming reduced consistency. | Used f-strings and renamed to `print_sales`. |
| Unused import | Style | 300 | `json` was imported but not used. | Removed the import. |

**Verification note:** The repository starter was inspected from GitHub. This environment could not install or execute Pylint, Bandit, or Flake8, so the PDF contains clearly labelled review findings and commands rather than fabricated tool output. Run the commands locally to obtain authentic reports.
