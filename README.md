# Appium_UI_Autotest
To Do:
week1-->2017.1.21 
完成page和baseStep部分内容

# Dev Notes
## 2017.1.12
确定框架大体结构，分为config、page、result、test、util、apk六部分
## 2017.1.17
添加device类，用于读取xml配置文件，连接手机，获取设备型号名称、版本、品牌以及获取meminfo、cpuinfo、手机分辨率等信息
## 2017.1.18
1.添加Homepage登录，我的资料，注册等元素，添加basesteps.py,用于存放公用方法

2.添加homepage元素定位信息，添加LocateHeper类，以（"id","vaule"）的形式查找元素。