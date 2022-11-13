import requests
from behave import *
# from allure_behave.hooks import allure_report

url = 'http://dummy.restapiexample.com/api/v1/employee/1'
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Charset": "utf-8",
    "Accept-Encoding": 'gzip, deflate',
    "Accept-Language": "en-US",
}


@given('the mock url')
def step_impl(context):
    context.url = url


@when('the user hit the endpoint')
def step_impl(context):
    context.response = requests.session().get(url, headers=headers)


@Then('a valid json response is retrieved with right data with 200 status code')
def step_impl(context):
    print("================ Scenario 1 =====================")
    print(context.response.json())
    assert context.response.status_code == 200, "Response code is different: % s" % context.response.status_code + \
                                                " Error: " + str(context.response.content)

    json_response = context.response.json()
    assert json_response['status'] == "success", "request failed: %s" % json_response

    json_response = context.response.json()
    assert json_response['message'] == "Successfully! Record has been fetched.", "Invalid message: %s" % json_response


# allure_report("test-results/reports")
