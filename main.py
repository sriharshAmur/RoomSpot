# from bs4 import BeautifulSoup
# import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


if __name__ == '__main__':
    path = r'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(executable_path = path)

    # login
    url = "https://www.roomspot.nl/mijn-roomspot/inloggen"
    driver.get(url)
    time.sleep(2)
    username = driver.find_element_by_id("username")
    login = driver.find_element_by_name("loginForm").find_elements_by_tag_name("input")[-1]
    password = driver.find_element_by_id("password")
    username.send_keys("") #ENTER USERNAME HERE 
    password.send_keys("") # ENTER PASSWORD HERE
    driver.execute_script("arguments[0].click();", login)
    time.sleep(2)

    # go to offers, filter results and collect a links
    offers_url = "https://www.roomspot.nl/aanbod/te-huur"
    filters = '//*[@id="object-frontend-resultlist"]/div/div/div[1]/div/div[6]/div'
    lottery = "//div[contains(@class, 'option ng-scope has-description' )]"
    register = "//div[contains(@class, 'option ng-scope has-description' )]"
    ok_buton = '/html/body/div[6]/div[1]/div/div/div[3]/button[2]'
    houses = '/html/body/div[1]/main/div/div/div/div/div/div/div[3]/div/div[2]/section'
    href = './div/div/ng-include/div/a'
    respond = "reageer-button"
    house_links = []

    driver.get(offers_url)
    time.sleep(2)
    driver.find_element_by_xpath(filters).click()
    driver.find_elements_by_xpath(lottery)[1].click()
    driver.find_elements_by_xpath(lottery)[2].click()
    time.sleep(2)
    for house in driver.find_elements_by_xpath(houses):
        house_links.append(house.find_element_by_xpath(href).get_attribute("href"))
    # print(house_links)
    # open page and respond
    for link in house_links:
        driver.get(link)
        time.sleep(2)
        element = driver.find_element_by_class_name(respond)
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    print("done")
    driver.quit()


