import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import TestData


class TestLogin:
    def test_login_by_main_page_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.email_for_login_tests)
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.correct_password)
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*locators.ORDER_BUTTON_ON_MAIN_PAGE).text == 'Оформить заказ'

    def test_login_by_personal_account_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.email_for_login_tests)
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.correct_password)
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*locators.ORDER_BUTTON_ON_MAIN_PAGE).text == 'Оформить заказ'

    def test_login_by_registration_form_login_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.LOGIN_FORM_REGISTER_BUTTON).click()
        driver.find_element(*locators.LOGIN_BUTTON_ON_REGISTRATION_FORM).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.email_for_login_tests)
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.correct_password)
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*locators.ORDER_BUTTON_ON_MAIN_PAGE).text == 'Оформить заказ'

    def test_login_by_password_recovery_form_login_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE).click()
        driver.find_element(*locators.LOGIN_BUTTON_ON_PASSWORD_RECOVERY_PAGE).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.email_for_login_tests)
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys(TestData.correct_password)
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*locators.ORDER_BUTTON_ON_MAIN_PAGE).text == 'Оформить заказ'
