from socket import timeout
from selenium import webdriver
import Constants
import Locators
import MOCKED_DATA
import time


def RegisterTest(username, email, password,password1):
    driver=webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    dugmePrijaviSe=driver.find_element_by_css_selector(Locators.dugmePrijaviSe)
    dugmePrijaviSe.click()

    dugmeRegistrujSe=driver.find_element_by_css_selector(Locators.dugmeRegistrujSe)
    dugmeRegistrujSe.click()

    driver.maximize_window()

    PoljeKorisnickoIme = driver.find_element_by_css_selector(Locators.korisnicko_ime_registracije_css_selector)
    imejlPolje = driver.find_element_by_css_selector(Locators.imejl_registracije_css_selector)
    sifraPolje = driver.find_element_by_css_selector(Locators.sifra_registracije_css_selector)
    potvrdaSifrePolje = driver.find_element_by_css_selector(Locators.potvrda_sifre_registracije_css_selector)



    PoljeKorisnickoIme.send_keys(username)
    imejlPolje.send_keys(email)
    sifraPolje.send_keys(password)
    potvrdaSifrePolje.send_keys(password1)

    PoljeRegistrujSe=driver.find_element_by_css_selector(Locators.PoljeRegistrujSe)
    PoljeRegistrujSe.click()

    timeout(10)

for podatak in MOCKED_DATA.TEST_DATA:
    RegisterTest(podatak["username"],podatak["email"],podatak["password"],podatak["password1"])

RegisterTest("Aleksandar","API@einrot.com","Pavlovic1","Pavlovic1")

timeout(10)



    