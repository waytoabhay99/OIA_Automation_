import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login, question_create


def quesType_dropdown(driver):
    quesType = driver.find_element(By.ID, 'questionType')
    choose = Select(quesType)
    choose.select_by_value('dropdown')
    print('Selected Question type')

    time.sleep(2)
    value1 = driver.find_element(By.XPATH, "(//input[@formcontrolname='answer'])[1]")
    value1.send_keys("value 1 of the dropdown")
    print('value 1 entered')

    value2 = driver.find_element(By.XPATH, "(//input[@formcontrolname='answer'])[2]")
    value2.send_keys("value 2 of the dropdown")
    print('value 2 entered')

    submit = driver.find_element(By.XPATH, '//button[text()="Speichern"]')
    submit.click()
    print('Submit button clicked')
    time.sleep(2)

    ques_header = driver.find_element(By.CSS_SELECTOR, 'section[class="row header"]')
    print('Dropdown question - ' + ques_header.text + ' created')


def main():
    driver = launchBrowser()
    login(driver)
    question_create(driver)
    quesType_dropdown(driver)
    time.sleep(5)


if __name__ == '__main__':
    main()
