import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_display_abgeschlossen_orders(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)
    Abgeschlossen = driver.find_element(By.XPATH, '//button[text()="Abgeschlossen"]')
    driver.execute_script("arguments[0].click();", Abgeschlossen)
    log.info("Clicked on Abgeschlossen")
    time.sleep(8)
    try:
        Abgeschlossenorders_notfound = driver.find_element(By.XPATH,
                                                           "(//article[text()='Keine Daten gefunden' and "
                                                           "@class='no-data'])[3]")
        log.info("Customer not found ::" + Abgeschlossenorders_notfound.text)

    except NoSuchElementException:
        log.info("Orders in Abgeschlossen status searched successfully")
