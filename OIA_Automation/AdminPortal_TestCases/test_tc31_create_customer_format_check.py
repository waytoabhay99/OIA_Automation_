import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_customer_format_check(login):
    log = get_logger()
    driver = login
    driver.implicitly_wait(10)

    customer = driver.find_element(By.XPATH, "//a[text()=' Kunden ']")
    driver.execute_script("arguments[0].click();", customer)
    log.info("Clicked on Customer- Worked")

    click_createnewcustomer = driver.find_element(By.XPATH, "//button[text()=' Neuer Kunde ']")
    driver.execute_script("arguments[0].click();", click_createnewcustomer)
    log.info("Clicked on Customer creation")

    driver.find_element(By.ID, 'companyName').send_keys("Sopra")
    gen = driver.find_element(By.ID, 'gender')
    drp = Select(gen)
    drp.select_by_value('female')
    log.info('Selecetd female from dropdown')
    # #drp.select_by_value('male') working properly

    driver.find_element(By.ID, 'firstName').send_keys("Rv")
    log.info('Entered first name')
    driver.find_element(By.ID, 'lastName').send_keys("RS")
    log.info('Entered last name')

    try:
        driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']")
        driver.find_element(By.XPATH, "//input[@placeholder = 'Sachsendamm']").send_keys("Bernauer Straße 33")
        time.sleep(2)
        listElements = driver.find_elements(By.CSS_SELECTOR, ".pac-container div span.pac-icon")
        listElements[2].click()

    except ElementNotInteractableException:
        log.info("Address not found :: Please try again")

    driver.implicitly_wait(5)
    driver.find_element_by_id('inputAddress3').send_keys("France")
    log.info('Entered inputAddress3')
    driver.find_element_by_id('email').send_keys("revasharma0692+1@gmail.com")
    log.info('Entered email')
    driver.find_element_by_id('phone').send_keys("00000+491785551773")
    log.info('Entered phone')
    driver.find_element_by_id('invoiceEmail').send_keys("revasharma0692+1@gmail.com")
    log.info('Entered invoiceEmail')
    driver.find_element_by_id('vatin').send_keys("12345")
    log.info('Entered vatin')
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//button[text()='Speichern']").click()
    log.info('Selecetd female from dropdown')

    try:
        email_error = driver.find_element(By.XPATH, "//div[text()='Bitte gib ein gültiges E-Mail-Format ein.']")
        log.info("email is invalid:", email_error.text)

    except NoSuchElementException:
        log.info("Format of the Email address provided is correct")

    try:
        phone_error = driver.find_element(By.XPATH, "(//div[text()='Bitte gebe eine gültige Telefonnummer ein.'])[1]")
        log.info("Phone number is invalid: " + phone_error.text)

    except NoSuchElementException:
        log.info("Format of the phone number provided is correct")
