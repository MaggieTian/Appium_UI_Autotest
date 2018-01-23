# -*- coding: utf-8 -*-
# @Time    : 2018/1/22
# @Author  : 
# @File    : login_page.py

import logging
from Util.locate_helper import LocateHeper

class LoginPage():

    def __init__(self):

        self._close = LocateHeper.locator("id","com.sina.weibo:id/tv_title_bar_back") # 关闭
        self._register = LocateHeper.locator("id","com.sina.weibo:id/tv_title_bar_register") # 注册
        self._username = LocateHeper.locator("id","com.sina.weibo:id/etLoginUsername") # 登录用户名输入狂
        self._pwd = LocateHeper.locator("id","com.sina.weibo:id/etPwd") # 登录密码输入框
        self._login_button = LocateHeper.locator("id","com.sina.weibo:id/bnLogin") # 登录按钮

        self._other_login = LocateHeper.locator("xpath",'''
        android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.ImageView[1]
        ''')
        self._pageid = self._login_button

    def check(self,driver):
        if self._pageid is None:
            logging.error("the page id is None in loginpage")
            raise Exception
        else:
            try:
                if LocateHeper(driver).find(self._pageid):
                    return True
                else:
                    return False

            except Exception:

                logging.error("find elment {0} fail in {1}".format(self._pageid[1],"login page"))