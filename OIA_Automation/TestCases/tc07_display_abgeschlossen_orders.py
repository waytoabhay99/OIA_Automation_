import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def display_abgeschlossen_orders(driver):
    driver.implicitly_wait(10)
    Abgeschlossen = driver.find_element(By.XPATH, '//button[text()="Abgeschlossen"]')
    driver.execute_script("arguments[0].click();", Abgeschlossen)
    print("Clicked on Abgeschlossen")
    time.sleep(7)
    try:
        Abgeschlossenorders_notfound = driver.find_element(By.XPATH,
                                                           "(//article[text()='Keine Daten gefunden' and "
                                                           "@class='no-data'])[3]")
        print("Customer not found ::", Abgeschlossenorders_notfound.text)

    except NoSuchElementException:
        print("Orders in Abgeschlossen status searched successfully")


def main():
    driver = launchBrowser()
    login(driver)
    display_abgeschlossen_orders(driver)


if __name__ == '__main__':
    main()
