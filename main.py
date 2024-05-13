from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

print("Добро пожаловать в программу поиска информации в википедии")

class Wiki_question:
    def __init__(self, question):
        self.question = question
        question = input("Введите запрос и нажмите Enter: ")
        self.question = question



browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Selenium")

browser.quit()