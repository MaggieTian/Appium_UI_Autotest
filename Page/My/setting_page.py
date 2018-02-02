# -*- coding: utf-8 -*-
# @Time    : 2018/1/30
# @Author  : 
# @File    : setting_page.py
from Util.locate_helper import LocateHeper


class SettingPage():

    def __init__(self):

        self._setting = LocateHeper.locator("accessibility_id", "设置")                       # 设置
        self._add_friend = LocateHeper.locator("accessibility_id", "添加好友")                 # 添加好友
        self._user_info = LocateHeper.locator("id", "com.sina.weibo:id/layout_userinfo")      # 用户昵称
        self._back = LocateHeper.locator("accessibility_id", "返回")
        self._accout_manage = LocateHeper.locator("id", "com.sina.weibo:id/accountContent")    # 账号管理
        self._exit_accout = LocateHeper.locator("id", "com.sina.weibo:id/exitAccountContent")   # 退出账号
        self._title_text = LocateHeper.locator("id", "com.sina.weibo:id/titleText")             # 页面标识（账号管理）
        self._cancel = LocateHeper.locator("xpath", '''
        android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[1]
        ''')  # 取消退出登录

        self._sure = LocateHeper.locator("xpath", '''

        android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[3]

        ''')  # 确定退出登录

    def check(self):
        pass
