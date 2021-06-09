import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def createSupporterFormatError(driver):
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
    emailId.send_keys('uwe.hoffman1')
    # +str(random.randint(0, 99)) +

    telephone = driver.find_element(By.XPATH, '//input[@formcontrolname="phone"]')
    telephone.send_keys('+49000030396491624')

    password1 = driver.find_element(By.XPATH, '//input[@formcontrolname="password"]')
    password1.send_keys('Test@1234')
    print('1st password entered')

    password2 = driver.find_element(By.XPATH, '//input[@formcontrolname="confirmPassword"]')
    password2.send_keys('Test@1234')
    print('Password confirmed')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)

    try:
        email_err = driver.find_element(By.XPATH, '//div[text()="Bitte gib ein gültiges E-Mail-Format ein."]')
        print("Email error: " + email_err.text)
    except NoSuchElementException:
        print('Entered email is valid')

    try:
        phone_err = driver.find_element(By.XPATH, '//div[text()="Bitte gebe eine gültige Telefonnummer ein."]')
        print("Telefonnummer error: " + phone_err.text)
    except NoSuchElementException:
        print('Entered telefone nummer is valid')


def main():
    driver = launchBrowser()
    login(driver)
    createSupporterFormatError(driver)
    driver.quit()


if __name__ == '__main__':
    main()
