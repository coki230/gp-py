import requests
import pandas as pd


# 日内实时盘口（JSON）：
# r = requests.get("http://api.money.126.net/data/feed/1000002,1000001,1000881,0601398,money.api")
# print(r.text)

# 历史成交数据（CSV）：
# r = requests.get("http://quotes.money.163.com/service/chddata.html?code=0601398&start=20000720&end=20000722")
# print(r.text)

# 财务指标（CSV）：
# r = requests.get("http://quotes.money.163.com/service/zycwzb_601398.html?type=report")
# print(r.text)

# 资产负债表（CSV）：
# r = requests.get("http://quotes.money.163.com/service/zcfzb_601398.html")
# print(r.text)

# 利润表（CSV）：*****
# r = requests.get("http://quotes.money.163.com/service/lrb_601398.html")
# print(r.text)

# 现金流表（CSV）：
# r = requests.get("http://quotes.money.163.com/service/xjllb_601398.html")
# print(r.text)

# 日内实时盘口（JSON）：
r = requests.get("http://hq.sinajs.cn/list=sh600000,sh600004")
print(r.text)