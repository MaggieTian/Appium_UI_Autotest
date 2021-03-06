#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11
# @Author  : tianqi
# @File    : base_steps.py

import logging
import time
from behave import *
from Util.locate_helper import LocateHeper
from Util.check import check_page
'''
there are some common steps,such as click element or some input text into element
these steps not belong to some page
'''


@When("click {element} in {Page}")
def click_element(context,element,Page):

    page = check_page(Page)
    element = LocateHeper.get_protect_attribute(page, element)
    LocateHeper(context.driver).find(element).click()


@When("{element} input {text} in {page}")
def input_text(context, element, text, page):
    page = check_page(page)
    element = LocateHeper.get_protect_attribute(page,element)
    LocateHeper(context.driver).find(element).send_keys(text)


@When("waiting for {n} seconds")
def wait_for(context, n):
    time.sleep(int(n))


@When("slide screen")
def slide_screen(context):
    pass


@Given("In {Page}")
def in_page(context, Page):
    page = check_page(Page)
    # if not in parameter page,raise exception to stop run next steps
    if not page.check(context.driver):
        msg = "not in page {0}".format(Page)
        context.logger.error(msg)
        raise Exception(msg)


# 跳转到某个页面和处于某个页面是同样的实现
@Then("should Navigate to {Page}")
def navigat_to_page(context, Page):
    context.execute_steps('''
    Given In {0}
    '''.format(Page))


@Then("there should be {element} in {page}")
def check_element(context, element, page):
    page = check_page(page)
    element = LocateHeper.get_protect_attribute(page, element)
    if LocateHeper(context.driver).find(element):
        pass
    else:
        context.driver.get_screenshot_as_file(r'/Users/tianqi/Desktop/study/Appium_UI_Autotest/Log/test.png')
        context.logger.error("找不到元素{element} in {page}".format(element=element,page=page))
        raise Exception


@When("Switch to alert window and click {button} in {page}")
def swich_and_click(context, button, page):
    context.driver.switch_to_alert()
    page = check_page(page)
    button = LocateHeper.get_protect_attribute(page, button)
    LocateHeper(context.driver).find(button).click()

@Then("The text of {element} should be {value} in {page}")
def find_text(context, element,value,page):
    page = check_page(page)
    element = LocateHeper.get_protect_attribute(page,element)
    if LocateHeper(context.driver).find(element).get_text() != value:
        raise Exception("The text of {element} is not {value} in {page}".format(element=element,value=value,page=page))

