# -*- coding: utf-8 -*-
# @Time    : 2018/1/21
# @Author  : 
# @File    : map.py

from Page.Home.home_page import HomePage
from  Page.Home.login_page import LoginPage

'''
this is used to the params map to correct Page Class when call function
'''


_Page_Map = {
            'HomePage':HomePage,
            'LoginPage':LoginPage
}