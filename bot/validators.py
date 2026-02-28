def validate_symbol(symbol: str):
    if not symbol:
        raise ValueError("Symbol is required.")
    return symbol.upper()


def validate_side(side: str):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")
    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")
    return order_type


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    return quantity


def validate_price(price: float):
    if price is None or price <= 0:
        raise ValueError("Valid price required for placing the order.")
    return price


def validate_notional(symbol: str, quantity: float, price: float):
    """Ensure the order's notional (qty * price) meets the exchange minimum.

+    For USDT‑M futures the minimum is usually 100 USDT; the value can be
+    overridden with the BINANCE_MIN_NOTIONAL env var if Binance changes it
+    or you want a different threshold for testing.
+    """
    try:
        min_notional = float(os.getenv("BINANCE_MIN_NOTIONAL", "100"))
    except Exception:
        min_notional = 100.0

    notional = quantity * price
    if notional < min_notional:
        raise ValueError(
            f"Notional {notional} is below minimum required {min_notional}. "
            f"increase quantity or price."
        )
    return notional
