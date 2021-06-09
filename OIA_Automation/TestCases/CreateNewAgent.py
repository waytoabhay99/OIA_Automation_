import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from ImmoAgent.Resuables.Admin_Transversal import launchBrowser, login


def createAgent(driver):
    agent = driver.find_element(By.CSS_SELECTOR, '[href="/agents"]')
    driver.execute_script("arguments[0].click();", agent)
    print("Clicked on Agent")

    newAgent = driver.find_element(By.XPATH, '//button[text()=" Neuer Agent "]')
    driver.execute_script("arguments[0].click();", newAgent)
    print("Clicked on New Agent")

    salutation = driver.find_element(By.ID, 'gender')
    choose = Select(salutation)
    choose.select_by_value("1: female")
    print('Selected Female from Dropdown')

    firstname = driver.find_element(By.ID, 'firstName')
    firstname.send_keys('Martin')
    print('Entered First name')

    lastname = driver.find_element(By.ID, 'lastName')
    lastname.send_keys('King')
    print('Entered Last name')

    time.sleep(2)
    driver.find_element(By.ID, "inputAddress").send_keys("Hamburg")
    time.sleep(2)
    listElements = driver.find_elements(By.CSS_SELECTOR, "div.pac-container div span.pac-icon")
    print(listElements)
    listElements[1].click()
    print('Entered Address 1')

    time.sleep(2)
    opAddress = driver.find_element(By.ID, 'additionalAddress')
    opAddress.send_keys('Harburg Rathaus')
    print('Entered Adrs Optional')

    email = driver.find_element(By.ID, 'email')
    email.send_keys('myemai7l@email.de')
    print('Entered email')

    mobile = driver.find_element(By.ID, 'mobilePhone')
    mobile.send_keys('+919590199888')
    print('Entered Mobile Number')

    tele = driver.find_element(By.ID, 'phone')
    tele.send_keys('+919590199888')
    print('Entered Tele Number')

    jobStatus = driver.find_element(By.ID, 'jobStatus')
    jobStatus.send_keys('Employed')
    print('Entered Job Status')

    rds = driver.find_element(By.ID, 'radius')
    choose = Select(rds)
    choose.select_by_index(1)
    print('Selected Radius')

    radio = driver.find_element(By.ID, 'inlineRadio2')
    radio.click()
    print('Selected Nein')

    iban = driver.find_element(By.ID, 'iban')
    iban.send_keys('DE89370400440532013000')
    print('Entered IBAN')

    save = driver.find_element(By.XPATH, '//button[@type="submit"]')
    save.click()

    time.sleep(1)

    try:
        errorMessageOpacitiyValue = (driver.find_element(By.XPATH, '//div[@id="toast-container"]/div').value_of_css_property('opacity'))
        print(errorMessageOpacitiyValue)
        print(driver.find_element(By.XPATH, '//div[@aria-label="E-Mail existiert bereits"]').text)
    except NoSuchElementException:
        print(driver.find_element(By.XPATH, '//article[@class="col-lg-9 heading"]').text + ' creation Successful')

    # errorDivElementSize = len(driver.find_elements(By.XPATH, '//div[@id="toast-container"]/div'))
    # if errorDivElementSize > 0:
    #     print(driver.find_element(By.XPATH, '//div[@aria-label="E-Mail existiert bereits"]').text)
    # else:
    #     print(driver.find_element(By.XPATH, '//article[@class="col-lg-9 heading"]').text + 'creation Successful')


def main():
    driver = launchBrowser()
    login(driver)
    createAgent(driver)
    driver.quit()


if __name__ == '__main__':
    main()
