"""
实际爬取的过程中生成的json文件内会有“statisticsData”的统计文件，
每一个统计文件后都会跟随一个url，需要多次访问，
但是之前的访问方式只能访问一个url，如果不进行优化会造成很多麻烦，
所以需要将代码进行重构，来增加可扩展性

注：在网页地址前加上"view-source:"即可查看网页源码
如：view-source:https://www.kaoyan.cn/school/detail/519/zszy
"""

# 思路：
# 1. 重构代码，提高可扩展性
# 将功能封装到类中
# 每一个功能变成方法
# 通过run方法启动爬虫

# 2. 实现采集2020年1月25号以后的世界各国疫情数据
# 加载最近一日各国疫情数据
# 遍历数据，获取25号以来的各个国家疫情的url
# 发送请求，获取25号以来各个货架json字符串
# 解析字符串，添加到列表
# 以json格式保存数据

import requests as req
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm  # 进度条


class COVID_19(object):
    def __init__(self):
        self.home_url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia'  # 准备采集疫情首页的home_url

    def __get_content_from_url(self, url):
        """# 1.
        根据url获取响应内容的字符串数据
        :param url: 请求的url
        :return: 响应内容的字符串
        """
        response = req.get(url)
        return response.content.decode()

    def parse_home_page(self, homepage):
        """
        解析首页内容，获取解析后的python数据
        :param homepage: 首页内容
        :return: 解析后的首页数据
        """
        # 2. 提取近一日各国疫情数据
        soup = BeautifulSoup(homepage, 'lxml')
        script = soup.find(id="getAreaStat")
        text = script.text
        # print(text)
        # 3. 获取json格式字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # print(json_str)
        # 4. json转换为python
        data = json.loads(json_str)
        # print(lastdaycov)
        return data

    def save(self, data, path):  # 三个参数，自己，保存文件的数据，保存路径
        # 5. 以json格式保存
        with open(path, 'w', encoding='utf-8') as fp:  # 注意文件路径改为参数处的path
            json.dump(data, fp, ensure_ascii=False)  # 保存的数据改为data

    def crawl_last_day_COVID19(self):  # 抓取信息
        """
        采集最近一天的各国疫情信息
        :return:
        """
        # 1. 发送请求获取首页内容
        homepage = self.__get_content_from_url(self.home_url)
        # 2. 解析首页内容获取最近一天各国的疫情数据
        last_day_COVID19 = self.parse_home_page(homepage)
        # 3. 保存
        self.save(last_day_COVID19, '../COV_data/近一日中国疫情数据.json')

    def crawl_COVID19(self):
        """
        采集从1月25号以来各国疫情数据
        :return:
        """
        # 1. 加载各国疫情数据
        with open('../COV_data/近一日中国疫情数据.json', encoding='utf-8') as fp:
            last_day_COVID19 = json.load(fp)
        # print(last_day_COVID19)
        # 定义列表，用于存储各国从1月25以来的疫情数据
        COVID19_LIST = []
        # 2. 遍历数据，获取url
        for country in tqdm(last_day_COVID19, '采集1月25日以来的疫情信息'):  # 加进度条，第二个参数为显示信息
            # 3. 发送请求，获取从1月25号至今的json数据
            statistics_data_url = country['statisticsData']  # 获取统计数据的url
            statistics_data_json_str = self.__get_content_from_url(statistics_data_url)  # 获取统计的字符串
            # 4. 将json数据转换为python类型的数据，添加到列表中
            statistics_data = json.loads(statistics_data_json_str)['data']  # 要的是数据，所以直接加data
            # print(statistics_data)    此时的数据没有所属，即不知道是哪个国家的信息
            for oneday in statistics_data:  # 遍历的方式加上国家的名字，名字在json文件中有对应的键‘provinceName’
                oneday['provinceName'] = country['provinceName']  # 国家/省名称
                # oneday['countryShortCode'] = country['countryShortCode']        # 国家简称
            # print(statistics_data)
            COVID19_LIST.extend(statistics_data)  # 将元素放入列表用extend方法
        # 5. 保存列表以json格式
        self.save(COVID19_LIST, '../COV_data/中国疫情数据列表.json')

    def run(self):
        # self.crawl_last_day_COVID19()
        self.crawl_COVID19()


if __name__ == '__main__':
    spider = COVID_19()
    spider.run()

"""
数据示例 {
"confirmedCount": 1,                  确诊人数                  需要
"confirmedIncr": 1,                    新增确诊        
"curedCount": 0,                         治愈人数
"curedIncr": 0,                           新增治愈
"currentConfirmedCount": 1,     目前确认数               需要
"currentConfirmedIncr": 1,       目前确认增加
"dateId": 20200120,                  日期                         需要
"deadCount": 0,                           死亡人数                  需要
"deadIncr": 0,                             新增死亡
"highDangerCount": 0,                高危人数
"midDangerCount": 0,                 中危人数
"suspectedCount": 0,                  疑似人数
"suspectedCountIncr": 0,           疑似增加
"provinceName": "上海市"          省名称                     需要
},
"""
