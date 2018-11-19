
# -*- coding:UTF-8 -*-

import requests
import re
import urllib.parse
import json
import datetime
from collections import OrderedDict

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8  
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')   
self=requests.session()
self.verify=False
self.headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'kyfw.12306.cn',
    'Cache-Control':'no-cache',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

def shoppiao():

    data={
       'leftTicketDTO.train_date':'2018-10-26',#时间
        'leftTicketDTO.from_station':'BJQ',#出发站码
        'leftTicketDTO.to_station':'CBN',#目的地码
        'purpose_codes':'ADULT'#票类型ADULT成人，STUDENT学生
    }
    url='https://kyfw.12306.cn/otn/leftTicket/query?'
    requests.packages.urllib3.disable_warnings()
    # res=self.get(url,params=data)
    res=requests.get(url,params=data)
    print(res.status_code)
    print(res)
    print(res.text)
    dictr=json.loads(res.text)
    pklist=dictr.get('data').get('result')
    for item in pklist:
        sp_item = item.split('|')
        for index, item in enumerate(sp_item,0):

            print('{}:\t{}'.format(index, item))
        '''
        通过分析
        0：列车信息（订票时候需要） 1：信息 2：火车编号
        3：列车号 4：始发站   5：终点站   6：起始站  7：目标站    8：出发时间       9：到达时间
        10：行车时间
        11：有3种状态：Y, N, IS_TIME_NOT_BUY 分别对应，可以预定，不可以预定，其他原因----对应的是第1项
        12：参数leftTicket
        13：日期
        14：
        15：参数train_location
        21：高级动卧   22：        23：软卧 24：软座  25：特等座  26：无座 28：硬卧  29：硬座  30：二等座  31：一等座  32：商务座 33：动卧
       '''
        if sp_item[11]=='Y':#可以买票，开始订票
            if sp_item[30]!='无':#买二等座
                print(sp_item[30])
                if vel_longin_2():#验证登陆
                   print('已经登陆可以开始下单')
                   self.headers['X-Requested-With']='XMLHttpRequest'
                   secretStr=urllib.parse.unquote(sp_item[0])


                   self.headers['Referer'] = 'https://kyfw.12306.cn/otn/leftTicket/init'

                   submitOrderRequest(secretStr)

                   data = OrderedDict()
                   data["_json_att"] =''
                   data["fromStationTelecode"] =sp_item[6]
                   data["leftTicket"] = sp_item[12]
                   data['purpose_codes']='00'
                   data['REPEAT_SUBMIT_TOKEN']=''
                   data["seatType"] = 'O'
                   data["stationTrainCode"] = sp_item[3]
                   data["toStationTelecode"] =sp_item[7]
                   data["train_date"] = str(datetime.datetime.strptime(sp_item[13], '%Y%m%d').strftime('%a %b %d %Y %H:%M:%S GMT+0800'))
                   data["train_location"] = sp_item[15]
                   data["train_no"] =sp_item[2]

                   '''
                   data={
                        'train_date':str(datetime.datetime.strptime(sp_item[13], '%Y%m%d').strftime('%a %b %d %Y %H:%M:%S GMT+0800')),
                        'train_no':sp_item[2],#火车编号
                        'stationTrainCode':sp_item[3],#列车号
                        'seatType':'O',#座位类型 1是硬座(无座)，2是软座，3是硬卧，4是软卧,  O 大写字母  是高铁二等座，M是高铁一等座，商务座(9),特等座(P),高级软卧(6)
                       'fromStationTelecode':sp_item[6],#起始站编号
                        'toStationTelecode':sp_item[7],#目标站编号
                        'leftTicket':sp_item[12],
                        'train_location':sp_item[15],#15项Q6
                   }
                '''
                   shopdin(data)

                else:
                    login()
                    shoppiao()
        break



if __name__ == '__main__':
    #yanzhengma()
    shoppiao()
    # vel_longin_2()