from behave import *

@when('Im on {url}')
def step_impl(context, url):
    context.browser.visit(url)

@when('I fill username field {u_field} with {value}')
def step_impl(context, u_field, value):
    username_field = context.browser.find_by_id('id_'+u_field)
    username_field.send_keys(value)

@when('I fill password field {p_field} with {value}')
def step_impl(context, p_field, value):
    password_field = context.browser.find_by_id('id_' + p_field)
    password_field.send_keys(value)

@when('I click {button}')
def step_impl(context, button):
    submit_button = context.browser.find_by_xpath("//input[@type='submit' and @value='add']")
    submit_button.click()

@then('I should see {message}')
def step_impl(context, message):
    assert context.browser == message