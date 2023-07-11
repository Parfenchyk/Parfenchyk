import time
import unittest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_RuTracker_org_1(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://rutracker.org/")
        self.assertIn("RuTracker.org", driver.title)
        time.sleep(2)
        elem = driver.find_element(By.NAME, "nm")
        # ждем 2 секунды
        time.sleep(2)
        # набор Guardians of the Galaxy в найденном элементе
        elem.send_keys("Guardians of the Galaxy")
        # ждем 2 секунды
        time.sleep(2)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 2 секунды
        time.sleep(2)
        # проверка наличия строки "JavaScript"
        # на странице с результатами поиска
        self.assertIn("JavaScript", driver.page_source)
        # ждем 3 секунды
        time.sleep(5)

    def test_click_button_2(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://rutracker.org/")
        self.assertIn("RuTracker.org", driver.title)
        time.sleep(2)
        # ищем элемент - кнопка-ссылка "Конкурсы" внизу старницы по XPATH
        elem = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[3]/nav/div[2]/a[4]")
        # ждем 2 секунды
        time.sleep(2)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 2 секунды
        time.sleep(2)
        # проверка наличия строки "Awards"
        # на открывшейся странице
        self.assertIn("Awards", driver.page_source)
        # ждем 3 секунды
        time.sleep(5)

    def test_click_button_3(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://rutracker.org/forum/viewforum.php?f=1289")
        self.assertIn("Rutracker Awards (мероприятия и конкурсы) [стр. 1] :: Новости :: RuTracker.org", driver.title)
        time.sleep(2)
        # ищем элемент по XPATH- выпадающий спиосок внизу справа
        WebDriverWait(driver, 90).until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[4]/div[1]/div[2]/table/tbody/tr/td/div/div[2]/div/span/select")))
        dropdown = driver.find_element(By.XPATH,
                                       "/html/body/div[4]/div[1]/div[2]/table/tbody/tr/td/div/div[2]/div/span/select")
        time.sleep(2)
        se = Select(dropdown)
        # перебираем выпадающий список, пока не найдётся "Архив (Общий)" и выбираем эту позицию

        for item in se.options:
            if item.text == ' Архив (Общий) ':
                item.send_keys(Keys.RETURN)
                break
        time.sleep(3)


    def test_check_box_4(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://212.98.182.231:8028/ticket")
        time.sleep(2)

        # ищем элемент по ID - checkbox "Запомнить" и кликаем, чтобы появилась галочка
        cb = driver.find_element(By.ID, "IsRemember").click()
        time.sleep(3)

    def test_radio_5(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://212.98.182.231:8028/ticket")
        time.sleep(2)

        # ищем элемент - radio "по № карты для медобслуживания" и кликаем, чтобы переключился радиобаттон
        # c radio "по персональным данным" (установлен по умолчанию)
        cb = driver.find_element(By.ID, "sw1").click()
        time.sleep(3)


def tearDown(self):
    # закрытие браузера при окончании каждого теста
    self.driver.close()


if __name__ == '__main__':
    unittest.main()
