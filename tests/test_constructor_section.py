import locators
from selenium.webdriver.support import expected_conditions


class TestCunstructorSections:
    def test_transition_to_bun_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.FILLINGS_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.BUNS_BUTTON_ON_MAIN_PAGE).click()
        assert driver.find_element(*locators.BUNS_BUTTON_ON_MAIN_PAGE).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_transition_to_sauses_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.SAUSES_BUTTON_ON_MAIN_PAGE).click()
        assert driver.find_element(*locators.SAUSES_BUTTON_ON_MAIN_PAGE).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_transition_to_fillings_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.FILLINGS_BUTTON_ON_MAIN_PAGE).click()
        assert driver.find_element(*locators.FILLINGS_BUTTON_ON_MAIN_PAGE).get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


