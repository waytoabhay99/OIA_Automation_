import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_customer_bills_versendet(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    bills = driver.find_element(By.XPATH, "//a[text()=' Rechnungen ']")
    driver.execute_script("arguments[0].click();", bills)
    log.info("Clicked on bills")
    time.sleep(10)

    # #For Customer Bills
    driver.implicitly_wait(10)
    c_bills = driver.find_element(By.XPATH, '//section[text()=" Kunden-Rechnungen"]')
    driver.execute_script("arguments[0].click();", c_bills)
    log.info("Selected on customer bills")

    # display bills in Versendet status
    Versendet = driver.find_element(By.XPATH, '//button[text()="Versendet"]')
    driver.execute_script("arguments[0].click();", Versendet)
    log.info("Selected Versendet")
    time.sleep(10)

    try:
        no_datafound = driver.find_element(By.XPATH,
                                           "//article[text()='Keine Daten gefunden' and @class='text-center']")
        log.info("No bills available in status Versendet: " + no_datafound.text)

    except NoSuchElementException:
        second = driver.find_elements(By.XPATH, "//label[@class='sub-heading text-uppercase']")
        log.info("List of bills in Status - Versendet ")
        for x in range(len(second)):
            log.info("Bill Number: " + second[x].text)
