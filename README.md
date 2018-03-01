# Appium_UI_Autotest
To Do:
## week1-->2017.1.21
完成page和baseStep部分内容

## week2-->2017.1.28

1.添加页面专属steps
2.日志详细记录与异常处理

## week3-->2017.2.04

完成结果运行结果收集

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

## 2017.1.22
添加loginPage，完成一个完整的feature，验证登录功能，出现问题：跳转页面识别步骤，未识别输入框输入文本

## 2017.1.23
1.解决问题：不能正常跳转页面，识别输入框输入文本。（总结：再细心一点，log写全写好调试很有用）
2.添加Log部分，记录每次运行产生的详细log

## 2017.1.28
添加日志配置文件（json文件），通过加载配置文件来读入日志配置信息

## 2017.1.29
在所有feature执行之前读取配置信息设置日志。log_helper中添加获取Config文件目录部分。

## 2017.1.30

1.完成日志详细记录与异常处理
2.添加setting页面，login_steps处理跟login有关的steps

## 2017.1.31

1. 问题发现与解决：
在命令行（终端）使用behave运行feature,需要做以下配置：

    a)在C:\Python36\Lib\site-packages(该目录加入环境变量)目录下新建**.pth文件，里面写入各个package的绝对路径。
 原因是在IDE里运行py文件和命令行运行查找包的方式不一样；IDE会在项目根目录所有目录下去查找，而终端只会在当前目录下查找。
 因此会出现包引入的错误现象。
 
    b)修改behave目录下runner.py文件为，(打开文件时增加encoding="utf-8"以支持utf-8编码，不然项目里出现中文字符就会报编码错误)：
  with open(filename,encoding="utf-8") as f:
  此操作针对于python3以上的python版本

## 2018.2.02

1.添加判断界面是否出现某元素方法，完成退出登录。
2.添加识别弹出框点击按钮方法（识别弹出框并点击确认还有问题）
3.添加失败截图功能

## 2018.2.05

1.封装检验story中传入的page是否在页面映射中为一个函数，函数进行检验并返回页面对象
2添加runner.py用来读取run_config配置文件中的tag所在的场景，并运行。

## 2018.2.08
1. 去掉每一步骤中打印具体步骤，并进一步完善异常处理。
2. 重新配置日志打印，不使用xml配置文件，增加在每次feature和scenario执行之后将执行结果写入csv文件

## 2018.2.09
1.添加reportHTML模板，添加ReporterHelper模块用以读取CSV文件中的结果数据生成报告。（未全部完成）

## 2018.2.26
1.完成报告生成

## 2018.2.27
1. 完成测试结果的饼图说明
2. v1.0完成，可完整执行Test Case 中的feature，然后生成相应的log与测试报告

## 2018.3.1
1. 添加判断页面某个元素的text是否为某个值
2. 去掉steps中try,except。不然执行的所有Step都是成功的