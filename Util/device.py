#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12
# @Author  : MaggieTian
# @File    : device.py

import xml.etree.ElementTree as ET
import os
import logging

import time
from appium import webdriver
import subprocess
from Page.Home.home_page import HomePage
from Util.locate_helper import LocateHeper


project_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))  # 获取项目根目录路径
xml_file_path = os.path.join(project_path,r"Config/")  # 获取Config文件夹路径,所有配置文件都放在config文件夹下

class Device:

    def __init__(self):
        self.devices = {}  # 用于存放读取到的device信息

    # 读取xml配置文件获取连接设备的Desired Capabilities
    def get_device(self, file_name):
        '''

        :param file_name: the xml config file used to store the data for conneting phone
        :return: no vaule
        '''

        try:
            tree = ET.parse(xml_file_path + file_name)
            root = tree.getroot()
            for node in root:  # 标签名为key,标签里的内容为value
                self.devices[node.tag] = node.text
            print("手机设备信息：{device}".format(device=self.devices))

        except Exception:
            logging.error("Error:parse file:" + xml_file_path + file_name)  # 记录异常错误信息

    # 连接设备
    def connect_device(self,url):
        '''
        :param url:the url for conneting phone by driver
        :return: if sucessfully connect return driver,else return False
        '''
        try:
            driver = webdriver.Remote(url, self.devices)
            return driver
        except Exception:
            return False

    # 得到手机信息
    def getPhoneInfo(self):
        cmd = "adb -s " + self.devices['deviceName'] + " shell cat /system/build.prop "
        print(cmd)
        # phone_info = os.popen(cmd).readlines()
        phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).stdout.readlines()
        result = {"release": "", "model": "", "brand": "", "device": ""}  # 记录最终需要的手机信息参数
        release = "ro.build.version.release="  # 版本
        model = "ro.product.model="  # 型号
        brand = "ro.product.brand="  # 品牌
        device = "ro.product.device="  # 设备名
        for line in phone_info:
            for i in line.split():
                temp = i.decode()
                if temp.find(release) >= 0:
                    result["release"] = temp[len(release):]
                    break
                if temp.find(model) >= 0:
                    result["model"] = temp[len(model):]
                    break
                if temp.find(brand) >= 0:
                    result["brand"] = temp[len(brand):]
                    break
                if temp.find(device) >= 0:
                    result["device"] = temp[len(device):]
                    break
        print(result)
        return result

    # 得到最大运行内存
    def get_men_total(self):
        cmd = "adb -s " + self.devices['deviceName'] + " shell cat /proc/meminfo"
        get_cmd = os.popen(cmd).readlines()
        men_total = 0
        men_total_str = "MemTotal"
        for line in get_cmd:
            if line.find(men_total_str) >= 0:
                men_total = line[len(men_total_str) + 1:].strip()
                break
        return men_total

    # 得到几核cpu
    def get_cpu_kel(self):
        cmd = "adb -s " + self.devices['deviceName'] + " shell cat /proc/cpuinfo"
        get_cmd = os.popen(cmd).readlines()
        find_str = "processor"
        int_cpu = 0
        for line in get_cmd:
            if line.find(find_str) >= 0:
                int_cpu += 1
        return str(int_cpu) + "核"

    # 得到手机分辨率
    def get_app_pix(self):
        result = os.popen("adb -s " + self.devices['deviceName']+ " shell wm size", "r")
        return result.readline().split("Physical size:")[1]

    # 得到手机屏幕大小
    @classmethod
    def get_size(cls, driver):

        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)


# debug
if __name__ == "__main__":
    device = Device()
    device.get_device("device.xml")
    print(device)
    driver = device.connect_device('http://localhost:4723/wd/hub')
    print(device.get_app_pix())
    print(device.get_men_total())
    print(device.get_size(driver))
    page = HomePage()
    time.sleep(30)
    LocateHeper(driver).find(page.login).click()

#新浪微博
#com.sina.weibo
#com.sina.weibo.SplashActivity