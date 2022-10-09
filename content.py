#!/user/bin/env python
# coding=utf-8
'''
@project : 爬虫
@author  : zmj1997
#@file   : content.py
#@ide    : PyCharm
#@time   : 2022-10-09 16:42:56
'''
import requests
import random
tian='d8fa4c88980a1b6e86354e1b437453ee'
chp='caihongpi'
pyqwenan='pyqwenan'
gjmj='gjmj'
ensentence='ensentence'

def get_chp():

    chp_url = f"http://api.tianapi.com/{chp}/index?key={tian}"
    chp_res = requests.get(chp_url).json()
    return "🌈 " + chp_res["newslist"][0]["content"]

def get_pyqwenan():

    chp_url = f"http://api.tianapi.com/{pyqwenan}/index?key={tian}"
    chp_res = requests.get(chp_url).json()
    return "🌈 " + chp_res["newslist"][0]["content"]

def get_gjmj ():
    chp_url = f"http://api.tianapi.com/{gjmj}/index?key={tian}"
    chp_res = requests.get (chp_url).json ()
    return "🌈 " + chp_res["newslist"][0]["content"]

def get_ensentence ():
    chp_url = f"http://api.tianapi.com/{ensentence}/index?key={tian}"
    chp_res = requests.get (chp_url).json ()
    return "🌈 " + chp_res["newslist"][0]["en"]

def get_emoticon():
    emoticon_list = ["(￣▽￣)~*", "(～￣▽￣)～", "︿(￣︶￣)︿", "~(￣▽￣)~*", "(oﾟ▽ﾟ)o", "ヾ(✿ﾟ▽ﾟ)ノ", "٩(๑❛ᴗ❛๑)۶", "ヾ(◍°∇°◍)ﾉﾞ", "ヾ(๑╹◡╹)ﾉ", "(๑´ㅂ`๑)", "(*´ﾟ∀ﾟ｀)ﾉ", "(´▽`)ﾉ", "ヾ(●´∀｀●)",
                     "(｡◕ˇ∀ˇ◕)", "(≖ᴗ≖)✧", "(◕ᴗ◕✿)", "(❁´◡`❁)*✲ﾟ*", "(๑¯∀¯๑)", "(*´・ｖ・)", "(づ｡◕ᴗᴗ◕｡)づ", "o(*￣▽￣*)o", "(｀・ω・´)", "( • ̀ω•́ )✧", "ヾ(=･ω･=)o", "(￣３￣)a", "(灬°ω°灬)", "ヾ(•ω•`。)", "｡◕ᴗ◕｡"]
    return random.choice(emoticon_list)