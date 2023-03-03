from typing import List, Tuple, Optional
import logging
import numpy as np
import pandas as pd


def are_all_items_same(items: List) -> bool:
    return all(x == items[0] for x in items)


def calculate_mean(items: List) -> float:
    return sum(items)/len(items)


def round_to_two_decimals(decimal_number: float) -> float:
    """Rounds number to two decimal points

    Args:
        decimal_number (float): number to round

    Returns:
        float: rounded number
    """
    return round(decimal_number, 2)


def calculate_mean_take_profit(open_high: List[Tuple[float, float]]) -> float:
    """Calculates mean take profit

    Args:
        open_high (List[Tuple[float, float]]): Open and high prices

    Returns:
        float: calculated mean take profit
    """
    accumulated_p = sum([(high_price / open_price - 1) for open_price, high_price in open_high])
    return accumulated_p / len(open_high)


def calculate_weighted_mean_take_profit(open_high: List[Tuple[float, float]],
                                        fast_n: int,
                                        fast_weight: int,
                                        logger: Optional[logging.Logger] = None) -> float:
    """Calculates the weighted take profit

    Args:
        open_high (List[Tuple[float, float]]): Open and high prices
        fast_n (int): Number of last n prices to calculate the fast take profit from
        fast_weight (int): Weight to give to fast take profit
        logger (logging.Logger, optional): Logger. Defaults to None.

    Returns:
        float: calculated weighted mean take profit
    """
    mean_tp_slow = calculate_mean_take_profit(open_high)
    mean_tp_fast = calculate_mean_take_profit(open_high[-fast_n:])
    weighted_tp = (mean_tp_slow + fast_weight * mean_tp_fast) / (1 + fast_weight)

    mean_tp_slow = round_to_two_decimals(mean_tp_slow)
    mean_tp_fast = round_to_two_decimals(mean_tp_fast)
    weighted_tp = round_to_two_decimals(weighted_tp)

    if logger:
        logger.info(f"Slow tp: {mean_tp_slow} Fast tp: {mean_tp_fast} Weighted tp: {weighted_tp}")
    return round_to_two_decimals(weighted_tp)


def calculate_sharpe_ratio(profits: List[float]) -> float:
    """The Sharpe ratio is a measure of risk-adjusted return that compares the
       average return of an investment to the standard deviation of its returns.
       The method takes a list of profits as input and returns the Sharpe ratio as a float.

    Args:
        profits (List[float]): list of profits/returns generated by the strategy

    Returns:
        float: mean of the profits divided by the standard deviation of the profits.
    """
    return round(np.mean(profits) / np.std(profits), 2)


def calculate_percentage_losers(profits: List[float]) -> float:
    n_losers = len([loser for loser in profits if loser < 0.0])
    if len(profits) == 0:
        return 0.0
    return round(n_losers / len(profits), 2)


def calculate_max_consecutive_losers(profits: List[float]) -> int:
    """Returns the maximum number of consecutive losers

    Args:
        profits (List[float]): list of profits

    Returns:
        int: number of maximum consecutive losing profits
    """
    max_losers = 0
    current_losers = 0
    for profit in profits:
        if profit < 0:
            current_losers += 1
        else:
            if current_losers > max_losers:
                max_losers = current_losers
            current_losers = 0
    if current_losers > max_losers:
        max_losers = current_losers
    return max_losers


def calculate_cumulative_returns(profits: List[float]) -> List[float]:
    return [sum(profits[0: i + 1]) for i, p in enumerate(profits)]


def calculate_max_drawdown(profits: List[float]) -> float:
    if len(profits) == 0:
        return 0
    cumulative_returns = calculate_cumulative_returns(profits)
    return round(min(cumulative_returns), 2)


def calculate_correlation(instrument_1_symbol: str,
                          instrument_2_symbol: str,
                          instrument_1_open: List[float],
                          instrument_2_open: List[float]) -> float:
    data = {instrument_1_symbol : instrument_1_open, instrument_2_symbol: instrument_2_open}
    df = pd.DataFrame(data)
    correlation = df[instrument_1_symbol].corr(df[instrument_2_symbol])
    print(f"The correlation between {instrument_1_symbol} and {instrument_2_symbol} is {correlation}")
    return correlation


def calculate_rolling_correlation(instrument_1_symbol: str,
                                  instrument_2_symbol: str,
                                  instrument_1_open: List[float],
                                  instrument_2_open: List[float],
                                  window: int = 20) -> List[float]:
    data = {instrument_1_symbol : instrument_1_open, instrument_2_symbol: instrument_2_open}
    df = pd.DataFrame(data)
    rolling_correlation = df[instrument_1_symbol].rolling(window).corr(df[instrument_2_symbol])
    return rolling_correlation

def calculate_net_profit_eur(open_price: float,
                             close_price: float,
                             contract_value: int,
                             quote_currency_to_eur_conversion: float,
                             cmd: int):
    price_difference = 0
    if cmd == 0:
        #buy
        price_difference = close_price - open_price
    elif cmd == 1:
        #sell
        price_difference = open_price - close_price
    else:
        raise ValueError("Wrong cmd {cmd}, acceptable values are 0 or 1")
    net_profit_quote_currency = price_difference * contract_value
    return net_profit_quote_currency * quote_currency_to_eur_conversion
