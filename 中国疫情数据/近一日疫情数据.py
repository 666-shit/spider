import requests as req
from bs4 import BeautifulSoup
import re
import json

# 1. 发送请求，获取疫情首页
url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia'
response = req.get(url)
homepage = response.content.decode()

# 2. 提取近一日各国疫情数据
soup = BeautifulSoup(homepage, 'lxml')
script = soup.find(id="getAreaStat")
text = script.text
# print(text)
# 3. 获取json格式字符串
json_str = re.findall(r'\[.+\]', text)[0]
# print(json_str)
# 4. json转换为python
lastdaycov = json.loads(json_str)
# print(lastdaycov)
# 5. 以json格式保存
with open('../COV_data/近一日中国疫情数据.json', 'w', encoding='utf-8') as fp:  # 注意文件操作处一定要加上encoding
    json.dump(lastdaycov, fp, ensure_ascii=False)   # 取消自动转为Unicode编码
