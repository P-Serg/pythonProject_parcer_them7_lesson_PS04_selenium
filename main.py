from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

print("Добро пожаловать в программу поиска информации в википедии")

def question_input():
    question = input("введите запрос и нажмите Enter: ")
    return question


browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Selenium")

browser.quit()