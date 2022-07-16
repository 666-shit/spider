import requests as re

str = re.get('http://ncov.dxy.cn/ncovh5/view/pneumonia')  # 请求库必须要加上'http://'才能访问
print(str.content.decode())  # decode，解码默认utf-8编码。使用decode(encoding='gbk')会报错，因为有的字符不在gbk编码中
