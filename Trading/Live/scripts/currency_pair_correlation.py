from Trading.Live.Client.client import XTBLoggingClient
from Trading.Instrument.instrument import Instrument

from dotenv import load_dotenv
import os
import logging
import pandas as pd
import numpy as np

if __name__ == '__main__':

    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=FORMAT)

    MAIN_LOGGER = logging.getLogger('Main Logger')
    MAIN_LOGGER.setLevel(logging.DEBUG)
    MAIN_LOGGER.propagate = True

    load_dotenv()
    username = os.getenv("XTB_USERNAME")
    password = os.getenv("XTB_PASSWORD")
    mode = os.getenv("XTB_MODE")
    client = XTBLoggingClient(username, password, mode, False)

    n = 100
    eur_chf = client.getLastNCandleHistory(Instrument('EURCHF', '1D'), n)['open']
    eur_huf = client.getLastNCandleHistory(Instrument('EURHUF', '1D'), n)['open']
    chf_huf = client.getLastNCandleHistory(Instrument('CHFHUF', '1D'), n)['open']
    usd_huf = client.getLastNCandleHistory(Instrument('USDHUF', '1D'), n)['open']
    eur_usd = client.getLastNCandleHistory(Instrument('EURUSD', '1D'), n)['open']


    data = {"EURUSD" : eur_usd, "USDHUF": usd_huf}
    df = pd.DataFrame(data)
    correlation = df["EURUSD"].corr(df["USDHUF"])

    print(f"The correlation between EURUSD and USDHUF is {correlation}")