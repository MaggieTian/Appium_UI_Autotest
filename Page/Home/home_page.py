#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18
# @Author  : tianqi
# @File    : home_page.py


from Util.locate_helper import LocateHeper


class HomePage():
    # init the element in HomePage

    def __init__(self):
        self.login = LocateHeper.locator("id", "com.sina.weibo:id/titleSave")
        self.register = LocateHeper.locator("ID", "com.sina.weibo:id/titleBack")
        self.my_profile = LocateHeper.locator("accessibility_id", "我的资料")
