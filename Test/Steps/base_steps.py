#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11
# @Author  : tianqi
# @File    : base_steps.py
from appium import webdriver
from behave import *
'''
there are some common steps,such as click element or some input text into element
these steps not belong to some page
'''


@When("click {element}")
def click_element(context,element):
    element.click()


@When("{element} input {text}")
def input_text(context, element, text):
    element.send_keys(text)
