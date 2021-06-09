import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ImmoAgent.Resuables.Admin_Transversal import randomize
from ImmoAgent.Resuables.test_logging import get_logger


def test_create_conditional_question(login):
    log = get_logger()
    driver = login
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    log.info("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    nav_questionnaire = driver.find_element(By.XPATH, '(//section[@class="tab-width-11 text-center text-uppercase '
                                                      'deselected-nav-tab cursor"])[1]')
    driver.execute_script("arguments[0].click();", nav_questionnaire)
    log.info('Navigate to Questionnaire')

    time.sleep(3)
    create_qnr = driver.find_element(By.XPATH, '//button[@class="btn primary-button"]')
    driver.execute_script("arguments[0].click();", create_qnr)
    log.info('Clicked on new Questionnaire')
    driver.implicitly_wait(10)

    enter_desc = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@formcontrolname'
                                                                                           '="description"]')))
    enter_desc.send_keys('Customer Specific Questionnaire - Automation run ' + str(random.randint(3, 99)))
    log.info('Entered questionnaire description')
    time.sleep(3)

    i = randomize()
    driver.find_elements(By.XPATH, '//input[@type="checkbox"]')[i].click()
    j = randomize()
    if i == j:
        j = j + 1
    driver.find_elements(By.XPATH, '//input[@type="checkbox"]')[j].click()
    log.info('Selected Asset Class')

    i = randomize()
    driver.find_elements(By.XPATH, '(//div[@class="deselected-state"])')[i].click()
    j = randomize()
    if i == j:
        j = j + 1
    driver.find_elements(By.XPATH, '(//div[@class="deselected-state"])')[j].click()
    log.info('Selected services')

    ques_next = driver.find_element(By.XPATH, '//button[@type="submit"]')
    ques_next.click()
    log.info('Go next after filling details')
    time.sleep(2)

    cust_sp = driver.find_element(By.XPATH, '//button[@class="btn toggle-button customerSpecificButton"]')
    driver.execute_script("arguments[0].click();", cust_sp)
    log.info('Customer specific details')
    time.sleep(2)

    cust_text = driver.find_element(By.XPATH, '(//input[@type="text"])[2]')
    driver.execute_script("arguments[0].click();", cust_text)
    log.info('Click on customer text box')
    driver.implicitly_wait(5)

    select_cust = driver.find_element(By.XPATH, '//input[@aria-label="Tesla Inc."]')
    driver.execute_script("arguments[0].click();", select_cust)
    log.info('Customer selected')
    driver.implicitly_wait(5)

    save_cust = driver.find_element(By.XPATH, '// button[ @ type = "submit"]')
    driver.execute_script("arguments[0].click();", save_cust)
    log.info('Clicked on submit')

    # qsnre_header = driver.find_element(By.XPATH, '//article[@class="col-lg-5"]//article')
    # log.info('Created customer questionnaire: ' + qsnre_header.text)
