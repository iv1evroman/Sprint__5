from selenium.webdriver.common.by import By


PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a')  # Кнопка личный кабинет
LOGIN_FORM_REGISTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')  # Кнопка зарегистрироваться под формой входа
NAME_INPUT_FIELD_REGISTER_FORM = (By.XPATH, '//label[ text()="Имя" ]/parent::div/input')  # Поле Имя на форме регистрации
EMAIL_INPUT_FIELD_REGISTER_FORM = (By.XPATH, '//label[ text()="Email" ]/parent::div/input')  # Поле email на форме регистрации
PASSWORD_INPUT_FIELD_REGISTER_FORM = (By.XPATH, '//label[ text()="Пароль" ]/parent::div/input')  # Поле пароль на форме регистрации
REGISTER_FORM_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка зарегистрироваться на странице регистрации
INCORRECT_PASSWORD_WARNING = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')  # Ошибка выводящаяся при некорректно заполненном пароле на форме регистрации
LOGIN_BUTTON_ON_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')  # Кнопка Войти в аккаунт на главной странице
EMAIL_INPUT_FIELD_LOGIN_FORM = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # Поле email на форме входа
PASSWORD_INPUT_FIELD_LOGIN_FORM = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # Поле пароль на форме входа
LOGIN_BUTTON_ON_LOGIN_FORM = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')  # Кнопка Войти на форме входа
ORDER_BUTTON_ON_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')  # Кнопка Оформить заказ на главной странице
LOGIN_BUTTON_ON_REGISTRATION_FORM = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')  # Кнопка войти под формой регистрации
PASSWORD_RECOVERY_BUTTON_ON_LOGIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')  # Кнопка Восстановить пароль на странице входа
LOGIN_BUTTON_ON_PASSWORD_RECOVERY_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')  # Кнопка Войти на странице восстановления пароля
PROFILE_BUTTON_ON_PERSONAL_ACCOUNT_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a')  # Кнопка Профиль на странице Личный кабинет
CONSTRUCTOR_BUTTON_ON_THE_TOP = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')  # Кнопка конструктор на шапке сайта
FLUORESCENT_BUN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]')  # Кнопка выбора флюоресцентной булки
LOGO_ON_THE_TOP = (By.XPATH, '//*[@id="root"]/div/header/nav/div')  # Логотип Stellar Burgers
EXIT_BUTTON_ON_PROFILE_PAGE = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')  # Кнопка выход на странице Личного кабинета
FILLINGS_BUTTON_ON_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')  # Кнопка перехода к разделу начинки
BUNS_BUTTON_ON_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')  # Кнопка перехода к разделу булки
SAUSES_BUTTON_ON_MAIN_PAGE = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')  # Кнопка перехода к разделу соусы
SPICY_SAUSE_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]')  # Кнопка выбора острого соуса