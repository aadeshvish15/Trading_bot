# bot/client.py
import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

class BinanceFuturesClient:
    def __init__(self, testnet=True):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        if not api_key or not api_secret:
            raise RuntimeError("API key/secret missing in .env")

        # create client (python-binance). We will override FUTURES_URL for testnet.
        self.client = Client(api_key, api_secret)

        # set the futures testnet base - required for python-binance futures
        # NOTE: python-binance uses FUTURES_URL for futures endpoints
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # quick verify
        try:
            self.client.futures_ping()
        except Exception as e:
            raise RuntimeError("Futures ping failed — check keys or testnet URL") from e

    # High level wrappers used by orders.py
    def place_order(self, **kwargs):
        # kwargs: symbol, side, type, quantity, price (if LIMIT), timeInForce, etc.
        return self.client.futures_create_order(**kwargs)

    def cancel_order(self, symbol, orderId=None, origClientOrderId=None):
        return self.client.futures_cancel_order(symbol=symbol, orderId=orderId, origClientOrderId=origClientOrderId)

    def get_open_orders(self, symbol=None):
        return self.client.futures_get_open_orders(symbol=symbol)

    def get_account(self):
        return self.client.futures_account()