from selenium.webdriver.common.by import By
from colorama import Fore, Style


def login(driver, domain, data):
    '''Функция для входа в систему

    Аргументы:
        driver - экземпляр браузера;
        domain - адрес, на котором работает веб-сервер;
        data - данные, которые передаем для авторизации в веб-приложении.
    
    Возвращаемое значение:
        bool - результат авторизации
    '''
    try:
        # Открываем необходимую страницу
        driver.get(f"{domain}/auth/login")
        # Получаем поля username и password через поиск элементов с использованием XPath
        input_username = driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/input")
        input_password = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/input")
        # Вставляем в поля необходимые значения
        # Логин
        input_username.send_keys(data['login'])
        # Пароль
        input_password.send_keys(data['password'])
        # Находим кнопку для авторизации и даем команду на ее нажатие
        driver.find_element(By.XPATH, "/html/body/main/div/form/button").click()
        # Если есть уведомление об успешной аутентификации
        if "Вы успешно аутентифицированы." in driver.find_element(By.XPATH, "/html/body/div[1]").text:
            # Выводим результат в консоль
            print(Fore.GREEN, driver.find_element(By.XPATH, "/html/body/div[1]").text, Style.RESET_ALL, sep='')
            # Возвращаем результат корректной аутентификации
            return True
        else:
            # Выводим информаци об ошибке
            print(Fore.RED, "Аутентификация провалена :(", Style.RESET_ALL, sep='')
            # Прерываем тестирование, отправив значение False для assert в main.py
            return False
    except:
        # Если на одном из предыдущих шагов возникла ошибка, то выводим об этом информацию
        print(Fore.RED,"ERROR:", Style.RESET_ALL, "Во время авторизации произошла ошибка!", sep='')
        return False


# Функция для проверки корректности авторизации
def authorization(driver, domain):
    # Создаем учетные данные, которые необходимо проверить
    data = {
            'login': "admin",
            'password': "Pa$$w0rd",
        }
    # Пытаемся войти в приложение
    if not login(driver, domain, data):
        return False
    return True



def logout(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div/a").click()

        if "Вы вышли из своей учетной записи" in driver.find_element(By.XPATH, "/html/body/div[1]").text:
            print(Fore.GREEN, driver.find_element(By.XPATH, "/html/body/div[1]").text, Style.RESET_ALL)
            return True
        else:
            print(Fore.RED, "Выход провален :(", Style.RESET_ALL, sep='')
            return False
    except:
        print(Fore.RED,"ERROR:", Style.RESET_ALL, "Во время выхода произошла ошибка!", sep='')
        return False
