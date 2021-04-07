#Maps a symbol to a tuple (address, pairID) - find the pairID by inspecting the network traffic response
SYMBOLS_URL = {
            # Forex
            "USDJPY": ("https://www.investing.com/currencies/usd-jpy", 3),
            "AUDCAD": ("https://www.investing.com/currencies/aud-cad", 47),
            "AUDCHF": ("https://www.investing.com/currencies/aud-chf", 48),
            "AUDJPY": ("https://www.investing.com/currencies/aud-jpy", 49),
            "AUDNZD": ("https://www.investing.com/currencies/aud-nzd", 50),
            "AUDUSD": ("https://www.investing.com/currencies/aud-usd", 5),
            "CADCHF": ("https://www.investing.com/currencies/cad-chf", 14),
            "CADJPY": ("https://www.investing.com/currencies/cad-jpy", 51),
            "CHFHUF": ("https://www.investing.com/currencies/chf-huf", 90),
            "CHFJPY": ("https://www.investing.com/currencies/chf-jpy", 51),
            "CHFPLN": ("https://www.investing.com/currencies/chf-pln", 86),
            "EURAUD": ("https://www.investing.com/currencies/eur-aud", 15),
            "EURCAD": ("https://www.investing.com/currencies/eur-cad", 16),
            "EURCHF": ("https://www.investing.com/currencies/eur-chf", 10),
            "EURCNH": ("https://www.investing.com/currencies/eur-cnh", 1623),
            "EURCZK": ("https://www.investing.com/currencies/eur-czk", 156),
            "EURGBP": ("https://www.investing.com/currencies/eur-gbp", 6),
            "EURHUF": ("https://www.investing.com/currencies/eur-huf", 117),
            "EURJPY": ("https://www.investing.com/currencies/eur-jpy", 9),
            "EURMXN": ("https://www.investing.com/currencies/eur-mxn", 101),
            "EURNOK": ("https://www.investing.com/currencies/eur-nok", 37),
            "EURNZD": ("https://www.investing.com/currencies/eur-nzd", 52),
            "EURPLN": ("https://www.investing.com/currencies/eur-pln", 46),
            "EURRON": ("https://www.investing.com/currencies/eur-ron", 1689),
            "EURRUB": ("https://www.investing.com/currencies/eur-rub", 1691),
            "EURSEK": ("https://www.investing.com/currencies/eur-sek", 61),
            "EURTRY": ("https://www.investing.com/currencies/eur-try", 66),
            "EURUSD": ("https://www.investing.com/currencies/eur-usd", 1),

            "USDMXN": ("https://www.investing.com/currencies/usd-mxn", 39),
            "USDJPY": ("https://www.investing.com/currencies/usd-jpy", 3),
            "USDCHF": ("https://www.investing.com/currencies/usd-chf", 4),
            "USDCAD": ("https://www.investing.com/currencies/usd-cad", 7),
            "GBPUSD": ("https://www.investing.com/currencies/gbp-usd", 2),
            "AUDUSD": ("https://www.investing.com/currencies/aud-usd", 5),

            # Indices
            "DE30": ("https://www.investing.com/indices/germany-30", 172),
            "EU50": ("https://www.investing.com/indices/eu-stocks-50-futures", 8867),
            "UK100": ("https://www.investing.com/indices/uk-100", 27),
            "US30": ("https://www.investing.com/indices/us-30", 169),
            "US500": ("https://www.investing.com/indices/us-spx-500", 166),
            # Crypto
            "BTCUSD": ("https://www.investing.com/crypto/bitcoin/btc-usd", 945629),
            "ETHUSD": ("https://www.investing.com/crypto/ethereum/eth-usd", 997650),
            "ETHBTC": ("https://www.investing.com/crypto/ethereum/eth-btc", 1010776),
            "ADABTC": ("https://www.investing.com/crypto/cardano/ada-btc", 1055844),
            "BCHBTC": (
                "https://www.investing.com/crypto/bitcoin-cash/bch-btc",
                1031042,
            ),
            "BCHUSD": (
                "https://www.investing.com/crypto/bitcoin-cash/bch-usd",
                1058255,
            ),
            "DASH": ("https://www.investing.com/crypto/dash/dash-usd", 1010785),
            "DSHBTC": ("https://www.investing.com/crypto/dash/dash-btc", 1010783),
            "EOS": ("https://www.investing.com/crypto/eos/eos-usd", 1119415),
            "EOSBTC": ("https://www.investing.com/crypto/eos/eos-btc", 1129125),
            "EOSETH": ("https://www.investing.com/crypto/eos/eos-eth", 1058146),
            # Stocks
            "GME": ("https://www.investing.com/equities/gamestop-corp", 13845),
            # Commodities
            "NATGAS": (
                "https://www.investing.com/commodities/natural-gas-technical",
                8862,
            ),
            "SILVER": ("https://www.investing.com/commodities/silver", 8836),
            "GOLD": ("https://www.investing.com/commodities/gold", 8830),
            "NATGAS": ("https://www.investing.com/commodities/gold", 8862),
        }

XTB_TO_INVESTING={
    "BITCOIN":"BTCUSD",
    "ETHEREUM":"ETHUSD"
}
