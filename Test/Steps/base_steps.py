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


@When("click {element} in {page}")
def click_element(context,element,page):
    if page in _Page_Map.keys():
        page = _Page_Map[page]()
        element = LocateHeper.get_protect_attribute(page, element)
        LocateHeper(context.driver).find(element).click()

    else:
        logging.error("{0} map to Page object fail".format(page))


@When("{element} input {text} in {page}")
def input_text(context, element, text,page):
    if page in _Page_Map.keys():
        page = _Page_Map[page]()
        element = LocateHeper.get_protect_attribute(page,element)
        LocateHeper(context.driver).find(element).click()
    else:
        logging.error("{0} map to Page object fail".format(page))



@When("waiting for {n} seconds")
def wait_for(context,n):
    time.sleep(int(n))


@When("slide screen")
def slide_screen(context):
    pass


@Given("In {Page}")
def in_page(context,Page):

    if Page in _Page_Map.keys():
        page = _Page_Map[Page]()
        if not page.check(context.driver):
            logging.error("not in page {0}".format(Page))
    else:
        logging.error("{0} map to Page object fail".format(Page))


# 跳转到某个页面和处于某个页面是同样的实现
@Then("should Navigate to {Page}")
def navigat_to_page(context,Page):
    context.execute_steps('''
    Given In {Page}
    ''')

def find_text(text):
    pass
