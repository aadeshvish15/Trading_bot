# cli.py (outline)
import argparse
from bot.logging_config import setup_logger
from bot.validators import *
# validators now include notional check for minimum order value
from bot.orders import OrderService

def main():
    setup_logger()
    parser = argparse.ArgumentParser(prog="trading_bot")
    sub = parser.add_subparsers(dest="cmd")

    # market
    p_market = sub.add_parser("market")
    p_market.add_argument("--symbol", required=True)
    p_market.add_argument("--side", required=True)
    p_market.add_argument("--quantity", type=float, required=True)

    # limit
    p_limit = sub.add_parser("limit")
    p_limit.add_argument("--symbol", required=True)
    p_limit.add_argument("--side", required=True)
    p_limit.add_argument("--quantity", type=float, required=True)
    p_limit.add_argument("--price", type=float, required=True)

    # cancel
    p_cancel = sub.add_parser("cancel")
    p_cancel.add_argument("--symbol", required=True)
    p_cancel.add_argument("--orderId", type=int)

    # open orders
    p_open = sub.add_parser("open")

    args = parser.parse_args()
    service = OrderService()

    try:
        if args.cmd == "market":
            symbol = validate_symbol(args.symbol)
            side = validate_side(args.side)
            qty = validate_quantity(args.quantity)
            resp = service.market(symbol, side, qty)
            print(resp)

        elif args.cmd == "limit":
            symbol = validate_symbol(args.symbol)
            side = validate_side(args.side)
            qty = validate_quantity(args.quantity)
            price = validate_price(args.price)
            # make sure value meets exchange notional minimum
            validate_notional(symbol, qty, price)
            resp = service.limit(symbol, side, qty, price)
            print(resp)

        elif args.cmd == "cancel":
            resp = service.cancel(args.symbol, orderId=args.orderId)
            print(resp)

        elif args.cmd == "open":
            resp = service.open_orders()
            print(resp)

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()
