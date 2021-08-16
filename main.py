"""Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о
письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный) """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import cridentials


class WebScrapper_mail():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/fedorpetrenko/Downloads/chromedriver')
        self.url = 'https://mail.ru'
        self.login = None

    def login_mail(self):
        driver = self.driver
        driver.get(self.url)

        elem = driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[1]/div[2]/input')
        elem.send_keys(cridentials.USERMAIL)

        button = driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[1]')
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(button).click(button).perform()

        password = driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[2]/input')
        driver.implicitly_wait(10)
        password.send_keys(cridentials.PASSWORD)
        password.send_keys(Keys.ENTER)

        all_mail = driver.find_elements_by_xpath('//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div['
                                                 '2]/div/div/div/div/div[1]/div/div/div[1]/div/div/div/a')

        for mail in all_mail:
            mail.click()

            driver.back()

        all_mail = self.login
        return all_mail



a = WebScrapper_mail
a.login_mail()
