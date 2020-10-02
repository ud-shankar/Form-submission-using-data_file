from Source.datafile import test_data
import random
import pytest
from pytest_bdd import scenario, given, when, then
from Drivers.Chromedriver import driver
from Pages.locators import form_locators


data = test_data()


@pytest.mark.forms                  # Used to run in the terminal using command pytest -m forms
@scenario('../Features/Form_fill.feature', 'User access test-data from yaml file to randomly access data and fill the form')
def test_forms():
    pass


@given("User opens DemoQA sample forms page")
def classic_created():
    driver.get("https://demoqa.com/automation-practice-form/")
    driver.implicitly_wait(30)


@when("User enters first and last names")
def student_name():
    send_element(form_locators.first_name, data.Names())
    send_element(form_locators.last_name, data.Names())


@when("User enters mail id, mobile number and subject")
def subject_email():
    send_element(form_locators.email, data.email())
    send_element(form_locators.mobile_number, data.phone_number())


@when("User selects gender and hobbies")
def radio_checkbox():
    radio = random.randint(1, 3)
    checkbox = random.randint(1, 3)
    radio_button = driver.find_element_by_xpath(form_locators.gender.format(radio))
    checkbox_button = driver.find_element_by_xpath(form_locators.hobbies.format(checkbox))
    driver.execute_script("arguments[0].click();", radio_button)        # javascript click when you encounter element click interceptions
    driver.execute_script("arguments[0].click();", checkbox_button)


@when("User enter address in textbox")
def address():
    send_element(form_locators.current_address, data.address())
    submit = driver.find_element_by_id(form_locators.submit)
    driver.execute_script("arguments[0].scrollIntoView(true);", submit)         # to scroll into view dropdown elements and submit button


@when("User selects state and city from the dropdown list")
def state_city():
    i = random.randint(0,3)
    j = random.randint(0,1)
    driver.find_element_by_id(form_locators.state).click()
    driver.implicitly_wait(10)
    driver.find_element_by_id(form_locators.state_list.format(i)).click()
    driver.find_element_by_id(form_locators.city).click()
    driver.implicitly_wait(10)
    driver.find_element_by_id(form_locators.city_list.format(j)).click()


@then("User clicks on submit button")
def submit():
    driver.find_element_by_id(form_locators.submit).click()
    driver.implicitly_wait(5)
    driver.find_element_by_id(form_locators.close).click()


def send_element(element, value):
    driver.find_element_by_id(element).send_keys(value)


@pytest.fixture(scope="session", autouse=True)
def posttest(request):
    yield driver
    driver.quit()