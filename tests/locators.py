from selenium.webdriver.common.by import By


PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/a[contains(@href, "account")]')  # Кнопка личный кабинет
LOGIN_FORM_REGISTER_BUTTON = (By.CLASS_NAME, 'Auth_link__1fOlj')  # Кнопка зарегистрироваться под формой входа
NAME_INPUT_FIELD_REGISTER_FORM = (By.XPATH, '//label[ text()="Имя" ]/parent::div/input')  # Поле Имя на форме регистрации
EMAIL_INPUT_FIELD_REGISTER_FORM = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')  # Поле email на форме регистрации
PASSWORD_INPUT_FIELD_REGISTER_FORM = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')  # Поле пароль на форме регистрации
REGISTER_FORM_BUTTON = (By.XPATH, './/button[contains(text(),"Зарегистрироваться")]')  # Кнопка зарегистрироваться на странице регистрации
INCORRECT_PASSWORD_WARNING = (By.CSS_SELECTOR, '.input__error')  # Ошибка выводящаяся при некорректно заполненном пароле на форме регистрации
LOGIN_BUTTON_ON_MAIN_PAGE = (By.XPATH, './/button[contains(text(),"Войти в аккаунт")]')  # Кнопка Войти в аккаунт на главной странице
EMAIL_INPUT_FIELD_LOGIN_FORM = (By.XPATH, './/input[@name="name"]')  # Поле email на форме входа
PASSWORD_INPUT_FIELD_LOGIN_FORM = (By.XPATH, './/input[@name="Пароль"]')  # Поле пароль на форме входа
LOGIN_BUTTON_ON_LOGIN_FORM = (By.XPATH, './/button[contains(text(),"Войти")]')  # Кнопка Войти на форме входа
ORDER_BUTTON_ON_MAIN_PAGE = (By.XPATH, './/button[contains(text(),"Оформить заказ")]')  # Кнопка Оформить заказ на главной странице
LOGIN_BUTTON_ON_REGISTRATION_FORM = (By.XPATH, './/a[contains(@href, "login")]')  # Кнопка войти под формой регистрации
PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE = (By.XPATH, './/a[contains(@href, "forgot-password")]')  # Кнопка Восстановить пароль на странице входа
LOGIN_BUTTON_ON_PASSWORD_RECOVERY_PAGE = (By.XPATH, './/a[contains(@href, "login")]')  # Кнопка Войти на странице восстановления пароля
PROFILE_BUTTON_ON_PERSONAL_ACCOUNT_PAGE = (By.XPATH, './/a[contains(@href, "account/profile")]')  # Кнопка Профиль на странице Личный кабинет
CONSTRUCTOR_BUTTON_ON_THE_TOP = (By.XPATH, './/p[contains(text(),"Конструктор")]')  # Кнопка конструктор на шапке сайта
FLUORESCENT_BUN_BUTTON = (By.XPATH, './/img[contains(@alt, "Флюоресцентная булка R2-D3")]')  # Кнопка выбора флюоресцентной булки
LOGO_ON_THE_TOP = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')  # Логотип Stellar Burgers
EXIT_BUTTON_ON_PROFILE_PAGE = (By.XPATH, './/button[contains(text(),"Выход")]')  # Кнопка выход на странице Личного кабинета
FILLINGS_BUTTON_ON_MAIN_PAGE = By.XPATH, './/span[contains(text(),"Начинки")]/parent::div'# Кнопка перехода к разделу начинки
BUNS_BUTTON_ON_MAIN_PAGE = By.XPATH, './/span[contains(text(),"Булки")]/parent::div'  # Кнопка перехода к разделу булки
SAUSES_BUTTON_ON_MAIN_PAGE = By.XPATH, './/span[contains(text(),"Соусы")]/parent::div'  # Кнопка перехода к разделу соусы
SPICY_SAUSE_BUTTON = (By.XPATH, './/img[contains(@alt, "Соус Spicy-X")]')  # Кнопка выбора острого соуса