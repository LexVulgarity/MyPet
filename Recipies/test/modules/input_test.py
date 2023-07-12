from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Auth_test:

    by_dict = {'ID' : By.ID, 'NAME' : By.NAME, 'LINK_TEXT' : By.LINK_TEXT,
               'XPATH' : By.XPATH, 'PARTIAL_LINK_TEXT' : By.PARTIAL_LINK_TEXT,
               'CLASS_NAME' : By.CLASS_NAME}
    names = []

    def __init__(self, path: str):
        self.driver_path = path


    def open_brows(self, link, secs=0):
        s = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.get(link)
        time.sleep(secs)

    def search_by(self,name,n: str, a, secs=0):
        if n in self.by_dict:
            name = self.driver.find_element(self.by_dict[n], a)
            self.names.append(name)
            time.sleep(secs)


    def input_keys(self, keys: str, secs=0):
        self.names[-1].clear()
        self.names[-1].send_keys(keys)
        time.sleep(secs)

    def enter_keys(self,secs=0):
        self.names[-1].send_keys(Keys.ENTER)
        time.sleep(secs)

    def click(self):
        self.names[-1].click()

    def move_to_element(self):
        find=self.driver.find_element(By.CLASS_NAME,'opisanie')
        actions = ActionChains(self.driver)
        actions.move_to_element(find)
        actions.perform()