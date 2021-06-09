import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger
from ImmoAgent.Resuables.Admin_Transversal import question_create


def test_create_conditional_question(login):
    log = get_logger()
    driver = login
    question_create(driver)
    quesType = driver.find_element(By.ID, 'questionType')
    choose = Select(quesType)
    choose.select_by_value('bedingte')
    log.info('Selected Question type')
    time.sleep(2)

    condition1 = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="confirmingStatement"]')
    condition1.send_keys('This is first possible answer')
    log.info('Condition 1 entered')

    condition2 = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="negativeStatement"]')
    condition2.send_keys('This is second possible answer')
    log.info('Condition 2 entered')

    freetext = driver.find_element(By.ID, 'freeText')
    freetext.click()
    log.info('Chekced free text checkbox')

    submit = driver.find_element(By.XPATH, '//button[text()="Speichern"]')
    submit.click()
    log.info('Submit button clicked')
    time.sleep(2)

    ques_header = driver.find_element(By.CSS_SELECTOR, 'section[class="row header"]')
    log.info('Conditional question - ' + ques_header.text + ' created')
