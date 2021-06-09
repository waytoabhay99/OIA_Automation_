import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_customer_bills_freigegeben(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    bills = driver.find_element(By.XPATH, "//a[text()=' Rechnungen ']")
    driver.execute_script("arguments[0].click();", bills)
    log.info("Clicked on bills")
    time.sleep(10)

    # # display bills in FREIGEGEBEN status
    Freigegeben = driver.find_element(By.XPATH, '//button[text()="Freigegeben"]')
    driver.execute_script("arguments[0].click();", Freigegeben)
    log.info('Selected Freigegeben')
    time.sleep(5)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        log.info("No bills available in status Freigegeben: " + no_datafound.text)

    except NoSuchElementException:
        third = driver.find_elements(By.XPATH, "//label[text()='Rechnungsnumber']//following-sibling::article")
        log.info("list of bills in Status - Freigegeben ")
        for x in range(len(third)):
            log.info("Bill Number:: " + third[x].text)
    time.sleep(5)
