import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_drafts_orders(driver):
    driver.implicitly_wait(10)

    draft = driver.find_element(By.XPATH, '//button[text()="Draft"]')
    driver.execute_script("arguments[0].click();", draft)
    print("Clicked on Draft")
    time.sleep(8)
    try:
        draftsorders_notfound = driver.find_element(By.XPATH,
                                                    "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        print("Customer not found ::", draftsorders_notfound.text)

    except NoSuchElementException:
        print("Orders in draft status searched successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_drafts_orders(driver)


if __name__ == '__main__':
    main()
