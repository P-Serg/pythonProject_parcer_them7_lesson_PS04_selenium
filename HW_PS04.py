from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

print("Добро пожаловать в программу поиска информации в Википедии")


class WikiQuestion:
    def __init__(self):
        self.question = input("Введите запрос и нажмите Enter: ")
        self.browser = webdriver.Firefox()
        self.search_query()

    def search_query(self):
        search_url = "https://ru.wikipedia.org/wiki/Служебная:Search?search=" + self.question
        self.browser.get(search_url)
        time.sleep(3)
        self.handle_article()

    def handle_article(self):
        while True:
            print("\n1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")

            choice = input("Выберите действие (1, 2, 3): ").strip()

            if choice == '1':
                self.browse_paragraphs()
            elif choice == '2':
                self.browse_links()
            elif choice == '3':
                self.browser.quit()
                print("Вы вышли из программы.")
                break
            else:
                print("Некорректный выбор. Попробуйте еще раз.")

    def browse_paragraphs(self):
        paragraphs = self.browser.find_elements(By.TAG_NAME, 'p')
        for i, paragraph in enumerate(paragraphs):
            print(f"\nПараграф {i + 1}:\n{paragraph.text}\n")
            action = input("Введите 'n' для следующего параграфа, 'm' для меню: ").strip().lower()
            if action == 'm':
                break

    def browse_links(self):
        links = self.browser.find_elements(By.CSS_SELECTOR, '#bodyContent a')
        valid_links = []
        for link in links:
            href = link.get_attribute('href')
            if href and href.startswith('https://ru.wikipedia.org/wiki/'):
                valid_links.append((link.text, href))

        if not valid_links:
            print("Нет связанных страниц.")
            return

        for i, (title, href) in enumerate(valid_links):
            print(f"{i + 1}. {title}")

        link_choice = input("Введите номер связанной страницы для перехода (или 'm' для меню): ").strip()
        if link_choice.lower() == 'm':
            return

        try:
            link_index = int(link_choice) - 1
            if 0 <= link_index < len(valid_links):
                self.browser.get(valid_links[link_index][1])
                time.sleep(3)
            else:
                print("Некорректный номер. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    WikiQuestion()
