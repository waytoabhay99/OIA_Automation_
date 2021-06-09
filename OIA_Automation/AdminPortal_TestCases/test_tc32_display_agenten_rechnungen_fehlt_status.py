import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_customer_bills_fehlt(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)
    bills = driver.find_element(By.XPATH, "//a[text()=' Rechnungen ']")
    driver.execute_script("arguments[0].click();", bills)
    log.info("Clicked on bills")
    time.sleep(20)

    # display bills in FEHLT status
    fehlt = driver.find_element(By.XPATH, '//button[text()="Fehlt"]')
    driver.execute_script("arguments[0].click();", fehlt)
    time.sleep(5)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        log.info("No bills available in status Fehlt::" + no_datafound.text)

    except NoSuchElementException:
        second = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        log.info("list of bills in Status - Fehlt ")
        for x in range(len(second)):
            log.info("Bill Number:: " + second[x].text)
