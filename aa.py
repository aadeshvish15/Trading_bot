from binance.client import Client
import time
import json

BINANCE_API_KEY="i6cY5dOCw0cHufatGUGLRZ1rl8lMKBERclmsNCif78naP1HlEMOP56jSlIRxKNWD"
BINANCE_API_SECRET="gowb3diioC0AE6LWsNX5ydyvwJ79PTSpIE1SgkDw0xqNkT9O4pie2D1e6EaDzhBT"

client=Client(BINANCE_API_KEY,BINANCE_API_SECRET,testnet=True)
account_info = client.futures_account()

# Convert to formatted JSON string
json_data = json.dumps(account_info, indent=4)

print(json_data)