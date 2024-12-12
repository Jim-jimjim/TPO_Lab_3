import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestChangeCount(unittest.TestCase):

    def setUp(self):
        """Инициализация драйвера перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://goldapple.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_add_product_to_cart(self):
        """Тест: Проверка обновления количества товара в корзине"""

        driver = self.driver

        # Находим первый товар
        first_product_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[1]'
        first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, first_product_xpath)))

        # Прокручиваем страницу вниз на 5% для отображения элемента
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.05);")

        # Нажимаем кнопку "Добавить в корзину"
        add_to_cart_button_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[1]/div/div/div/div/article/div/div/div/div[3]/button'
        add_to_cart_button = first_product.find_element(By.XPATH, add_to_cart_button_xpath)
        add_to_cart_button.click()

        # Ожидаем добавления, иначе иногда падает
        time.sleep(2)

        # Переходим в корзину
        cart_button_xpath = '//*[@id="__layout"]/div/header/div[2]/div[2]/button[5]'
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, cart_button_xpath)))
        cart_button.click()

        time.sleep(1)

        # Находим элемент изменения количества
        change_count_element_xpath = '//*[@id="__layout"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div/div/div/article'
        change_count_element = self.wait.until(EC.presence_of_element_located((By.XPATH, change_count_element_xpath)))
        ActionChains(driver).move_to_element(change_count_element).perform()
        time.sleep(2)

        # Находим количество
        count_xpath = '//*[@id="__layout"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div/div/div/article/div[2]/div[1]/div/input'
        count = change_count_element.find_element(By.XPATH, count_xpath)
        old_count = count.get_attribute('_value')
        # Находим кнопку добавления
        add_count_button_xpath = '//*[@id="__layout"]/div/div[4]/aside[4]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div/div/div/article/div[2]/div[1]/div/button[2]'
        add_count_button = change_count_element.find_element(By.XPATH, add_count_button_xpath)

        add_count_button.click()
        time.sleep(2)

        new_count = (count.get_attribute('_value'))
        self.assertGreater(new_count, old_count, "Тест провален: Количество товара меньше минимального измененного.")

    def tearDown(self):
        """Закрываем браузер после выполнения теста"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

