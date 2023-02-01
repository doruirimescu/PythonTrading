from exception_with_retry import exception_with_retry

from Trading.live.client.client import XTBTradingClient
from Trading.utils.send_email import send_email
from Trading.config.config import USERNAME, PASSWORD, MODE, MONITOR_FOREX_TRADE_SWAPS_ONCE
from dotenv import load_dotenv
from datetime import datetime
import os
import logging
from time import sleep


if __name__ == '__main__':

    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT)

    MAIN_LOGGER = logging.getLogger('Main logger')
    MAIN_LOGGER.setLevel(logging.DEBUG)
    MAIN_LOGGER.propagate = True

    load_dotenv()
    username = os.getenv("XTB_USERNAME")
    password = os.getenv("XTB_PASSWORD")
    mode = os.getenv("XTB_MODE")
    client = XTBTradingClient(USERNAME, PASSWORD, MODE, False)

    open_trade_swaps = client.get_swaps_of_forex_open_trades()
    MAIN_LOGGER.info("Open trade swaps: " + str(open_trade_swaps))

    @exception_with_retry(n_retry=10, sleep_time_s=5.0)
    def monitor_once():
        for symbol, swap in open_trade_swaps:
            if swap < 0.0:
                subject = "Swap has gone negative for " + symbol
                body = f"Symbol: {symbol} Swap: {str(swap)} Date:{str(datetime.now())}"
                send_email(subject, body)

        total_profit, total_swap, text_message = client.get_total_forex_open_trades_profit_and_swap()
        biggest_swaps = client.get_top_ten_biggest_swaps()
        subject = "Daily swap report " + str(datetime.now())
        body = text_message + f"\nTotal profit: {str(total_profit)} Total swap: {str(total_swap)}"
        body += f"\nBiggest swaps:{biggest_swaps}"
        send_email(subject, body)
        MAIN_LOGGER.info(body)

    if MONITOR_FOREX_TRADE_SWAPS_ONCE == "True":
        monitor_once()
    else:
        while True:
            hour_now = datetime.now().hour
            minute_now = datetime.now(). minute
            if hour_now == 7:
                # Each morning at 7 am
                monitor_once()
            sleep(3600)
