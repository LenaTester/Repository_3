from telnetlib import EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from framework_from_scratch.page_objects.home_page import HomePage
from framework_from_scratch.utilities.driver_factory import DriverFactory

@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1, is_headless=False)
    driver.get('http://loveread.ec/')
    yield driver
    driver.quit()

@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)

@pytest.fixture()
def successful_login(get_home_page, create_driver):
    home_page = get_home_page
    user_page = home_page.set_user_email('OlenaL').set_password('VTfRkcJVNi').click_login_button()
    return user_page

@pytest.fixture()
def non_successful_login_wrong_login(get_home_page, create_driver):
    home_page = get_home_page
    WrongCreds = home_page.set_user_email('Natasha').set_password('VTfRkcJVNi').click_login_button_wrong_creds()
    return WrongCreds

@pytest.fixture()
def non_successful_login_wrong_password(get_home_page, create_driver):
    home_page = get_home_page
    WrongCreds = home_page.set_user_email('OlenaL').set_password('OlenaL').click_login_button_wrong_creds()
    return WrongCreds

@pytest.fixture()
def successful_login_go_to_profile(get_home_page, create_driver):
    home_page = get_home_page
    ProfilePage = home_page.set_user_email('OlenaL').set_password('VTfRkcJVNi').click_login_button().click_profile_page_button()
    return ProfilePage

@pytest.fixture()
def new_pass(successful_login_go_to_profile, create_driver):
    profile_page = successful_login_go_to_profile
    NewSuccessfulPassword = profile_page.set_new_password('VTfRkcJVNi').set_new_password_confirmation('VTfRkcJVNi').click_save_button()
    return NewSuccessfulPassword

@pytest.fixture()
def new_email(successful_login_go_to_profile, create_driver):
    profile_page = successful_login_go_to_profile
    NewEmailPage = profile_page.set_new_email('elena.liashchenko03103@gmail.com').email_submit_button()
    return NewEmailPage

@pytest.fixture()
def new_wrong_email(successful_login_go_to_profile, create_driver):
    profile_page = successful_login_go_to_profile
    user_page = profile_page.set_new_email('test').email_submit_button()
    return user_page