import locators


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.LOGIN_FORM_REGISTER_BUTTON).click()
        driver.find_element(*locators.NAME_INPUT_FIELD_REGISTER_FORM).send_keys('Рома')
        driver.find_element(*locators.EMAIL_INPUT_FIELD_REGISTER_FORM).send_keys('romanivlev14999@yandex.ru')
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_REGISTER_FORM).send_keys('privetik')
        driver.find_element(*locators.REGISTER_FORM_BUTTON).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_incorrect_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.LOGIN_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.LOGIN_FORM_REGISTER_BUTTON).click()
        driver.find_element(*locators.NAME_INPUT_FIELD_REGISTER_FORM).send_keys('Ваcя')
        driver.find_element(*locators.EMAIL_INPUT_FIELD_REGISTER_FORM).send_keys('123@invox.ru')
        driver.find_element(*locators.PASSWORD_INPUT_FIELD_REGISTER_FORM).send_keys('hello')  # 5 символов
        driver.find_element(*locators.REGISTER_FORM_BUTTON).click()
        assert driver.find_element(*locators.INCORRECT_PASSWORD_WARNING).text == 'Некорректный пароль'
        driver.quit()
