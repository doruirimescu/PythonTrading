
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

@dataclass
class MaxDrawdown:
    date: datetime
    value: float

@dataclass
class Trade:
    cmd: int #0 buy, 1 sell
    entry_date: datetime
    exit_date: datetime
    open_price: float
    close_price: float
    symbol: Optional[str] = None
    max_drawdown: Optional[MaxDrawdown] = None

    def duration_days(self):
        return (self.exit_date - self.entry_date).days

    def calculate_max_drawdown_price_diff(self, data):
        max_drawdown = 1000000
        drawdown_date = None
        for i, d in enumerate(data['date']):
            if d >= self.entry_date and d <= self.exit_date:
                if self.cmd == 0:
                    max_drawdown = min(max_drawdown, data['low'][i] - self.open_price)
                    drawdown_date = d
        self.max_drawdown = MaxDrawdown(date=drawdown_date, value=max_drawdown)

class StrategySummary:
    def __init__(self, trades: List[Trade], n_days: int, should_reinvest: bool,
                 desired_cash_invested: int, contract_size: int, profit_currency: str,
                 category_name: str) -> None:
        #TODO: move all the analyze code here.
        pass

    def _calculate(self):
        pass

    def print(self):
        pass
