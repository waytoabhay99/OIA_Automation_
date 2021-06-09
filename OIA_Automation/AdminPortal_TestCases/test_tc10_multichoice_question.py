import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger
from ImmoAgent.Resuables.Admin_Transversal import question_create


def test_create_multichoice_question(login):
    log = get_logger()
    driver = login
    question_create(driver)
    quesType = driver.find_element(By.ID, 'questionType')
    choose = Select(quesType)
    choose.select_by_value('mehrfachauswahl')
    log.info('Selected Question type')

    time.sleep(1)
    in1 = driver.find_element(By.XPATH, '(//input[@formcontrolname="answer"])[1]')
    in1.send_keys('multi-selection1')
    log.info('Input 1 entered')

    in2 = driver.find_element(By.XPATH, '(//input[@formcontrolname="answer"])[2]')
    in2.send_keys('multi-selection2')
    log.info('Input 2 entered')

    submit = driver.find_element(By.XPATH, '//button[text()="Speichern"]')
    submit.click()
    log.info('Submit button clicked')

    ques_header = driver.find_element(By.CSS_SELECTOR, 'section[class="row header"]')
    log.info('Multiple choice question - ' + ques_header.text + ' created')