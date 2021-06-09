import random
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def create_rub(driver):
    question = driver.find_element(By.XPATH, '//a[text()=" Fragebögen "]')
    driver.execute_script("arguments[0].click();", question)
    print("Clicked on Questionnaire")
    driver.implicitly_wait(10)

    button_rub = driver.find_element(By.XPATH, '(//button[@class="btn primary-button mr-2 transparent-btn"])[1]')
    driver.execute_script("arguments[0].click();", button_rub)
    print("Clicked on New Rubrik Button")

    rub_name = driver.find_element(By.ID, 'new-rubrik')
    rub_name.send_keys('Automation Test Rubrik '+str(random.randint(0,99)))
    print('Rubrik name enreted')

    driver.find_element(By.XPATH, '//button[@class="btn primary-button"]').click()
    print('Save the new Rubrik')


def main():
    driver = launchBrowser()
    login(driver)
    create_rub(driver)


if __name__ == '__main__':
    main()
