import locators
from selenium.webdriver.support import expected_conditions


class TestCunstructorSections:
    def test_transition_to_bun_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.FILLINGS_BUTTON_ON_MAIN_PAGE).click()
        driver.find_element(*locators.BUNS_BUTTON_ON_MAIN_PAGE).click()
        assert expected_conditions.visibility_of_element_located(locators.FLUORESCENT_BUN_BUTTON)

    def test_transition_to_sauses_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.SAUSES_BUTTON_ON_MAIN_PAGE).click()
        assert expected_conditions.invisibility_of_element_located(locators.FLUORESCENT_BUN_BUTTON)

    def test_transition_to_fillings_section(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*locators.FILLINGS_BUTTON_ON_MAIN_PAGE).click()
        assert expected_conditions.invisibility_of_element_located(locators.SPICY_SAUSE_BUTTON)


