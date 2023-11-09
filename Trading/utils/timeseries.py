import numpy as np
from datetime import datetime
def slice_data_np(history, i):
    # Slice data
    data = dict()
    data['open'] = np.array(history['open'][:i], dtype=float)
    data['high'] = np.array(history['high'][:i], dtype=float)
    data['low'] = np.array(history['low'][:i], dtype=float)
    data['close'] = np.array(history['close'][:i], dtype=float)
    data['date'] = history['date'][:i]
    return data
