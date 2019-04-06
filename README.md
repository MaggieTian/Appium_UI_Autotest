# Appium_UI_Autotest


This is a simple autotest framework about WEBO APP UI.It uses behave + appium + allure report to completed.


behave is behaviour-driven development, Python style.Behavior-driven development (or BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project. We have a page further describing this philosophy.

**behave** uses tests written in a natural language style, backed up by Python code.this is the introduction and development document:[behave](https://behave.readthedocs.io/en/latest/)



**Allure Framework** is a flexible lightweight multi-language test report tool that not only shows a very concise representation of what have been tested in a neat web report form, but allows everyone participating in the development process to extract maximum of useful information from everyday execution of tests.
this is the introduction and development document:[Allure Framework](https://docs.qameta.io/allure)


## Directory Structure

+  **Apk** is the directory that stores apk packages
+  **Config** all configuration file in this directory
+  **Log**  is the directory that stores log files
+  **Test** is the directory that stores TestCase(behave features) and  Steps
+  **Page** this framework used PageObject, so that the directory stores Pages in weiboAPP
+  **Utill** stores all the tools program

## How To Run

+ clone the project

  <code> git clone https://github.com/MaggieTian/Appium_UI_Autotest.git</code>

+ change dir to behave features dir
 
  <code>cd Test/TestCase</code>
  
+ run the command to execute test to genenrate allure report dir

  <code>behave -f allure_behave.formatter:AllureFormatter -o allure_result ./</code>
  
+ generate allure report

  <code>allure serve allure_result </code>
  
  then you will see the allure report that in a opening browser,such as below picture:
  
  ![Allure Report](https://github.com/MaggieTian/Appium_UI_Autotest/blob/master/Photo/allure_report.png?raw=true)
  
  

## Integrate Allure Framework In Jenkins


if you want to the autest framework works in Jenkins, the configration about Allure can refer to my CSDN BLOG [Jenkins Allure Report 插件的相关配置](https://blog.csdn.net/MaggieTian77/article/details/80834074)
