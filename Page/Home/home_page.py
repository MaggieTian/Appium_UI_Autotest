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
        self._follow = LocateHeper.locator("id","com.sina.weibo:id/tv_groupName")
        self._publish = LocateHeper.locator("id","com.sina.weibo:id/plus_icon")
        self._find = LocateHeper.locator("accessibility_id","发现")
        self._weibo = LocateHeper.locator("accessibility_id","微博")
        self._page_id = LocateHeper.locator("id","com.sina.weibo:id/video_root_view") # 用来标识页面

    # check the current page by page id
    def check(self,driver):

        if self._page_id is None:
            logging.error("the home pace id is None")
            raise Exception
        else:
            try:
                if LocateHeper(driver).find(self._page_id):
                    return True
                else:
                    return False

            except Exception:

                logging.error("can not find element"+self._page_id)



    def get(self,name):
        pass







