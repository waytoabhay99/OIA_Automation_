import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_ergebnisaufbereitung_orders(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    ergebnisaufbereitung = driver.find_element(By.XPATH, '//button[text()="Ergebnisaufbereitung"]')
    driver.execute_script("arguments[0].click();", ergebnisaufbereitung)
    log.info("Clicked on Ergebnisaufbereitung")
    time.sleep(12)
    try:
        Ergebnisaufbereitungorders_notfound = driver.find_element(By.XPATH,
                                                                  "(//article[text()='Keine Daten gefunden' and "
                                                                  "@class='no-data'])[3]")
        log.info("Customer not found ::" + Ergebnisaufbereitungorders_notfound.text)

    except NoSuchElementException:
        log.info("Orders in Ergebnisaufbereitung status searched successfully")
