# -*- coding: utf-8 -*-
# @Time    : 2018/1/18
# @Author  : MaggieTian
# @File    : locate_helper.py

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import logging



# support for android find element by accessibility_id and android_uiautomator
By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID


# Map the method to find element
_LOCATOR_MAP = {
                'id': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'class_name': By.CLASS_NAME,
                'accessibility_id':By.ACCESSIBILITY_ID,
                'android_uiautomator':By.ANDROID_UIAUTOMATOR,
                }


'''
LocateHeper is used to encapsulation the find_element_by_* of appium

in order to fill the value and find method in the page object
'''


class LocateHeper(object):

    def __init__(self,driver):

        self.driver = driver

    # translate the parameter {method} to the menthod of By

    @staticmethod
    def locator(method,vaule):
        if method in _LOCATOR_MAP.keys():

            return _LOCATOR_MAP[method],vaule
        else:
            logging.error("{0} is not in find method".format(method))
            raise Exception

    # find element
    def find(self,location):

        element = self.driver.find_element(by=location[0], value=location[1])
        if element:
            return element
        else:
            logging.error("not found element {0}".format(location))

    # get the protected element
    @staticmethod
    def get_protect_attribute(page_object, name):
        name = "_"+name
        if hasattr(page_object,name):
            return getattr(page_object,name)
        else:
            logging.error("there is no {1} in {0},please input right element name".format(page_object,name))



