import locators
from data import TestData
from helpers import Helpers


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.LOGIN_FORM_REGISTER_BUTTON).click()
        driver.find_element(*locators.NAME_INPUT_FIELD_REGISTER_FORM).send_keys(TestData.name_for_registration_test)
        driver.find_element(*locators.EMAIL_INPUT_FIELD_REGISTER_FORM).send_keys(Helpers.random_email(self))
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_REGISTER_FORM).send_keys(TestData.correct_password)
        driver.find_element(*locators.REGISTER_FORM_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_incorrect_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.LOGIN_FORM_REGISTER_BUTTON).click()
        driver.find_element(*locators.NAME_INPUT_FIELD_REGISTER_FORM).send_keys(TestData.name_for_registration_test)
        driver.find_element(*locators.EMAIL_INPUT_FIELD_REGISTER_FORM).send_keys(Helpers.random_email(self))
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_REGISTER_FORM).send_keys(TestData.incorrect_password_for_registration_test)  # 5 символов
        driver.find_element(*locators.REGISTER_FORM_BUTTON).click()
        assert driver.find_element(*locators.INCORRECT_PASSWORD_WARNING).text == 'Некорректный пароль'
