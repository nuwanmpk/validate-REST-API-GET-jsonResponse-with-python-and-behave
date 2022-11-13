import requests
from behave import *

url = 'http://dummy.restapiexample.com/api/v1/employee/#'
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Charset": "utf-8",
    "Accept-Encoding": 'gzip, deflate',
    "Accept-Language": "en-US",
}


@given('the mock url with an special character')
def step_impl(context):
    context.url = url


@when('the user consume the endpoint')
def step_impl(context):
    context.response = requests.session().get(url, headers=headers)


@Then('a valid error message is showing to the user')
def step_impl(context):
    print("================ Scenario 2 =====================")
    print(context.response.json())
    json_response = context.response.json()
    assert json_response['message'] == "Error Occured! Page Not found, contact rstapi2example@gmail.com", "Invalid message: %s" % json_response
