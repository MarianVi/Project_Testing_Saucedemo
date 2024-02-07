from selenium import webdriver


class Browser:
    browser = webdriver.Chrome()
    browser.maximize_window()

    def close(self):
        self.browser.quit()