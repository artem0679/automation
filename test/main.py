from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities import phase
from authorization import authorization, logout

from time import sleep

# Функция для запуска автоматизированного тестирования
def auto_test():
   # Создание экземпляра драйвера
   options = webdriver.ChromeOptions()
   # Добавление необходимых агрументов
   options.add_argument("start-maximized")
   options.add_argument("disable-infobars")
   options.add_argument("--disable-extensions")
   options.add_argument("--disable-gpu")
   options.add_argument("--disable-dev-shm-usage")
   options.add_argument("--no-sandbox")
   # Создание экземпляра Chrome
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="123.0.6312.106").install()), options=options)
   driver.implicitly_wait(10)
   # Задаем адрес, на котором работает наше приложение
   domain = "http://127.0.0.1:80"
   # Передаем адрес в экземпляр
   driver.get(domain)
   # Запускаем тестирование авторизации
   phase(1, "Тестирование авторизации")
   # Вызываем тест для авторизации
   result_authorization = authorization(driver, domain)
   # Если результат будет False, то в терминал будет выведена ошибка,
   # а тест завершится с результатом FAILED
   assert result_authorization == True, "Ошибка модуле авторизации."
   # Закрываем экземпляр бразуера и выходим из него
   driver.close()
   driver.quit()

def main():
   # Запуск автотеста
   auto_test()
   print('\n\n\n')

main()
