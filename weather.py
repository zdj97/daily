#!/user/bin/env python
# coding=utf-8
'''
@project : 爬虫
@author  : zmj1997
#@file   : weather.py
#@ide    : PyCharm
#@time   : 2022-10-09 15:16:54
'''
from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
from bs4 import BeautifulSoup
import re
today = datetime.now ()

# city_code = os.environ["CITY_CODE"]
city_code='101100201'

# city_code = '101230508'  # 进入https://where.heweather.com/index.html查询你的城市代码
api = 'http://t.weather.itboy.net/api/weather/city/'  # API地址，必须配合城市代码使用

def get_weather_icon(text):
    weather_icon = "🌤️"
    weather_icon_list = ["☀️",  "☁️", "⛅️",
                         "☃️", "⛈️", "🏜️", "🏜️", "🌫️", "🌫️", "🌪️", "🌧️"]
    weather_type = ["晴", "阴", "云", "雪", "雷", "沙", "尘", "雾", "霾", "风", "雨"]
    for index, item in enumerate(weather_type):
        if re.search(item, text):
            weather_icon = weather_icon_list[index]
            break
    return weather_icon

def get_weather_new ():
    tqurl = api + city_code
    response = requests.get (tqurl)
    d = response.json ()  # 将数据以json形式返回，这个d就是返回的json数据
    # print(d)
    if (d['status'] == 200):  # 当返回状态码为200，输出天气状况
        parent = d["cityInfo"]["parent"]  # 省
        city = d["cityInfo"]["city"]  # 市
        update_time = d["time"]  # 更新时间
        date = d["data"]["forecast"][0]["ymd"]  # 日期
        week = d["data"]["forecast"][0]["week"]  # 星期
        weather_type = d["data"]["forecast"][0]["type"]  # 天气
        weather_ic=get_weather_icon(weather_type)
        wendu_high = d["data"]["forecast"][0]["high"]  # 最高温度
        wendu_low = d["data"]["forecast"][0]["low"]  # 最低温度
        shidu = d["data"]["shidu"]  # 湿度
        pm25 = str (d["data"]["pm25"])  # PM2.5
        pm10 = str (d["data"]["pm10"])  # PM10
        quality = d["data"]["quality"]  # 天气质量
        fx = d["data"]["forecast"][0]["fx"]  # 风向
        fl = d["data"]["forecast"][0]["fl"]  # 风力
        ganmao = d["data"]["ganmao"]  # 感冒指数
        tips = d["data"]["forecast"][0]["notice"]  # 温馨提示
        # cpurl = 'https://qmsg.zendee.cn/send/' + spkey  # 自己改发送方式，我专门创建了个群来收消息，所以我用的group
        # 天气提示内容
        # tdwt = "\n-----------------------------------------" + "\n❤【今日份天气】\n❤城市： " + parent + city + \
        #        "\t❤日期： " + date +' ' + week + "\n"+weather_ic+"天气: " + weather_type + "\t❤温度: " + wendu_high + " / " + wendu_low + "\t❤湿度: " + \
        #        shidu + "\n❤PM25: " + pm25 + "\t❤PM10: " + pm10 + "\t❤空气质量: " + quality + \
        #        "\n❤风力风向: " + fx + fl + "\n❤感冒指数: " + ganmao + "\n❤温馨提示： " + tips + "\n❤更新时间: " + update_time
        # # print (tdwt)
    return parent ,city,date,week,weather_ic,weather_type,wendu_high,wendu_low,shidu,pm25,pm10,quality,fx,fl,ganmao,tips,update_time