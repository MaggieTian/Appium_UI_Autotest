#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12
# @Author  : MaggieTian
# @File    : device.py

import xml.etree.ElementTree as ET
import os
import logging
from appium import webdriver

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))  # 获取项目根目录路径
xml_file_path = os.path.join(project_path,"Config\\")  # 获取Config文件夹路径,所有配置文件都放在config文件夹下

class Device:

    def __init__(self):
        global devices
        devices = {}  # 用于存放读取到的device信息

    # 读取xml配置文件获取连接设备的Desired Capabilities
    def get_device(self, file_name):

        try:
            tree = ET.parse(xml_file_path + file_name)
            root = tree.getroot()
            for node in root:  # 标签名为key,标签里的内容为value
                devices[node.tag] = node.text

        except Exception:
            logging.error("Error:parse file:" + xml_file_path + file_name)  # 记录异常错误信息

    # 连接设备
    def connect_device(self,url):

        driver = webdriver.Remote(url, devices)
        return driver






# debug
if __name__ == "__main__":
    device = Device()
    device.get_device("device.xml")
    print(devices)
    device.connect_device('http://localhost:4723/wd/hub')




