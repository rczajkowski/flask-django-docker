import json

from behave import *
import requests

def after_scenario(context, scenario):
    print('Finished running a scenario')

@given('the API at the URL "{url}"')
def step_impl(context, url):
    context.url = url

@when('I send a signed {method} request to the "{path}" path')
def step_impl(context, method, path):
    if method == 'GET':
        context.response = requests.get(context.url + path)

    elif method == 'POST':
        user = json.dumps({u'username': 'testuser', u'password': 'tespassword'})
        headers = {'content-type': 'application/json'}

        context.response = requests.post(url=context.url + path, data=user, headers=headers)
    elif method == 'PUT':
        data = json.dumps({u'username': 'edituser'})
        headers = {'content-type': 'application/json'}
        context.response = requests.put(url=context.url + path, data=data, headers=headers)
    else:
        context.response = requests.delete(url=context.url + path)

@then('status code {status:d} should be returned')
def step_impl(context, status):
    print (context.response)
    assert context.response.status_code == status


