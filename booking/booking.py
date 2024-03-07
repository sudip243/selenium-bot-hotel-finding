import os
from selenium.webdriver.common.by import By
import bot.booking.constants as const
from selenium import webdriver  # importing webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r""):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)  # for wait 15 sec
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        self.find_element(By.XPATH, "//button[@aria-label='Dismiss sign in information.']").click()
        self.find_element(By.XPATH, "//button[@data-testid='header-currency-picker-trigger']").click()
        self.find_element(By.XPATH, f"//div[text()='{currency}']").click()

    def select_place_to_go(self, place_to_go):
        self.find_element(By.XPATH, "//input[@name='ss']").send_keys(place_to_go)
        self.find_element(By.XPATH, "//li[@id='autocomplete-result-0']").click()

    def select_date(self, checkin_date, checkout_date):
        self.find_element(By.XPATH, f"//span[@data-date='{checkin_date}']").click()
        self.find_element(By.XPATH, f"//span[@data-date='{checkout_date}']").click()

    def select_adault(self,count=1):
        self.find_element(By.XPATH,"//button[@data-testid='occupancy-config']").click()
