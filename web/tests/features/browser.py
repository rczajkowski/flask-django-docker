from selenium import webdriver


class Browser(object):

    base_url = 'http://0.0.0.0:8100'
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def visit(self, location=''):

        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def find_by_value(self, value):
        return self.driver.find_elements_by_name(value)

    def find_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)