import time
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def questionnaire_sec(driver):
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    print("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    nav_questionnaire = driver.find_element(By.XPATH, '(//section[@class="tab-width-11 text-center text-uppercase '
                                                      'deselected-nav-tab cursor"])[1]')
    driver.execute_script("arguments[0].click();", nav_questionnaire)
    print('Navigate to Questionnaire')

    time.sleep(2)
    create_qnr = driver.find_element(By.XPATH, '//button[@class="btn primary-button"]')
    driver.execute_script("arguments[0].click();", create_qnr)
    print('Clicked on new Questionnaire')

    enter_desc = driver.find_element(By.XPATH, '//input[@formcontrolname="description"]')
    enter_desc.send_keys('Create questionnaire for Automation test')
    print('Entered questionnaire description')

    driver.find_element(By.XPATH, '//input[@value="office"]').click()
    driver.find_element(By.XPATH, '//input[@value="retail"]').click()
    driver.find_element(By.XPATH, '//input[@value="logistics"]').click()
    driver.find_element(By.XPATH, '//input[@value="industrial"]').click()
    print('Selected Asset Class')

    driver.find_element(By.XPATH, '(//div[@class="deselected-state"])[1]').click()
    driver.find_element(By.XPATH, '(//div[@class="deselected-state"])[2]').click()
    driver.find_element(By.XPATH, '(//div[@class="deselected-state"])[9]').click()
    driver.find_element(By.XPATH, '(//div[@class="deselected-state"])[10]').click()
    print('Selected services')

    ques_next = driver.find_element(By.XPATH, '//button[@type="submit"]')
    ques_next.click()
    print('Go next after filling details')
    time.sleep(2)
    
    submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.execute_script("arguments[0].click();", submit)
    print('Clicked on submit')
    time.sleep(2)

    qsnre_header = driver.find_element(By.XPATH, '//article[@class="col-lg-5"]//article')
    print('Created questionnaire: ' +qsnre_header.text)


def main():
    driver = launchBrowser()
    login(driver)
    questionnaire_sec(driver)
    driver.close()


if __name__ == '__main__':
    main()
