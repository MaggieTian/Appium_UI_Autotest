#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11
# @Author  : tianqi
# @File    : base_steps.py

import logging
import time
from behave import *
from Util.map import _Page_Map
from Util.locate_helper import LocateHeper


'''
there are some common steps,such as click element or some input text into element
these steps not belong to some page
'''


@When("click {element} in {Page}")
def click_element(context,element,Page):
    logging.info("click {element} in {Page}".format(element=element, Page=Page))
    if Page in _Page_Map.keys():
        page = _Page_Map[Page]()
        element = LocateHeper.get_protect_attribute(page, element)
        LocateHeper(context.driver).find(element).click()

    else:
        logging.error("{0} map to Page object fail".format(Page))


@When("{element} input {text} in {page}")
def input_text(context, element, text, page):
    logging.info("{element} input {text} in {page}".format(element=element,text=text,page=page))
    if page in _Page_Map.keys():
        page = _Page_Map[page]()
        element = LocateHeper.get_protect_attribute(page,element)
        LocateHeper(context.driver).find(element).send_keys(text)
    else:
        logging.error("{0} map to Page object fail".format(page))


@When("waiting for {n} seconds")
def wait_for(context,n):
    logging.info("waiting for {n} seconds".format(n=n))
    time.sleep(int(n))


@When("slide screen")
def slide_screen(context):
    pass


@Given("In {Page}")
def in_page(context, Page):
    logging.info("In {Page}".format(Page=Page))

    if Page in _Page_Map.keys():
        page = _Page_Map[Page]()
        if not page.check(context.driver):
            logging.error("not in page {0}".format(Page))
    else:
        logging.error("{0} map to Page object fail".format(Page))


# 跳转到某个页面和处于某个页面是同样的实现
@Then("should Navigate to {Page}")
def navigat_to_page(context, Page):

    logging.info("should Navigate to {Page}".format(Page=Page))
    context.execute_steps('''
    Given In {0}
    '''.format(Page))


@Then("there should be {element} in {page}")
def check_element(context, element, page):
    logging.info("there should be {element} in {page}".format(element=element,page=page))
    if page in _Page_Map.keys():
        page = _Page_Map[page]()
        element = LocateHeper.get_protect_attribute(page, element)
        if LocateHeper(context.driver).find(element):
            pass
        else:
            context.driver.get_screenshot_as_file(r'/Users/tianqi/Desktop/study/Appium_UI_Autotest/Log/test.png')
            logging.error("找不到元素{element} in {page}".format(element=element,page=page))
            raise Exception

    else:
        logging.error("给定参数{page}不再映射中".format(page=page))
        raise Exception


@When("Switch to alert window and click {button} in {page}")
def swich_and_click(context, button, page):
    logging.info("Switch to alert window and click {button} in {page}".format(button=button,page=page))
    try:
        context.driver.switch_to_alert()
        button = LocateHeper.get_protect_attribute(_Page_Map[page](), button)
        LocateHeper(context.driver).find(button).click()
    except Exception:
        context.driver.get_screenshot_as_file(r'/Users/tianqi/Desktop/study/Appium_UI_Autotest/Log/test.png')
        logging.error("can not Switch to alert window and click {button}".format(button=button))


def find_text(text):
    pass
