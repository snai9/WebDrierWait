import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def muliti_click(target_element, next_element):
    def _predicate(driver):
        driver.find_element(*target_element).click()
        return driver.find_element(*next_element)
    return _predicate


def wait_until():
    driver = webdriver.Edge()
    # driver.get("https://vip.ceshiren.com/#/ui_study")
    driver.get("https://www.baidu.com")

    WebDriverWait(driver, 10).until(
        muliti_click(
            (By.ID, "primary_btn"),
            (By.XPATH, "//*[text()='该弹框点击两次后才会弹出']")
        ))


if __name__ == '__main__':
    wait_until()
    time.sleep(5)
