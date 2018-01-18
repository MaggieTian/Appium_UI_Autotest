#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18
# @Author  : tianqi
# @File    : home_page.py
from page_objects import PageObject, PageElement
from appium import webdriver

class HomePage():
    # driver = webdriver.Remote("")
    def __init__(self,driver):
        self.login = driver.find_element_by_id("com.sina.weibo:id/titleSave")
        self.register = driver.find_element_by_id("com.sina.weibo:id/titleBack")
        self.my_profile = driver.find_element_by_accessibility_id("我的资料")

