
# -*- coding: utf-8 -*-
# @Time    : 2018/2/5
# @Author  : MaggieTian
# @File    : runner.py

import xml.etree.ElementTree as ET
from Util.log_helper import LogHelper
import os
import logging

command = "behave"
root_path =os.path.abspath(os.path.dirname(__file__)) # 得到项目根目录
# 从配置文件中读取运行的tag,若没有tag则运行全部feature
tree = ET.parse(os.path.join(LogHelper.config_file_path, "run_config.xml"))
root = tree.getroot()
if root:
    for node in root:
        if node.text:
            command += " --tags={}".format(node.text)
command += r" >{path}{sep}{filename}".format(path=root_path+os.sep+"Log", sep=os.sep, filename="out.txt")
logging.info("run command is {cmd}".format(cmd=command))


test_path = root_path+os.sep+"Test"
os.chdir(test_path)
p = os.popen("dir")
os.popen(command)