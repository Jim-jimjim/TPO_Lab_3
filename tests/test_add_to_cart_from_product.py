import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddToCartFromProduct(unittest.TestCase):

    def setUp(self):
        """Инициализация драйвера перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://goldapple.ru/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_add_product_to_cart_from_product(self):
        """Тест: Добавление товара в корзину со страницы товара"""

        driver = self.driver

        # Находим первый товар
        first_product_xpath = '//*[@id="__layout"]/div/main/section[3]/div/section/div/div[2]/div[1]'
        first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, first_product_xpath)))

        # Прокручиваем страницу вниз на 5% для отображения элемента
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight * 0.05);")

        first_product.click()
        time.sleep(3)

        # Нажимаем кнопку "Добавить в корзину"
        add_to_cart_button_xpath = '//*[@id="__layout"]/div/main/article/div[1]/div[1]/form/div[4]/div/button'
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, add_to_cart_button_xpath)))
        add_to_cart_button.click()

        # Ожидаем добавления, иначе иногда падает
        time.sleep(2)

        # Переходим в корзину
        cart_button_xpath = '//*[@id="__layout"]/div/header/div[2]/div[2]/button[5]'
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, cart_button_xpath)))
        cart_button.click()

        time.sleep(1)

        # Проверяем, что товар появился в корзине
        cart_items_xpath = '//*[@id="__layout"]/div/div[4]/aside[5]/div[2]/div/div[1]/div/div/div/div[2]/article/div/section[2]/div/div/section/div/div/div/div/article'
        cart_items = self.wait.until(EC.presence_of_element_located((By.XPATH, cart_items_xpath)))

        self.assertTrue(cart_items, "Тест провален: Товар отсутствует в корзине.")

    def tearDown(self):
        """Закрываем браузер после выполнения теста"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


