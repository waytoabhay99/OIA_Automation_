import random
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.test_logging import get_logger


def test_new_rubrik(login):
    log = get_logger()
    driver = login
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    log.info("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    button_rub = driver.find_element(By.XPATH, '(//button[@class="btn primary-button mr-2 transparent-btn"])[1]')
    driver.execute_script("arguments[0].click();", button_rub)
    log.info("Clicked on New Rubrik Button")

    rub_name = driver.find_element(By.ID, 'new-rubrik')
    rub_name.send_keys('Automation Test Rubrik ' + str(random.randint(0, 99)))
    log.info('Rubrik name enreted')

    driver.find_element(By.XPATH, '//button[@class="btn primary-button"]').click()
    log.info('Save the new Rubrik')