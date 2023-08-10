import cryptocompare

from typing import List
from app.index.utils.price_format import price_formatter


class CryptoPrices:
    def __init__(self):
        self.coins = cryptocompare.get_price(
            ["BTC", "ETH", "LTC", "BCH", "XRP", "BSV", "EOS", "XLM", "ADA", "TRX"],
            ["USD", "MXN"],
        )

    def get_name(self) -> dict:
        return self.name

    def get_prices(self) -> dict:
        coins_list: List[str] = [
            "BTC",
            "ETH",
            "USDT",
            "USDC",
            "BNB",
            "XRP",
            "BUSD",
            "ADA",
            "SOL",
            "DOGE",
        ]
        name_list: List[str] = [
            "Bitcoin",
            "Ethereum",
            "Tether",
            "USD Coin",
            "Binance Coin",
            "XRP",
            "Binance USD",
            "Cardano",
            "Solana",
            "Dogecoin",
        ]
        usd_price_list: List[float] = []
        mxn_price_list: List[float] = []

        while True:
            for coin in self.coins:
                usd_price_list.append(getting_price(self.coins[coin]["USD"]))
                mxn_price_list.append(getting_price(self.coins[coin]["MXN"]))

            break

        return {
            "coins_list": coins_list,
            "name_list": name_list,
            "usd_price_list": usd_price_list,
            "mxn_price_list": mxn_price_list,
        }


@price_formatter
def getting_price(price):
    return price