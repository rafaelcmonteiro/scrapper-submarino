import csv
import time
import unidecode
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.submarino.com.br/categoria/livros')
browser.implicitly_wait(10)


def next_page(category_name, num):
    browser.get(f'https://www.submarino.com.br/categoria/livros/{category_name}/'
                f'pagina-{num}?ordenacao=relevance')


def returning_to_book_page():
    browser.get('https://www.submarino.com.br/categoria/livros')


def writing(name, data_set):
    for data in data_set:
        with open(f'{name}.txt', 'a') as f:
            f.write(data + '\n')


def get_dirty_categories():
    dirty_categories = browser.find_elements_by_xpath(
        '//a[@class="filter-list-link filter-show-result filter-list-link-basic '
        'filter-hide-count"]')

    return dirty_categories


def btn_click(xpath):
    btn = browser.find_element_by_xpath(xpath)
    btn.click()


def get_categories():
    dirty_categories = get_dirty_categories()
    categories = []

    # Possivel dict
    categories_and_sub = {}

    for index, category in enumerate(dirty_categories):
        if 0 <= index < 40:
            categories.append(category.text)

    writing('categories', categories)


def categories_administrator():
    with open('categories.txt') as f:
        values = unidecode.unidecode(f.read())

    new_values = (values.replace(' ', '-').lower())
    new_list = new_values.split("\n")
    for value in new_list:
        browser.get(f'https://www.submarino.com.br/categoria/livros/{value}?ordenacao='
                    'relevance')
        get_all_books(value)


def get_all_books(category_name):
    list_values = []
    for index in range(2, 3):
        books = browser.find_elements_by_xpath('//h2[@class="TitleUI-bwhjk3-15 khKJTM TitleH2-sc-1wh9e1x-1 fINzxm"]')
        prices = browser.find_elements_by_xpath('//*[@class = "PriceWrapper-bwhjk3-13 eBwWGp ViewUI-sc-1ijittn-6 '
                                                'iXIDWU"]')

        # funcionou parcialmente = '//span[@id = "content-middle"]'
        for x in range(len(books)-1):
            string_books = f'{books[x].text};{prices[x].text}'
            list_values.append(string_books)

        writing('submarino_books', list_values)
        list_values = []
        print(category_name)
        next_page(category_name, index)
        # browser.close()
