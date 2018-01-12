#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12
# @Author  : MaggieTian
# @File    : get_device.py

import xml.etree.ElementTree as ET
import os
import logging

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))  # 获取项目根目录路径
xml_file_path = os.path.join(project_path,"Config\\")  # 获取Config文件夹路径,所有配置文件都放在config文件夹下


def get_device(file_name):

    global devices
    devices = {}                    # 用于存放读取到的device信息
    try:
        tree = ET.parse(xml_file_path+file_name)
        root = tree.getroot()
        for node in root:                 # 标签名为key,标签里的内容为value
            devices[node.tag] = node.text

    except Exception:
        logging.error("Error:parse file:"+xml_file_path+file_name)   # 记录异常错误信息


# debug
if __name__ == "__main__":
    get_device("device.xml")
    print(devices)




