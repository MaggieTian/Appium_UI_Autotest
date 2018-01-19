#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18
# @Author  : tianqi
# @File    : home_page.py


from Util.locate_helper import LocateHeper
import logging


class HomePage():

    # init the element in HomePage

    def __init__(self):

        self.login = LocateHeper.locator("id", "com.sina.weibo:id/titleSave")
        self.register = LocateHeper.locator("id", "com.sina.weibo:id/titleBack")
        self.my_profile = LocateHeper.locator("accessibility_id", "我的资料")
        self.register = LocateHeper.locator("id","com.sina.weibo:id/titleBack")
        self.follow = LocateHeper.locator("id","com.sina.weibo:id/tv_groupName")
        self.publish = LocateHeper.locator("id","com.sina.weibo:id/plus_icon")
        self.find = LocateHeper.locator("accessibility_id","发现")
        self.weibo = LocateHeper.locator("accessibility_id","微博")
        self.page_id = LocateHeper.locator("") # 用来标识页面


    def check(self):

        if self.page_id is None:
            logging.error("the home pace id is None")
            raise Exception
        else:
            try:
                LocateHeper.find(self.page_id)
            except Exception:
                logging.error("can not find element"+self.page_id)





