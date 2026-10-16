"""Retail point-of-sale and discount tracker.

Demonstrates checkout totals, promo codes, stock updates, and receipt logging.
"""
import ast
import logging
import random
from pathlib import Path
from typing import Iterable

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
LOGGER = logging.getLogger(__name__)

PRICE_LIST = {"pen": 10.0, "notebook": 45.0, "bag": 799.0, "bottle": 150.0}
sales_total = 0.0
receipt_lines = []


def process_checkout(cart_items: Iterable[tuple], tax_rate: float = 0.05,
                     receipts: list | None = None) -> float:
    """Calculate a checkout total and record a receipt.

    Unknown products and invalid quantities are rejected rather than silently
    ignored. Tax rates must be between zero and one.
    """
    global sales_total
    if not 0 <= tax_rate <= 1:
        raise ValueError("tax_rate must be between 0 and 1")
    if receipts is None:
        receipts = []

    subtotal = 0.0
    for item, quantity in cart_items:
        if item not in PRICE_LIST:
            raise ValueError(f"Unknown product: {item}")
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError(f"Quantity for {item} must be a positive integer")
        subtotal += PRICE_LIST[item] * quantity

    total = subtotal * (1 + tax_rate)
    receipts.append(total)
    sales_total += total
    receipt_lines.append(f"Receipt #{random.randint(1000, 9999)} total={total:.2f}")
    return total


def apply_promo_code(code_str: str) -> float:
    """Apply a restricted arithmetic promo expression without eval()."""
    global sales_total
    try:
        expression = ast.parse(code_str, mode="eval").body
    except SyntaxError as exc:
        raise ValueError("Invalid promo expression") from exc

    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.Name) and node.id == "total":
            return sales_total
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div)):
            left, right = evaluate(node.left), evaluate(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if right == 0:
                raise ValueError("Division by zero in promo expression")
            return left / right
        raise ValueError("Promo may only use total, numbers, and + - * /")

    result = evaluate(expression)
    if result < 0:
        raise ValueError("Promo result cannot be negative")
    return result


def update_stock(item: str, qty: int) -> None:
    """Validate and report a stock adjustment (stock quantities are not modeled)."""
    if item not in PRICE_LIST:
        raise ValueError(f"Unknown product: {item}")
    if not isinstance(qty, int) or isinstance(qty, bool) or qty == 0:
        raise ValueError("Stock adjustment must be a non-zero integer")
    LOGGER.info("Stock updated for %s by %d", item, qty)


def save_receipt_log(file: str = "pos_log.txt") -> None:
    """Append receipts to a log and close the file reliably."""
    with Path(file).open("a", encoding="utf-8") as receipt_file:
        for line in receipt_lines:
            receipt_file.write(line + "\n")


def print_sales() -> None:
    """Print the running sales total."""
    print(f"Sales so far: {sales_total:.2f}")


def main() -> None:
    """Run a small demonstration of the point-of-sale workflow."""
    print("Bill 1:", process_checkout([("pen", 3), ("notebook", 2)]))
    print("Bill 2:", process_checkout([("bag", 1)]))
    update_stock("pen", 5)
    print("After promo:", apply_promo_code("total * 0.9"))
    code = input("Enter promo code (e.g. total - 50): ").strip() or "total - 50"
    try:
        print("After your promo:", apply_promo_code(code))
    except ValueError as exc:
        LOGGER.warning("Promo rejected: %s", exc)
    save_receipt_log()
    print_sales()


if __name__ == "__main__":
    main()
