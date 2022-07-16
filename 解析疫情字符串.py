import requests as req
from bs4 import BeautifulSoup as bs
import re
import json

# 发送请求获取首页内容
response = req.get('http://ncov.dxy.cn/ncovh5/view/pneumonia')
homepage = response.content.decode()
# print(homepage)

# 使用bs提取数据
soup = bs(homepage, 'lxml')
script = soup.find(id='getAreaStat')
text = script.text
# print(text)

# 使用正则表达式提取json字符串
json_str = re.findall(r'\[.+\]', text)[0]  # 中括号表示数意集，只要出现在中括号内的都可以匹配
# print(json_str)

# 把json字符串转换为python类型数据
last_day_covid19 = json.loads(json_str) # ，
print(last_day_covid19)






