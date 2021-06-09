import time
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login, delete_all


def questionnaire_jobSub(driver):
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    print("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    nav_questionnaire = driver.find_element(By.XPATH, '(//section[@class="tab-width-11 text-center text-uppercase '
                                                      'deselected-nav-tab cursor"])[1]')
    driver.execute_script("arguments[0].click();", nav_questionnaire)
    print('Navigate to Questionnaire')

    time.sleep(3)
    fisrt_chevron = driver.find_element(By.XPATH, '(//i[@class="fas fa-chevron-right btn grey-icon"])[12]')
    fisrt_chevron.click()
    print('Clicked on first chevron')
    time.sleep(3)

    bearbiten = driver.find_element(By.CSS_SELECTOR, 'button[class="btn edit-button secondary-button"]')
    bearbiten.click()
    print('Clicked on bearbiten')
    time.sleep(2)

    # deleting from Questionnaire
    question_list = driver.find_elements(By.CSS_SELECTOR, 'label[class="form-check-label rubric-heading"]')
    delete_all(driver, question_list)
    # for x in range(len(question_list)):
    driver.close()


def main():
    driver = launchBrowser()
    login(driver)
    questionnaire_jobSub(driver)
    time.sleep(4)


if __name__ == '__main__':
    main()
