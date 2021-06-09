import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login, question_create


def quesType_multiChoice(driver):
    quesType = driver.find_element(By.ID, 'questionType')
    choose = Select(quesType)
    choose.select_by_value('mehrfachauswahl')
    print('Selected Question type')

    time.sleep(1)
    in1 = driver.find_element(By.XPATH, '(//input[@formcontrolname="answer"])[1]')
    in1.send_keys('selection1')
    print('Input 1 entered')

    in2 = driver.find_element(By.XPATH, '(//input[@formcontrolname="answer"])[2]')
    in2.send_keys('selection2')
    print('Input 2 entered')

    submit = driver.find_element(By.XPATH, '//button[text()="Speichern"]')
    submit.click()
    print('Submit button clicked')

    ques_header = driver.find_element(By.CSS_SELECTOR, 'section[class="row header"]')
    print('Multiple choice question - ' + ques_header.text + ' created')


def main():
    driver = launchBrowser()
    login(driver)
    question_create(driver)
    quesType_multiChoice(driver)
    time.sleep(5)
    # driver.quit()


if __name__ == '__main__':
    main()