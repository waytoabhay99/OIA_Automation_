import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_display_bearbeitung_orders(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    InBearbeitung = driver.find_element(By.XPATH, '//button[text()="In Bearbeitung"]')
    driver.execute_script("arguments[0].click();", InBearbeitung)
    log.info("Clicked on In Bearbeitung")
    time.sleep(8)
    try:
        InBearbeitungorders_notfound = driver.find_element(By.XPATH,
                                                           "(//article[text()='Keine Daten gefunden' and "
                                                           "@class='no-data'])[3]")
        log.info("Customer not found ::" + InBearbeitungorders_notfound.text)

    except NoSuchElementException:
        log.info("Orders in InBearbeitung status searched successfully")
