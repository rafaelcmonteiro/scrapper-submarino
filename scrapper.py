import csv
import time

from selenium import webdriver
from unidecode import unidecode

browser = webdriver.Firefox()
browser.get('https://www.submarino.com.br/categoria/livros')
browser.implicitly_wait(10)


def next_page(num):
    browser.get('https://www.submarino.com.br/categoria/livros/administracao-e-negocios/administracao/'
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
        if 17 < index < 57:
            categories.append(category.text)

    writing('categories', categories)

    for index, category in enumerate(categories):
        # limitando o código.
        if index == 2:
            break

        time.sleep(10.0)
        category = unidecode(category)
        category_value = category.lower().replace(' ', '-')

        print(category_value)

        btn_click(f'//a[@href="/categoria/livros/{category_value}?ordenacao=relevance"]')

        time.sleep(10.0)
        try:
            btn_click('/html/body/div[1]/div/div/div/div[3]/div/div[2]/div['
                      '2]/div/aside/div[1]/div[2]/div/div/div/span/div/div/section['
                      '1]/div/button')
        except:
            print('Não existe.')

        dirty_categories_again = get_dirty_categories()

        sub_categories = []
        for category_again in dirty_categories_again:
            if category_again.text == 'vade mecum rideel':
                break
            else:
                sub_categories.append(category_again.text)

        writing(category, sub_categories)

        # Returning to book page function
        returning_to_book_page()


def get_all_books():
    browser.get('https://www.submarino.com.br/categoria/livros/administracao-e-negocios/administracao?ordenacao'
                '=relevance')
    list_values = []
    for index in range(2, 22):
        print(index)
        books = browser.find_elements_by_xpath('//h2[@class="TitleUI-bwhjk3-15 khKJTM TitleH2-sc-1wh9e1x-1 fINzxm"]')
        prices = browser.find_elements_by_xpath('//*[@class = "PriceWrapper-bwhjk3-13 eBwWGp ViewUI-sc-1ijittn-6 '
                                                'iXIDWU"]')

        # funcionou parcialmente = '//span[@id = "content-middle"]'
        for x in range(len(books)-1):
            string_books = f'{books[x].text};{prices[x].text}'
            list_values.append(string_books)
        print(list_values)

        writing('submarino_books', list_values)

        next_page(index)
        # browser.close()
