import json

# 准备json字符串
json_str = """
[
    {
        "provinceName":"美国",
        "currentConfirmedCount":1179041,
        "confirmedCount":1643499
    },
    {
        "provinceName":"英国",
        "currentConfirmedCount":222227,
        "confirmedCount":259559
    }
]
"""
# json字符串转换为python数据
rs = json.loads(json_str)  # json字符串转python用json.loads()方法
print(rs)
print(type(rs))  # <class 'list'>
print(type(rs[0]))  # <class 'dict'>
# json文件转化为python类型的数据
# 构建指向该文件的文件对象
with open('data/test.json', encoding='utf-8') as fp:  # 如果此处报错，新建一个data/test.json文件即可解决
    # 由于是在编译器中新建路径，编译器会将其转换为gbk编码，所以读取后显示为乱码，这里需要指定文件读取的编码方式为‘utf-8’
    # 加载该对象转换为python类型数据
    python_list = json.load(fp)  # 传递json文件对象用load()方法
    print(python_list)
    print(type(python_list))  # <class 'list'>
    print(type(python_list[0]))  # <class 'dict'>
