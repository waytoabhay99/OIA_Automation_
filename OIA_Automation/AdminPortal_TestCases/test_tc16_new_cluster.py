import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ImmoAgent.Resuables.test_logging import get_logger


def test_new_cluster(login):
    log = get_logger()
    driver = login
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    log.info("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    button_clu = driver.find_element(By.XPATH, '(//button[@class="btn primary-button mr-2 transparent-btn"])[2]')
    driver.execute_script("arguments[0].click();", button_clu)
    log.info("Clicked on New Cluster Button")

    rubType = driver.find_element(By.ID, 'rubrikId')
    choose = Select(rubType)
    choose.select_by_value('2c8f78af-f79e-40f0-99d4-61e78d97e78b')
    log.info('Selected Rubrik type')

    clu_name = driver.find_element(By.XPATH, '//input[@formcontrolname="clusterName"]')
    clu_name.send_keys('Automation test cluster' + str(random.randint(0, 99)))
    log.info('Entered cluster name')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    log.info('Save the new cluster')