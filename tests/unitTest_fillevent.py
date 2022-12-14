import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings


class ll_ATS(unittest.TestCase):
    # set up the test class - assign the driver to Chrome - if using a different
    # browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Chrome()
        warnings.simplefilter('ignore', ResourceWarning)  # ignore resource warning if occurs

    # Test if Customer list is displayed when Customers is clicked in the Navigation bar
    # Customer list is shown if the 'summary' button exists on the page
    def test_ll(self):

        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)  # pause to allow screen to load

        # click the login button - user must be logged in to view the Customer list
        elem = driver.find_element(By.XPATH,'//*[@id="myNavbar"]/ul[2]/li[2]/a').click()

        # find the username and password input boxes and login
        user = "testuser"  # must be a valid username for the application
        pwd = "test123"  # must be the password for a valid user

        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)  # pause to allow screen to load

        # find 'Customers' and click it – note this is all one Python statement
        elem = driver.find_element(By.XPATH, '//*[@id="myNavbar"]/ul[1]/li[3]/a').click()
        time.sleep(3)  # pause to allow screen to change

        elem = driver.find_element(By.XPATH, '//*[@id="events"]/div[1]/p/a').click()
        time.sleep(3)  # pause to allow screen to change

        elem = driver.find_element(By.XPATH, '//*[@id="app-layout"]/div[2]/div/div[2]/a').click()
        time.sleep(3)  # pause to allow screen to change

        elem = driver.find_element(By.XPATH, '//*[@id="id_Club"]/option[2]').click()
        time.sleep(3)

        event_name = "test"
        name = driver.find_element(By.XPATH, '//*[@id="id_event_name"]')
        name.send_keys(event_name)
        time.sleep(2)
        event_category = "test"
        name = driver.find_element(By.XPATH, '//*[@id="id_event_category"]')
        name.send_keys(event_category)
        time.sleep(2)
        description = "test"
        name = driver.find_element(By.XPATH, '//*[@id="id_description"]')
        name.send_keys(description)
        time.sleep(2)
        location = "test"
        name = driver.find_element(By.XPATH, '//*[@id="id_location"]')
        name.send_keys(location)
        time.sleep(2)
        elem = driver.find_element(By.XPATH, '//*[@id="event_form"]/div/div/input[1]').click()
        time.sleep(3)
        try:
            elem = driver.find_element(By.XPATH, '//*[@id="logout-form"]/button').click()
            print("Test passed - New event has been added")
            assert True
        # else report that the test failed
        except NoSuchElementException:
            self.fail("Failed - user may not exist")
def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

