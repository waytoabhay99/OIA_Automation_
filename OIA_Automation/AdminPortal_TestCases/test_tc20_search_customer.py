import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_search_customer(login):
    log = get_logger()
    driver = login
    cust = driver.find_element(By.XPATH, "//a[text()=' Kunden ']")
    driver.execute_script("arguments[0].click();", cust)
    log.info("Clicked on customer")
    time.sleep(5)
    driver.find_element(By.XPATH, '(//input[@name="searchTerm"])[2]').send_keys("Mike Davidson")

    time.sleep(3)
    order_notfound = len(driver.find_elements(By.XPATH, "(//article[text()='Keine Daten gefunden'])[3]"))
    if order_notfound == 1:
        log.info("No Data Displayed")
    else:
        log.info("Search results are displayed")