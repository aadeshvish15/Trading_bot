# bot/config.py
TESTNET_BASE = "https://testnet.binancefuture.com"
FAPI_V1 = "/fapi/v1"
FAPI_V2 = "/fapi/v2"

# full endpoints (examples)
ORDER = f"{TESTNET_BASE}{FAPI_V1}/order"
OPEN_ORDERS = f"{TESTNET_BASE}{FAPI_V1}/openOrders"
ACCOUNT = f"{TESTNET_BASE}{FAPI_V2}/account"

