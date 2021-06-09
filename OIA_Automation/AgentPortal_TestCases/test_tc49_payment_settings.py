import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.AgentPortal_TestCases.test_logging import get_logger

def test_payment_settings(login):
    log = get_logger()
    driver = login
    # #click on profile

    profile = driver.find_element(By.XPATH, '//a[text()=" Profil "]')
    driver.execute_script("arguments[0].click();", profile)
    log.info("Clicked on Profile")
    time.sleep(5)

    # #Click on edit payment settings
    profile = driver.find_element(By.XPATH, '//label[text()="Zahlungs daten ändern"]')
    driver.execute_script("arguments[0].click();", profile)
    log.info("Clicked on edit payment settings")
    time.sleep(7)

    status1 = driver.find_element(By.ID, 'isCompany').is_selected()
    log.info(status1)

    if status1 == False:
        toggle1 = driver.find_element(By.XPATH, '//label[@for="isCompany"]')
        driver.execute_script("arguments[0].click();", toggle1)
        log.info("Clicked on toggle1")

    else:
        log.info("status is True")

    try:
        driver.find_element(By.ID, 'companyName').clear()
        time.sleep(5)
        driver.find_element(By.ID, 'companyName').send_keys("check1")

    except NoSuchElementException:
        log.info("Company name not found")

    time.sleep(5)
    driver.find_element(By.ID, 'iban').clear()
    time.sleep(5)
    driver.find_element(By.ID, 'iban').send_keys("Check2")
    log.info("Iban added")

    driver.find_element(By.ID, 'taxNumber').clear()
    time.sleep(5)

    driver.find_element(By.ID, 'taxNumber').send_keys("111111")
    log.info("Taxnumber added")

    driver.find_element(By.XPATH, '//button[text()="Speichern "]').click()
    log.info("Clicked on submit -- Details added submitted successfully")
    time.sleep(5)
