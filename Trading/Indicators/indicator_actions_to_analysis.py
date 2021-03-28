from Trading.Indicators.indicator_value_to_action import IndicatorAction
from enum import Enum
class TechnicalAnalysis(Enum):
    """Enumeration class for investing.com analysis response"""

    STRONG_SELL = "Strong Sell"
    SELL = "Sell"
    NEUTRAL = "Neutral"
    BUY = "Buy"
    STRONG_BUY = "Strong Buy"
class IndicatorActionsToAnalysis:
    def __init__(self, n_indicators = 12, strong=70.0, weak=50.0):
        self.__strong = strong
        self.__weak = weak
        self.__n_indicators = n_indicators

    def convert(self, actions):
        n_buy = 0
        n_sell = 0
        n_neutral = 0
        for action in actions:
            if action == IndicatorAction.BUY:
                n_buy += 1
            elif action == IndicatorAction.SELL:
                n_sell += 1
            else:
                n_neutral += 1
        percentage_buy  = n_buy  / (n_buy + n_sell) * 100
        percentage_sell = n_sell / (n_buy + n_sell) * 100

        if n_buy >=self.__n_indicators/2:
            return TechnicalAnalysis.STRONG_BUY
        elif n_sell >=self.__n_indicators/2:
            return TechnicalAnalysis.STRONG_SELL

        if percentage_buy > percentage_sell:
            return TechnicalAnalysis.BUY
        if percentage_sell > percentage_buy:
            return TechnicalAnalysis.SELL
        else:
            return TechnicalAnalysis.NEUTRAL