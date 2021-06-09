import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login, question_create


def quesType_conditional(driver):
    quesType = driver.find_element(By.ID, 'questionType')
    choose = Select(quesType)
    selected = choose.select_by_value('bedingte')
    print('Selected Question type')
    time.sleep(2)

    condition1 = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="confirmingStatement"]')
    condition1.send_keys('This is first possible answer')
    print('Condition 1 entered')

    condition2 = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="negativeStatement"]')
    condition2.send_keys('This is second possible answer')
    print('Condition 2 entered')

    freetext = driver.find_element(By.ID, 'freeText')
    freetext.click()
    print('Chekced free text checkbox')

    submit = driver.find_element(By.XPATH, '//button[text()="Speichern"]')
    submit.click()
    print('Submit button clicked')
    time.sleep(2)

    ques_header = driver.find_element(By.CSS_SELECTOR, 'section[class="row header"]')
    print('Conditional question - '+ques_header.text+' created')


def main():
    driver = launchBrowser()
    login(driver)
    question_create(driver)
    quesType_conditional(driver)

if __name__ == '__main__':
    main()
