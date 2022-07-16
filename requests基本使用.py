# 1. 导入模块
import requests as re

# 2. 发送请求，获取响应
response = re.get('http://ncov.dxy.cn/ncovh5/view/pneumonia')  # 请求库必须要加上'http://'才能访问

# 3. 获取数据
# print(response.encoding)  # 编码方式为ISO-8859-1，所以直接显示text，汉字部分会出现乱码
# response.encoding = 'utf-8'
# print(response.text)
# print(response.content)     # response.content是获取二进制数据，如<title>\xe7\x99\xbe……
print(response.content.decode())        # decode，解码默认utf-8编码。使用decode(encoding='gbk')会报错，因为有的字符不在gbk编码中

