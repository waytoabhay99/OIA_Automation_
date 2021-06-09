import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_Ergebnisaufbereitung_orders(driver):
    driver.implicitly_wait(10)
    ergebnisaufbereitung = driver.find_element(By.XPATH, '//button[text()="Ergebnisaufbereitung"]')
    driver.execute_script("arguments[0].click();", ergebnisaufbereitung)
    print("Clicked on Ergebnisaufbereitung")
    time.sleep(7)
    try:
        Ergebnisaufbereitungorders_notfound = driver.find_element(By.XPATH,
                                                                  "(//article[text()='Keine Daten gefunden' and "
                                                                  "@class='no-data'])[3]")
        print("Customer not found ::", Ergebnisaufbereitungorders_notfound.text)

    except NoSuchElementException:
        print("Orders in Ergebnisaufbereitung status searched successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_Ergebnisaufbereitung_orders(driver)


if __name__ == '__main__':
    main()
