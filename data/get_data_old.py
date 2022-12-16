import tushare as ts
import pandas as pd

# 日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率

data = ts.get_hist_data('000001')
df = pd.DataFrame(data)
print(df.head().to_string())
print(df.iloc[0:5, 0:5])

