import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome(r'C:\Users\LNevraev\Desktop\IBSPython\chromedriver.exe')
        self.drv.get('http://google.com/ncr')

    def test_search(self):
        # поиск selenide
        assert 'Google' in self.drv.title
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.ENTER)
        # проверка ссылки
        assert 'selenide.org' in self.drv.find_element_by_tag_name('cite').text
        # картинки
        self.drv.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
        # проверяем связь картинки с сайтом
        assert 'selenide.org' in self.drv.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[2]/div').text
        # все
        self.drv.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]').click()
        # проверка ссылки
        assert 'selenide.org' in self.drv.find_element_by_tag_name('cite').text

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
