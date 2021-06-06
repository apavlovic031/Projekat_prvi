from socket import timeout
from selenium import webdriver
import Constants
import Locators
import MOCKED_DATA
import time



def TestLogin(email, password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    dugmePrijaviSe=driver.find_element_by_css_selector(Locators.dugmePrijaviSe)
    dugmePrijaviSe.click()

    driver.maximize_window()

    imejlPolje = driver.find_element_by_css_selector(Locators.imejl_login_css_selector)
    sifraPolje = driver.find_element_by_css_selector(Locators.sifra_login_css_selector)

    PoljeUlogujSe = driver.find_element_by_css_selector(Locators.login_button_css_selector)

    imejlPolje.send_keys(email)
    sifraPolje.send_keys(password)

    PoljeUlogujSe.click()

timeout(10)


for podatak in MOCKED_DATA.TEST_DATA:
    TestLogin(podatak["email"],podatak["password"])

timeout(10)

TestLogin("API@einrot.com", "Pavlovic1")



