import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_customer_bills_offen(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    bills = driver.find_element(By.XPATH, "//a[text()=' Rechnungen ']")
    driver.execute_script("arguments[0].click();", bills)
    log.info("Clicked on bills")
    time.sleep(20)

    # #Click on filter icons of bills:

    offen = driver.find_element(By.XPATH, '//button[text()="Offen"]')
    driver.execute_script("arguments[0].click();", offen)
    log.info('Clicked on offen')
    time.sleep(5)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        log.info("No bills available::", no_datafound.text)

    except NoSuchElementException:
        first = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        log.info("List of bills in Status - OFFEN")
        for x in range(len(first)):
            log.info("Bill Number: " + first[x].text)
