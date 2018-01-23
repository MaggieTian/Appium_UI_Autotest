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

        self._login = LocateHeper.locator("id", "com.sina.weibo:id/titleSave")
        self._register = LocateHeper.locator("id", "com.sina.weibo:id/titleBack")
        self._my_profile = LocateHeper.locator("accessibility_id", "我的资料")
        self._register = LocateHeper.locator("id","com.sina.weibo:id/titleBack")
        self._follow = LocateHeper.locator("id","com.sina.weibo:id/tv_groupName")  # 关注
        self._publish = LocateHeper.locator("id","com.sina.weibo:id/plus_icon")
        self._find = LocateHeper.locator("accessibility_id","发现")
        self._weibo = LocateHeper.locator("accessibility_id","微博")
        self._page_id = self._follow     # 用来标识页面

    # check the current page by page id
    def check(self,driver):

        if self._page_id is None:
            logging.error("the home page id is None",self.__class__.__name__)
            raise Exception
        else:
            try:
                if LocateHeper(driver).find(self._page_id):
                    return True
                else:
                    return False

            except Exception:

                logging.error("can not find element"+self._page_id[1])



    def get(self,name):
        pass







