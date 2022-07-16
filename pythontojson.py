import json

# python转为json
# python类型数据
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
rs = json.loads(json_str)  # 这里用json.loads，不能用json.load
# 完成转换
json_str = json.dumps(rs, ensure_ascii=False)  # dumps(obj)方法传递python类型数据，ensure_ascii指是否使用ascii码，不用则显示为汉字
print(json_str)
# python以json格式存储到文件
# 构建写入的文件对象
with open('data/test1.json', 'w') as fp:
    # 写入
    json.dump(rs, fp, ensure_ascii=False)  # dump(obj, fp) 对象作为第一个参数，写入的文件作为第二个参数
