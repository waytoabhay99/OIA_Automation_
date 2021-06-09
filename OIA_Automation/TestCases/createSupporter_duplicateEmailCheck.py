import time
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def createSupporterDupEmail(driver):
    settings = driver.find_element(By.CSS_SELECTOR, '[href="/settings"]')
    driver.execute_script("arguments[0].click();", settings)
    print("Clicked on Settings")

    newSupporter = driver.find_element(By.XPATH, '//button[@type="button" and @class="btn toggle-button '
                                                 'text-uppercase pl-0"]')
    driver.execute_script("arguments[0].click();", newSupporter)
    print("Clicked on New Supporter")

    radioAdmin = driver.find_element(By.ID, 'inlineRadio2')
    radioAdmin.click()
    print('Admin supporter selected for creation')

    firstName = driver.find_element(By.XPATH, '//input[@formcontrolname="firstName"]')
    firstName.send_keys('Uwe')
    print('Entered First name')

    lastName = driver.find_element(By.XPATH, '//input[@formcontrolname="lastName"]')
    lastName.send_keys('Hoffman')
    print('Entered Last name')

    emailId = driver.find_element(By.XPATH, '//input[@formcontrolname="email"]')
    emailId.send_keys('uwe.hoffman1@email.com')
    # +str(random.randint(0, 99)) +

    telephone = driver.find_element(By.XPATH, '//input[@formcontrolname="phone"]')
    telephone.send_keys('+4930396491624')

    password1 = driver.find_element(By.XPATH, '//input[@formcontrolname="password"]')
    password1.send_keys('Test@1234')
    print('1st password entered')

    password2 = driver.find_element(By.XPATH, '//input[@formcontrolname="confirmPassword"]')
    password2.send_keys('Test@1234')
    print('Password confirmed')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)

    if driver.find_element(By.ID, 'toast-container').is_displayed() == True:
        print('Duplicate email found :'+driver.find_element(By.ID, 'toast-container').text)
    else:
        print("No duplicate email found")


def main():
    driver = launchBrowser()
    login(driver)
    createSupporterDupEmail(driver)
    driver.quit()


if __name__ == '__main__':
    main()
