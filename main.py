# -*- coding:utf-8 -*-
"""
@author:
@file: demo.py
@time: 2023/5/18 11:14
@desc: 
"""
import json
 
import requests
from requests import session

se = session()
 
url = "https://match.yuanrenxue.cn/jssm"
 
payload = "https://match.yuanrenxue.cn/jssm"
 
headers = {
    'content-length': '0',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'origin': 'https://match.yuanrenxue.cn',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.cn/match/3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1717399607; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1717399607; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1717399607; sessionid=5499mx5wpasgo78h8v49rs6wb32mkb0o; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1717401882',
}
 
se.headers = headers
# response = se.post(url, verify=False)
 
# print(response.text)
# print(response.headers)
# print(response.cookies)
# exit()
# url = "https://match.yuanrenxue.cn/api/match/3?page=1"
# response = se.request("GET", url, headers=headers)
# print(response.text)
# exit()
 
 
if __name__ == '__main__':
    values = []
    jssm_url = "https://match.yuanrenxue.cn/jssm"
    for page in range(1, 6):
        url = "https://match.yuanrenxue.cn/api/match/3?page={}".format(str(page))
        se.post(jssm_url)
        res = se.get(url)
        values.extend([val['value'] for val in json.loads(res.text)['data']])
 
    print(values)
    print(max(values, key=values.count))
