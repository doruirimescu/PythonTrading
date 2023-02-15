from typing import List, Tuple, Optional
import logging
import numpy as np

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
    return round(n_losers / len(profits), 2)
