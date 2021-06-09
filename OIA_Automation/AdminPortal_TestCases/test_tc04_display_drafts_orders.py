import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_display_draft_orders(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    draft = driver.find_element(By.XPATH, '//button[text()="Draft"]')
    driver.execute_script("arguments[0].click();", draft)
    log.info("Clicked on Draft")
    time.sleep(10)
    try:
        draftsorders_notfound = driver.find_element(By.XPATH,
                                                    "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        log.info("Customer not found ::" + draftsorders_notfound.text)

    except NoSuchElementException:
        log.info("Orders in draft status searched successfully")
