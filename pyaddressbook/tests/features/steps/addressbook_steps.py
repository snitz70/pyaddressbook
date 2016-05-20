from behave import *
from hamcrest import *
from pyaddressbook import addressbook
import peewee
import mock


@given('I want to use an addressbook')
def i_want_to_use_addressbook(context):
    pass


@given('I want to create a new addressbook')
def new_addresbook(context):
    pass


@when('I create a new {addressbook_name}')
def create_new_addressbook(context, addressbook_name):
    context.name = addressbook_name
    mock_addr = mock.Mock()
    mock_addr.create_addressbook.return_value = addressbook.Addressbook(name=context.name)
    context.addressbook = mock_addr.create_addressbook(addressbook_name)


@when('{addressbook_name} already exists')
def already_exists(context, addressbook_name):
    context.name = addressbook_name


@then('I expect that the addressbook will not get created')
def not_created(context):
    mock_addr = mock.Mock()
    mock_addr.create_addressbook.side_effect = peewee.IntegrityError
    assert_that(calling(mock_addr.create_addressbook), raises(peewee.IntegrityError))


@then('I expect the new one to be created')
def check_if_created(context):
    assert_that(context.addressbook.name, equal_to(context.name))

