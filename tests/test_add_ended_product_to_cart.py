import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddEndedToCartFromProduct(unittest.TestCase):

    def setUp(self):
        """Инициализация драйвера перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://goldapple.ru/19000165305-eros-man-eau-de-parfume")
        self.wait = WebDriverWait(self.driver, 10)

        # Определяем xPath локаторы (или лучше в коде ниже?)
        self.add_to_cart_button_xpath = '//*[@id="__layout"]/div/main/article/div[1]/div[1]/form/div[4]/div/button'

    def test_add_ended_product_to_cart_from_product(self):
        """Тест: Добавление отсутствующего товара в корзину со страницы товара"""

        # Ищем кнопку "Добавить в корзину"
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((
            By.XPATH, self.add_to_cart_button_xpath
        )))

        self.assertEqual(add_to_cart_button.text, 'УЗНАТЬ О ПОСТУПЛЕНИИ', "Тест провален: Товар отсутствует в корзине.")

    def tearDown(self):
        """Закрываем браузер после выполнения теста"""
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
