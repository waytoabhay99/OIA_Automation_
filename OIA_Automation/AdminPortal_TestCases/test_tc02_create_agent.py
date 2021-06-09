import random
import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_agent(login):
    log = get_logger()
    driver=login
    agent = driver.find_element(By.CSS_SELECTOR, '[href="/agents"]')
    driver.execute_script("arguments[0].click();", agent)
    log.info("Clicked on Agent")
    driver.implicitly_wait(10)

    newAgent = driver.find_element(By.CSS_SELECTOR, '[href="/agents/create"]')
    driver.execute_script("arguments[0].click();", newAgent)
    log.info("Clicked on New Agent")

    salutation = driver.find_element(By.ID, 'gender')
    choose = Select(salutation)
    choose.select_by_value("1: female")
    log.info('Selected Female from Dropdown')

    firstname = driver.find_element(By.ID, 'firstName')
    firstname.send_keys('Martin')
    log.info('Entered First name')

    lastname = driver.find_element(By.ID, 'lastName')
    lastname.send_keys('King')
    log.info('Entered Last name')

    time.sleep(2)
    try:
        driver.find_element(By.ID, "inputAddress").send_keys("Hamburg 18")
        time.sleep(2)
        listElements = driver.find_elements(By.CSS_SELECTOR, "div.pac-container div span.pac-icon")
        listElements[3].click()
        log.info('Entered Address 1')
    except ElementNotInteractableException:
        log.info('Address not found : Please try again')

    time.sleep(2)
    opAddress = driver.find_element(By.ID, 'additionalAddress')
    opAddress.send_keys('Harburg Rathaus')
    log.info('Entered Adrs Optional')

    email = driver.find_element(By.ID, 'email')
    email.send_keys('testemail' + str(random.randint(3,99)) + '@email.de')
    log.info('Entered email')

    mobile = driver.find_element(By.ID, 'mobilePhone')
    mobile.send_keys('+919590199888')
    log.info('Entered Mobile Number')

    tele = driver.find_element(By.ID, 'phone')
    tele.send_keys('+919590199888')
    log.info('Entered Tele Number')

    jobStatus = driver.find_element(By.ID, 'jobStatus')
    jobStatus.send_keys('Employed')
    log.info('Entered Job Status')

    rds = driver.find_element(By.ID, 'radius')
    choose = Select(rds)
    choose.select_by_index(1)
    log.info('Selected Radius')

    radio = driver.find_element(By.ID, 'inlineRadio2')
    radio.click()
    log.info('Selected Nein')

    iban = driver.find_element(By.ID, 'iban')
    iban.send_keys('DE89370400440532013000')
    log.info('Entered IBAN')

    save = driver.find_element(By.XPATH, '//button[@type="submit"]')
    save.click()

    time.sleep(1)

    try:
        errorMessageOpacitiyValue = (
            driver.find_element(By.XPATH, '//div[@id="toast-container"]/div').value_of_css_property('opacity'))
        log.info(errorMessageOpacitiyValue)
        log.info('Duplicate user email found: '+driver.find_element(By.XPATH, '//div[@aria-label="E-Mail existiert bereits"]').text)
    except NoSuchElementException:
        log.info(driver.find_element(By.XPATH, '//article[@class="col-lg-9 heading"]').text + ' creation Successful')
