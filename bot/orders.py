# bot/orders.py
import logging
from bot.client import BinanceFuturesClient

class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def market(self, symbol, side, quantity):
        logging.info("placing market order %s %s %s", symbol, side, quantity)
        resp = self.client.place_order(symbol=symbol, side=side, type="MARKET", quantity=quantity)
        logging.info("market response: %s", resp)
        return resp

    def limit(self, symbol, side, quantity, price):
        logging.info("placing limit order %s %s %s @ %s", symbol, side, quantity, price)
        resp = self.client.place_order(symbol=symbol, side=side, type="LIMIT",
                                      quantity=quantity, price=price, timeInForce="GTC")
        logging.info("limit response: %s", resp)
        return resp

    def cancel(self, symbol, orderId=None, origClientOrderId=None):
        logging.info("cancel request %s %s %s", symbol, orderId, origClientOrderId)
        resp = self.client.cancel_order(symbol, orderId=orderId, origClientOrderId=origClientOrderId)
        logging.info("cancel response: %s", resp)
        return resp

    def open_orders(self, symbol=None):
        return self.client.get_open_orders(symbol)