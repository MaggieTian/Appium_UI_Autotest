Feature: every function test in HomePage

  Scenario: run test login in homepage

#     When waiting for 20 seconds
#     Given In HomePage
#     When click login in HomePage
#     And waiting for 10 seconds
#     Then should Navigate to LoginPage
#     When username input 13248226806 in LoginPage
#     And  pwd input tianqi57714670QQ in LoginPage
#     And click login_button in LoginPage
     When  waiting for 10 seconds
     When click my_profile in HomePage
     Then there should be setting in SettingPage
     When sign out
     And waiting for 3 seconds
     Then should Navigate to LoginPage


