#!/user/bin/env python
# coding=utf-8
'''
@project : 爬虫
@author  : zmj1997
#@file   : main.py
#@ide    : PyCharm
#@time   : 2022-10-09 15:20:53
'''
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
from weather import get_weather_new
from content import get_chp,get_gjmj,get_ensentence,get_pyqwenan,get_emoticon

app_id = 'wx0daeaf9a80a86fee'
app_secret = '87b121ed81da303d546b320e93b132a3'
user_id = 'oF-WK5ro4x_4iOAW9WSijpvQCYq0'
template_id ='q-gx3vvHs3IZmzlEgJBxSxpxbIgv46CD2Ar5lbecZfs'

parent ,city,date,week,weather_ic,weather_type,wendu_high,wendu_low,shidu,\
pm25,pm10,quality,fx,fl,ganmao,tips,update_time=get_weather_new()

chp=get_chp()
gjmj=get_gjmj()
pyqwenan=get_pyqwenan()
ensentence=get_ensentence()
emotion=get_emoticon()

tmp="🌈早上好~今日份天气{} \n🏙 城市： ".format(emotion) + parent + city + \
       "\n🗓︎ 日期： " + date + ' ' + week + "\n" + weather_ic + "天气: " + weather_type + "\n🌡 温度: " + wendu_high + " / " + \
      wendu_low  + "\n💕 空气质量: " + quality + \
     fx + fl + "\n😷 感冒指数: " + ganmao + \
       '\n'+gjmj+'\n'+ensentence+ \
      "\n💕 温馨提示： " + tips + "\n💕 更新时间: " + update_time
print(tmp)
d ={'data':{'value':tmp}}

client = WeChatClient (app_id, app_secret)
wm = WeChatMessage (client)
res = wm.send_template (user_id, template_id, d)
print (d)