import random
import time
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_supporter_positive(login):
    log = get_logger()
    driver = login
    settings = driver.find_element(By.CSS_SELECTOR, '[href="/settings"]')
    driver.execute_script("arguments[0].click();", settings)
    log.info("Clicked on Settings")

    newSupporter = driver.find_element(By.XPATH, '//button[@type="button" and @class="btn toggle-button '
                                                 'text-uppercase pl-0"]')
    driver.execute_script("arguments[0].click();", newSupporter)
    log.info("Clicked on New Supporter")

    radioAdmin = driver.find_element(By.ID, 'inlineRadio2')
    radioAdmin.click()
    log.info('Admin supporter selected for creation')

    firstName = driver.find_element(By.XPATH, '//input[@formcontrolname="firstName"]')
    firstName.send_keys('Uwe')
    log.info('Entered First name')

    lastName = driver.find_element(By.XPATH, '//input[@formcontrolname="lastName"]')
    lastName.send_keys('Hoffman')
    log.info('Entered Last name')

    emailId = driver.find_element(By.XPATH, '//input[@formcontrolname="email"]')
    emailId.send_keys('uwe.hoffmans1' + str(random.randint(0, 99)) + '@email.com')
    # '+str(random.randint(0, 99)) +'

    telephone = driver.find_element(By.XPATH, '//input[@formcontrolname="phone"]')
    telephone.send_keys('+4930396491624')

    password1 = driver.find_element(By.XPATH, '//input[@formcontrolname="password"]')
    password1.send_keys('Test@1234')
    log.info('1st password entered')

    password2 = driver.find_element(By.XPATH, '//input[@formcontrolname="confirmPassword"]')
    password2.send_keys('Test@1234')
    log.info('Password confirmed')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    log.info('Clicked on submit')
    time.sleep(1)

    errorDivElementSize = len(driver.find_elements(By.XPATH, '//div[@id="toast-container"]/div'))
    if errorDivElementSize > 0:
        log.info(driver.find_element(By.ID, "toast-container").text)
    else:
        log.info('Supporter - '+driver.find_element(By.XPATH, '//section[@class="row header"]').text + ' - created successfully')