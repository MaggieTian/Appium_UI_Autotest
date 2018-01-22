Feature: every function test in HomePage

  Scenario: run test login in homepage

     When waiting for 20 seconds
     Given In HomePage
     When click login in HomePage
     And waiting for 10 seconds
    Then should Navigate to LoginPage
     When username input 1729430864@qq.com in LoinPage
     And  pwd input tianqi57714670 in LoinPage
     And click login_button in LoginPage
     And  waiting for 10 seconds
     Then should Navigate to HomePage
    