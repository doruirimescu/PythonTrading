from Trading.algo.technical_analyzer.technical_analysis import TechnicalAnalysis
from Trading.algo.indicators.indicator_value_to_action import IndicatorValueToAction, IndicatorAction
from abc import ABC, abstractmethod
import numpy
# import talib


class TechnicalAnalyzer(ABC):
    @abstractmethod
    def analyse(self, *args, **kwargs) -> TechnicalAnalysis:
        pass


class DailyBuyTechnicalAnalyzer(TechnicalAnalyzer):
    """Buy and wait for take profit, then close. Once per day.
    """
    #TODO: take last_100_days_take_profit_percentage, last_10_days_take_profit_percentage
    #TODO:  last_10_days_take_profit_percentage < 0.05, do not trade.
    #TODO: weighted mean between last_100 and last_10 with weight on 2:1
    def __init__(self, take_profit_percentage: float):
        # Should take the last 100 days candles of the instrument and check if to sell or buy
        self._take_profit_percentage = take_profit_percentage

    def analyse(self, has_already_traded_instrument_today: bool = False, open_price: float = 0.0,
                current_price: float = 0.0, is_market_closing_soon: bool = False) -> TechnicalAnalysis:
        """Buy once per day (when market opens). Wait for take profit target to be achieved and close trade. If target not achieved, close when market is closing.

        Args:
            has_already_traded_instrument_today (bool): True if instrument has already been traded once today
            open_price (float): Price at which market opened today for this instrument
            current_price (float): Current price of this instrument
            is_market_closing_soon (bool): If market is closing soon (soon is to be defined by caller)

        Returns:
            TechnicalAnalysis: STRONG_BUY if to open trade, STRONG_SELL if to close trade, NEUTRAL if to not do anything
        """
        if not has_already_traded_instrument_today:
            return TechnicalAnalysis.STRONG_BUY
        else:
            if 1 - current_price/open_price >= self._take_profit_percentage:
                return TechnicalAnalysis.STRONG_SELL
            if is_market_closing_soon:
                return TechnicalAnalysis.STRONG_SELL
        return TechnicalAnalysis.NEUTRAL



# def RSI14(data: list):
#     iva = IndicatorValueToAction(75,25,5)
#     data = numpy.array(data)
#     rsi = talib.RSI(data, timeperiod=14)
#     action = iva.analyse(rsi[-1])
#     print(rsi)
#     return action

# #TODO: Investigate this one
# def STOCH9_6(data:list):
#     data = numpy.array(data)
#     #stoch = talib.STOCHF(high, low, close, fastd_period=9, fastk_period=6)

# def MACD_12_26(data:list):
#     data = numpy.array(data)
#     macd = talib.MACD()

# #TODO: Investigate this one
# def ROC(data:list):
#     data = numpy.array(data)
#     talib.ROC(data)
