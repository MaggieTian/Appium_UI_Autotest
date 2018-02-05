
# -*- coding: utf-8 -*-
# @Time    : 2018/2/5
# @Author  : MaggieTian
# @File    : runner.py

import xml.etree.ElementTree as ET
from Util.log_helper import LogHelper
import os
import logging

command = "behave"
# 从配置文件中读取运行的tag,若没有tag则运行全部feature
tree = ET.parse(os.path.join(LogHelper.config_file_path, "run_config.xml"))
root = tree.getroot()
if root:
    for node in root:
        if node.text:
            command += " --tags={}".format(node.text)
command += r" >out.txt"
print(command)
logging.info("run command is {cmd}".format(cmd=command))

root_path = os.path.dirname(__file__)
os.popen("cd {path}".format(path=os.path.join(root_path,os.sep+"Test")))
# os.popen(command)