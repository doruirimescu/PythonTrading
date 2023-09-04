import json
import plotly.express as px
from plotly.subplots import make_subplots

import plotly.graph_objects as go
from constants import FILTERED_ANALYSIS_FILENAME, DATE_TODAY
from Trading.alphaspread.alphaspread import valuation_type_order, ValuationType

stock_valuation = dict()

# open data file
with open(FILTERED_ANALYSIS_FILENAME, "r") as f:
    data = json.load(f)

for stk in data:
    symbol = stk["symbol"]
    valuation_type = stk["valuation_type"]
    valuation_score = stk["valuation_score"]
    solvency_score = stk["solvency_score"]
    stock_valuation[symbol] = (valuation_type, valuation_score, solvency_score)


sorted_stock_valuation_new = sorted(
            stock_valuation.items(),
            key=lambda item: (item[1][2])
        )


fig = make_subplots(
                rows=1, cols=1,
                subplot_titles=("Top Stocks Valuation"),
                specs=[[{"type": "xy"}]]
        )
[print(item[1][2] ) for item in sorted_stock_valuation_new]
# Add bar chart
stock_names = [item[0] for item in sorted_stock_valuation_new]
scores = [item[1][1] for item in sorted_stock_valuation_new]
solvencies = [item[1][2] for item in sorted_stock_valuation_new]

texts = [f"Valuation: {score}, Solvency: {solvency}" for score, solvency in zip(scores, solvencies)]

colors = ['red' if item[1][0] == 'Overvalued' else 'green' for item in sorted_stock_valuation_new]
fig.add_trace(go.Bar(x=stock_names, y=scores, text=texts, textposition='auto', marker_color=colors), row=1, col=1)

# Update layout
fig.update_layout(title_text="Stock Analysis")
fig.show()
