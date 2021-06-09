import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_bearbeitung_orders(driver):
    driver.implicitly_wait(10)
    InBearbeitung = driver.find_element(By.XPATH, '//button[text()="In Bearbeitung"]')
    driver.execute_script("arguments[0].click();", InBearbeitung)
    print("Clicked on In Bearbeitung")
    time.sleep(7)
    try:
        InBearbeitungorders_notfound = driver.find_element(By.XPATH,
                                                           "(//article[text()='Keine Daten gefunden' and "
                                                           "@class='no-data'])[3]")
        print("Customer not found ::", InBearbeitungorders_notfound.text)

    except NoSuchElementException:
        print("Orders in InBearbeitung status searched successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_bearbeitung_orders(driver)


if __name__ == '__main__':
    main()
