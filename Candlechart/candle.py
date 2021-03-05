from enum import Enum
class CandleType(Enum):
    """According to https://en.wikipedia.org/wiki/Candlestick_pattern
    """
    BIG = -1                #Distinguish with body
    BODY = 0                #Distinguish with big
    DOJI = 1
    LONG_LEGGED_DOJI = 2
    DRAGONFLY_DOJI = 3
    GRAVESTONE_DOJI = 4
    HAMMER = 5              #Distinguish with shaven head
    HANGINGMAN = 6          #Same as hammer, but in downtrend
    INVERTED_HAMMER = 7     #Distinguish with shaven bottom
    SHOOTING_STAR = 8       #Same as inverted hammer, but in uptrend
    MARUBOZU = 9
    SPINNING_TOP = 10
    SHAVEN_HEAD = 11        #Distinguish with hammer
    SHAVEN_BOTTOM = 12      #Distinguish with inverted_hammer
    UNDEFINED = 13

class Color(Enum):
    RED = 0
    BLACK = 0
    GREEN = 1
    WHITE = 1

# Wt, Wb, b
candle_type_dict = {
                    CandleType.MARUBOZU  : (0.0, 0.0, 1.0),
                    CandleType.BODY : (1.0/3.0, 1.0/3.0, 1.0/3.0),
                    CandleType.DOJI : (0.5, 0.5, 0.0),
                    CandleType.DRAGONFLY_DOJI   : (0.0, 1.0, 0.0),
                    CandleType.GRAVESTONE_DOJI  : (1.0, 0.0, 0.0),
                    CandleType.HAMMER : (0, 2.0/3.0, 1.0/3.0),
                    CandleType.INVERTED_HAMMER:(2.0/3.0, 0.0,1.0/3.0)
                    }
class CandleClassifier:
    def __init__(self, candle):
        self.open_  = candle.open_
        self.close_ = candle.close_
        self.high_  = candle.high_
        self.low_   = candle.low_

        self.swing_ = abs(self.high_-self.low_)
        self.body_ = abs(self.open_-self.close_)/(abs(self.high_-self.low_))

        self.c_ = candle.getColor() == Color.GREEN

        self.wt_ = (self.high_ -(self.c_*self.close_ + (1-self.c_)*self.open_)) / self.swing_
        self.wb_ = ((self.c_*self.open_ + (1-self.c_)*self.close_) - self.low_) / self.swing_

        self._type = self.__classify()

    def getWickBottom(self):
        return self.wb_

    def getWickTop(self):
        return self.wt_

    def getType(self):
        return self._type

    def __classify(self):
        """Calculate error from ideal type for each possible type, and return the one with minimum error

        Returns:
            [CandleType]: classified candle type
        """
        classifications = dict()
        for ideal_tuple in candle_type_dict:
            error = 0.0
            error += abs(self.wt_ - candle_type_dict[ideal_tuple][0])
            error += abs(self.wb_ - candle_type_dict[ideal_tuple][1])
            error += abs(self.body_ - candle_type_dict[ideal_tuple][2])
            classifications[ideal_tuple] = error
        best_match = min(classifications, key=classifications.get)

        #TODO Clarify between Doji and Long-legged doji
        #TODO Clarify between Inverted Hammer and Shooting star

        #Clarify between hammer and shaven_head
        if best_match == CandleType.HAMMER:
            if self.wt_ < 0.05:
                best_match = CandleType.SHAVEN_HEAD

        #Clarify between inverted hammer and shaven_head
        if best_match == CandleType.INVERTED_HAMMER:
            if self.wb_ < 0.05:
                best_match = CandleType.SHAVEN_BOTTOM

        return best_match

class Candle:
    def __init__(self, open, high, low, close, date = None):
        """[summary]

        Args:
            open ([float]): [open price]
            high ([float]): [high price]
            low ([float]): [low price]
            close ([float]): [close price]
        """

        self.validate(open, close, high, low)

        self.open_ = open
        self.close_= close
        self.high_ = high
        self.low_  = low

        if self.open_ < self.close_:
            self.color_ = Color.GREEN
        else:
            self.color_ = Color.RED

        self.body_percentage_ = float( abs(open-close)/(abs(high-low)) )
        self.type_ = self.__calcType()
        self.date_ = date

    def validate(self, open, close, high, low):
        if open < 0.0:
            raise Exception("Open price smaller than 0")
        elif close < 0.0:
            raise Exception("Close price smaller than 0")
        elif high < 0.0:
            raise Exception("High price smaller than 0")
        elif low < 0.0:
            raise Exception("Low price smaller than 0")
        elif low > high:
            raise Exception("Low is higher than high")

    def getColor(self):
        return self.color_

    def getType(self):
        return self.type_

    def __calcType(self):
        classifier = CandleClassifier(self)
        return classifier.getType()
