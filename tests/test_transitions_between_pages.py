import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestTransitions:
    def test_transition_to_personal_account_by_click(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys('romanivlev14999@yandex.ru')
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys('privetik')
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.PROFILE_BUTTON_ON_PERSONAL_ACCOUNT_PAGE))
        assert driver.find_element(*locators.PROFILE_BUTTON_ON_PERSONAL_ACCOUNT_PAGE).text == 'Профиль'

    def test_transition_to_constructor_by_clicking_constructor_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys('romanivlev14999@yandex.ru')
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys('privetik')
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.CONSTRUCTOR_BUTTON_ON_THE_TOP))
        driver.find_element(*locators.CONSTRUCTOR_BUTTON_ON_THE_TOP).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.FLUORESCENT_BUN_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transition_to_constructor_by_clicking_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys('romanivlev14999@yandex.ru')
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys('privetik')
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.LOGO_ON_THE_TOP))
        driver.find_element(*locators.LOGO_ON_THE_TOP).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.FLUORESCENT_BUN_BUTTON))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_exit_by_clicking_exit_button_on_profile_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.EMAIL_INPUT_FIELD_LOGIN_FORM).send_keys('romanivlev14999@yandex.ru')
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_LOGIN_FORM).send_keys('privetik')
        driver.find_element(*locators.LOGIN_BUTTON_ON_LOGIN_FORM).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.EXIT_BUTTON_ON_PROFILE_PAGE))
        driver.find_element(*locators.EXIT_BUTTON_ON_PROFILE_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_FORM))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
