# Created by dinusha.a at 11/11/2022
Feature: Get json response from REST-API request
  # Enter feature description here

  # success scenario
  Scenario: Get successful json object from a mock rest api
      Given the mock url
      When the user hit the endpoint
      Then a valid json response is retrieved with right data with 200 status code

  # Negative scenario
  Scenario: Get validation error message response from invalid mock API url
      Given the mock url with an special character
      When the user consume the endpoint
      Then a valid error message is showing to the user