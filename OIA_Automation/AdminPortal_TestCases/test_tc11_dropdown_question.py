import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger
from ImmoAgent.Resuables.Admin_Transversal import question_create


def test_create_dropdown_question(login):
    log = get_logger()
    driver = login
    question_create(driver)
    quesType = driver.find_element(By.ID, 'questionType')
    choose = Select(quesType)
    choose.select_by_value('dropdown')
    log.info('Selected Question type')

    time.sleep(2)
    value1 = driver.find_element(By.XPATH, "(//input[@formcontrolname='answer'])[1]")
    value1.send_keys("value 1 of the dropdown")
    log.info('value 1 entered')

    value2 = driver.find_element(By.XPATH, "(//input[@formcontrolname='answer'])[2]")
    value2.send_keys("value 2 of the dropdown")
    log.info('value 2 entered')

    submit = driver.find_element(By.XPATH, '//button[text()="Speichern"]')
    submit.click()
    log.info('Submit button clicked')
    time.sleep(2)

    ques_header = driver.find_element(By.CSS_SELECTOR, 'section[class="row header"]')
    log.info('Dropdown question - ' + ques_header.text + ' created')