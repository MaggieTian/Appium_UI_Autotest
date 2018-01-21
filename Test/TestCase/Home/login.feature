Feature: every function test in HomePage

  Scenario: run test login in homepage

     When waiting for 20 seconds
     Given In HomePage
     When click login in HomePage
     And waiting for 10 seconds
#     Then should Navigate to LoginPagge
