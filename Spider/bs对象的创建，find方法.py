from bs4 import BeautifulSoup as bs
import requests as re

# 对象创建
# soup = bs('<html>data</html>', 'lxml')  # BeautifulSoup 可以自动修正代码，如加上了body标签
# 这里可能会遇到警告GuessedAtParserWarning，此时输入的是soup = bs('<html>data</html>')，在>'后面加上'lxml'指定一个解析器就可以
# print(soup)

# find方法
# 1. 导入模块
# from bs4 import BeautifulSoup as bs

# 2. 准备文档字符串
# url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia' # 这里html不能直接放链接，应该用requests请求获得的text传给这里的url
# str = re.get('http://ncov.dxy.cn/ncovh5/view/pneumonia')  # 好像不行
html = '''<title>123</title>
<a id = "link1">a1 = 456 </a>
<a id = "link2">a2 = 789 </a>
<a id = "link3">a1 = 456 </a>'''  # 这里手动写一个就可以了
# 3. 创建bs对象
soup = bs(html, 'lxml')

# 4. 查找title标签
title = soup.find('title')
print(title)

# 5. 查找a标签
a = soup.find('a')
print(a)  # 这里只返回取到的第一个a
# 查找所有a标签
a_s = soup.find_all('a')  # find_all()函数可以返回找到的所有标签
print(a_s)

# 根据属性进行查找
# id为link1的标签
# 通过名命参数找
b = soup.find(id="link1")
print(b)
# 通过attrs指定属性字典进行查找
a = soup.find(attrs={'id': 'link2'})  # 字典
print(a)

# 根据文本内容查找
text = soup.find(text='a1 = 456 ')
print(text)

# tag对象
print(type(a))  # <class 'bs4.element.Tag'>
print('标签名: ', a.name)
print('标签所有属性: ', a.attrs)
print('标签文本内容: ', a.text)










