# Appium_UI_Autotest
To Do:
week1-->2017.1.21
完成page和baseStep部分内容
week2-->2017.1.28
1.添加页面专属steps
2.日志详细记录与异常处理

# Dev Notes
## 2017.1.12
确定框架大体结构，分为config、page、result、test、util、apk六部分
## 2017.1.17
添加device类，用于读取xml配置文件，连接手机，获取设备型号名称、版本、品牌以及获取meminfo、cpuinfo、手机分辨率等信息
## 2017.1.18
1.添加Homepage登录，我的资料，注册等元素，添加basesteps.py,用于存放公用方法

2.添加homepage元素定位信息，添加LocateHeper类，以（"id","vaule"）的形式查找元素。

##2017.1.21
完成homepage 和basesteps部分内容
1.basesteps中添加公用方法：跳转页面、在某个页面点击元素、发送text等。
2.每个页面中的元素是protected属性，可根据传入的字符串参数获取到。每个页面对象只存放元素和check方法。
3.map.py文件里用来映射字符串和页面对象。
4.enviroment.py中配置每次运行所有feature前连接手机，featutre运行结束后断开。
