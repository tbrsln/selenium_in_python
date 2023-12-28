#Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSeleniumIde():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_seleniumIdeTest(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 832)
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"username\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"password\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys("secret_sauce")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").text == "Remove"
    self.vars["SelectedProductinList"] = self.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > .inventory_item_name").text
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").text == "Remove"
    assert self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "2"
    self.driver.find_element(By.LINK_TEXT, "2").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1"
    self.vars["SelectedProductinBasket"] = self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "self.vars[\"SelectedProductinList\"]"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]").send_keys("Tuba")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    assert self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]").text == "Error: Last Name is required"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]").send_keys("Arslan")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]").send_keys("16300")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]").click()
    self.vars["SelectedProduct"] = self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
    assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text == "self.vars[\"SelectedProductinList\"]"
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".complete-header").text == "Thank you for your order!"
    self.driver.close()
  