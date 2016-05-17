from behave import *
from hamcrest import *
from pyaddressbook import addressbook


@given('I want to use an addressbook')
def i_want_to_use_addressbook(context):
    pass


@when('I create a new {addressbook_name}')
def create_new_addressbook(context, addressbook_name):
    context.name = addressbook_name
    context.addressbook = addressbook.Addressbook(addressbook_name)


@when('{addressbook_name} already exists')
def already_exists(context, addressbook_name):
    context.addressbook2 = addressbook.Addressbook(addressbook_name)


@then('I expect that the addressbook will not get created')
def not_created(context):
    pass


@then('I expect the new one to be created')
def check_if_created(context):
    assert_that(context.addressbook.name, equal_to(context.name))

