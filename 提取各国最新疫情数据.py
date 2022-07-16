# 导入包
import requests as re
from bs4 import BeautifulSoup as bs

# 发送请求获取首页内容
response = re.get('http://ncov.dxy.cn/ncovh5/view/pneumonia')
homepage = response.content.decode()
# print(homepage)

# 使用bs提取数据
soup = bs(homepage, 'lxml')
script = soup.find(text='西藏自治区')
text = script.text
print(text)




