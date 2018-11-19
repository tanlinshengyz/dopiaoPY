# from login import Login
import os
import requests
import json
import time
from collections import deque, OrderedDict


class Station:
    """ 查询车票信息 """

    def __init__(self):
        # 使用登录时候的session,这样好一些!
        # self.session = Login.session
        # self.headers = Login.headers
        # self.session = requests.session()
        self.session = requests.session()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'kyfw.12306.cn',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

    def station_name_code(self):
        """
        功能:获取每个站点的名字和对应的代码,并保存到本地
        :return: 无
        """
        filename = 'station_name.txt'

        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        resp = self.session.get(url, headers=self.headers)
        if resp.status_code == 200:
            print(resp.text)
            print('station_name_code():获取站点信息成功!')
            with open(filename, 'w') as f:
                for each in resp.text.split('=')[1].split('@'):
                    if each != "'":
                        f.write(each)
                        f.write('\n')
        else:
            print('station_name_code() error! status_code:{}, url: {}'
                  .format(resp.status_code, resp.url))

    def save_station_code(self, filename):
    	#存车站名称喝code对应json
        if not os.path.exists(filename):
            print('save_station_code():', filename, '不存在,正在下载!')
            self.station_name_code()
        name_code_dict = {}
        with open(filename, 'r') as f:
            for line in f:
                name = line.split('|')[1]
                code = line.split('|')[2]
                name_code_dict[name] = code
        file = 'name_code.json'
        with open(file, 'w') as f:
            json.dump(name_code_dict, f, ensure_ascii=False)

    def 


def main():
    filename = 'station_name.txt'
    station = Station()
    station.station_name_code()
    station.save_station_code(filename)
    # station.query_ticket()

if __name__ == '__main__':
    main()
