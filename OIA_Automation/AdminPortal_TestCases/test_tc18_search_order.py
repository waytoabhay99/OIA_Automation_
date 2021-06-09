import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_search_order(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(5)
    # Auftrage = driver.find_element(By.XPATH, "//input[@name='searchTerm' and @placeholder='Aufträge durchsuchen']")
    # driver.execute_script("arguments[0].click();", Auftrage)
    # log.info("Clicked on Aufträge/orders")
    #
    # driver.find_element(By.NAME, 'searchTerm').send_keys("209927_00060")
    search = driver.find_element(By.XPATH, "//input[@name='searchTerm' and @placeholder='Aufträge durchsuchen']")
    driver.execute_script("arguments[0].click();", search)
    log.info("Clicked on Search")
    search.send_keys("209927_00060")
    log.info('Entered search criteria')
    time.sleep(3)
    try:
        order_notfound = driver.find_element(By.XPATH,
                                             "(//article[text()='Keine Daten gefunden' and @class='no-data'])[3]")
        log.info("No order found: " + order_notfound.text)
    except NoSuchElementException:
        log.info("Order is searched successfully")
