import requests
from bs4 import BeautifulSoup as bs
from enum import Enum
from datetime import datetime
import symbols_url

# Defines a response from investing.com
class InvestingAnalysisResponse(Enum):
    """Enumeration class for investing.com analysis response"""

    STRONG_SELL = "Strong Sell"
    SELL = "Sell"
    NEUTRAL = "Neutral"
    BUY = "Buy"
    STRONG_BUY = "Strong Buy"

class InvestingCandlestickAnalysisReliability(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
class InvestingCandleStickAnalysisResponse:
    def __init__(self, pattern, timeframe, reliability, candles_ago, date):
        self.pattern = pattern
        self.timeframe = timeframe
        self.reliability = reliability
        self.candles_ago = candles_ago
        self.date = date
##TODO split into InvestingTechnical and InvestingCandlestick classes in different files
class Investing:
    def __init__(self):

        # symbols maps a symbol to a tuple (address, pairID) - find the pairID by inspecting the network traffic response
        self.symbols = symbols_url.SYMBOLS_URL

    def getAvailableSymbols(self):
        response = [i for i, j in self.symbols.items()]
        return response

    def getTechnicalAnalysis(self, symbol, period):
        symbol = symbol.upper()
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": self.symbols[symbol][0],
            "X-Requested-With": "XMLHttpRequest",
        }

        periods = {
            "1m": 60,
            "5m": 300,
            "15m": 900,
            "30m": 1800,
            "1h": 3600,
            "5h": 18000,
            "D": 86400,
            "W": "week",
            "M": "month",
        }

        body = {"pairID": self.symbols[symbol][1], "period": "", "viewType": "normal"}

        with requests.Session() as s:
            body["period"] = periods[period]
            r = s.post(
                "https://www.investing.com/instruments/Service/GetTechincalData",
                data=body,
                headers=headers,
            )
            soup = bs(r.content, "lxml")
            response = list()

            for i in soup.select("#techStudiesInnerWrap .summary"):
                response_text = i.select("span")[0].text
                print(response_text)
                response.append(InvestingAnalysisResponse(response_text))
        return response

    def sanitizeTimeframe(self, timeframe):
        if timeframe == "1":
            return "1m"
        elif timeframe == "5":
            return "5m"
        elif timeframe == "15":
            return "15m"
        elif timeframe == "30":
            return "30m"
        return timeframe

    def getTimeFormatter(self, timeframe):
        if timeframe =='1m':
            return "%b %d, %Y %I:%M%p"
        elif timeframe =='5m':
            return "%b %d, %Y %I:%M%p"
        elif timeframe =='15m':
            return "%b %d, %Y %I:%M%p"
        elif timeframe =='30m':
            return "%b %d, %Y %I:%M%p"
        elif timeframe =='1H':
            return "%b %d, %Y %I:%M%p"
        elif timeframe =='5H':
            return "%b %d, %Y %I:%M%p"
        elif timeframe =='1D':
            return "%b %d, %Y"
        elif timeframe =='1W':
            return "%b %d, %Y"
        elif timeframe =='1M':
            return "%b %y"

    def getCandlestickAnalysis(self, symbol, period=None):
        ret = list()

        symbol = symbol.upper()
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
        }

        url = self.symbols[symbol][0] + "-candlestick"

        with requests.Session() as s:
            r = s.post(url, headers=headers)
            soup = bs(r.content, "lxml")
            response = list()

            row_id = 0
            table = soup.find("tr", id="row" + str(row_id))
            while table is not None:
                pattern = str()
                timeframe = str()
                reliability = str()
                candles_ago = str()
                date = str()

                counter = 0
                for child in table.contents:
                    if counter == 3:
                        pattern = child.contents[0]
                    elif counter == 5:
                        timeframe = child.contents[0]
                        timeframe = self.sanitizeTimeframe(timeframe)
                    elif counter == 7:
                        reliability = InvestingCandlestickAnalysisReliability(child["title"])
                    elif counter == 9:
                        candles_ago = child.contents[0]
                    elif counter == 11:
                        date = child.contents[0]
                    counter += 1

                if (period is None) or (timeframe == period):

                    #Check that it is not a current candle
                    if(date is not ''):
                        date = datetime.strptime(date, self.getTimeFormatter(timeframe))

                    print("Pattern: \t" + pattern)
                    print("Timeframe: \t" + timeframe)
                    print("Reliability: \t" + reliability.name)
                    print("Candles ago: \t" + candles_ago)
                    print(date)

                    print("------------------------------")

                row_id += 1
                table = soup.find("tr", id="row" + str(row_id))

i = Investing()

print(i.getTechnicalAnalysis("BTCUSD", "30m"))

#i.getCandlestickAnalysis("BTCUSD")
