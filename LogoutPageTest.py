from socket import timeout
from selenium import webdriver
import Constants
import Locators
import MOCKED_DATA
import time

def LogoutPageTest(email,password):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    dugmePrijaviSe=driver.find_element_by_css_selector(Locators.dugmePrijaviSe)
    dugmePrijaviSe.click()
    imejlPolje = driver.find_element_by_css_selector(Locators.imejl_login_css_selector)
    sifraPolje = driver.find_element_by_css_selector(Locators.sifra_login_css_selector)

    PoljeUlogujSe = driver.find_element_by_css_selector(Locators.login_button_css_selector)

    imejlPolje.send_keys(email)
    sifraPolje.send_keys(password)

    PoljeUlogujSe.click()
    driver.maximize_window()



    PoljeOdjaviSe=driver.find_element_by_css_selector(Locators.PoljeOdjaviSe)
    PoljeOdjaviSe.click()

    driver.maximize_window()



    

    if(driver.current_url==f"{Constants.BASE_URL}{Constants.LOGIN_PAGE}"):
        print("Uspesno odjavljen")
    else:
        print("Neuspesna odjava")
    time.sleep(30)

LogoutPageTest ("API@einrot.com", "Pavlovic1")