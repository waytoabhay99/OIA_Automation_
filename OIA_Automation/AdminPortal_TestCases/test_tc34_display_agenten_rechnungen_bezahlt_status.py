import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_customer_bills_bezahlt(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    bills = driver.find_element(By.XPATH, "//a[text()=' Rechnungen ']")
    driver.execute_script("arguments[0].click();", bills)
    log.info("Clicked on bills")
    time.sleep(10)

    bills = driver.find_element(By.XPATH, "//a[text()=' Rechnungen ']")
    driver.execute_script("arguments[0].click();", bills)
    log.info("Clicked on bills")
    time.sleep(10)

    # display bills in BEZAHLT status
    Bezahlt = driver.find_element(By.XPATH, '//button[text()="Bezahlt"]')
    driver.execute_script("arguments[0].click();", Bezahlt)
    log.info('Selected Bezahlt')
    time.sleep(10)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        log.info("No bills available in status Bezahlt: " + no_datafound.text)

    except NoSuchElementException:
        fourth = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        log.info("List of bills in Status - Bezahlt ")
        for x in range(len(fourth)):
            log.info("Bill Number: " + fourth[x].text)
